"""Download required models for Whispa App."""

import os
import sys
import logging
from pathlib import Path
from typing import Optional
from concurrent.futures import ThreadPoolExecutor
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqGeneration
from faster_whisper import download_model

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Model configurations
WHISPER_MODELS = {
    "tiny": {"size": 150},    # ~150MB
    "base": {"size": 290},    # ~290MB
    "small": {"size": 461},   # ~461MB
    "medium": {"size": 1500}, # ~1.5GB
    "large": {"size": 2900}   # ~2.9GB
}

TRANSLATION_MODELS = {
    "English": "Helsinki-NLP/opus-mt-ROMANCE-en",
    "Spanish": "Helsinki-NLP/opus-mt-en-es",
    "French": "Helsinki-NLP/opus-mt-en-fr",
    "German": "Helsinki-NLP/opus-mt-en-de",
    "Chinese": "Helsinki-NLP/opus-mt-en-zh",
    "Japanese": "Helsinki-NLP/opus-mt-en-jap"
}

def get_cache_dir() -> Path:
    """Get the cache directory for models."""
    if sys.platform == "win32":
        base = Path(os.getenv("LOCALAPPDATA", "")) / "WhispaApp"
    else:
        base = Path.home() / ".cache" / "whispa_app"
    return base / "models"

def download_whisper_model(model_name: str, cache_dir: Optional[Path] = None) -> bool:
    """
    Download a Whisper model.
    
    Args:
        model_name: Name of the model to download
        cache_dir: Optional cache directory
        
    Returns:
        bool: True if successful
    """
    try:
        logger.info(f"Downloading Whisper model: {model_name}")
        download_model(
            model_name,
            cache_dir=str(cache_dir) if cache_dir else None,
            local_files_only=False
        )
        return True
    except Exception as e:
        logger.error(f"Failed to download Whisper model {model_name}: {e}")
        return False

def download_translation_model(lang: str, model_name: str, cache_dir: Optional[Path] = None) -> bool:
    """
    Download a translation model.
    
    Args:
        lang: Target language
        model_name: HuggingFace model name
        cache_dir: Optional cache directory
        
    Returns:
        bool: True if successful
    """
    try:
        logger.info(f"Downloading translation model for {lang}")
        AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
        AutoModelForSeq2SeqGeneration.from_pretrained(model_name, cache_dir=cache_dir)
        return True
    except Exception as e:
        logger.error(f"Failed to download translation model for {lang}: {e}")
        return False

def download_all_models(
    whisper_models: list[str] = ["tiny", "base", "small"],
    translation_langs: list[str] = ["English", "Spanish"],
    cache_dir: Optional[Path] = None,
    max_workers: int = 2
) -> bool:
    """
    Download all required models.
    
    Args:
        whisper_models: List of Whisper models to download
        translation_langs: List of translation languages
        cache_dir: Optional cache directory
        max_workers: Maximum number of concurrent downloads
        
    Returns:
        bool: True if all downloads successful
    """
    if cache_dir is None:
        cache_dir = get_cache_dir()
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    success = True
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Download Whisper models
        whisper_futures = [
            executor.submit(download_whisper_model, model, cache_dir)
            for model in whisper_models
        ]
        
        # Download translation models
        translation_futures = [
            executor.submit(download_translation_model, lang, TRANSLATION_MODELS[lang], cache_dir)
            for lang in translation_langs if lang in TRANSLATION_MODELS
        ]
        
        # Wait for completion
        for future in whisper_futures + translation_futures:
            if not future.result():
                success = False
                
    return success

def main():
    """Command-line interface."""
    import argparse
    parser = argparse.ArgumentParser(description="Download models for Whispa App")
    parser.add_argument(
        "--models",
        nargs="+",
        choices=list(WHISPER_MODELS.keys()),
        default=["tiny", "base", "small"],
        help="Whisper models to download"
    )
    parser.add_argument(
        "--languages",
        nargs="+",
        choices=list(TRANSLATION_MODELS.keys()),
        default=["English", "Spanish"],
        help="Translation languages to download"
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        help="Custom cache directory"
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=2,
        help="Maximum concurrent downloads"
    )
    
    args = parser.parse_args()
    success = download_all_models(
        args.models,
        args.languages,
        args.cache_dir,
        args.max_workers
    )
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main() 