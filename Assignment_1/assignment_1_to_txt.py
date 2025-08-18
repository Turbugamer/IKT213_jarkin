import cv2
import os

cam = cv2.VideoCapture(0, cv2.CAP_V4L2)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cam.get(cv2.CAP_PROP_FPS)

out_dir = "Assignment_1/solutions"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "camera_outputs.txt"), "w", encoding="utf-8") as f:
    f.write(f"fps: {round(fps)}\n")
    f.write(f"height: {frame_height}\n")
    f.write(f"width: {frame_width}\n")

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('Assignment/output.avi', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cam.read()
    if not ret or frame is None:
        print("Error: Failed to read frame from camera.")
        break

    out.write(frame)

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
out.release()
cv2.destroyAllWindows()