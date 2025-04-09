# LootVault_Game
# 💰 LootVault - All-in-One Python Desktop App

**LootVault** is a desktop app built using Python and Tkinter. It combines a quiz game (like KBC), a simple banking system, account creation with CAPTCHA, and themes — all in one place. You can run it using Python or install it as a Windows app using the included setup file. The app has no external library dependencies.

---

## 🔥 Features:
- 🎮 **Quiz Game**: Play questions from easy, medium, and hard levels with 4 options. Win virtual money and quit anytime to keep your earnings.
- 🏦 **Banking System**: Deposit, withdraw, and check your balance using a simple interface.
- 👤 **Account Creation**: Create users with a username and password. CAPTCHA check is required during signup.
- 🎨 **Themes**: Click buttons to change the background color of the app.
- 🆘 **Help Section**: Built-in help to understand how the app works.

---

## 💻 How to Run the App (Using Python Source)
1. Clone or download the repository.
2. Make sure you have **Python 3** installed.
3. Run the app:
   ```bash
   python lootvault.py
   ```

---

## 🪄 How to Install and Use EXE Version (No Python Needed)
1. Go to the `dist/` folder (or where you saved the setup).
2. Double-click `LootVault Setup.exe`.
3. Follow the setup wizard and install it like a normal Windows application.
4. After installation, open it from the Start menu or desktop shortcut.

✅ The EXE was built using **Inno Setup** — you don’t need Python installed to run it.

---

## 🛠️ How to Build the EXE Yourself (Optional)
- Install `pyinstaller` (if not installed):
  ```bash
  pip install pyinstaller
  ```
- Create the EXE:
  ```bash
  pyinstaller --noconfirm --onefile lootvault.py
  ```
- Then use **Inno Setup** to create an installer from the `.exe` file. You can use the provided `.iss` script to automate the setup process.

Download Inno Setup here: [https://jrsoftware.org/isinfo.php](https://jrsoftware.org/isinfo.php)

---

## 📁 Folder Structure
```
LootVault/
├── lootvault.py          # Main Python file
├── details.txt           # Auto-generated for saving user credentials
├── dist/                 # Contains the EXE and Setup file
│   └── LootVault Setup.exe
├── LootVault.iss         # Inno Setup script
└── README.md             # This file
```

---

## 🔐 Important Note on Security
Usernames and passwords are saved in plain text (`details.txt`). For real apps, you should use password hashing (like `hashlib`) and better file storage methods.

---

## 🚀 Future Upgrades (Optional Ideas)
- Save user balance separately per account
- Add login system with encrypted passwords
- Add sound effects, animations, or leaderboard
- Include more themes or light/dark mode
- Save quiz score history

---

## 👑 Credits & License
- Made with Python & Tkinter 🐍
- Free to use and modify under the **MIT License**
- Author: PRIYANSHU GUPTA

---

