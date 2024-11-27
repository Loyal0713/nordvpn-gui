import subprocess
import tkinter as tk
from tkinter import ttk, messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("NordVPN GUI")

        self.country_var = tk.StringVar()
        self.city_var = tk.StringVar()

        self.init_ui()

    def init_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.grid(row=0, column=0, padx=10, pady=10)

        # Country dropdown
        ttk.Label(main_frame, text="Country").grid(row=0, column=0, padx=10, pady=10)
        self.country_dropdown = ttk.Combobox(main_frame, textvariable=self.country_var)
        self.country_dropdown["values"] = [""] + self.get_countries()
        self.country_dropdown.bind("<<ComboboxSelected>>", self.on_country_change)
        self.country_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # City dropdown
        ttk.Label(main_frame, text="City").grid(row=1, column=0, padx=10, pady=10)
        self.city_dropdown = ttk.Combobox(main_frame, textvariable=self.city_var)
        self.city_dropdown["values"] = [""]
        self.city_dropdown.grid(row=1, column=1, padx=10, pady=10)

        # Connect button
        self.connect_button = ttk.Button(
            main_frame, text="Connect", command=self.on_connect
        )
        self.connect_button.grid(row=2, column=0, padx=10, pady=10)

        # Disconnect button
        self.disconnect_button = ttk.Button(
            main_frame, text="Disconnect", command=self.on_disconnect
        )
        self.disconnect_button.grid(row=2, column=1, padx=10, pady=10)

        # Status panel
        status_frame = ttk.Frame(self.root, relief=tk.SUNKEN, borderwidth=1)
        status_frame.grid(row=0, column=1, padx=10, pady=10, sticky=tk.N + tk.S)

        self.status_text = tk.Text(status_frame, width=40, height=20, state=tk.DISABLED)
        self.status_text.pack(padx=10, pady=10)

        self.update_status_panel()

    # Helper methods
    def update_status_panel(self):
        '''Update the status panel with the current NordVPN connection status'''
        status_info = self.status()
        self.status_text.config(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        self.status_text.insert(tk.END, status_info)
        self.status_text.config(state=tk.DISABLED)

    def on_country_change(self, event):
        country = self.country_var.get()
        if country:
            cities = [""] + self.get_cities(country)
            self.city_dropdown["values"] = cities

    def on_connect(self):
        country = self.country_var.get()
        city = self.city_var.get()
        try:
            self.connect(country, city)
            self.update_status_panel()
            messagebox.showinfo("Success", "Connected successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def on_disconnect(self):
        '''Disconnect from NordVPN'''
        try:
            self.disconnect()
            self.update_status_panel()
            messagebox.showinfo("Success", "Disconnected successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def run_command(self, cmd):
        '''Driver function to run shell commands'''
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout

    def get_countries(self):
        cmd = "nordvpn countries"
        return self.run_command(cmd).split()

    def get_cities(self, country):
        cmd = f"nordvpn cities {country}"
        return self.run_command(cmd).split()

    def connect(self, country=None, city=None):
        '''Connect to NordVPN using the specified country and city'''
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


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
