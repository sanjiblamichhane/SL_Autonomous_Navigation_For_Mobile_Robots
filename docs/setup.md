# SETTING UP

## OVERVIEW

This section will explain how to setup raspberry pi 3 (in short we'll call it ```pi```) and install ROS on it to work with Intel Realsense Camera T265 (in short we'll call it ```IRCamera```).

## OBJECTIVES:
Let's break the requirement into the following objectives:
- Install ROS on Raspberry pi
- Establish SSH connection between pi and your laptop within your network.
- Install Intel RealSense Camera T265 (IR265) SDK on Raspberry pi 
- Test Communication between IRT265 and ROS

## METHODOLOGY
### TASK 1 - Install ROS on Raspberry Pi 3b:
  - Download and install Ubuntu 16.04(LXDE) and ROS Kinetic for raspberry pi3 using this [link ](https://downloads.ubiquityrobotics.com/pi.html).
  The good thing about installing an imager from Ubiquity Robotics is that it comes with a preinstalled ROS on a Ubuntu 16.04 distro, which is handy especially when not all linux distribution can support ros on a raspberry pi 3 hardware.

- After a successful loading of the image file, we can login to the pi:
  Username: ubuntu user
  Password: ubuntu
  
  These credientials are default values.It is highly recommended that you change it after a successful login.

#### PROBLEM:
The pi imager we just loaded was specially cusotmized for Ubiquity's own robotics; but, we are not using their robot. Therefore, we need to change a few configurations to meet our need.

##### SOLUTION:
Full guidance on how to use their raspberry pi image without a magni was provided [here.](https://learn.ubiquityrobotics.com/image_no_magni)
- Magni robot is a mobile robot base supplied by ubiquity robotics. Learn more about Magni [here](
https://www.ubiquityrobotics.com/product/magni-silver/#:~:text=Magni%20is%20a%20Mobile%20Robot,and%20power%20is%20already%20working) . 

#### PROBLEM
The pi comes with a default name ```ubuntu@ubiquity```. This means anyone who also installed this image like we did will have the same username. This is a problem because multiple robots will have the same name.

##### SOLUTION:
We need to change the host name of the pi. To do so, open terminal and type the following:
``` 
$ ssh ubuntu@ubiquityrobot.local
```
The password is : ``` ubuntu ```

Now lets finally change the hostname so we can use pifi
```
$ sudo pifi set-hostname <NEWHOSTNAME>
```
For our case: let’s call it; ```omnigpr```. 
Now, The reboot the pi so that the new hostname is effective. 

#### PROBLEM
The raspberry pi image we just installed comes with a WiFi hotspot by default. But we do not want to connect our robot to their hotspot. Instead, we need to connect our robot to our own network wherever we run our robot.

##### SOLUTION:
Full documentation is [here.](https://learn.ubiquityrobotics.com/connect_network)

Summary of how to connect the robot to your network: 
- Directly connect to your local wifi network as you’d do for your any other laptop. In case the wifi networks are not available or seen, open terminal and type
```
$ pifi list seen
```
- Login to the network with this command
```
$ sudo pifi add <network-name> <network-password>
```
- After connecting to the network, reboot the pi
```
$ sudo reboot
```
### TASK 2 - Establish SSH connection between pi and your laptop within your network:

#### PROBLEM
The pi is connected to our local network, now we need to communicate with the pi from our laptop via SSH protocol. 

##### SOLUTION
In order to do that, we need to find the ip address of the pi. Type the following in the terminal window.
```
$ ifconfig 
```
As we can see the ip address was: ```192.168.x.xx```.
You might have a different ip since it is a different device and connected over different network.

From a laptop device connected over the same wifi as the pi, we can create a ssh connection as the following.
```
$ ssh ubuntu@192.168.x.xx
```

### TASK 3 - Install Intel RealSense Camera T265 (IR265) SDK on Raspberry pi:

### TASK 4 - Test Communication between IRT265 and ROS: 


## CONCLUSION:
- Successfully installed Ubuntu 16.04, ROS Kinetic on the pi
- Established ssh connection between pi and our laptop. 


