from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCone
from OCC.Core.TopLoc import TopLoc_Location
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Core.gp import gp_Pnt, gp_Trsf, gp_Vec, gp_Ax1, gp_Dir
from OCC.Display.OCCViewer import rgb_color
from dataclasses import dataclass


a=1
b=2
@dataclass
class Cone:
    radius: float
    height: float
    def make_cone(self):
        return BRepPrimAPI_MakeCone(self.radius,0,self.height).Shape()
    def __str__(self):
        return f"radius:{self.radius},height:{self.height}"

my_conesp = Cone(1,4).make_cone()

my_cone = BRepPrimAPI_MakeCone(1,0,4).Shape()
cone=TopoDS_Shape(my_cone)
T=gp_Trsf()
T.SetTranslation(gp_Vec(0,5,0))
loc=TopLoc_Location(T)
cone.Location(loc)
print(f"sbus{a},sbu{b}")
if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(my_cone, update=True,color=rgb_color(1,0,0))
    display.DisplayShape(cone, update=True,color=rgb_color(0,0,1))
    display.DisplayShape(my_conesp, update=True,color=rgb_color(0,1,0))
    start_display()
