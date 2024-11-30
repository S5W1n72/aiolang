import asyncio
from aiolang import Translate

async def main():
    async with Translate() as translate:
        request = await translate.translate("Hello, World!", "KO")
        print(request)

if __name__ == "__main__":
    asyncio.run(main())
