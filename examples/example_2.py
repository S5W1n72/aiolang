import asyncio
from aiolang import Translate

async def main():
    translate = Translate()
    request = await translate("Hello, World!", "KO")
    print(request)

if __name__ == "__main__":
    asyncio.run(main())
