#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import requests
import time

#ipカメラの映像をimgに保存
URL = "http://172.20.11.46/-wvhttp-01-/video.cgi"
s_video = cv2.VideoCapture(URL)
ret, img = s_video.read()

#ipカメラの映像をjpgファイルに保存
path = './img/photo.jpg'
cv2.imwrite(path,img)

#テキストファイルの読み込み
f = open('seat.txt')

#seatdataに席番号保存
seatdata = f.read()
f.close()

#席番号の表示
print seatdata

time.sleep(1)

'''
#hueに紐づけを行う
HUE_API = 'http://172.20.11.208/api/rwm9ymUfYdNgNJP5oONJePaam7bnqUBfgPRBrm1O/lights'

#hueを調光する
requests.put(HUE_API + '/2/state', json = {"on":True, "bri":1, "xy":[0.48, 0.41]})
'''
