import base64
import collections
from io import BytesIO

import requests
from PIL import Image
from sklearn.externals import joblib


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
            if pixdata[x, y] != threshold:
                pixdata[x, y] = 255
                a = a + 1

            else:
                pixdata[x, y] = 0
                b = b + 1;

    if (b / a) < 0.05:
        print("阀值为：" + str(threshold));
        print(g)

    return img, b / a


def spit2():
    json = getimg()
    print(json)
    IMGCode = json['attachment']['IMGCode']
    codeUUID = json['attachment']['codeUUID']
    imgdata = base64.b64decode(IMGCode)
    image_data = BytesIO(imgdata)
    im = Image.open(image_data)

    dms = [];
    data = []
    im.show()
    for j in range(5):
        box = (20 * j, 00, (1 + j) * 20, 30)
        dm = im.crop(box)
        dm = dm.convert("L")
        dm, rate = iamge2imbw(dm)
        dms.append(dm)
        data.append(dm.getdata())
    return data, dms, codeUUID;


def getimg(url='https://www.chaoex.io/12lian/user/getimg'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    r = requests.post(url, headers=headers)

    return r.json();


def login(url, codid, vercode):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36,android'}
    email = '982973525@qq.com'
    pwd = 'E068C79304F7FE08CCA7D5B4137004DE'
    data = {'email': email,
            'pwd': pwd,
            'codeid': codid,
            'vercode': vercode,
            'source': 1
            }

    r = requests.post(url, data=data, headers=headers)
    return r.json()


def train():
    knn = joblib.load("knn.m")
    scaler = joblib.load("scaler.m")

    return knn, scaler


def train_real():
    knn, scaler = train();
    test_x, dms, codeUUID = spit2()
    scaler.transform(test_x)
    vercode = ''.join(knn.predict(test_x))
    print(codeUUID)
    print(vercode)

    #r = login('https://www.chaoex.io/12lian/user/loginGAFirst', codeUUID, vercode)
    #print(r)


if __name__ == '__main__':
    train_real();
