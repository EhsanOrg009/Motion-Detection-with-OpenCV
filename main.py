import cv2
import time
import os


save_dir = "motion_captures"
os.makedirs(save_dir, exist_ok=True)


cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Error opening camera")
    exit()


ret, frame1 = cap.read()
ret, frame2 = cap.read()

motion_counter = 0

while cap.isOpened():

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)

    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        motion_detected = True

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)

    if motion_detected:
        filename = f"{save_dir}/motion_{motion_counter}_{int(time.time())}.jpg"
        cv2.imwrite(filename, frame1)
        print(f"[INFO] Motion detected: {filename}")
        motion_counter += 1
        time.sleep(1)


    frame1 = frame2
    ret, frame2 = cap.read()

    if not ret:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()