import cv2

def capture_image_from_camera(camera_port=0):
    camera = cv2.VideoCapture(camera_port)
    retval, im = camera.read()
    if retval:
        return im
    else:
        return False
