from PIL import Image

word = Image.open("Word_matrix.png")
print(word.size)

mask = Image.open("mask.png")
# print(mask.size)
new_mask = mask.resize((1015, 559))
new_mask.putalpha(128)
# print(new_mask.show())
print(new_mask.size)

word.paste(im=new_mask, box=(0,0), mask=new_mask)
print(word.show())