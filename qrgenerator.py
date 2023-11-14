import qrcode
features = qrcode.QRCode(version = 1,box_size=40,border=3)
print("enter data to be converted into qrcode")
data = input()
features.add_data(data)
features.make(fit=True)
generate_image = features.make_image(fill_color="black",back_color="white")
generate_image.save('qrcode.png')
