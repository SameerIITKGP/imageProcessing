import cv2

img = cv2.imread('1750024.jpg')
orig = img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray,11,17,17)
edged = cv2.Canny(gray,30,200)
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None
for c in cnts:
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	if len(approx) == 4:
		screenCnt = approx
		break

#screenCnt is the array of indices of the rectangle, Clockwise from the top left corner
#Adjusting so that the rectangle covers both the rectangles
screenCnt[0][0][0] -= 2
screenCnt[0][0][1] -= 2
screenCnt[1][0][0] += 2
screenCnt[3][0][1] += screenCnt[3][0][1]/4
screenCnt[2][0][0] = screenCnt[1][0][0]
screenCnt[3][0][0] = screenCnt[0][0][0]
screenCnt[1][0][1] = screenCnt[0][0][1]
screenCnt[2][0][1] = screenCnt[3][0][1]

l1 = screenCnt[0][0][0]
t1 = screenCnt[0][0][1]
r1 = screenCnt[2][0][0]
b1 = screenCnt[2][0][1]

print l1,t1,r1,b1

image = orig[t1:b1, l1:r1]
cv2.imwrite('testing_output.jpg',image)
cv2.namedWindow('image')
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()