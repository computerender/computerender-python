# Computerender Python Client

[![PyPI](https://img.shields.io/pypi/v/computerender.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/computerender)][pypi status]
![License](https://img.shields.io/pypi/l/computerender)

[![Tests](https://github.com/computerender/computerender-python/workflows/Tests/badge.svg)][tests]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/computerender/
[tests]: https://github.com/computerender/computerender-python/actions?workflow=Tests
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

Python client for using the computerender API.

## Updates

- v0.1: Improved Error handling
- v0.0: Img2img!

## Installation

```console
$ pip install computerender
```

## Examples

```python

from computerender import Computerender
import asyncio

cr = Computerender()

# Generate image and save to file
with open("cow.jpg", "wb") as f:
    img_bytes = asyncio.run(cr.generate("a cow wearing sunglasses"))
    f.write(img_bytes)

# Generate image with custom parameters
img_bytes = asyncio.run(cr.generate("testing", w=1024, h=384, iterations=20))

# img2img generation reading from and writing to files
with open("cow.jpg", "rb") as in_f:
    img_bytes = asyncio.run(
        cr.generate(
            "van gogh painting of a cow wearing sunglasses",
            img=in_f.read()
        )
    )
with open("van_gogh_cow.jpg", "wb") as out_f:
    out_f.write(img_bytes)

# img2img one-liner reading and writing to file
open("fly.jpg", "wb").write(asyncio.run(cr.generate("fly", img=open("cow.jpg", "rb").read())))

# Generate image and use it for img2img without saving anything to files
img_bytes = asyncio.run(
    cr.generate("testing", w=1024, h=384, iterations=20)
)
result_bytes = asyncio.run(
    cr.generate("testing style transfer", img=img_bytes)
)
```

"a cow wearing sunglasses"
<img src="https://i.imgur.com/nhEQtQo.jpg"
alt="a cow wearing sunglasses" width="256"/>

"van gogh painting of a cow wearing sunglasses"
<img src="https://i.imgur.com/0qV4YB2.jpg"
alt="van gogh painting of a cow wearing sunglasses" width="256"/>

## License

Distributed under the terms of the [MIT license][license]
