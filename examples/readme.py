"""The example from the readme as a script for testing purposes."""

import asyncio

from computerender import Computerender


cr = Computerender()

# generate image and save to file

with open("cow.jpg", "wb") as f:
    img_bytes = asyncio.run(cr.generate("cool cow party"))
    f.write(img_bytes)

# generate image with custom parameters
img_bytes = asyncio.run(cr.generate("testing", w=1024, h=384, iterations=20))

# img2img generation reading from and writing to files

with open("cow.jpg", "rb") as in_f:
    img_bytes = asyncio.run(cr.generate("anime cow party", img=in_f.read()))

with open("anime_cow.jpg", "wb") as out_f:
    out_f.write(img_bytes)

# img2img one-liner reading and writing to file

open("fly.jpg", "wb").write(
    asyncio.run(cr.generate("fly", img=open("cow.jpg", "rb").read()))
)

# generate image and use it for img2img without saving anything to files

img_bytes = asyncio.run(cr.generate("testing", w=1024, h=384, iterations=20))

result_bytes = asyncio.run(cr.generate("testing style transfer", img=img_bytes))
