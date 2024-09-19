import sys
import cv2
import os

def video2frames(video_dir, frames_dir):
    video = cv2.VideoCapture(video_dir)

    if not video:
        print("invalid video path error")
    frame_count = 0
    
    while(video.isOpened()):
        ret, frame = video.read()
        if not ret:
            print("reached to end of video")
        if frame is not None:
            frame = cv2.resize(frame, (1920, 1080))
        else:
            print("frame is empty")
            break
        if(int(video.get(1)) % 1 == 0):
            cv2.imwrite(os.path.join(frames_dir, 'frame_%d.png' % int(video.get(1))), frame)
            print("Saved frame number : " + str(int(video.get(1))))
        frame_count += 1

    video.release()

if __name__ == '__main__':
    _, video_dir, frames_dir = sys.argv

    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)
    
    video2frames(video_dir, frames_dir)