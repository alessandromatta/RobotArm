from pxr import Usd, UsdGeom

file_path = "omniverse://localhost/Projects/RobotArm/Assets/gripper.usda"
stage = Usd.Stage.Open(file_path)

# Sform with geometry as Gripper
gripper_xform = UsdGeom.Xform.Define(stage, "/Gripper")
sphere = UsdGeom.Sphere.Define(stage, "/Gripper/Geometry")

sphere.GetRadiusAttr().Set(2)

stage.Save()

