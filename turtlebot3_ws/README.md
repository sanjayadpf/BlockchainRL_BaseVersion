
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

#terminal 03 real time SLAM


source devel/setup.bash

roslaunch turtlebot3_slam turtlebot3_gmapping_RL.launch

# terminal04 Q learning

rosrun server_RL.py


