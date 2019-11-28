#!/usr/bin/python
# -*- coding=utf-8 -*-


import subprocess
import os
import bpy
import json
from .draw import draw_molecule

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,)

from bpy.types import (Panel,
                       AddonPreferences,
                       Operator,
                       PropertyGroup,)



class PG_MyProperties (PropertyGroup):
    # 字符串界面
    smile_string : StringProperty(
        name="Smi",
        description=":",
        default="",
        maxlen=2048,
    )


class OT_DrawChemicalStructureOperator (bpy.types.Operator):
    bl_idname = "wm.draw_chemical_structure"
    bl_label = "Draw Structure"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        # mytool.smile_string

        script_path = os.path.dirname(os.path.realpath(__file__))

        # suppose create mol.json after parse command
        parse_path = os.path.join(script_path, 'parse.py')
        parse_command = ['python', parse_path, mytool.smile_string]
        subprocess.Popen(parse_command)

        # draw molecule
        show_bonds, join = True, True
        PATH = os.path.dirname(os.path.realpath(__file__))
        json_path = os.path.join(PATH, 'mol.json')

        with open(json_path) as fid:
            molecule = json.load(fid)
        draw_molecule(molecule, show_bonds=show_bonds, join=join)

        return {'FINISHED'}


class OBJECT_PT_setting_panel (Panel):
    # 用户输入设置面板，此处用于输入Smile字符串
    bl_idname = "OBJECT_PT_setting_panel"
    bl_label = "Setting Panel"
    # bl_space_type = "PROPERTIES"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    # bl_region_type = "TOOL_PROPS"
    # Tab的名称
    bl_category = "Blender Chemicals"
    bl_context = "objectmode"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        # 绘制界面
        layout.prop(mytool, "smile_string")
        layout.operator("wm.draw_chemical_structure")
