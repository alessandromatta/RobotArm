from pxr import Usd, UsdGeom

file_path = "omniverse://localhost/Projects/RobotArm/Assets/base.usda"

stage = Usd.Stage.Open(file_path)

# Xform with geometry as Base
base_xform = UsdGeom.Xform.Define(stage, "/Base")
cylinder = UsdGeom.Cylinder.Define(stage, "/Base/Geometry")

cylinder.GetRadiusAttr().Set(8)
cylinder.GetHeightAttr().Set(1.5)

stage.Save()



