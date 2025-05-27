# Changelog

All notable changes to Whispa App will be documented in this file.

## [2.2.0] - 2025-05-26

### Added
- Progress bar updates during transcription
- Automatic CPU fallback when GPU is not available
- Better error handling and user feedback
- Telemetry improvements for tracking app usage and performance

### Fixed
- Fixed transcription device selection and compute type handling
- Fixed translation telemetry method naming
- Fixed progress bar updates during long operations
- Improved error messages and user feedback

### Changed
- Updated About dialog with new contact information
- Improved model loading with better device capability detection
- Enhanced UI responsiveness during long operations
- Better handling of translation errors

### Dependencies
- Added sacremoses package for improved translation support
- Updated requirements.txt with latest package versions

## [2.1.0] - 2025-05-25

### Added
- Initial release with basic transcription and translation functionality
- Support for multiple Whisper models (tiny, base, small, medium, large)
- Basic GUI with customizable theme
- File format support for WAV, MP3, M4A
- Translation support for multiple languages 