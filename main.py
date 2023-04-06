import cv2
import time


silly_cat = cv2.imread('variant-8.jpg', cv2.IMREAD_COLOR)
cropped_silly_cat = silly_cat[187:587, 400:800]
cv2.imshow('ct', cropped_silly_cat)
cv2.waitKey(0)
cv2.destroyAllWindows()

cam = cv2.VideoCapture(0)
size = (800, 600)
i = 0
while True:
    ret, frame = cam.read()
    if not ret:
        break
    frame = cv2.resize(frame, size, interpolation=cv2.INTER_LINEAR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(contour)
        xx = x + int(w*0.5)
        yy = y + int(h*0.5)
        cv2.line(frame, (xx, y), (xx, y+h), (0, 255, 0), 2)
        cv2.line(frame, (x, yy), (x+w, yy), (0, 255, 0), 2)
        cv2.putText(frame, f'{x + (w // 2)}, {y + (h // 2)}', (10, 590), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
    frame[yy-32:yy+32, xx-32:xx+32] = cv2.imread('fly.png')
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.1)
    i += 1

cam.release()
