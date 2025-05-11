import qrcode

img = qrcode.make("https://www.baidu.com")
print(type(img))
img.save("baidu.png")
# img.show()
