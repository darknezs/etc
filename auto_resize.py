import cv2
import os

'''
นำโค้ดไปอยู่ในโฟลเดอร์รูป แล้วรัน
'''

os.makedirs('newsize')
arr_img_ext = [".png",".PNG"]
for filename in os.listdir("."):
    # if ".png" in filename or ".PNG" in filename:
    if filename[-4:] in arr_img_ext:
        img = cv2.imread(str(filename), cv2.IMREAD_UNCHANGED)

        width = 750
        height = 500
        dim = (width, height)

        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        print('Resized Dimensions : ',resized.shape)
        cv2.imwrite('newsize/' + filename + '750_500.png', resized)
