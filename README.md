# ros_robot package

## Prequisits
Install `teleop_twist_keyboard` [package](http://wiki.ros.org/teleop_twist_keyboard)
```
sudo apt-get install ros-noetic-teleop-twist-keyboard
``` 
## Instructions
- Run folowing commands in seprate terminals:
```
$ roslaunch ros_robot rviz.launch //terminal 1
$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py //terminal 2
$ python3 controller.py //terminal 3

```
Once `teleop_twist_keyboard` is running, you can see instructions on how to controll the robot with keyboard.