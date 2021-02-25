import os
from PIL import Image

path = os.getcwd() + '\\'
extensions = ['jpg', 'jpeg', 'png', 'tiff', 'tif', 'bmp']

list_images = []
for i in os.listdir(path):
    if i[i.rfind(".") + 1:].lower() in extensions:
        list_images.append(i)

with open(path + '_Изображения_рекомендация.txt', 'a') as file:
    file.write('{: ^16} | {} | {: ^10} | {} | {: ^10} | {: ^10} | {: ^10}\n'.format('Имя файла',
                                                                                    'Расширение', 'Размеры',
                                                                                    'Цветовая модель',
                                                                                    'DPI', 'Печать, см', 'Решение'))

for i in list_images:
    advice = '+'
    img = Image.open(path + i)
    try:
        x1 = str(img.info['dpi'])
        x2 = str(round(img.size[0] / 300 * 2.54, 1)) + 'x' + str(round(img.size[1] / 300 * 2.54, 1))
        if round(img.size[0] / 300 * 2.54, 1) < 8:
            advice = 'Замена, W < 8 см'
        if round(img.size[1] / 300 * 2.54, 1) < 3:
            advice = 'Замена, H < 3 см'
    except:
        x1 = '(???, ???)'
        x2 = '???x???'
        advice = 'Заменить'
    with open(path + '_Изображения_рекомендация.txt', 'a') as file:
        file.write('{:<16.16} | {: ^10} | {: ^10} | {: ^15} | {: ^10} | {: ^10} | {: ^10}\n'.
                   format(i.rstrip('.' + i[i.rfind(".") + 1:]),
                          i[i.rfind(".") + 1:],
                          str(str(img.size[0]) + 'x' + str(img.size[1])),
                          img.mode,
                          x1, x2, advice))
