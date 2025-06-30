#!/usr/bin/env bash
set -euo pipefail

# 1. Ensure Homebrew is installed
if ! command -v brew >/dev/null 2>&1; then
  echo "🍺 Homebrew not found. Installing Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  # Add Homebrew to PATH
  if [[ -f /opt/homebrew/bin/brew ]]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
  elif [[ -f /usr/local/bin/brew ]]; then
    eval "$(/usr/local/bin/brew shellenv)"
  fi
else
  echo "🍺 Homebrew detected."
fi

# 2. Install or update R
if ! command -v R >/dev/null 2>&1; then
  echo "R not found. Installing R..."
  brew install r
else
  echo "R is installed. Updating R..."
  brew upgrade r --formula || echo "✓ R is already up-to-date."
fi

# 3. Install or update RStudio
echo "🔍 Checking RStudio status..."
if brew list --cask rstudio >/dev/null 2>&1; then
  echo "RStudio (Homebrew) detected. Updating RStudio..."
  brew upgrade --cask rstudio || echo "✓ RStudio is already up-to-date."
elif [ -d "/Applications/RStudio.app" ]; then
  echo "Standalone RStudio.app found in /Applications. Uninstalling and using Homebrew Cask..."
  # Quit RStudio if running
  osascript -e 'tell application "RStudio" to quit' >/dev/null 2>&1 || true
  rm -rf "/Applications/RStudio.app"
  echo "Reinstalling RStudio via Homebrew..."
  brew install --cask rstudio
else
  echo "RStudio not found. Installing RStudio via Homebrew..."
  brew install --cask rstudio
fi

# 5. Completion message
echo
echo "Congratulations, you are now running the most current versions of R and RStudio!"

# 4. List installed R packages
echo
echo "Here are your currently installed R packages and versions:"
Rscript -e 'ip <- installed.packages()[,c("Package","Version")];
             for(i in seq_len(nrow(ip))) {
               cat(ip[i,1], ":", ip[i,2], "\n")
             }'
