import qrcode
from PIL import Image

qr = qrcode.QRCode(version =1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size = 10,border=4,)

qr.add_data("https://i.im.ge/2024/10/13/kwJ9Fa.1000017266.jpeg")
qr.make(fit= True)

img = qr.make_image(fill_color ="Black",black_color="white")
img.save("divya.png")