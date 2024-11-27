#!/usr/bin/env python3

import subprocess
import tkinter as tk
from tkinter import ttk, messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("NordVPN GUI")

        # Create main frame
        main_frame = ttk.Frame(root)
        main_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        # Country selection
        ttk.Label(main_frame, text="Country:").grid(row=0, column=0, sticky='w', padx=5)
        self.country_var = tk.StringVar()
        self.country_combo = ttk.Combobox(main_frame, textvariable=self.country_var)
        self.country_combo.grid(row=0, column=1, sticky='ew', padx=5)
        self.country_combo.bind("<<ComboboxSelected>>", self.on_country_change)

        # City selection
        ttk.Label(main_frame, text="City:").grid(row=1, column=0, sticky='w', padx=5)
        self.city_var = tk.StringVar()
        self.city_combo = ttk.Combobox(main_frame, textvariable=self.city_var)
        self.city_combo.grid(row=1, column=1, sticky='ew', padx=5)

        # Auth frame
        auth_frame = ttk.Frame(main_frame)
        auth_frame.grid(row=2, column=0, columnspan=2, pady=5)
        
        self.login_btn = ttk.Button(auth_frame, text="Login", command=self.on_login)
        self.login_btn.grid(row=0, column=0, padx=5)
        
        self.logout_btn = ttk.Button(auth_frame, text="Logout", command=self.on_logout)
        self.logout_btn.grid(row=0, column=1, padx=5)

        # Connect/Disconnect buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=5)
        
        self.connect_btn = ttk.Button(button_frame, text="Connect", command=self.on_connect)
        self.connect_btn.grid(row=0, column=0, padx=5)
        
        self.disconnect_btn = ttk.Button(button_frame, text="Disconnect", command=self.on_disconnect)
        self.disconnect_btn.grid(row=0, column=1, padx=5)

        # Status display
        self.status_text = tk.Text(main_frame, height=5, width=40)
        self.status_text.grid(row=4, column=0, columnspan=2, pady=5)

        # Configure grid weights
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Initialize UI state
        self.update_countries()
        self.update_auth_buttons()
        self.update_status()

    def update_countries(self):
        """Update the countries dropdown with available countries"""
        countries = [""] + self.get_countries()
        self.country_combo["values"] = countries

    def update_status(self):
        """Update the status text widget with current VPN status"""
        status_info = self.status()
        self.status_text.config(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        self.status_text.insert(tk.END, status_info)
        self.status_text.config(state=tk.DISABLED)

    def on_country_change(self, event):
        """Handle country selection change"""
        country = self.country_var.get()
        if country:
            cities = [""] + self.get_cities(country)
            self.city_combo["values"] = cities

    def on_login(self):
        """Handle login button click"""
        try:
            result = self.login()
            self.update_auth_buttons()
            self.update_status()
        except Exception as e:
            messagebox.showerror("Error", f"Login failed: {e}")

    def on_logout(self):
        """Handle logout button click"""
        try:
            self.logout()
            self.update_auth_buttons()
            self.update_status()
            messagebox.showinfo("Success", "Logged out successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Logout failed: {e}")

    def on_connect(self):
        country = self.country_var.get()
        city = self.city_var.get()
        try:
            self.connect(country, city)
            self.update_status()
            messagebox.showinfo("Success", "Connected successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def on_disconnect(self):
        '''Disconnect from NordVPN'''
        try:
            self.disconnect()
            self.update_status()
            messagebox.showinfo("Success", "Disconnected successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def run_command(self, cmd):
        '''Driver function to run shell commands'''
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout

    def get_countries(self):
        cmd = "nordvpn countries"
        countries = self.run_command(cmd).split()
        countries.remove("United_States")
        countries.insert(0, "United_States")
        return countries

    def get_cities(self, country):
        cmd = f"nordvpn cities {country}"
        return self.run_command(cmd).split()

    def connect(self, country="", city=""):
        # Check login status first
        if not self.is_logged_in():
            from tkinter import messagebox
            answer = messagebox.askquestion(
                "Login Required",
                "You need to log in first. Would you like to log in now?"
            )
            if answer == 'yes':
                self.login()
            return "Login required"
            
        # Proceed with connection if logged in
        if country and city:
            cmd = f"nordvpn connect {country} {city}"
        elif country:
            cmd = f"nordvpn connect {country}"
        else:
            cmd = "nordvpn connect"
        return self.run_command(cmd)

    def disconnect(self):
        cmd = "nordvpn disconnect"
        return self.run_command(cmd)

    def status(self):
        cmd = "nordvpn status"
        return self.run_command(cmd)
    
    def is_logged_in(self):
        cmd = "nordvpn account"
        result = self.run_command(cmd)
        return "Email Address" in result
    
    def login(self):
        cmd = "nordvpn login"
        result = self.run_command(cmd)
        
        # Extract URL from command output
        if "Continue in the browser:" in result:
            url = result.split(": ")[1].strip()
            
            # Create popup with clickable link
            import webbrowser
            from tkinter import messagebox
            
            # Custom dialog with link
            answer = messagebox.askquestion(
                "NordVPN Login",
                "Click 'Yes' to open the login page in your browser\n\n" + 
                "URL: " + url
            )
            
            # Open URL if user clicks Yes
            if answer == 'yes':
                webbrowser.open(url)
                
        return result

    def logout(self):
        cmd = "nordvpn logout"
        return self.run_command(cmd)

    def update_auth_buttons(self):
        is_logged = self.is_logged_in()
        self.login_btn['state'] = 'disabled' if is_logged else 'normal'
        self.logout_btn['state'] = 'normal' if is_logged else 'disabled'
        self.connect_btn['state'] = 'normal' if is_logged else 'disabled'


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
