# R and RStudio Installer/Updater for macOS (Homebrew-based)

This Bash script automates the installation and update process for **R** and **RStudio** on macOS systems using **Homebrew**.
Running this script will install R and RStudio
If R and RStudio are already installed, this script will update both
---

## Features

- Installs **Homebrew** if it’s not already installed.
- Installs **R** or upgrades it to the latest version.
- Installs **RStudio** via Homebrew Cask or upgrades it if already installed.
- Detects standalone RStudio apps in `/Applications` and replaces them with the Homebrew-managed version.
- This will not impact your installed packages, but the script will displays currently installed R packages with their versions after installation/update for peace of mind.

---

## Usage

1. Open your Terminal.

2. Launch the Script

Open your terminal and navigate to the directory where your script and Dockerfile live using the cd command

Then activate and run the script:

chmod +x R_Maintainer.sh
./R_Maintainer.sh

---

## How It Works

1. **Homebrew Check & Install:**  
   The script checks if Homebrew is installed; if not, it installs Homebrew and configures your shell environment.

2. **R Installation/Update:**  
   It installs R if missing or attempts to upgrade it if already present.

3. **RStudio Installation/Update:**  
   The script prefers managing RStudio via Homebrew Cask. If a standalone RStudio app exists in `/Applications`, it will quit and remove it, then reinstall RStudio via Homebrew.

4. **R Package Listing:**  
   After successful install/update, it lists all currently installed R packages and their versions.

---

## Requirements

- macOS with Terminal access
- Internet connection for downloading Homebrew, R, and RStudio

---

## Notes

- The script uses `set -euo pipefail` for safer execution and will stop on errors.
- Make sure you have permissions to install software and modify `/Applications`.
- Running this script multiple times is safe; it will only install or update as needed.

---

## License & Attribution

This script was created by Logan Cohen and is intended for educational and personal use.

---
- Program logic created by by Logan Cohen for use in an educational genomics setting on Apple Silicon (M3 Pro).
- Assistance with debugging and documentation was provided by Lyric (OpenAI’s GPT-4o model)
