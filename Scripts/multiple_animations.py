from pxr import Usd, UsdGeom, Sdf

file_path = "omniverse://localhost/Projects/RobotArm/multiple_animations.usda"
animated_robot_path = "omniverse://localhost/Projects/RobotArm/animated_robot.usda"

stage = Usd.Stage.Open(file_path)

# Add components function, adding offset to it
def add_component(path, file_path, prim_path, translation, rotation, layer_offset = None):
    component = UsdGeom.Xform.Define(stage, path)
    if layer_offset is not None:
        component.GetPrim().GetReferences().AddReference(file_path, primPath = prim_path, layerOffset = layer_offset)
    else:
        component.GetPrim().GetReferences().AddReference(file_path, primPath = prim_path)
    xform = UsdGeom.XformCommonAPI(component)
    xform.SetTranslate(translation)
    xform.SetRotate(rotation)
    xform.SetScale((1, 1, 1))

# Set time Code
# stage.SetStartTimeCode(1)
# stage.SetEndTimeCode(192)

# Add the ground and the animated robots
ground = UsdGeom.Xform.Define(stage, "/Ground")
original_robot = UsdGeom.Xform.Define(stage, "/OriginalRobot")
shifted_robot = UsdGeom.Xform.Define(stage, "/ShiftedRobot")
speed_robot = UsdGeom.Xform.Define(stage, "/SpeedRobot")

add_component("/Ground", animated_robot_path, "/Ground", (0, 0, 0), (0, 0, 0))
# Original robot
add_component("/OriginalRobot/AnimatedRobot", 
              animated_robot_path, 
              "/AnimatedRobot", 
              (20, 0, 0), 
              (0, 0, 0))
# Shifted robot
add_component("/ShiftedRobot/AnimatedRobot", 
              animated_robot_path, 
              "/AnimatedRobot", 
              (0, 0, 0), 
              (0, 0, 0),
              layer_offset = Sdf.LayerOffset(offset = 48))
# Speed robot
add_component("/SpeedRobot/AnimatedRobot", 
              animated_robot_path, 
              "/AnimatedRobot", 
              (-20, 0, 0), 
              (0, 0, 0),
              layer_offset = Sdf.LayerOffset(scale = 0.5))                             
