import asyncio
from aiolang import Translate

async def main():
    translator = Translate()
    request = await translator.translate("Hello, World!", "FA")
    print(request)

if __name__ == "__main__":
    asyncio.run(main())
