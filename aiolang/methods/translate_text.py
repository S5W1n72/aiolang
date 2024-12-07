import aiohttp
from ..exceptions import TranslationError
from ..language.langs_text import LangsText


class TranslateText:
    """
    A class for translating text from a source language to a target language using Google's translation service.
    Supports asynchronous requests to the Google Translation API.

    Attributes:
        GOOGLE_URL (str): The URL endpoint for Google's Translation API.
    """

    GOOGLE_URL = "https://translate.googleapis.com/translate_a/single"

    @staticmethod
    async def translate(text: str, target_lang: str, source_lang: str = "auto") -> str:
        """
        Translates the given text from the source language to the target language using Google's Translation API.

        Args:
            text (str): The text to translate.
            target_lang (str): The language code for the translation output.
            source_lang (str, optional): The language code of the source text. Defaults to "auto" to detect automatically.

        Raises:
            TranslationError: If the source or target language is unsupported.
            TranslationError: If the text exceeds 5000 characters.

        Returns:
            str: The translated text.
        """

        # Check if the source language is supported (if not 'auto')
        if source_lang != "auto" and source_lang not in LangsText.SUPPORTED_LANGUAGES:
            raise TranslationError(
                f"Source language '{source_lang}' is not supported.",
                solution="Please provide a valid source language code.",
                level="Critical"
            )

        if target_lang not in LangsText.SUPPORTED_LANGUAGES:
            raise TranslationError(
                f"Target language '{target_lang}' is not supported.",
                solution="Please provide a valid target language code.",
                level="Critical"
            )

        # Check if the text is too long
        if len(text) > 5000:
            raise TranslationError(
                "Text exceeds the maximum allowed length of 5000 characters.",
                solution="Please shorten the text to be translated.",
                level="Critical"
            )

        params = {
            "client": "gtx",
            "sl": source_lang,
            "tl": target_lang,
            "dt": "t",
            "q": text
        }

        try:
            # Make an asynchronous request to the translation API
            async with aiohttp.ClientSession() as session:
                async with session.get(TranslateText.GOOGLE_URL, params=params) as response:
                    if response.status != 200:
                        raise TranslationError(
                            f"Failed to fetch translation. Status code: {response.status}",
                            solution="Please try again later.",
                            level="Critical"
                        )

                    translation = await response.json()
                    return translation[0][0][0]

        except aiohttp.ClientError as e:
            raise TranslationError(
                f"An error occurred while making the request: {str(e)}",
                solution="Please check your internet connection or try again later.",
                level="Critical"
            )