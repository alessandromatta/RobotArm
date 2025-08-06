from pxr import Usd, UsdGeom

file_path = "omniverse://localhost/Projects/RobotArm/animated_robot.usda"
robot_path = "omniverse://localhost/Projects/RobotArm/robot.usda"

stage = Usd.Stage.Open(file_path)

# Xform for the ground as the parent 
ground = UsdGeom.Xform.Define(stage, "/Ground")
plane = UsdGeom.Plane.Define(stage, "/Ground/Geometry")
# The size if the plane was manually changed in the stage, because script gave error
# plane.GetPrim().GetAttribute("size").Set(10.0)
# Error: Does not have this attribute

# Xform for the animated robot as the parent
robotRoot = UsdGeom.Xform.Define(stage, "/AnimatedRobot")

# Function to add components for the robot as Xforms with references
# Same function as in final_robot.py 
# (Will update later so i can import it from final_robot.py)
def add_component(path, file_path, prim_path, translation, rotation):
    component = UsdGeom.Xform.Define(stage, path)
    component.GetPrim().GetReferences().AddReference(file_path, primPath = prim_path)
    xform = UsdGeom.XformCommonAPI(component)
    xform.SetTranslate(translation)
    xform.SetRotate(rotation)
    xform.SetScale((1, 1, 1))

# Set time Code
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(192)

# Adding the robot
add_component("/AnimatedRobot/Robot", robot_path, "/Robot", (0, 0, 1), (0, 0, 0))

# Spin the base of the robot 
base = stage.GetPrimAtPath("/AnimatedRobot/Robot/Base")
base_xform = UsdGeom.Xformable(base)
base_spin = base_xform.AddRotateZOp(opSuffix="spin")
base_spin.Set(time = 1, value = 0)
base_spin.Set(time = 192, value = 360)

# Spin the upper arm of the robot 
upper_arm = stage.GetPrimAtPath("/AnimatedRobot/Robot/UpperArm")
upper_arm_xform = UsdGeom.Xformable(upper_arm)
upper_arm_spin = upper_arm_xform.AddRotateZOp(opSuffix="spin")
upper_arm_spin.Set(time = 1, value = 0)
upper_arm_spin.Set(time = 96, value = 360)

# Scale the gripper
gripper = stage.GetPrimAtPath("/AnimatedRobot/Robot/Gripper")
gripper_xform = UsdGeom.Xformable(gripper)
gripper_scale = gripper_xform.AddScaleOp(opSuffix="scale")
gripper_scale.Set(time = 1, value = (1, 1, 1))
gripper_scale.Set(time = 96, value = (2, 2, 2))
gripper_scale.Set(time = 192, value = (1, 1, 1))

stage.Save()
