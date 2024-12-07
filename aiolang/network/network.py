# Directory: aiolang/network
# File: network.py
from typing import Optional, Dict, Any
import aiohttp
from ..exceptions import TranslationError


class Network:
    """Handles network requests using aiohttp.

    This class provides a static method to perform GET requests
    with proper error handling and detailed exception messages.
    """

    @staticmethod
    async def request(url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Perform an asynchronous GET request.

        Args:
            url (str): The URL to send the GET request to.
            params (Optional[Dict[str, Any]]): Parameters to include in the request.

        Returns:
            Dict[str, Any]: The JSON response from the server if the request is successful.

        Raises:
            TranslationError: Custom error with level, message, and solution details.
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        return response
                    raise TranslationError(
                        f"Unexpected response status: {response.status}",
                        solution="Verify the API endpoint and parameters",
                        level="Warning",
                    )
        except aiohttp.ClientConnectionError as error:
            raise TranslationError(
                f"Client connection error occurred: {error}",
                solution="Check your internet connection or the URL",
                level="Critical",
            )
        except aiohttp.ClientResponseError as error:
            raise TranslationError(
                f"Client response error: {error}",
                solution="Ensure the server is reachable and the URL is correct",
                level="Warning",
            )
        except aiohttp.InvalidURL:
            raise TranslationError(
                "The URL provided is invalid",
                solution="Check the URL formatting and structure",
                level="Info",
            )
        except aiohttp.ClientPayloadError as error:
            raise TranslationError(
                f"Payload error while processing the response: {error}",
                solution="Ensure the server is returning a valid payload",
                level="Warning",
            )