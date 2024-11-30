from .google import GoogleAPI
from .langs import Langs
from .exceptions import TranslationError

class Translate:
    """Handles translation requests to Google Translate."""

    def __init__(self) -> None:
        """Initializes the Translate class."""
        pass

    async def __aenter__(self):
        """Called when entering an async context (async with)."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting an async context (async with)."""
        pass

    async def __call__(self, text: str, target_lang: str, source_lang: str = "auto") -> str:
        """
        Allows the Translate object to be used as a callable function.
        This method translates the text to the target language when called directly.
        """
        return await self.translate(text, target_lang, source_lang)

    async def translate(self, text: str, target_lang: str, source_lang: str = "auto") -> str:
        """Translates text to the target language."""
        if not isinstance(text, str) or not text:
            raise TranslationError(
                "Input text must be a non-empty string.", solution="Please provide a valid string."
            )

        if len(text) > 5000:
            raise TranslationError(
                "Input text exceeds 5000 characters limit.",
                solution="Please provide text with fewer than 5000 characters."
            )

        supported_languages = Langs.SUPPORTED_LANGUAGES
        if target_lang.lower() not in supported_languages:
            raise TranslationError(
                f"Target language '{target_lang}' is not supported.",
                solution="Please choose a supported target language from the list."
            )

        if source_lang.lower() != "auto" and source_lang.lower() not in supported_languages:
            raise TranslationError(
                f"Source language '{source_lang}' is not supported.",
                solution="Please choose a supported source language from the list or use 'auto'."
            )

        try:
            api = GoogleAPI(text, target_lang, source_lang)
            return await api.translate()
        except Exception as error:
            raise TranslationError(
                f"Translation failed: {str(error)}",
                solution="Ensure your network connection is stable and try again."
            )
