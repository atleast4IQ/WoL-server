# Wake-on-LAN Web Trigger

This is a minimal Python Flask application that allows you to trigger Wake-on-LAN (WOL) packets via a web request.

## Features

- Send a WOL magic packet to a specified MAC address via HTTP
- Easy to deploy on any system with Python

## Requirements

- Python 3
- Flask
- wakeonlan

Install dependencies with:

```bash
pip install flask wakeonlan
```

## Usage
```bash
python main.py
```
This starts a web server on http://0.0.0.0:5000

### Send a WOL packet:
Open a browser or send a request to:
```
http://<server-ip>:5000/<mac-address>
```

## Notes
- Ensure WOL is enabled in BIOS and on the network adapter.
- With PORT Forwarding this tool can be accessed from outside the local network (USE AT YOUR OWN RISK)
