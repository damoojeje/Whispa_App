# Whispa App 🎙️➡️📝➡️🌍

[![PyPI Version](https://img.shields.io/pypi/v/whispa-app)](https://pypi.org/project/whispa-app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Windows Installer](https://img.shields.io/badge/Download-Windows_Installer-blue)](https://github.com/damoojeje/Whispa_App/releases/latest)

**Audio Transcription & Translation Desktop GUI**  
*Powered by OpenAI's Whisper and MarianMT*

---

## Features ✨

- **Audio Transcription**  
  Convert WAV/MP3/M4A files to text using 5 Whisper model sizes  
  `tiny` | `base` | `small` | `medium` | `large`

- **Text Translation**  
  Supports Spanish, French, German, Chinese, Japanese

- **System Monitoring**  
  Real-time CPU/RAM/GPU usage stats

- **Cross-Platform**  
  Windows installer available • Python package for developers

---

## Installation 🛠️

### Windows Users
[Download the installer](https://github.com/damoojeje/Whispa_App/releases/latest) (160MB)  
1. Run `WhispaApp-Setup.exe`
2. Follow installation prompts
3. Launch from Start Menu

### Python Developers
```bash
# 1. Install CPU-optimized PyTorch
pip install torch --index-url https://download.pytorch.org/whl/cpu

# 2. Install Whispa App
pip install whispa_app

# 3. Download models (first time)
whispa --prefetch

# 4. Launch GUI


Usage Guide 📖
Quick Start
Browse for an audio file

Select Model:
Model Selection

Transcribe: Real-time progress tracking

Translate: Choose target language

Save: Export as TXT or clipboard

Advanced Settings
Setting Description
VRAM Threshold  Minimum GPU memory for acceleration
Beam Size Balance speed vs accuracy
VAD Filter  Skip silent segments
Project Structure 📂
Whispa_App/
├── src/                  # Source code
│   └── whispa_app/       # Core modules
│       ├── assets/       # Icons
│       ├── ui/           # GUI components
│       └── *.py          # Functionality
├── installer/            # Inno Setup script
└── Releases/             # Windows installers
Contributing 🤝
Fork the repository

Create feature branch:
git checkout -b feature/new-feature

Commit changes:
git commit -m "Add awesome feature"

Push to branch:
git push origin feature/new-feature

Open a Pull Request

Note: Include tests for new features!

License 📄
MIT License - Full Text
Copyright © 2025 Damilare Eniolabi

Acknowledgments 🙏
OpenAI Whisper models

MarianMT translation framework

Hugging Face Transformers library

CustomTkinter for modern GUI

Report Issues • Contact