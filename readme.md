# InvisiNet

InvisiNet is a Python-based network monitoring tool designed for use in security systems or smart home applications. It detects devices connected to your local network, identifies new devices that connect, and alerts you if an unrecognized device is detected. 

## Features

- **Automatic Network Detection:** Automatically identifies the network range for scanning.
- **Device Monitoring:** Monitors devices connected to the network and detects new devices in real-time.
- **Friendly Device Recognition:** Recognizes and distinguishes known (friendly) devices from unknown ones using a predefined list of MAC addresses.
- **Alerts:** Plays an alert sound when a new, unrecognized device connects to the network.
- **Customizable Audio Alerts:** Uses custom audio files for different events like scanning and new device detection.

## How It Works

1. **Network Scanning:** The tool automatically detects the network range using the device's network interface and scans the network for connected devices.

2. **Device Identification:** The MAC addresses of detected devices are compared against a list of known, friendly devices stored in the `mac.ini` file.

3. **Alert Mechanism:** 
   - If a new device connects to the network that isn't in the list of friendly MAC addresses, the tool plays an alert sound and logs the device's details.
   - If a known device reconnects, the tool logs a friendly message and welcomes the device back.

4. **Continuous Monitoring:** The tool continuously scans the network and alerts in real-time for any new device connections.


## Installation

1. **Clone the Repository:**
   - Clone the InvisiNet repository from GitHub, install the requirments, and run InvisiNet:
     ```bash
     git clone https://github.com/calinux-py/InvisiNet.git && cd InvisiNet && pip install -r requirements.txt && cd InvisiNet && python main.py
     ```
     
   - The script will automatically start scanning your network and monitoring for new devices.

## Applications

InvisiNet can be utilized in various scenarios, including but not limited to:

- **Security Systems:** Monitor the network for unauthorized devices and raise an alarm if a new device connects.
- **Smart Home Applications:** Integrate with smart home systems to automatically identify and manage device connectivity. For example, when you arrive home and your device connects to the network, it can trigger other events, such as turning on smart lights, smart AC, activating speakers, etc.
- **Fun:** Offers about 60 seconds worth of entertainment.

## License

I dont care.
