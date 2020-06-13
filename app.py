import cv2

img = cv2.imread("galaxy.jpg", 0)
img2 = cv2.imread("kangaroos-rain-australia_71370_990x742.jpg", 0)
img3 = cv2.imread("Lighthouse.jpg", 0)
img4 = cv2.imread("Moon sinking, sun rising.jpg", 0)

# print(type(img))
# print(img)


images = [img, img2, img3, img4]
for image in images:
    resized_image = cv2.resize(image, (400, 400))
    cv2.imshow("IMAGES", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
