Assignment 1
"Robot Arm" assignment: Building a robot arm using USD.
[I used USD Composer for this.]

Assignment 2
Adding animations and physics to the robot from assignment 1

## Components of the robot

- Base | Cylinder
- Lower Arm | Cube
- Upper Arm | Cube
- Gripper | Sphere


## New Folder Structure

RobotArm
-------	Assets
	-------	base.usda
	-------	lower_arm.usda
	-------	upper_arm.usda
	-------	gripper.usda
-------	Scripts
	-------	base.py
	-------	lower_arm.py
	-------	upper_arm.py
	-------	gripper.py
	------- animated_robot.py
	------- multiple_animations.py
	------- physics_robot.py
-------	final_robot.py
-------	robot.usda
------- animated_robot.usda
------- multiple_animations.usda
------- physics_robot.usda
-------	RobotArm.png


## Preview 
Screenshot of the final robot provided as RobotArm.png in the project
Link to the video of the animations and physics: https://drive.google.com/file/d/1dcuRiwYsZV8N_GzC8q6rlNniczf-idOY/view?usp=sharing


## Extra Notes (Assignment 1)

- Regarding materials, i waited until i assembled everything in robot.usda (final_robot.py), then i applied materials manually because i had trouble 
  doing it in scripts.
- Regarding positioning of the components in robot.usda, i tested it manually until i found good rotations and tranlates, then i copied the values in the 
  script.