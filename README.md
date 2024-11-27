# NordVPN GUI

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)

A simple GUI wrapper for the NordVPN Linux CLI.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)

## Requirements

- Python 3.x
- tkinter
- NordVPN CLI

## Installation

1. Install Python 3.x
2. Install tkinter
3. Install NordVPN CLI by following the instructions [here](https://nordvpn.com/download/linux/)
4. Clone this repository

## Usage

1. Make the script executable:

```bash
chmod +x app.py
```

2. Run the script using terminal or right-click and select "Run as a Program"
3. If not authenticated, login using the "Login" button
   1. This will open a pop up to open a browser to authenticate
4. Due to how the NordVPN CLI works, you'll need to close and reopen the GUI after connecting/disconnecting
5. Use the "Connect" and "Disconnect" buttons to connect and disconnect from the VPN
   1. Leaving the "Country" field blank will connect to the fastest server available
   2. Leaving the "City" field blank will connect to the fastest server available in the selected country

## Features

- Country and city selection
- Quick connect to the fastest server (leave the "Country" and "City" fields blank)
- Login and logout
- Status display

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.
