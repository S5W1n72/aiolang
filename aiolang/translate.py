from .google import GoogleAPI
from .langs import Langs
from .exceptions import TranslationError


class Translate:
    """Handles translation requests to Google Translate."""

    def __init__(self):
        """Initializes the Translate class."""
        pass

    async def translate(self, text: str, lang_target: str) -> str:
        """Translates text to the target language.

        Args:
            text (str): The text to translate.
            lang_target (str): The target language code.

        Returns:
            str: The translated text.

        Raises:
            TranslationError: If the input is invalid or translation fails.
        """
        if not text:
            raise TranslationError(
                "Input text cannot be empty", solution="Please provide a non-empty string."
            )

        if not isinstance(text, str):
            raise TranslationError(
                "The provided input is not a valid string", solution="Please provide a valid string input."
            )

        if len(text) > 5000:
            raise TranslationError(
                "Input text exceeds 5000 characters limit.",
                solution="Please provide text with fewer than 5000 characters."
            )

        if lang_target.lower() not in Langs.SUPPORTED_LANGUAGES:
            raise TranslationError(
                f"Language '{lang_target}' is not supported.",
                solution="Please choose a supported language from the list."
            )

        try:
            # Create GoogleAPI instance and get the translation
            api = GoogleAPI(text, lang_target)
            return await api.translate()
        except Exception as e:
            raise TranslationError(
                f"Translation failed: {str(e)}",
                solution="Ensure your network connection is stable and try again."
            )