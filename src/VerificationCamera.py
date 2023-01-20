import cv2
def gstreamer_pipeline(
    sensor_id=0,
    capture_width=1080,
    capture_height=680,
    display_width=640,
    display_height=480,
    framerate=30,
    flip_method=2,
):
    return (
        "nvarguscamerasrc sensor-id=%d ! "
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )
def list_ports():
    """
    Test the available CSI cameras.
    """
    dev_camera = 0
    working_cameras = []
    while dev_camera < 2: #max 2 CSI cameras
        camera = cv2.VideoCapture(gstreamer_pipeline(sensor_id=dev_camera))
        is_reading, img = camera.read()
        w = camera.get(3)
        h = camera.get(4)
        if is_reading:
            print("Camera %s is working and reads images (%s x %s)" %(dev_camera,h,w))
            working_cameras.append(dev_camera)
            cv2.imshow(f"Camera{dev_camera}", img)
            cv2.waitKey(0)
        dev_camera +=1
    return working_cameras
def summary(working_cams):
    print("\n\n#################SUMMARY#################")
    print(f'{len(working_cams)} camera(s) working.')
    print("#########################################")
working_cameras = list_ports()
summary(working_cameras)