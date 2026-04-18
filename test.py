import cv2

img = cv2.imread("dataset/defect/scratches_4.jpg")

if img is None:
    print("Image not found")
else:
    cv2.imshow("Test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()