# -*- coding: utf-8 -*-
import requests
import time

chairNum = 0

count = 0

#HUE_API = 'http://172.20.11.175/api/rwm9ymUfYdNgNJP5oONJePaam7bnqUBfgPRBrm1O/lights'
HUE_API = 'http://172.20.11.100/api/63ZZIKaPKgHxO3KBsJhz2NMn3t5ftZsjjG1mEDME/lights'

#緑
#requests.put(HUE_API + '/4/state', json = {"on":True, "bri":1, "xy":[0.10, 0.80]})

#赤
#requests.put(HUE_API + '/4/state', json = {"on":True, "bri":100, "xy":[0.66,0.31]})

#青
requests.put(HUE_API + '/4/state', json = {"on":True, "bri":100, "xy":[0.18,0.06]})

'''
#ipカメラの映像をimgに保存
#URL = "http://172.20.11.46/-wvhttp-01-/video.cgi"
URL = "http://172.20.11.41:80/snapshot.cgi"
s_video = cv2.VideoCapture(URL)
ret, img = s_video.read()

#ipカメラの映像をjpgファイルに保存
path = "./img/photo.jpg"
cv2.imwrite(path,img)

#テキストファイルの読み込み
f = open('seat.txt')

#seatdataに席番号保存
seatdata = f.read()
seatdata = int(seatdata)
f.close()

#席番号の表示
print seatdata

# 画像の読み込み
img_src1 = cv2.imread('./img/image_01.jpg', 1)
img_src2 = cv2.imread('./img/image_02.jpg', 1)

if seatdata == 2:
    cv2.imwrite('./img/tes.jpg', img_src1)

#img_src1 = img_src1[0:500,500:1000]
#img_src2 = img_src2[0:500,500:1000]

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

contoured = cv2.imread("./img/image_01.jpg", 1)
forcrop = cv2.imread("./img/image_01.jpg", 1)

#contoured = contoured[0:500,500:1000]
#forcrop = forcrop[0:500,500:1000]

im2, contours, hierarchy = cv2.findContours(img_binary2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#contours, hierarchy= cv2.findContours(img_binary2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

crops = []
#ここ変える
min_size = 30000
obj_num = 0

def padding_position(x, y, w, h, p):
    return x - p, y - p, w + p * 2, h + p * 2

for c in contours:
    #print cv2.contourArea(c)
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
'''
