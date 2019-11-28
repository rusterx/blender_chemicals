#!/usr/bin/python
# -*- coding=utf-8 -*-


bl_info = {
    "name": "Blender Chemicals",
    "description": "Draw Chemical Structure Using Blender",
    "author": "Xing Tingyang",
    "version": (0, 0, 2),
    "blender": (2, 80, 0),
    "location": "3D View > Tools",
    "warning": "",
    "wiki_url": "https://xingtingyang.com/",
    "tracker_url": "",
    "category": "Development"
}

import bpy

from .blender_chemicals import (
    PG_MyProperties,
    OBJECT_PT_setting_panel,
    OT_DrawChemicalStructureOperator,
)

from bpy.utils import (register_class, unregister_class)

from bpy.props import PointerProperty


classes = (
    # 设置属性
    PG_MyProperties,
    # 设置面板
    OBJECT_PT_setting_panel,
    OT_DrawChemicalStructureOperator,
)


addon_name = __name__


def register():
    for cls in classes:
        register_class(cls)
    bpy.types.Scene.my_tool = PointerProperty(type=PG_MyProperties)


def unregister():
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.my_tool

