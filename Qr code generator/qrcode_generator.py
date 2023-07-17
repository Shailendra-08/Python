import qrcode

data = "Hello, this is a test QR code."
qr = qrcode.make(data)
qr.save("test_qrcode.png")
