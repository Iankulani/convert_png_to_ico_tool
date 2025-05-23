from PIL import Image

img = Image.open("picture.png")
img.save("app_icon.ico", format='ICO', sizes=[(256, 256)])
