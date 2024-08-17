# ASCII Video Converter

This Python project allows you to convert video frames into ASCII art and display the resulting ASCII video in the terminal. It uses the `ascii-magic` library to convert images to ASCII and `cv2` to extract frames from a video file. The video can be played back in the terminal using symbols and dots.

## Repository Name

`ascii-video-converter`

## Description

`ascii-video-converter` is a Python-based tool that extracts frames from a video, converts them to ASCII art, and plays the ASCII video in the terminal. Users can control playback speed during the video playback. This project is compatible with Windows and uses `ascii-magic`, `PIL`, and `cv2`.

## Features

- Extract frames from any video file.
- Convert video frames to ASCII art using customizable settings.
- Display ASCII video in the terminal with playback controls.

### Project Structure

- `main.py`: The main script to run the project.
- `ConvertAscii`: A class to convert images to ASCII.
- `Display`: A class to handle ASCII video playback.
- `ExtractFrame`: A class to extract frames from a video.
  
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/harshkasat/ascii-video-converter.git
    cd ascii-video-converter
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Create the `requirements.txt` file with the following dependencies:
    ```
    pillow
    opencv-python
    ascii-magic
    ```

## Usage

To use the tool, simply provide the path to a video file as a command-line argument:

```bash
python main.py path_to_video.mp4
```
### Controls

- `+`: Increase playback speed.
- `-`: Decrease playback speed.
- `q`: Quit playback.

