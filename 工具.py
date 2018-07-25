import collections
import numpy as np
import os

from PIL import Image

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


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
    print(path)
    im = Image.open(path)

    im = iamge2imbw(im, 0)

    box = (0, 120, 300, 125)
    dm = im.crop(box)
    dm.show()
    w, h = dm.size
    pixdata = dm.load()
    l = []

    for i in range(h):
        longs = []
        for j in range(w):
            if pixdata[j, i] == 0:
                longs.append(j)

        l.append(test(longs))
    return float(sum(l)) / len(l)


def test(a):
    begin = 0;
    reuslt = []
    flag = a[0]
    for index, aa in enumerate(a):
        f = aa - flag
        if f > 10 or len(a) == index + 1:
            seq = a[begin:index]
            reuslt.append(float(sum(seq)) / len(seq))
            begin = index

        flag = aa

    if len(reuslt) < 2:
        return 650
    else:
        return reuslt[1] - reuslt[0]


def createData1(path='train/'):
    xx = []
    yy = []
    lists = os.listdir(path)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort()

    for i in lists:
        im = Image.open(path + i)
        l = i.split("_");

        box = (0, 40, 200, 70)
        im = im.crop(box)
        # im.show()

        data = im.getdata()

        # data = np.matrix(data, dtype='float')   # 转换成矩阵
        yy.append(l[0])
        xx.append(np.array(data))
    pca = PCA(n_components=2)


    return xx, yy


if __name__ == '__main__':
    xx, yy = createData1()
    pca = PCA(n_components=2)

    colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']
    xx = pca.fit_transform(xx)

    for index, i in enumerate(yy):

        if i == 'no':
            plt.scatter(xx[index][0], xx[index][1], c='yellow');
        elif i == 'yes':
            plt.scatter(xx[index][0], xx[index][1], c='black');

        else:
            plt.scatter(xx[index][0], xx[index][1], c='blue');
    plt.show()
