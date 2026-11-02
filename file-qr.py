import qrcode

# لینک سایت دیگه‌ای که می‌خوایم تبدیل بشه
my_link = "https://ut.ac.ir"

# ساخت QR کد
qr = qrcode.make(my_link)

# ذخیره کردن عکس
qr.save("site_qr.png")

print("عکس QR کد ساخته شد!")