## README

### Overview
This MATLAB application (`tool`) is designed to analyze data from foot-mounted IMUs (Inertial Measurement Units) to extract steps and provide visualization capabilities. The application allows users to load data files, select video files for visualization, label step boundaries, extract steps, and save annotated step data.

### System Requirements
- MATLAB 2023 or later
- Compatible operating system (Windows, macOS, Linux)

### Installation
1. Download or clone the repository to your local machine.
2. Open MATLAB 2023.
3. Navigate to the directory where you saved the repository.
4. Open the `tool.mlapp` file in MATLAB.

### Usage
1. Launch MATLAB and open the `tool.mlapp` file.
2. Run the `tool` class to start the application.
3. Load data by clicking the "Load Data" button and selecting a CSV file containing IMU data.
4. Select a video file by clicking the "Select Video" button.
5. Use the sliders to navigate through the data and visualize the corresponding frames in the video.
6. Label step boundaries by clicking the "Label Step Boundary" button and selecting the start and end points of steps.
7. Optionally, use the "Label Start / End" button to mark additional points of interest for step start and step end.
8. Extract steps by clicking the "Extract Step" button and providing the step length in centimeters.
9. Repeat steps 6-8 for each step in the data.
10. Save annotated step data by clicking the "Save Labels" button.

### Notes
- Ensure that the CSV data file contains the necessary columns for acceleration data.
- Make sure the video file is compatible and corresponds to the data timeline.
- Follow on-screen instructions and hints for seamless navigation and interaction with the application.