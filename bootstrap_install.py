import subprocess, sys, os

EMBEDDED = os.path.join(sys.argv[1], "python.exe")  # path to embeddable python
VENV_DIR = os.path.join(sys.argv[2], "venv")

# 1. Create venv
subprocess.check_call([EMBEDDED, "-m", "venv", VENV_DIR])

PIP = os.path.join(VENV_DIR, "Scripts", "pip.exe")
WHISPA = os.path.join(VENV_DIR, "Scripts", "WhispaApp.exe")  # if you bundle a launcher

# 2. Upgrade pip & install core deps + CPU‐torch
subprocess.check_call([PIP, "install", "--upgrade", "pip"])
subprocess.check_call([PIP, "install", "--no-cache-dir", "-r", "requirements.txt"])
subprocess.check_call([PIP, "install", "--no-cache-dir", "torch==2.0.1+cpu", "--index-url", "https://download.pytorch.org/whl/cpu"])

# 3. Prefetch models
subprocess.check_call([os.path.join(VENV_DIR, "Scripts", "whispaapp.exe"), "--prefetch"])
