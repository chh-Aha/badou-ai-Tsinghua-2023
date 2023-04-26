import numpy as np
import cv2
def billnear(img,out_dim):
    src_h, src_w, channels = img.shape
    dst_h = out_dim[0]
    dst_w = out_dim[1]
    if src_h == dst_h and src_w==dst_w:
        return img.copy()

    dst_img = np.zeros((dst_h,dst_w,channels),np.uint8)
    scale_x = float(src_w)/dst_w
    scale_y = float(src_h)/dst_h

    for c in range(channels):
        for dst_y  in range(dst_h):
            for dst_x in range(dst_w):

                src_x = (dst_x +0.5)*scale_x - 0.5
                src_y = (dst_y +0.5)*scale_y - 0.5

                src_x0 = int(np.floor(src_x))
                src_x1 = min(src_x0+1, src_w-1)
                src_y0 = int(np.floor(src_y))
                src_y1 = min(src_y0+1, src_h-1)

                temp0 = (src_x1 - src_x)*img[src_y0,src_x0,c] + (src_x - src_x0)*img[src_y0,src_x1,c]
                temp1 = (src_x1 - src_x)*img[src_y1,src_x0,c] + (src_x - src_x0)*img[src_y1,src_x1,c]
                dst_img[dst_y,dst_x,c] = int((src_y1-src_y)*temp0+(src_y-src_y0)*temp1)
    return dst_img

if __name__ == '__main__':
    img = cv2.imread('lenna.png')
    zoom = billnear(img,(300,300))
    cv2.imshow('1',zoom)
    cv2.waitKey(0)

#
# def bilinear(img,out_dim):
#     h,w,c = img.shape
#     dst_h,dst_w = out_dim[0],out_dim[1]
#     out_img = np.zeros((out_dim[0],out_dim[1],c),np.uint8)
#     if h==dst_h and w==dst_w:
#         return img.copy()
#     scale_x,scale_y = float(w)/dst_w,float(h)/dst_h
#     for i in range(c):
#         for dst_x in range(dst_w):
#             for dst_y in range(dst_h):
#                 src_x = np.floor((dst_x+0.5)*scale_x) - 0.5
#                 src_y = np.floor((dst_y+0.5)*scale_y) - 0.5
#
#                 src_x0 = int(np.floor(src_x))
#                 src_x1 = min(src_x0+1, w-1)
#                 src_y0 = int(np.floor(src_y))
#                 src_y1 = min(src_y0+1, h-1)
#
#                 temp0 = (src_x1-src_x)*img[src_y0,src_x0,i]+(src_x-src_x0)*img[src_y0,src_x1,i]
#                 temp1 = (src_x-src_x0)*img[src_y1,src_x0,i]+(src_x-src_x0)*img[src_y1,src_x1,i]
#
#                 out_img[dst_y,dst_x,i] = int((src_y1-src_y) * temp0 + (src_y-src_y0) * temp1)
#     return out_img
#
# if __name__ == '__main__':
#     img = cv2.imread('lenna.png')
#     zoom = bilinear(img,(400,400))
#     cv2.imshow('1',zoom)
#     cv2.waitKey(0)