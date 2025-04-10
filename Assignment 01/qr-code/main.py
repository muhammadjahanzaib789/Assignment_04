import qrcode
import image
qr = qr.code.QRCode(
    version=15,
    box_size =10,
    border =5

)

data  = "https://www.youtube.com/results?search_query=humanitarian"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color ="white")
img.save("test.png")