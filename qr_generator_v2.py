# pip install qrcode
# librería para la generación del qr

# pip install Pillow
# librería para la manipulación de imágenes

import qrcode

# data corresponde a la información contenida en el qr
data = 'https://www.python.org/'

# por defecto
img = qrcode.make(data)
# ruta donde se guarda
img.save('D:/Pyhon_Projects/proj_03_QR_Code_v2/QR_Generado/MyQR.png')

# personalización de valores
qr = qrcode.QRCode(version=1, box_size=8, border=2)
qr.add_data(data)
qr.make(fit=True)
# img = qr.make_image(fill_color='red', back_color='black')
# los colores se pueden indicar con su nombre o valor hexadecimal
img = qr.make_image(fill_color='#007FAB', back_color='#ffffff80')

# ruta donde se guarda
img.save('D:/Pyhon_Projects/proj_03_QR_Code_v2/QR_Generado/MyQR2.png')
