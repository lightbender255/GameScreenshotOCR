import cv2
import pytesseract
import tempfile
import os

imageFilePath = "F:\\Games2\\Steam\\userdata\\69635695\\760\\remote\\346110\\screenshots\\20230305235438_1.jpg"
imageFileNameWithExtenstion = os.path.basename(imageFilePath)
imageFileName = os.path.splitext(imageFileNameWithExtenstion)[0]

# userTempDir = tempfile.gettempdir()
userTempDir = "."

img = cv2.imread(imageFilePath)
(h, w) = img.shape[:2]
img = cv2.resize(img, (w*3, h*3))
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(h, w) = gry.shape[:2]

s_idx = 0
e_idx = int(h/15)

for i, _ in enumerate(range(0, 15)):
    gry_crp = gry[s_idx:e_idx, 0:w]
    thr = cv2.threshold(
        gry_crp, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    thr = cv2.dilate(thr, None, iterations=1)
    filename = f"{userTempDir}/{imageFileName}_{i}.png"
    cv2.imwrite(filename, thr)
    txt = pytesseract.image_to_string(thr, config="--psm 6")
    print(txt)
    s_idx = e_idx
    e_idx = s_idx + int(h/15)
    os.remove(filename)
    # cv2.imshow("thr", thr)
    # cv2.waitKey(0)
