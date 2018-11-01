# -*- coding: UTF-8 -*-
import cv2
import math
import numpy as np
import os
import requests
import time

#import win32com.client  # ライブラリをインポート

if __name__ == '__main__':

    chairNum = 0
    count = 0

    #ipカメラの映像をimgに保存
    #URL = "http://172.20.11.46/-wvhttp-01-/video.cgi"


    URL = "http://172.20.11.41:80/snapshot.cgi"
    s_video = cv2.VideoCapture(URL)
    ret, img = s_video.read()

    #ipカメラの映像をjpgファイルに保存
    path = "./img/image_02.jpg"
    cv2.imwrite(path,img)

    #IPカメラの画像を取ってくる処理はここまで

    time.sleep(2)
    '''
    #テキストファイルの読み込み
    f = open('seat.txt')

    #seatdataに席番号保存
    seatdata = f.read()
    seatdata = int(seatdata)
    f.close()

    #席番号の表示
    print seatdata
    '''
    # 画像の読み込み
    img_src1 = cv2.imread('./img/image_01.jpg', 1)
    img_src2 = cv2.imread('./img/image_02.jpg', 1)

    # 背景画像との差分を算出
    img_diff = cv2.absdiff(img_src2, img_src1)
    cv2.imwrite('./img/img_diff.jpg', img_diff)

    #グレーに変更
    img_gray = cv2.cvtColor(img_diff, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('./img/img_gray.jpg', img_gray)

    # 二値化
    img_binary = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)[1]
    img_binary2 = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)[1]

    # 膨張処理、収縮処理を施してマスク画像を生成
    operator = np.ones((3, 3), np.uint8)
    img_dilate = cv2.dilate(img_binary2, operator, iterations=4)
    img_binary2 = cv2.erode(img_dilate, operator, iterations=4)

    cv2.imwrite('./img/img_binary2_0.jpg', img_binary2)

    #jpgファイル生成
    cv2.imwrite('./img/img_gen.jpg', img_binary)

    #画素（高さ，幅，チャンネル数）を取得
    print (img_binary.shape)

    contoured = cv2.imread("./img/image_02.jpg", 1)
    forcrop = cv2.imread("./img/image_02.jpg", 1)

    #contoured = contoured[0:500,500:1000]
    #forcrop = forcrop[0:500,500:1000]

    im2, contours, hierarchy = cv2.findContours(img_binary2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #contours, hierarchy= cv2.findContours(img_binary2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    crops = []
    #ここ変える
    min_size = 10000
    obj_num = 0

    def padding_position(x, y, w, h, p):
        return x - p, y - p, w + p * 2, h + p * 2

    for c in contours:
        print cv2.contourArea(c)
        if cv2.contourArea(c) < min_size:
            continue
        obj_num += 1
        # rectangle area
        x, y, w, h = cv2.boundingRect(c)
        x, y, w, h = padding_position(x, y, w, h, 5)
        # crop the image
        cropped = forcrop[y:(y + h), x:(x + w)]
        #cropped = resize_image(cropped, (210, 210))
        crops.append(cropped)
        # draw contour
        cv2.drawContours(contoured, c, -1, (0, 0, 255), 3)  # contour
        cv2.rectangle(contoured, (x, y), (x + w, y + h), (0, 255, 0), 3)  #rectangle contour

    cv2.imwrite('./img/contoured.jpg', contoured)
    print('obj_num ↓ ')
    print(obj_num)

    HUE_API = 'http://172.20.11.175/api/rwm9ymUfYdNgNJP5oONJePaam7bnqUBfgPRBrm1O/lights'
    #HUE_API = 'http://172.20.11.100/api/63ZZIKaPKgHxO3KBsJhz2NMn3t5ftZsjjG1mEDME/lights'

    if obj_num >= 1:
        #赤
        requests.put(HUE_API + '/2/state', json = {"on":True, "bri":1, "xy":[0.66,0.31]})
    else:
        #青
        requests.put(HUE_API + '/2/state', json = {"on":True, "bri":1, "xy":[0.18,0.06]})

    """
    #緑
    requests.put(HUE_API + '/2/state', json = {"on":True, "bri":1, "xy":[0.10, 0.80]})
    height, width = img_binary.shape

    print(width)
    print(height)

    for i in range(0, height):
        for j in range(0, width):
            pixel = img_binary[i, j]
            if int(pixel) != 0 :
                count+=1

    print (count)

    if count > 14000:
        print('物を忘れてますよ')
    else:
        print('忘れ物はないです')

    cluster = [[-1 for x in range(width)] for y in range(height)]
    cluster_cnt = 0

    #クラスタに分ける
    for y in range(0, height, 1):
        for x in range(0, width, 1):
            if img_binary2[y, x] > 0:
                if y-1 > 0 and cluster[y-1][x] > -1:
                    cluster[y][x] = cluster[y-1][x]
                if x-1 > 0 and cluster[y][x-1] > -1:
                    cluster[y][x] = cluster[y][x-1]
                if cluster[y][x] < 0:
                    cluster_cnt += 1
                    cluster[y][x] = cluster_cnt

    print(cluster_cnt)

    for y in range(height-1, 0, -1):
        for x in range(width-1, 0, -1):
            if img_binary2[y, x] > 0:
                if y-1 > 0 and cluster[y-1][x] > -1:
                    cluster[y-1][x] = cluster[y][x]
                if x-1 > 0 and cluster[y][x-1] > -1:
                    cluster[y][x-1] = cluster[y][x]

    print('aaa')
    clu_ele_num = [0 for i in range(cluster_cnt+1)]

    #クラスタの数数える
    for y in range(0, height, 1):
        for x in range(0, width, 1):
            if cluster[y][x] > -1:
                clu_ele_num[cluster[y][x]] += 1

    pix_num = 4000
    cnt = 0
    for i in range(0, cluster_cnt, 1):
        if clu_ele_num[i] > pix_num:
            cnt += 1
            print(clu_ele_num[i])
    print (cnt)

    #小さいクラスタを無視
    for y in range(0, height, 1):
        for x in range(0, width, 1):
            if cluster[y][x] > -1 and clu_ele_num[cluster[y][x]] < pix_num:
                img_binary2[y, x] = 0

    cv2.imwrite("./img/img_binary.jpg", img_binary)
    cv2.imwrite("./img/img_binary2.jpg", img_binary2)
    """
