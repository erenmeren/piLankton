#!/usr/bin/env python3
from PIL import Image
from inky import InkyWHAT
from time import sleep

inky_display = InkyWHAT('black')
inky_display.set_border(inky_display.WHITE)

images = [ 'assests/images/folder-download.png',
            'assests/images/folder-upload.png',
            'assests/images/wifi-connect.png',
            'assests/images/wifi-disconnect.png',
            'assests/images/logo_1.png',
            'assests/images/logo_2.png',
        ]

for x in images:
  
  image = Image.open(x)
  w, h = image.size

  wHat_w = 400
  wHat_h = 300

  img = Image.new("P", (wHat_w, wHat_h), 0xFF)

  img.paste(image, (int((wHat_w - w) / 2) , int((wHat_h - h) / 2)) )

  inky_display.set_image(img)
  inky_display.show()

  sleep(2)


