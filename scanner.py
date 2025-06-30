import cv2
import numpy as np
import imutils
import os

# Show current working directory
print("Current working directory:", os.getcwd())

# Load image
image = cv2.imread("C:/Users/Administrator/OneDrive/Desktop/COMP_VISION_PROJ/pic.jpg")
if image is None:
    print("Error: Could not load image.")
    exit()

orig = image.copy()
image = imutils.resize(image, height=500)

# Step 1: Preprocess
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)

cv2.imshow("Step 1 - Edges", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 2: Find contours
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

screenCnt = None
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    if len(approx) == 4:
        screenCnt = approx
        break

if screenCnt is None:
    print("Error: Could not detect document edges.")
    exit()

# Step 3: Perspective transform helpers
def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped

# Step 4: Apply perspective transform
warped = four_point_transform(orig, screenCnt.reshape(4, 2) * (orig.shape[0] / 500.0))

# Confirm shape
print("Warped image shape:", warped.shape)

# Display scanned result
cv2.imshow("Scanned", imutils.resize(warped, height=650))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 5: Save scanned image to output/
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "my_pic.jpg")

saved = cv2.imwrite(output_path, warped)
if saved:
    print(f"Scanned image saved successfully at: {output_path}")
else:
    print("Error: Failed to save the scanned image.")
