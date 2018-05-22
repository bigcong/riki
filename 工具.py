import collections
import os

from PIL import Image


def iamge2imbw(img, inde=1):
    """传入image对象进行灰度、二值处理"""
    img = img.convert("L")  # 转灰度
    pixdata = img.load()
    w, h = img.size
    # 遍历所有像素，大于阈值的为黑色
    total = 0
    a = 0;
    b = 1;

    gg = []
    for y in range(h):
        for x in range(w):
            gg.append(pixdata[x, y])

    g = collections.Counter(gg)

    threshold = list(g.most_common())[inde][0]

    for y in range(h):
        for x in range(w):
            if pixdata[x, y] == threshold:
                pixdata[x, y] = 255
                a = a + 1

            else:
                pixdata[x, y] = 0
                b = b + 1;

    if (b / a) < 0.05:
        print("阀值为：" + str(threshold));
        print(g)
    return img


def yes_or_no(path='/Users/cc/cc/riki/data/1526976909512.png'):
    im = Image.open(path)
    im = iamge2imbw(im, 0)
    im.show()

    print(im.size)
    box = (0, 120, 650, 126)
    dm = im.crop(box)
    print(dm.size)
    dm.show()


if __name__ == '__main__':
    lists = os.listdir('/Users/cc/cc/riki/data')
    for l in lists:
        yes_or_no(l)
