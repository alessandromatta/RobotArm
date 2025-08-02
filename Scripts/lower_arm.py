from pxr import Usd, UsdGeom

file_path = "omniverse://localhost/Projects/RobotArm/Assets/lower_arm.usda"

stage = Usd.Stage.Open(file_path)

# Xform with geometry as LowerArm
lower_arm_xform = UsdGeom.Xform.Define(stage, "/LowerArm")
cube = UsdGeom.Cube.Define(stage, "/LowerArm/Geometry")

xformable = UsdGeom.Xformable(cube.GetPrim())
xformable.SetXformOpOrder([])
xformable.AddTranslateOp().Set((0, 0, 0))
xformable.AddRotateXYZOp().Set((0, 0, 0))
xformable.AddScaleOp().Set((1, 1, 5))

stage.Save()

