from PIL import Image, ImageFilter

if __name__ == '__main__':
    img = Image.open('./Pokedex/pikachu.jpg')
    filtered_img = img.filter(ImageFilter.BLUR)
    filtered_img2 = img.filter(ImageFilter.SMOOTH)
    filtered_img3 = img.filter(ImageFilter.SHARPEN)

    print(img)#<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x1600C4AF400>
    print(img.format)#JPEG
    print(img.size)#(640, 640)
    print(img.mode)#RGB

    filtered_img = img.convert('L')#black and white

    filtered_img.save("grey.png", 'png')
    filtered_img2.save("blur.png", 'png')

