from PIL import Image
import pyautogui

img = Image.open('img/videogame.png', 'r')
w, h = img.size
pix = list(img.getdata())
image = [pix[n:n+w] for n in range(0, w*h, w)]

qtd = 0
x0 = 164
y0 = 238
pyautogui.hotkey('alt', 'tab')
for line in image:
    for pixels in line:
        rgb1 = str(pixels).replace('(',"")
        rgb2 = rgb1.replace(')',"")
        rgb = rgb2.split(',')
        r = (rgb[0])
        g = (rgb[1])
        b = (rgb[2])

        pyautogui.click(1086,82)
        pyautogui.doubleClick(872,458)
        pyautogui.write(r)
        pyautogui.doubleClick(880,475)
        pyautogui.write(g)
        pyautogui.doubleClick(875,498)
        pyautogui.write(b)
        pyautogui.click(766,532)
        pyautogui.click(497,531)

        pyautogui.click(x0, y0)
        x0 = x0 + 1
    x0 = 164
    y0 = y0 + 1


