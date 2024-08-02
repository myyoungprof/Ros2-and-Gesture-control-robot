# Ros2-and-Gesture-control-robot
Robot control using hand gestures with computer vision with ROS2 humble

The scope of this project involves the use of hand gestures obtained from user with the help of computer vision to control a mobile robot.
We also employed a safety mechanism that uses a sensor to detect an obstacles and halt execution of control commands from hand gestures to avoid crashes.
The entire project was executed with the use of ROS frame work integrated with hardware.

# ROS 2 and Gesture Control Robot

This project involves controlling a robot using hand gestures with computer vision and ROS 2 Humble. The system also employs a safety mechanism using a distance sensor to avoid collisions.

## Prerequisites

Ensure you have the following installed on your system:
- ROS 2 Humble
- Python 3
- `colcon` build tool
- `rosdep`

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/myyoungprof/Ros2-and-Gesture-control-robot.git
    cd Ros2-and-Gesture-control-robot
    ```

2. **Install dependencies:**

    Use `rosdep` to install dependencies:

    ```sh
    rosdep update
    rosdep install --from-paths src --ignore-src -r -y
    ```

3. **Build the package:**

    ```sh
    colcon build --packages-select car_project
    ```

4. **Source the workspace:**

    ```sh
    source install/setup.bash
    ```


## Nodes

### GestureControl

- **Function:** Controls the robot car using hand gestures detected by a camera.
- **Executable:** `GestureControl`
- **Command to run individually:** 
    ```sh
    ros2 run car_project GestureControl
    ```

### DistanceSensor

- **Function:** Monitors the distance to obstacles using an ultrasonic sensor.
- **Executable:** `DistanceSensor`
- **Command to run individually:** 
    ```sh
    ros2 run car_project DistanceSensor
    ```

### Control Node

- **Function:** Main control node that receives inputs from other nodes and commands the robot car.
- **Executable:** `control_node`
- **Command to run individually:** 
    ```sh
    ros2 run car_project control_node
    ```

## Running the Nodes Together

To run all nodes together, use the provided launch file:

1. **Ensure your workspace is sourced:**

    ```sh
    source install/setup.bash
    ```

2. **Run the launch file:**

    ```sh
    ros2 launch car_project display.py
    ```
## Acknowledgments

- [ROS 2 Documentation](https://docs.ros.org/en/humble/)
- [colcon Documentation](https://colcon.readthedocs.io/en/released/)




