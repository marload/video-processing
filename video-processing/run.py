import argparse
import cv2

from process import process

parser = argparse.ArgumentParser()
parser.add_argument("video", help="video path")
parser.add_argument("output", help="output path")

args = parser.parse_args()
print(args)

def main():
    VIDEO_PATH = args.video
    OUTPUT_PATH = args.output

    # Video Read
    video = cv2.VideoCapture(VIDEO_PATH)
    WIDTH = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    HEIGHT = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    FPS = int(video.get(cv2.CAP_PROPS.FPS))

    # Video Process
    video = process(video, WIDTH, HEIGHT, FPS)
    print('Processing...')

    # Video Write
    CODEC = cv2.VideoWriter_fourcc(*'XVID')
    writer = cv2.VideoWriter(OUTPUT_PATH, CODEC, FPS, (WIDTH, HEIGHT))
    print('Video has been saved to [{}].'.format(OUTPUT_PATH))

    
    

    