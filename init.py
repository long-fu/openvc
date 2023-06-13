import cv2
import numpy as np

def is_docker():
    # Is environment a Docker container?
    return Path('/workspace').exists()  # or Path('/.dockerenv').exists()

def is_colab():
    # Is environment a Google Colab instance?
    try:
        import google.colab
        return True
    except ImportError:
        return False

def check_imshow():
    # Check if environment supports image displays
    try:
        assert not is_docker(), 'cv2.imshow() is disabled in Docker environments'
        assert not is_colab(), 'cv2.imshow() is disabled in Google Colab environments'
        cv2.imshow('test', np.zeros((1, 1, 3)))
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        return True
    except Exception as e:
        print(f'WARNING: Environment does not support cv2.imshow() or PIL Image.show() image displays\n{e}')
        return False

# path = 'bus.jpg'
# image = cv2.imread(path) 
# cv2.imshow("image show", image)

# cv2.waitKey(10000000)

source = ""

# for i, s in enumerate(sources):  # index, source
    # Start thread to read frames from video stream
    # print(f'{i + 1}/{n}: {s}... ', end='')
    # if 'youtube.com/' in s or 'youtu.be/' in s:  # if source is YouTube video
    #     check_requirements(('pafy', 'youtube_dl'))
    #     import pafy
    #     s = pafy.new(s).getbest(preftype="mp4").url  # YouTube URL
    # s = eval(s) if s.isnumeric() else s  # i.e. s = '0' local webcam
    # cap = cv2.VideoCapture(s)
    # assert cap.isOpened(), f'Failed to open {s}'
    # w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # self.fps[i] = max(cap.get(cv2.CAP_PROP_FPS) % 100, 0) or 30.0  # 30 FPS fallback
    # self.frames[i] = max(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), 0) or float('inf')  # infinite stream fallback

    # _, self.imgs[i] = cap.read()  # guarantee first frame
    # self.threads[i] = Thread(target=self.update, args=([i, cap, s]), daemon=True)
    # print(f" success ({self.frames[i]} frames {w}x{h} at {self.fps[i]:.2f} FPS)")
    # self.threads[i].start()
    
def show_image_file(path):
    image = cv2.imread(path) 
    cv2.imshow("image show", image)
    cv2.waitKey(10000000)

def play_video_file(path):
    cap = cv2.VideoCapture(path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(fps, width, height)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            cap.release()
            break
        cv2.imshow("framw",frame)
        # int(1000 / fps)
        cv2.waitKey(int(1000 / fps))
    cap.release()
    pass

def play_rtmp(source):
    cap = cv2.VideoCapture(source)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(fps, width, height)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            cap.release()
            break
        cv2.imshow("framw",frame)
        # int(1000 / fps)
        # cv2.waitKey(int(1000 / fps))
        cv2.waitKey(int(fps))
    cap.release()
    pass

def main():
    # play_video_file("rtmp-test.mp4")
    play_rtmp("rtmp://192.168.1.13:1935/rtmp-test")
    pass

if __name__ == "__main__":
    main()