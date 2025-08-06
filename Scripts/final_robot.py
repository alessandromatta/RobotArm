from pxr import Usd, UsdGeom

file_path = "omniverse://localhost/Projects/RobotArm/robot.usda"
base_path =  "omniverse://localhost/Projects/RobotArm/Assets/base.usda"
lower_arm_path = "omniverse://localhost/Projects/RobotArm/Assets/lower_arm.usda"
upper_arm_path = "omniverse://localhost/Projects/RobotArm/Assets/upper_arm.usda"
gripper_path =  "omniverse://localhost/Projects/RobotArm/Assets/gripper.usda"

stage = Usd.Stage.Open(file_path)

# Xform for the robot as the parent
robotRoot = UsdGeom.Xform.Define(stage, "/Robot")

# Function to add components for the robot as Xforms with references
def add_component(path, file_path, prim_path, translation, rotation):
    component = UsdGeom.Xform.Define(stage, path)
    component.GetPrim().GetReferences().AddReference(file_path, primPath = prim_path)
    xform = UsdGeom.XformCommonAPI(component)
    xform.SetTranslate(translation)
    xform.SetRotate(rotation)
    xform.SetScale((1, 1, 1))

# Adding the components
add_component("/Robot/Base", base_path, "/Base", (0, 0, 0), (0, 0, 0))
add_component("/Robot/LowerArm", lower_arm_path, "/LowerArm", (0, 0, 5.5), (0, 0, 0))
add_component("/Robot/UpperArm", upper_arm_path, "/UpperArm", (-1.8, 0, 14.32), (0, -22.5, 0))
add_component("/Robot/Gripper", gripper_path, "/Gripper", (-4, 0, 19.5), (0, 0, 0))

stage.Save()