from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeCone
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopAbs import TopAbs_FACE
from OCC.Core.TopLoc import TopLoc_Location
from OCC.Core.gp import gp_Trsf, gp_Vec
from OCC.Display.SimpleGui import init_display

# 创建几何体
cylinder = BRepPrimAPI_MakeCylinder(10, 20).Shape()
cone = BRepPrimAPI_MakeCone(5, 0, 20).Shape()

# 统计面数
explorer = TopExp_Explorer(cone, TopAbs_FACE)
face_count = 0
while explorer.More():
    face_count += 1
    explorer.Next()
print(f"Total number of faces: {face_count}")


# 显示实体
display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(cylinder, update=True)
trsf = gp_Trsf()
trsf.SetTranslation(gp_Vec(25, 0, 0))# 将cone沿x轴平移25个单位
loc = TopLoc_Location(trsf)
cone_loc = cone.Moved(loc)
display.DisplayShape(cone_loc, update=True)
display.DisplayShape(cone, update=True)
display.FitAll()
start_display()


