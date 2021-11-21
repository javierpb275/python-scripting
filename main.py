from PIL import Image, ImageFilter

if __name__ == '__main__':
    img = Image.open('./astro.jpg')
    img.thumbnail((400, 400))
    img.save('thumbnail.jpg')

    print(img.size)#(400, 381)


