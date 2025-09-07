import cv2 as cv


def read_video(video_path):
    cap = cv.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frames, output_video_path):
    fourcc = cv.VideoWriter_fourcc(*'avc1')
    out = cv.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0])) # Come back to understand
    for frame in output_video_frames:
        out.write(frame)
    out.release()