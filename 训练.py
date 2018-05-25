import time

import pymouse, pykeyboard, os, sys
from PIL import ImageGrab
from pymouse import *
from pykeyboard import PyKeyboard

from sklearn import preprocessing, neighbors, svm

from 工具 import iamge2imbw, createData1

k = PyKeyboard()
xx, yy = createData1();

begin = int(time.time())


def train():
    X, y = createData1()
    scaler = preprocessing.StandardScaler().fit(X)
    scaler.transform(X)
    knn = neighbors.KNeighborsClassifier(n_neighbors=2,n_jobs=2)
    # knn = svm.SVC()

    knn.fit(X, y)
    return knn, scaler


knn, scaler = train();
time.sleep(2)

k.tap_key(k.space)

time.sleep(4)

last = None
for i in range(50):
    im = ImageGrab.grab((800, 300, 2100, 600))
    w, h = im.size
    im.thumbnail((w // 4, h // 4))
    im = iamge2imbw(im, 0)
    box = (0, 40, 200, 70)

    dm = im.crop(box)
    test_data = [dm.getdata()];
    scaler.transform(test_data)
    p = knn.predict(test_data)
    t = str(int(time.time()) - begin) + '_' + str(int(time.time() * 1000))
    print(t)
    print(p)

    if p[0] == 'yes':
        k.tap_key(k.space)
        last = 1
        print('yes/yes_' + t + ".png")
        #im.save('yes/yes_' + t + ".png")
        #time.sleep(0.6)
    else:
        print("x")
        #im.save('data/no_' + t + ".png")
