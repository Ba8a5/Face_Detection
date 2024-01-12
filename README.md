# Face Detection and Tracking

This simple Python script uses OpenCV to perform real-time face detection using a webcam. The script detects faces, draws rectangles around them, and logs the number of detected faces along with the date and time into a CSV file.

## Prerequisites

- Python 3.x
- OpenCV (`pip install opencv-python`)

## Usage

1. Make sure you have Python installed on your system.
2. Install the required dependencies using `pip install opencv-python`.
3. Download the pre-trained Haar Cascade classifier file [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) from the OpenCV GitHub repository and place it in the same directory as the script.
4. Run the script using the command `python face_detection.py`.
5. Press 'x' to exit the application.

## Script Overview

The script performs the following steps:

1. Initializes the OpenCV face cascade classifier with the pre-trained Haar Cascade XML file.
2. Opens the webcam for capturing video frames.
3. Opens a CSV file (`faces_detected.csv`) for logging face detection data.
4. Reads frames from the webcam, converts them to grayscale, and detects faces using the cascade classifier.
5. Records the date, time, and the number of detected faces in a CSV file every 10 seconds or when the number of detected faces changes.
6. Draws rectangles around detected faces and displays the frames in a window.
7. Press 'x' to exit the application.

## CSV File Format

The CSV file (`faces_detected.csv`) stores the following information:

- Date: YYYY-MM-DD
- Time: HH:MM:SS
- Number of Detected Faces

## Acknowledgments

The face detection is performed using the Haar Cascade classifier, which is a part of the OpenCV library.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and customize the script based on your specific requirements or contribute to its improvement!
