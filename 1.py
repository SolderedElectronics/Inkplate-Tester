from PIL import Image
from thermalprinter import *

with ThermalPrinter(port='/dev/cu.usbserial-0001') as printer:
    # Picture
    printer.image(Image.open('/Users/nitkonitkic/Downloads/Webp.net-resizeimage(2).png'))

    # Bar codes
    printer.barcode_height(80)
    printer.barcode_position(BarCodePosition.BELOW)
    printer.barcode_width(3)
    printer.barcode('012345678901', BarCode.EAN13)

    # Styles
    printer.out('Bold', bold=True)
    printer.out('Double height', double_height=True)
    printer.out('Double width', double_width=True)
    printer.out('Inverse', inverse=True)
    printer.out('Rotate 90°', rotate=True, codepage=CodePage.ISO_8859_1)
    printer.out('Strike', strike=True)
    printer.out('Underline', underline=1)
    printer.out('Upside down', upside_down=True)

    # Chinese (almost all alphabets exist)
    printer.out('现代汉语通用字表', chinese=True,
                chinese_format=Chinese.UTF_8)

    # Greek (excepted the ΐ character)
    printer.out('Στην υγειά μας!', codepage=CodePage.CP737)

    # Accents
    printer.out('Voilà !', justify='C', strike=True,
                underline=2, codepage=CodePage.ISO_8859_1)

    # Line feeds
    printer.feed(2)
