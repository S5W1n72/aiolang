from .methods.translate_text import TranslateText
from .methods.text_to_voice import TextToVoice


class Aiolang:
    """
    A class that provides translation and text-to-speech functionality.
    """

    def __init__(self):
        """
        Initializes the Aiolang object.
        """
        pass

    async def __aenter__(self):
        """
        Initializes the contact manager when entering the async context.

        Returns:
            Aiolang: The Aiolang instance with the initialized contact manager.
        """
        self._contact_manager = await self._initialize_contact_manager()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Handles cleanup when exiting the async context.
        """
        await self._cleanup_contact_manager()

    async def translate_text(self, text: str, target_lang: str, source_lang: str = "auto") -> str:
        """
        Calls the static method translate() from the TranslateText class.

        Args:
            text (str): The text to translate.
            target_lang (str): The target language code.
            source_lang (str): The source language code, default is 'auto'.

        Returns:
            str: The translated text.
        """
        return await TranslateText.translate(text, target_lang, source_lang)

    async def text_to_voice(self, source_lang: str, text: str, file_name: str) -> str:
        """
        Calls the static method text_to_voice() from the TextToVoice class.

        Args:
            source_lang (str): The source language code.
            text (str): The text to convert to speech.
            file_name (str): The output file name for the audio.

        Returns:
            str: Path or identifier for the generated audio file.
        """
        return await TextToVoice.text_to_voice(source_lang, text, file_name)

    async def _initialize_contact_manager(self):
        """
        Initializes the contact manager for the Aiolang instance.

        Returns:
            object: The initialized contact manager.
        """
        # Placeholder for actual contact manager initialization logic
        return "initialized_contact_manager"

    async def _cleanup_contact_manager(self):
        """
        Cleans up the contact manager when exiting the context.
        """
        # Placeholder for contact manager cleanup logic
        pass
