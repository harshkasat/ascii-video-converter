from PIL import Image, ImageEnhance 
import time
import sys, errno
import os
import cv2
from ascii_magic import AsciiArt
import msvcrt # for windows compatibility


class ConvertAscii:
    def convert_image_to_ascii(self, image_path, output_path, width=80):
        try:
            art = AsciiArt.from_image(path=image_path)
            art.image = ImageEnhance.Color(art.image).enhance(1) 
            art.to_file(output_path)
        except Exception as e:
            raise e

    def convert_frames_to_ascii(self, input_dir, output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
            for frame_file in os.listdir(input_dir):
                if frame_file.endswith('.png'):
                    output_file = os.path.join(output_dir, frame_file.replace('.png', '.txt'))
                    self.convert_image_to_ascii(os.path.join(input_dir, frame_file), output_file)
        except Exception as e:
            raise e

class Display:
    def display_ascii_video(ascii_dir, frame_rate=1):
        try:
            ascii_files = sorted([f for f in os.listdir(ascii_dir) if f.endswith('.txt')])
            
            print("ASCII Video Playback")
            print("Controls: '+' to speed up, '-' to slow down, 'q' to quit")
            
            for ascii_file in ascii_files:
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
                with open(os.path.join(ascii_dir, ascii_file), 'r') as f:
                    print(f.read())
                
                start_time = time.time()
                while time.time() - start_time < 1/frame_rate:
                    if kbhit():
                        key = getch()
                        if key == '+':
                            frame_rate = min(frame_rate * 1.5, 30)
                            print(f"\nSpeed increased. Current frame rate: {frame_rate:.2f} fps")
                        elif key == '-':
                            frame_rate = max(frame_rate / 1.5, 0.1)
                            print(f"\nSpeed decreased. Current frame rate: {frame_rate:.2f} fps")
                        elif key.lower() == 'q':
                            print("\nQuitting...")
                            return
                    time.sleep(0.1)  # Short sleep to prevent high CPU usage
        except Exception as e:
            raise e

class ExtractFrame:

    def extract_frames(input_video, output_directory):
        try:
            os.makedirs(output_directory, exist_ok=True)
            video = cv2.VideoCapture(input_video)
            frame_count = 1

            while True:
                success, frame = video.read()
                if not success:
                    break

                output_file = os.path.join(output_directory, f"frame_{frame_count:04d}.png")
                cv2.imwrite(output_file, frame)

                video.set(cv2.CAP_PROP_POS_MSEC, (frame_count) * 1000)
                frame_count += 1

            video.release()
            print(f"Extracted {frame_count - 1} frames to {output_directory}")
        except Exception as e:
            raise e

def kbhit():
    return msvcrt.kbhit()

def getch():
    return msvcrt.getch().decode()

def main():
    if len(sys.argv) < 2:
        raise FileNotFoundError("Please provide the path to the video file")
    input_video = sys.argv[1]
    frames_dir = "output_frames"
    ascii_dir = "ascii_frames"

    # Extract frames from video
    ExtractFrame.extract_frames(input_video, frames_dir)

    # Convert frames to ASCII
    converter = ConvertAscii()
    converter.convert_frames_to_ascii(frames_dir, ascii_dir)

    # Display ASCII video
    Display.display_ascii_video(ascii_dir, frame_rate=0.5)  # Start with 0.5 fps (2 seconds per frame)

if __name__ == "__main__":
    main()