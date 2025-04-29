; WhispaAppInstaller.iss
[Setup]
AppName=Whispa App
AppVersion=2.1.0
AppPublisher=Damilare Eniolabi
AppPublisherURL=https://github.com/damoojeje/whispa_app
DefaultDirName={autopf}\WhispaApp
DefaultGroupName=Whispa App
OutputBaseFilename=WhispaApp-Setup
Compression=lzma2/ultra64
SolidCompression=yes
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
SetupIconFile=src\whispa_app\assets\icon.ico
WizardImageFile=src\whispa_app\assets\installer\wizard_image.bmp
WizardSmallImageFile=src\whispa_app\assets\installer\wizard_small.bmp

[Files]
; Main executable and dependencies
Source: "venv\Scripts\whispa.exe"; DestDir: "{app}"; Flags: ignoreversion

; Assets (icons)
Source: "src\whispa_app\assets\*"; DestDir: "{app}\assets"; Flags: recursesubdirs

; Python dependencies
Source: "venv\Lib\site-packages\*"; DestDir: "{app}\lib"; Excludes: "__pycache__"; Flags: recursesubdirs

[Icons]
Name: "{group}\Whispa App"; Filename: "{app}\whispa.exe"; IconFilename: "{app}\assets\icon.ico"
Name: "{commondesktop}\Whispa App"; Filename: "{app}\whispa.exe"; IconFilename: "{app}\assets\icon.ico"

[Run]
; Prefetch models after installation
Filename: "{app}\whispa.exe"; Parameters: "--prefetch"; Flags: runascurrentuser

; Launch app after install
Filename: "{app}\whispa.exe"; Description: "Launch Whispa App"; Flags: postinstall nowait