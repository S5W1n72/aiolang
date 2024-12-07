<p align="center">
<img src="https://raw.githubusercontent.com/S5W1n72/aiolang/refs/heads/main/icon.png" alt="icon" width="128">
<br>

<b> Translate Google Framework For Python</b>
</p>

## aiolang

> Simple, modern, asynchronous for API building use or normal user use.

---

### Example Usage
#### Model 1
```python
import asyncio
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
```
#### Model 2
```python
import asyncio
from aiolang import Aiolang, TranslationError

async def main():
    aiolang = Aiolang()
    try:
        result = await aiolang.translate_text("hello", "fa")
        print(result)
    except TranslationError as log:
        log.display_error()

if __name__ == "__main__":
    asyncio.run(main())
```
---

### Key Features

- API:
>No key needed. Google translator public API is used.

- Easy:
>Simple appearance and syntax for novice users.

- Async:
>Written asynchronously for greater flexibility.

---

### Install

```bash
pip3 install -U aiolang
```

### support
- [email](mailto:aiolang.python@gmail.com)
- [telegram](https://t.me/aiolang)

<p align="center">
<img src="https://raw.githubusercontent.com/S5W1n72/aiolang/refs/heads/main/cover.png" alt="cover", width="360">
</p>
