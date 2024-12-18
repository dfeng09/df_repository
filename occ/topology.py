from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeCone
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopAbs import TopAbs_SOLID, TopAbs_FACE
from OCC.Core.TopoDS import topods
from OCC.Core.AIS import AIS_Shape
from OCC.Display.SimpleGui import init_display

# 创建几何体
cylinder = BRepPrimAPI_MakeCylinder(10, 20).Shape()
cone = BRepPrimAPI_MakeCone(5, 0, 20).Shape()

# 布尔融合
fused_shape = BRepAlgoAPI_Fuse(cylinder, cone).Shape()

# 检查并提取实体
explorer = TopExp_Explorer(cylinder, TopAbs_SOLID)
solids = []
while explorer.More():
    solid = topods.Solid(explorer.Current())
    solids.append(solid)
    explorer.Next()

if len(solids) == 0:
    raise RuntimeError("No solids found in the fused shape!")

shape = solids[0]  # 选择第一个实体

# 统计面数
explorer = TopExp_Explorer(shape, TopAbs_FACE)
face_count = 0
while explorer.More():
    face_count += 1
    explorer.Next()

print(f"Total number of faces: {face_count}")

# 显示实体
display, start_display, add_menu, add_function_to_menu = init_display()
ais_shape = AIS_Shape(shape)
display.DisplayShape(ais_shape, update=True)

# 启动显示
start_display()
