import cv2
import numpy as np


def hehe(img,nx,ny):
    w,h,k=img.shape

    print(w)
    print(h)
    print(k)
    
    nw=int(nx*w)
    nh=int(ny*h)
    newimg=np.zeros([nw,nh,k],np.uint8)
    

    for i in range(0,nw):
        for j in range(0,nh):
            newimg[i,j]=img[int(i/nx),int(j/ny)]
            #newimg[i,j]=img[int(i),int(j)]

    print(newimg.shape)
    return newimg


def copy(img):
    w,h,k=img.shape
    newimg=np.zeros([w,h,k],np.uint8)

    for i in range(0,w):
        for j in range(0,h):
            newimg[i,j]=img[i,j]
            
    return newimg

'''
def hehe(img,nx,ny):
    w,h,k=img.shape

    print(w)
    print(h)
    print(k):
    
    newimg=np.zeros([8,8,k])
    
    for i in range(0,8):
        for j in range(0,8):
            #print("X:%d,Y:%d" %(int(i/2),int(j/2)))
            newimg[i,j]=img[int(i/2),int(j/2)]
            print(newimg[i,j])
            print("-")
    return newimg
'''
    
#放大缩小
filename='F:/test.png'
img=cv2.imread(filename)

#res = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)



#cv2.imshow('Main Window',copy(img))

cv2.imshow('Main Window',hehe(img,0.5,0.5))
#cv2.imshow('Main Window',img)
cv2.waitKey() #任意键退出
cv2.destroyAllWindows()





    

    

