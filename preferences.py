import bpy

from bpy.props import BoolProperty

from bpy.types import AddonPreferences

class EI_ImportSettingsPrefs(AddonPreferences):
    bl_idname = __package__.split('.')[0]

    FBX_settings_expanded : BoolProperty(
    name="FBX Settings",
    description="FBX Settings",
    default = False
    )

    OBJ_settings_expanded : BoolProperty(
    name="OBJ settings",
    description="OBJ settings",
    default = False
    )
 
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        eImportProps = scene.addon_props

        layout.prop(
                self, "FBX_settings_expanded", text="FBX settings",
                icon='DISCLOSURE_TRI_DOWN' if self.FBX_settings_expanded
                else 'DISCLOSURE_TRI_RIGHT')
        if self.FBX_settings_expanded:
            row = layout.row()
            row.label(text='FBX Import Scale:')
            row.prop(eImportProps, "fbx_import_scale", expand=True)
            row = layout.row()                
            row.prop(eImportProps, "fbx_apply_transform")
            row.prop(eImportProps, "fbx_use_custom_normals")
            row = layout.row()
            row.prop(eImportProps, "fbx_use_image_search")
            row.prop(eImportProps, "fbx_use_alpha_decals")
            row = layout.row()
            row.label(text='Decal offset:')
            row.prop(eImportProps, "fbx_decal_offset", expand=True)
            row = layout.row()                
            row.prop(eImportProps, "fbx_use_anim")
            row.prop(eImportProps, "fbx_ignore_leaf_bones")
            row = layout.row()
            row.label(text='Animation Offset:')
            row.prop(eImportProps, "fbx_anim_offset", expand=True)
            row = layout.row()                
            row.prop(eImportProps, "fbx_use_subsurf")
            row.prop(eImportProps, "fbx_use_custom_props")
            row = layout.row()
            row.prop(eImportProps, "fbx_use_custom_props_enum_as_string")
            row.prop(eImportProps, "fbx_force_connect_children")
            row = layout.row()
            row.prop(eImportProps, "fbx_use_manual_orientation")
            row = layout.row()
            row.prop(eImportProps, "fbx_set_the_path_in_CV")
            row = layout.row()
            row.label(text='Forward Axis:')
            row.prop(eImportProps, "fbx_axis_forward", text="") 
            row = layout.row()
            row.label(text='Up Axis:')
            row.prop(eImportProps, "fbx_axis_up", text="") 
       
        layout.prop(
                self, "OBJ_settings_expanded", text="OBJ settings",
                icon='DISCLOSURE_TRI_DOWN' if self.OBJ_settings_expanded
                else 'DISCLOSURE_TRI_RIGHT')
        if self.OBJ_settings_expanded:
            row = layout.row()
            row.prop(eImportProps, "obj_use_smooth_groups")
            row = layout.row()
            row.prop(eImportProps, "obj_use_split_objects")
            row = layout.row()
            row.prop(eImportProps, "obj_use_split_groups")
            row = layout.row()
            row.prop(eImportProps, "obj_use_image_search")
            row = layout.row()
            row.label(text='Forward Axis:')
            row.prop(eImportProps, "obj_axis_forward", text="") 
            row = layout.row()
            row.label(text='Up Axis:')
            row.prop(eImportProps, "obj_axis_up", text="") 