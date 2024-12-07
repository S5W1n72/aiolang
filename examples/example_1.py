import asyncio
from aiolang import Aiolang, TranslationError

async def main():
    async with Aiolang() as aiolang:
        try:
            result = await aiolang.translate_text("hello", "fa")
            print(result)
        except TranslationError as log:
            log.display_error()

if __name__ == "__main__":
    asyncio.run(main())
