from PIL import Image, ImageFilter

if __name__ == '__main__':
    img = Image.open('./Pokedex/pikachu.jpg')
    filtered_img = img.convert('L')
    #crooked = filtered_img.rotate(90)
    # crooked.save("grey.png", 'png')
    #resize = filtered_img.resize((300, 300))
    #resize.save("grey.png", 'png')

    box = (100, 100, 400, 400)
    region = filtered_img.crop(box)
    region.save("grey.png", 'png')

    region.show()#show image


