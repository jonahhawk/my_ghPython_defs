import rhinoscriptsyntax as rs
import Grasshopper as gh

def reNickNameAllComponents():
    document = ghenv.Component.OnPingDocument()
    for component in document.Objects:
       nick = component.NickName
       if Find in nick:
           print nick
           newNick = nick.replace(Find, Replace)
           component.NickName = newNick

def reNickNameSelectedComponents():
    document = ghenv.Component.OnPingDocument()
    for component in document.Objects:
        if component.Attributes.Selected:
            print(component.Attributes.Selected)
            nick = component.NickName
            if Find in nick:
                print nick
                newNick = nick.replace(Find, Replace)
                component.NickName = newNick


if Run and not Selected:
    reNickNameAllComponents()
if Run and Selected:
    reNickNameSelectedComponents()
