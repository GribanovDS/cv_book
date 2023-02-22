import cv2

# Загрузить изображение
img = cv2.imread('./image.jpg')

# Отразить изображение по горизонтали
flipped_img = cv2.flip(img, 1)

# Отобразить отраженное изображение с помощью функции imshow()
cv2.imshow('Flipped Image', flipped_img)
cv2.waitKey()

# Отразить изображение по вертикали и отобразить его с помощью функции imshow()
flipped_img = cv2.flip(img, 0)
cv2.imshow('Flipped Image', flipped_img)
cv2.waitKey()

# Отразить изображение по вертикали и горизонтали и отобразить его с помощью функции imshow()
flipped_img = cv2.flip(img, -1)
cv2.imshow('Flipped Image', flipped_img)
cv2.waitKey()

# Освободить все окна с помощью функции destroyAllWindows()
cv2.destroyAllWindows()