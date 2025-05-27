# Whispa App

A powerful GUI application for audio transcription and translation using OpenAI's Whisper model.

## Features

- Transcribe audio files (WAV, MP3, M4A) to text
- Translate transcriptions to multiple languages
- Modern, customizable dark/light theme interface
- Progress tracking for long operations
- Automatic CPU/GPU detection and optimization
- Support for all Whisper model sizes (tiny to large)
- Local model caching for offline use
- Detailed error reporting and user feedback

## Installation

### From PyPI (Recommended)
```bash
pip install whispa-app
```

### From Source
```bash
git clone https://github.com/damoojeje/Whispa_App.git
cd Whispa_App
pip install -r requirements.txt
python -m whispa_app.main
```

### Windows Installer
Download the latest installer from the [Releases](https://github.com/damoojeje/Whispa_App/releases) page.

## Usage

1. Launch the app:
   ```bash
   whispa-app
   ```
   Or if installed from source:
   ```bash
   python -m whispa_app.main
   ```

2. Select an audio file using the "Browse" button
3. Choose a model size (larger = more accurate but slower)
4. Click "Transcribe" to start processing
5. Once transcribed, select a target language and click "Translate"
6. Use the "Save" buttons to export results

## System Requirements

- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- GPU support (optional):
  - NVIDIA GPU with CUDA support
  - 6GB VRAM recommended for large models

## Contact & Support

- Developer: Damilare Eniolabi
- Email: damilareeniolabi@gmail.com
- Website: www.eniolabi.com
- GitHub: https://github.com/damoojeje/Whispa_App

## License

MIT License - see LICENSE file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.