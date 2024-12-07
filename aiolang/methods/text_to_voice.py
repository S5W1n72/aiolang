import aiofiles
import aiohttp
from ..exceptions import TranslationError
from ..language.langs_voice import LangsVoice


class TextToVoice:
    """
    A class for converting text to voice using Google's Text-to-Speech service.

    Attributes:
        GOOGLE_URL (str): The URL endpoint for Google's Text-to-Speech API.
    """

    GOOGLE_URL = "https://translate.google.com/translate_tts"

    @staticmethod
    async def text_to_voice(source_lang: str, text: str, file_name: str) -> str:
        """
        Converts the given text into voice using Google's TTS service.

        Args:
            source_lang (str): The language code for the text.
            text (str): The text to convert into speech.
            file_name (str): The file name to save the audio.

        Raises:
            TranslationError: If the language is unsupported or the request fails.
            TranslationError: If the file format is not supported.
            TranslationError: If the text exceeds 5000 characters.

        Returns:
            str: A success message with the file name.
        """

        # Check if the provided language is supported
        if source_lang not in LangsVoice.SUPPORTED_LANGUAGES:
            raise TranslationError(
                "Language not supported.",
                solution="Please provide a valid language code.",
                level="Critical"
            )

        # Check if the file extension is valid
        if not (file_name.endswith('.mp3') or file_name.endswith('.ogg')):
            raise TranslationError(
                "Invalid file format.",
                solution="Only .mp3 and .ogg formats are supported.",
                level="Critical"
            )

        # Check if the text length is within the allowed limit (5000 characters)
        if len(text) > 5000:
            raise TranslationError(
                "Text exceeds the character limit.",
                solution="Please shorten your text to below 5000 characters.",
                level="Critical"
            )

        params = {
            "ie": "UTF-8",
            "client": "gtx",
            "q": text,
            "tl": source_lang,
        }

        # Make the request to the Google TTS API
        async with aiohttp.ClientSession() as session:
            async with session.get(TextToVoice.GOOGLE_URL, params=params) as response:
                if response.status == 200:
                    content = await response.read()
                    async with aiofiles.open(file_name, "wb") as file:
                        await file.write(content)
                    return f"Audio saved as '{file_name}'."
                raise TranslationError(
                    "Failed to retrieve data from TTS API.",
                    solution="Please try again later or check the API status.",
                    level="Warning"
                )