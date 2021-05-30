import cv2 as cv
MAX_KERNEL_LENGTH = 31
dst = None
window_name = 'Smoothing Demo'
src=cv.imread('vr.png')
for i in range(1, MAX_KERNEL_LENGTH, 2):
        dst = cv.GaussianBlur(src, (i, i), 5)
cv.imshow(window_name,dst)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("vaibhav.jpg", dst)