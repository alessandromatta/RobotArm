"Robot Arm" assignment: Building a robot arm using USD.
[I used USD Composer for this.]

## Components

- Base | Cylinder
- Lower Arm | Cube
- Upper Arm | Cube
- Gripper | Sphere


## Folder Structure

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
-------	final_robot.py
-------	robot.usda
-------	RobotArm.png


## Preview (Screenshot provided as RobotArm.png in the project)


## Extra Notes

- Regarding materials, i waited until i assembled everything in robot.usda (final_robot.py), then i applied materials manually because i had trouble 
  doing it in scripts.
- Regarding positioning of the components in robot.usda, i tested it manually until i found good rotations and tranlates, then i copied the values in the 
  script.