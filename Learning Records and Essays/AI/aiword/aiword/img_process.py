# coding:utf-8
import cv2
import copy
import numpy as np

#灰度化处理
def cvt_Color(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img


# 去边框/加边框
def get_Side(img):
    # 将图片的边缘变为白色
    height, width = img.shape
    for i in range(width):
        img[0, i] = 255
        img[height-1, i] = 255
    for j in range(height):
        img[j, 0] = 255
        img[j, width-1] = 255
    return img


# 中值滤波,降噪
def median_Blur(img, m=3):
    blur = cv2.medianBlur(img, m) #模板大小3*3
    return blur


# 二值化处理
def thresh_old(img, l=100, h=255):
    ret,im_fixed=cv2.threshold(img,l,h,cv2.THRESH_BINARY)
    #im_fixed = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
    return im_fixed


# 裁剪字符
def cut(img):
    # 查找检测物体的轮廓
    image, contours, hierarchy = cv2.findContours(img,2,2)
    

    #binary,contours,hierarchy= cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.imshow('image',image)
    # 计数器
    flag = 1
    for cnt in contours:
        # 最小的外接矩形, cnt是一个二值图, x,y是矩阵左上点的坐标, w,h是矩阵的宽和高
        x, y, w, h = cv2.boundingRect(cnt)
        # 画出矩形(图片，矩形左上角，矩形右下角，线框的颜色，线宽)
        #cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        '''# 用红色表示有旋转角度的矩形框架
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
        cv2.imwrite('contours.png', img)
        '''
        # x，y的值不能为0以及图片的大小要超过28*28(按照需求自己设置)，不然我们会得到其他的不想要的图片
        if x != 0 and y != 0 and w*h >= 1500:
            print((x,y,w,h))
            # 调整图像尺寸为28*28
            resize_img = cv2.resize(img[y:y+h, x:x+w], (28,28))
            # 再次二值化
            im_fixed = thresh_old(resize_img, 200, 255)
            # 显示图片
            cv2.imwrite('out_img/char%s.png'%flag, img[y:y+h, x:x+w])
            cv2.imwrite('out_img/resize%s.png'%flag, im_fixed)
            flag += 1


def process_img(filedir):
    #读入原始图像
    img=cv2.imread(filedir)
    #cv2.imshow('img',img)
    # 灰度图
    gary = cvt_Color(img)
    #cv2.imshow('gary',gary)
    # 降噪
    blur = median_Blur(gary)
    #cv2.imshow('blur',blur)
    # 二值化
    thresh = thresh_old(blur)
    # 裁剪
    cut(thresh)
    cv2.imshow('thresh',thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_img('pic/pic3.jpg')