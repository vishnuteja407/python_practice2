from PIL import Image

mac = Image.open('data1.png')

# print(type(mac))

# print(mac.show())
print(mac.size)
# print(mac.format_description)
# print(mac.filename)

# print(mac.crop((0,0,100,100)).show())

x = 0
y = 0
w = 1706/3
h = 1174/10

print(mac.crop((x,y,w,h)).show())

# print(mac.crop((0, 900, w, 1174)).show())

# computer = mac.crop((0, 900, w, 1174))
# mac.paste(im=computer, box=(1500, 900))
# print(mac.show())

# print(mac.resize((3000, 500)).show())
# print(mac.rotate(90).show())

photo1 = Image.open('10_02_15.jpg')
photo1.putalpha(150)
print(photo1.show())

photo2 = Image.open('10_02_15.jpg')
photo2.putalpha(0)
print(photo2.show())

photo2.paste(im=photo1, box=(0,0), mask=photo1)
print(photo2.show())

photo2.save("test.png")
