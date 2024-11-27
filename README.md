# NordVPN GUI

A simple GUI application for managing NordVPN connections using `tkinter`. This application is specifically aimed at Ubuntu/Linux users where there's no official GUI port for NordVPN.

## Features

- Connect to NordVPN servers by selecting a country and city.
- Disconnect from NordVPN.
- View current connection status, including server, hostname, IP, country, and city.

## Requirements

- Python 3.x
- `tkinter` library (usually included with Python)
- NordVPN CLI

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the NordVPN CLI by following the instructions on the [NordVPN website](https://nordvpn.com/download/linux/).
3. Clone this repository or download the `app.py` file.

## Usage

1. Open a terminal and navigate to the directory containing `app.py`.
2. Run the script using Python:

    ```sh
    python3 app.py
    ```

3. The GUI application will open. Use the dropdown menus to select a country and city, then click "Connect" to connect to a NordVPN server. Click "Disconnect" to disconnect from the VPN.
4. Leaving either country or city will let NordVPN pick the recommended country/city.

As a wrapper, the GUI application will run the NordVPN CLI commands in the background to connect and disconnect from servers.

## GUI Overview

- **Country Dropdown**: Select the country to connect to.
- **City Dropdown**: Select the city to connect to (populated based on the selected country).
- **Connect Button**: Connect to the selected NordVPN server.
- **Disconnect Button**: Disconnect from the current NordVPN server.
- **Status Panel**: Displays the current connection status, including server, hostname, IP, country, and city.

## Note

This application is untested on Windows and is specifically aimed at Ubuntu/Linux users (no official GUI port).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
