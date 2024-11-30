from typing import Dict
import aiohttp


class GoogleAPI:
    """Handles requests to the Google Translate API."""

    GOOGLE_TRANSLATE_URL = "https://translate.googleapis.com/translate_a/single"

    def __init__(self, text: str, target_lang: str, source_lang: str = "auto"):
        """Initializes the GoogleAPI class.

        Args:
            text (str): The text to be translated.
            target_lang (str): The target language code.
            source_lang (str): The source language code (default is 'auto').

        Raises:
            ValueError: If the input text is empty.
        """
        if not text:
            raise ValueError("No text provided for translation")

        self.text = text
        self.source_lang = source_lang
        self.target_lang = target_lang

    def _prepare_params(self) -> Dict[str, str]:
        """Prepares the request parameters for Google Translate API.

        Returns:
            dict: A dictionary with the necessary parameters for the API request.
        """
        return {
            "client": "gtx",
            "sl": self.source_lang,
            "tl": self.target_lang,
            "dt": "t",
            "q": self.text
        }

    async def _send_request(self, params: Dict[str, str]) -> Dict:
        """Sends the request to the Google Translate API asynchronously.

        Args:
            params (dict): The parameters to send in the request.

        Returns:
            dict: The JSON response from the API.

        Raises:
            ConnectionError: If there's a network issue.
            RuntimeError: For any other errors during the request.
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.GOOGLE_TRANSLATE_URL, params=params) as response:
                    response.raise_for_status()  # Will raise an exception for 4xx/5xx responses
                    return await response.json()
        except aiohttp.ClientError as err:
            raise ConnectionError(f"Network error occurred: {err}")
        except Exception as err:
            raise RuntimeError(f"An error occurred during the request: {err}")

    async def translate(self) -> str:
        """Translates the provided text using Google Translate API.

        Returns:
            str: The translated text.

        Raises:
            RuntimeError: If the translation request fails.
        """
        params = self._prepare_params()

        try:
            translation_data = await self._send_request(params)
            translated_text = translation_data[0][0][0]
            return translated_text
        except Exception as e:
            raise RuntimeError(f"Translation failed: {str(e)}")
