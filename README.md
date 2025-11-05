# Drone Disabler

Security research tool for testing vulnerabilities in Parrot Bebop drones.

## ⚠️ Legal Disclaimer

**IMPORTANT:** This tool was developed **EXCLUSIVELY** for educational purposes and authorized security research. The use of WiFi deauthentication (jamming) techniques is **ILLEGAL** in most jurisdictions without explicit authorization.

- ✅ Permitted use: Authorized penetration testing, security research, CTF competitions, controlled environments
- ❌ Prohibited use: Unauthorized network interference, service disruption, malicious attacks

**The author is not responsible for misuse of this tool. Use at your own risk.**

## 📋 Description

Drone Disabler is a security testing tool that demonstrates vulnerabilities in Parrot Bebop drones through:

1. **WiFi Network Scanning**: Identifies Parrot drones through known MAC prefixes
2. **Deauthentication Attack**: Disconnects the drone from the controller using WiFi deauth frames
3. **Forced Landing Command**: Connects to the drone and sends automatic landing command

### How It Works

```
┌─────────────────────┐
│ Scan WiFi           │
│ (wlan0)             │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Detect Parrot       │
│ Drone (MAC)         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Create Monitor      │
│ Interface (mon0)    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Deauth Attack       │
│ (aireplay-ng)       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Connect to Drone    │
│ via WiFi            │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Send Landing        │
│ Command             │
└─────────────────────┘
```

## 🔧 Requirements

### Operating System
- **Linux** (tested on Debian/Ubuntu)
- **Root privileges** (required for network operations)

### Hardware
- WiFi adapter compatible with monitor mode
- `phy1` interface available for monitor mode

### Software
- Python 2.7
- aircrack-ng
- iw / iwconfig
- dhclient

## 📦 Installation

### Method 1: Automatic Script

Run the included installation script:

```bash
chmod +x drone_disabler_install.sh
sudo ./drone_disabler_install.sh
```

The script will automatically install:
- aircrack-ng (WiFi testing suite)
- git, mercurial (version control)
- vim (text editor)
- libsdl1.2-dev (SDL libraries)
- python-pygame (Python graphics library)
- katarina (Parrot Bebop SDK)
- python-iwlist (WiFi scanning wrapper)

### Method 2: Manual Installation

```bash
# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install dependencies
sudo apt-get install -y aircrack-ng git vim mercurial libsdl1.2-dev python-pygame

# Clone Python dependencies
cd /tmp
hg clone https://bitbucket.org/robotika/katarina
cd katarina
sudo python setup.py install

cd /tmp
git clone https://github.com/iancoleman/python-iwlist
cd python-iwlist
sudo python setup.py install
```

## 🚀 Usage

### Prerequisites
1. Ensure you have a compatible WiFi adapter
2. Run as root
3. Verify that `wlan0` and `phy1` interfaces are available

### Execute

```bash
sudo python drone_disabler.py
```

### Expected Behavior

```
Scanning WiFi networks...
Scanning WiFi networks...
Parrot drone detected!
  ESSID: Bebop2-XXXXXX
  MAC: 90:03:B7:XX:XX:XX
  Channel: 6

Creating monitor interface...
Sending deauthentication attack...
Connecting to drone...
Sending landing command...
Drone successfully disabled!
```

## 🎯 Supported Drones

The tool detects Parrot drones through the following MAC prefixes:

| MAC Prefix | Model |
|------------|-------|
| 90:03:B7   | Parrot Bebop/Bebop 2 |
| A0:14:3D   | Parrot AR.Drone |
| 00:12:1C   | Parrot (legacy) |
| 00:26:7E   | Parrot (legacy) |
| 90:3A:E6   | Parrot Disco/Mambo |

## 🛠️ Troubleshooting

### Error: "No wireless networks found"
- Check if `wlan0` is active: `ifconfig wlan0`
- Ensure the WiFi adapter is connected

### Error: "Permission denied"
- Run the script as root: `sudo python drone_disabler.py`

### Error: "mon0: No such device"
- Check if `phy1` exists: `iw dev`
- Ensure your adapter supports monitor mode

### Error installing dependencies
- Use Python 2.7 (Python 3 is not compatible)
- Install pip2: `sudo apt-get install python-pip`

## 📚 Project Structure

```
drone_disabler/
├── README.md                    # This file
├── drone_disabler.py            # Main script
└── drone_disabler_install.sh    # Installation script
```

## 🔒 Security Considerations

### Ethical Aspects
- This tool demonstrates known vulnerabilities in commercial drones
- Use only in controlled environments and with authorization
- Respect local laws regarding radio signal interference

### Demonstrated Vulnerabilities
1. **WiFi Deauthentication**: Parrot drones use WiFi without adequate deauth protection
2. **Unauthenticated Access**: Connection to drone without credentials
3. **Lack of Encryption**: Commands sent in plain text

### Countermeasures
- Use drones with more secure protocols (e.g., OcuSync, Lightbridge)
- Implement strong authentication
- Use less vulnerable frequencies (5.8GHz with protection)

## 📖 References

- [Aircrack-ng Documentation](https://www.aircrack-ng.org/)
- [Parrot Bebop SDK](https://bitbucket.org/robotika/katarina)
- [WiFi Deauthentication Attack](https://en.wikipedia.org/wiki/Wi-Fi_deauthentication_attack)

## 📝 License

This project is provided "as is", without warranties of any kind. Use at your own risk.

## 🤝 Contributing

Contributions are welcome! Before contributing:
1. Ensure your changes are ethical
2. Test in a controlled environment
3. Document your changes

## ⚡ Final Warning

**This tool was created to demonstrate security vulnerabilities in commercial drones with the goal of improving the security of autonomous systems. Any malicious or illegal use is the sole responsibility of the user.**

---

**Developed for educational and security research purposes** 🛡️
