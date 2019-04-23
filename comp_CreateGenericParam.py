__author__ = "jonah.hawk"
__version__ = "2018.10.04"

import Grasshopper as gh
import System.Drawing as sd

comp = ghenv.Component
ghdoc = comp.OnPingDocument()
canvas = gh.Instances.ActiveCanvas

#the array accessor lets you pick which input you want
targetInput = comp.Params.Input[0]

#Define a function to expire this component. We'll need this later!
def expireThis(doc):
    comp.ExpireSolution(False)

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if not Count:
    Count = 3
if not Name:
    name = 0
if Name:
    name = 1
if not ABCD:
    ABCD = 0
if not Numb:
    Numb = 0
nameMode = name + ABCD*2 + Numb *4
print("nameMode: " + str(nameMode))


if Run and Count > 0:
    for i in range(Count):

        #create the node
        node = gh.Kernel.Parameters.Param_GenericObject()
        ghdoc.AddObject(node,False,ghdoc.ObjectCount+1)
        thisPivot = targetInput.Attributes.Pivot
        node.Attributes.Pivot =sd.PointF(thisPivot.X+100,thisPivot.Y+(i*22))
        num = ("{:0>2d}".format(i))
        #1 + 0 + 0
        if nameMode == 1:
            node.NickName = Name
        # 0 + 2 + 0
        if nameMode == 2:
            node.NickName = (alpha[i])
        # 1 + 2 + 0
        if nameMode == 3:
            node.NickName = Name + "_" + alpha[i] 
        # 0 + 0 + 4
        if nameMode == 4:
            node.NickName = num
        # 1 + 0 + 4
        if nameMode == 5:
            node.NickName = Name + "_" + num
        # 0 + 2 + 4
        if nameMode == 6:
            node.NickName = str(alpha[i]) + num
        if nameMode == 7:
            node.NickName = Name  + "_" + str(alpha[i]) + num

        node.IconDisplayMode= ghenv.Component.IconDisplayMode.name
