from pxr import Usd, UsdGeom, UsdPhysics, UsdShade

file_path = "omniverse://localhost/Projects/RobotArm/physics_robot.usda"
animated_robot_path = "omniverse://localhost/Projects/RobotArm/animated_robot.usda"

stage = Usd.Stage.Open(file_path)

# Set time Code
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(192)

# Add components function
def add_component(path, file_path, prim_path, translation, rotation):
    component = UsdGeom.Xform.Define(stage, path)
    component.GetPrim().GetReferences().AddReference(file_path, primPath = prim_path)
    xform = UsdGeom.XformCommonAPI(component)
    xform.SetTranslate(translation)
    xform.SetRotate(rotation)
    xform.SetScale((1, 1, 1))

# Add robot and ground
ground = UsdGeom.Xform.Define(stage, "/Ground")
rigid_animated_robot = UsdGeom.Xform.Define(stage, "/RigidAnimatedRobot")

add_component("/Ground", animated_robot_path, "/Ground", (0, 0, 0), (0, 0, 0))
add_component("/RigidAnimatedRobot/AnimatedRobot", animated_robot_path, "/AnimatedRobot", (0, 0, 5), (0, 0, 0))

# Add collider to the ground
ground_collider = UsdPhysics.CollisionAPI.Apply(ground.GetPrim())

# Add physics properties to the animated robot
physics_prim_robot = UsdPhysics.RigidBodyAPI.Apply(rigid_animated_robot.GetPrim())

# Add collider to the animated robot
robot_collider = UsdPhysics.CollisionAPI.Apply(rigid_animated_robot.GetPrim())

# Create a material for the robot's frictions and restitution
material = UsdShade.Material.Define(stage, "/Material")
materialPrim = material.GetPrim()
materialAPI = UsdPhysics.MaterialAPI.Apply(materialPrim)
materialAPI.CreateStaticFrictionAttr(1)
materialAPI.CreateDynamicFrictionAttr(0.7)
materialAPI.CreateRestitutionAttr(0.9)

# Bind the robot and the material
bindingAPI = UsdShade.MaterialBindingAPI.Apply(rigid_animated_robot.GetPrim())
shadeMaterial = UsdShade.Material(materialPrim)
bindingAPI.Bind(shadeMaterial)

stage.Save()
