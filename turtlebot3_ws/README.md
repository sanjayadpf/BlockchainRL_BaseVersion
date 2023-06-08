Clone the project

git clone https://github.com/sanjayadpf/BlockchainRL_BaseVersion

username: sanjayadpf
pw: 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


Go inside the src directory of turtlebot3_ws and run the following command

git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git


After that go back to turtlebot3_ws and run the follwoing

catkin_make

Open seperate terminals for each functionality

# terminal 01 Gazebo


source devel/setup.bash

roslaunch ros_world turtlebot3_world_RL.launch


# terminal 02 Run Rviz


source devel/setup.bash

roslaunch global_path_planning turtlebot3_ros_world_RL.launch

--For the actual robot 

--You don't need to run this for simulations

roslaunch global_path_planning turtlebot3_ros_real_world.launch

# terminal 03 real time SLAM


source devel/setup.bash

roslaunch turtlebot3_slam turtlebot3_gmapping_RL.launch

# terminal04 Q learning

rosrun server_RL.py


