"""Build Windows installer for Whispa App."""

import os
import sys
import shutil
import subprocess
import logging
from pathlib import Path
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Paths
ROOT_DIR = Path(__file__).parent.parent
DIST_DIR = ROOT_DIR / "dist"
BUILD_DIR = ROOT_DIR / "build"
INSTALLER_DIR = DIST_DIR / "installer"
ASSETS_DIR = ROOT_DIR / "src" / "whispa_app" / "assets"

def find_inno_setup() -> Optional[Path]:
    """Find Inno Setup compiler."""
    if sys.platform != "win32":
        return None
        
    possible_paths = [
        Path(os.environ.get("PROGRAMFILES(X86)", "")) / "Inno Setup 6" / "ISCC.exe",
        Path(os.environ.get("PROGRAMFILES", "")) / "Inno Setup 6" / "ISCC.exe",
    ]
    
    for path in possible_paths:
        if path.exists():
            return path
            
    return None

def build_exe():
    """Build executable using PyInstaller."""
    logger.info("Building executable with PyInstaller...")
    
    # Clean previous builds
    shutil.rmtree(DIST_DIR, ignore_errors=True)
    shutil.rmtree(BUILD_DIR, ignore_errors=True)
    
    # Create spec file
    spec_content = f"""
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['src/whispa_app/main.py'],
    pathex=['{ROOT_DIR}'],
    binaries=[],
    datas=[
        ('{ASSETS_DIR}', 'whispa_app/assets'),
    ],
    hiddenimports=[
        'customtkinter',
        'faster_whisper',
        'transformers',
        'huggingface_hub',
        'sentencepiece',
        'psutil'
    ],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='whispa',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='{ASSETS_DIR}/icon.ico'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='whispa'
)
"""
    
    spec_file = ROOT_DIR / "whispa.spec"
    spec_file.write_text(spec_content)
    
    # Run PyInstaller
    subprocess.run(
        [sys.executable, "-m", "PyInstaller", "whispa.spec", "--noconfirm"],
        check=True
    )
    
    # Clean up
    spec_file.unlink()

def build_installer():
    """Build installer using Inno Setup."""
    logger.info("Building installer with Inno Setup...")
    
    # Find Inno Setup compiler
    iscc = find_inno_setup()
    if not iscc:
        logger.error("Inno Setup not found. Please install Inno Setup 6.")
        sys.exit(1)
    
    # Create Inno Setup script
    iss_content = f"""
#define MyAppName "Whispa App"
#define MyAppVersion "2.2.0"
#define MyAppPublisher "Damilare Eniolabi"
#define MyAppURL "https://github.com/damoojeje/whispa_app"
#define MyAppExeName "whispa.exe"

[Setup]
AppId={{{{8A7D8AE1-5F9C-4F3B-8F7C-1A5D7E6A8B9C}}}}
AppName={{#MyAppName}}
AppVersion={{#MyAppVersion}}
AppPublisher={{#MyAppPublisher}}
AppPublisherURL={{#MyAppURL}}
AppSupportURL={{#MyAppURL}}
AppUpdatesURL={{#MyAppURL}}
DefaultDirName={{autopf}}\\{{#MyAppName}}
DisableProgramGroupPage=yes
LicenseFile={ROOT_DIR}\\LICENSE
OutputDir={DIST_DIR}
OutputBaseFilename=WhispaApp-Setup
SetupIconFile={ASSETS_DIR}\\icon.ico
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{{cm:CreateDesktopIcon}}"; GroupDescription: "{{cm:AdditionalIcons}}"

[Files]
Source: "{DIST_DIR}\\whispa\\*"; DestDir: "{{app}}"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{{autoprograms}}\\{{#MyAppName}}"; Filename: "{{app}}\\{{#MyAppExeName}}"
Name: "{{autodesktop}}\\{{#MyAppName}}"; Filename: "{{app}}\\{{#MyAppExeName}}"; Tasks: desktopicon

[Run]
Filename: "{{app}}\\{{#MyAppExeName}}"; Description: "{{cm:LaunchProgram,{{#StringChange(MyAppName, '&', '&&')}}}}"; Flags: nowait postinstall skipifsilent
"""
    
    iss_file = ROOT_DIR / "installer.iss"
    iss_file.write_text(iss_content)
    
    # Run Inno Setup compiler
    subprocess.run([str(iscc), "/Q", str(iss_file)], check=True)
    
    # Clean up
    iss_file.unlink()

def main():
    """Build both executable and installer."""
    try:
        build_exe()
        build_installer()
        logger.info(f"Installer created successfully at {DIST_DIR}/WhispaApp-Setup.exe")
    except subprocess.CalledProcessError as e:
        logger.error(f"Build failed: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 