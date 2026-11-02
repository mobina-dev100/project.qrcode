import qrcode

my_link = "https://ut.ac.ir"

qr = qrcode.make(my_link)

qr.save("site_qr.png")

print("عکس QR کد ساخته شد!")
