# -*- coding: UTF-8 -*-

import cv2
import math
import numpy as np
import os

if __name__ == '__main__':

    count = 0

    # 画像の読み込み
    img_src1 = cv2.imread("./img/image_01.jpg", 1)
    img_src2 = cv2.imread("./img/image_02.jpg", 1)

    # 背景画像との差分を算出
    img_diff = cv2.absdiff(img_src2, img_src1)

    #グレーに変更
    img_gray = cv2.cvtColor(img_diff, cv2.COLOR_BGR2GRAY)

    # 二値化
    img_binary= cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)[1]

    #jpgファイル生成
    cv2.imwrite('./img/img_gen.jpg', img_binary)

    #画素（高さ，幅，チャンネル数）を取得
    print (img_binary.shape)

    height, width = img_binary.shape
    print(width)
    print(height)

    for i in range(0, height):
        for j in range(0, width):
            pixel = img_binary[i, j]
            if int(pixel) != 0 :
                count+=1

    print count

    if count > 14000:
        print('物を忘れてますよ')
    else:
        print('忘れ物はないです')
