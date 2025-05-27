# ASCII Video Converter

A Python-based tool to convert videos into ASCII art and display them as ASCII videos.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)


## Project Overview

This project allows users to convert video files into ASCII art representations.  The video is first processed to extract individual frames. Each frame is then converted into an ASCII image using the `ascii_magic` library. Finally, these ASCII frames are displayed sequentially to create an ASCII video playback experience. Users can control the playback speed.

**Key Features:**

* Video to ASCII frame conversion.
* ASCII video playback with adjustable frame rate.
* User-friendly console-based interface.
* Cross-platform compatibility (Windows tested).


**Problem Solved:**

Provides a fun and novel way to view videos, particularly useful for low-bandwidth situations or as a demonstration of image processing techniques.


**Use Cases:**

* Creating unique visual effects.
* Demonstrating image-to-text conversion.
* Educational purposes in computer vision or image processing.


## Table of Contents

* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Project Architecture](#project-architecture)
* [Contributing](#contributing)
* [License](#license)


## Prerequisites

* Python 3.7 or higher
* Libraries listed in `requirements.txt`:
    * `ascii-magic==2.3.0`
    * `colorama==0.4.6`
    * `numpy==2.0.1`
    * `opencv-python==4.10.0.84`
    * `pillow==10.4.0`


## Installation

1. Clone the repository: `git clone https://github.com/harshkasat/ascii-video-converter.git`
2. Navigate to the project directory: `cd ascii-video-converter`
3. Install the required packages: `pip install -r requirements.txt`


## Usage

1. **Run the script:**  `python main.py <path_to_video>`  (Replace `<path_to_video>` with the actual path to your video file).
2. **Frame Extraction:** The script will automatically extract frames from the video and save them in the `output_frames` directory.
3. **ASCII Conversion:** It will then convert these frames to ASCII art and store them in the `ascii_frames` directory.
4. **ASCII Video Playback:** Finally, it will display the ASCII video in your console.  Use `+` to speed up, `-` to slow down, and `q` to quit.


## Project Architecture

The project consists of three main classes:

* **`ExtractFrame`:** This class handles the extraction of frames from the input video using OpenCV (`cv2`).  The `extract_frames` function reads the video, saves each frame as a PNG image, and controls the frame rate using `video.set(cv2.CAP_PROP_POS_MSEC, (frame_count) * 1000)`.

* **`ConvertAscii`:** This class converts each extracted frame (PNG image) into ASCII art using the `ascii_magic` library. The `convert_image_to_ascii` function enhances the color and saves the ASCII art to a `.txt` file.  The `convert_frames_to_ascii` function iterates through all PNG files in a directory and applies the conversion.

* **`Display`:** This class handles the display of the ASCII video in the console. The `display_ascii_video` function reads and prints each ASCII frame from the `ascii_frames` directory, managing the frame rate and responding to user input (speed control and quit).


## Contributing

Contributions are welcome! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file (This file needs to be created by the developer).


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. (This file needs to be created by the developer).

## Code Sample (main.py -  `ConvertAscii` class):

```python
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
```
