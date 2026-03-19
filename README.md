# 🚀 NMIT Parent Portal Auto Login

A simple automation tool that allows students to quickly log into the NMIT Parent Portal without manually entering credentials every time.

## 📌 Overview

This project includes:
- 🧠 Python automation script (core logic)
- 💻 Desktop GUI application (Windows)
- 📱 Android app (mobile version)

---

## 🧠 Python Script (Core)

The main script automates the login process using browser automation.

### ✨ Features

- 🔐 Automatically logs into parent portal  
- ⚡ Eliminates manual entry of USN and DOB  
- 🌐 Uses browser automation (Selenium)  
- 🎯 Works directly with the actual website  

### ⚙️ Requirements

- Python 3.8+  
- Google Chrome installed  
- Internet connection  

### 🚀 Usage

```bash
git clone https://github.com/your-username/nmit-portal-gui.git
cd nmit-portal-gui
pip install -r requirements.txt
python portal_app.py


---

## 💻 Desktop Application (GUI)

```markdown
## 💻 Desktop Application (GUI)

A simple Windows app built on top of the automation script.

### ✨ Features

- 👤 Multiple user profiles  
- ⚡ One-click login  
- 💾 Local storage  
- 🖥️ Clean GUI  

### 📥 Download

Download from the Releases section:

- `NMIT Portal GUI.exe`

## 📱 Android Application

A lightweight mobile app for quick portal access.

### ✨ Features

- ⚡ Opens portal instantly  
- 🔐 Auto-fills credentials  
- 📱 Smooth mobile experience  

### 📥 Download

Download from the Releases section:

- `app-arm64-v8a-release.apk`

### 📲 Installation

- Download APK  
- Enable *Install from unknown sources*  
- Install and open  

## File Structure

portal_app.py       # Core automation script
profiles.json       # Stores user profiles locally
icon.ico            # App icon
requirements.txt    # Dependencies
AndroidApp/         # Android project files
DesktopApp/         # Desktop build files

## 🔒 Privacy

- All data (USN, DOB) is stored locally on your device  
- No data is sent to any external server  

---

## ⚠️ Notes

- Desktop app works on Windows only  
- Chrome must be installed for automation  
- Portal session may expire, requiring re-login  

---

## 🙌 Contribution

Feel free to fork, improve UI, or add features.

---

## ⭐ Support

If you found this useful, consider giving it a star ⭐