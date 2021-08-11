#!/usr/bin/env python3
from PIL import Image
from inky import InkyWHAT

class Draw:

  @staticmethod
  def logo():

    inky_display = InkyWHAT('black')
    inky_display.set_border(inky_display.BLACK)

    image = Image.open('assests/images/logo_1.png')
    w, h = image.size

    wHat_w = 400
    wHat_h = 300

    img = Image.new("P", (wHat_w, wHat_h), 0xFF)

    img.paste(image, (int((wHat_w - w) / 2) , int((wHat_h - h) / 2)) )

    inky_display.set_image(img)
    inky_display.show()

  @staticmethod
  def qr_barcode():
    
    inky_display = InkyWHAT('black')
    inky_display.set_border(inky_display.WHITE)

    w=400
    h=300

    qrCode = Image.open("code.png").convert("RGBA")
    # qrCode_w = qrCode.size[0] # 225
    # qrCode_h = qrCode.size[1] # 225

    img = Image.new("P", (w, h), 0xFF)
    # draw = ImageDraw.Draw(img)

    img.paste(qrCode, ( 87 , 37 ))

    inky_display.set_image(img)
    inky_display.show()