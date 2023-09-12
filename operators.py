import os
import bpy

from bpy.types import Operator

class ImportAnyFile(Operator):
    bl_label = "Import any format"
    bl_idname = "import.any"
    bl_options = {'UNDO'}

    

    def execute(self, context):
        pathFC = context.window_manager.clipboard
        mytool = context.scene.addon_props

        if os.path.isdir(pathFC):
            folder = (os.listdir(path=pathFC))

            for filesD in folder:
                if filesD[0] == "\"":
                    filesD = filesD[1:-1] 
                if filesD[-4:] == ".obj" or filesD[-4:] == ".OBJ":
                    imported_object = bpy.ops.import_scene.obj(filepath=os.path.join(pathFC, filesD), 
                                                        use_smooth_groups=mytool.obj_use_smooth_groups,
                                                        use_split_objects=mytool.obj_use_split_objects, 
                                                        use_split_groups=mytool.obj_use_split_groups,
                                                        use_image_search=mytool.obj_use_image_search,
                                                        axis_forward=mytool.obj_axis_forward, axis_up=mytool.obj_axis_up)
                if filesD[-4:] == ".fbx" or filesD[-4:] == ".FBX":
                    imported_object = bpy.ops.import_scene.fbx(filepath=os.path.join(pathFC, filesD), 
                                                        global_scale=mytool.fbx_import_scale, 
                                                        bake_space_transform=mytool.fbx_apply_transform,
                                                        use_custom_normals=mytool.fbx_use_custom_normals,
                                                        use_image_search=mytool.fbx_use_image_search,
                                                        use_alpha_decals=mytool.fbx_use_alpha_decals, decal_offset=mytool.fbx_decal_offset,
                                                        use_anim=mytool.fbx_use_anim, anim_offset=mytool.fbx_anim_offset,
                                                        use_subsurf=mytool.fbx_use_subsurf,
                                                        use_custom_props=mytool.fbx_use_custom_props, 
                                                        use_custom_props_enum_as_string=mytool.fbx_use_custom_props_enum_as_string,
                                                        ignore_leaf_bones=mytool.fbx_ignore_leaf_bones, 
                                                        force_connect_children=mytool.fbx_force_connect_children,
                                                        use_manual_orientation=mytool.fbx_use_manual_orientation,
                                                        axis_forward=mytool.fbx_axis_forward, axis_up=mytool.fbx_axis_up)
        else:
        
            if pathFC[0] == "\"":
                pathFC = pathFC[1:-1]
        
                for x in range(50):
                    if pathFC[-1] == " ":
                        pathFC = pathFC[:-1]  


                

            if pathFC[-4:] == ".obj" or pathFC[-4:] == ".OBJ":
                imported_object = bpy.ops.import_scene.obj(
                                                    filepath=pathFC, use_smooth_groups=mytool.obj_use_smooth_groups, 
                                                    use_split_objects=mytool.obj_use_split_objects, 
                                                    use_split_groups=mytool.obj_use_split_groups,
                                                    use_image_search=mytool.obj_use_image_search,
                                                    axis_forward=mytool.obj_axis_forward, axis_up=mytool.obj_axis_up)
            if pathFC[-4:] == ".fbx" or pathFC[-4:] == ".FBX":
                imported_object = bpy.ops.import_scene.fbx(
                                                    filepath=pathFC, global_scale=mytool.fbx_import_scale, 
                                                    bake_space_transform=mytool.fbx_apply_transform,
                                                    use_custom_normals=mytool.fbx_use_custom_normals,
                                                    use_image_search=mytool.fbx_use_image_search,
                                                    use_alpha_decals=mytool.fbx_use_alpha_decals, decal_offset=mytool.fbx_decal_offset,
                                                    use_anim=mytool.fbx_use_anim, anim_offset=mytool.fbx_anim_offset,
                                                    use_subsurf=mytool.fbx_use_subsurf,
                                                    use_custom_props=mytool.fbx_use_custom_props, 
                                                    use_custom_props_enum_as_string=mytool.fbx_use_custom_props_enum_as_string,
                                                    ignore_leaf_bones=mytool.fbx_ignore_leaf_bones, 
                                                    force_connect_children=mytool.fbx_force_connect_children,
                                                    use_manual_orientation=mytool.fbx_use_manual_orientation,
                                                    axis_forward=mytool.fbx_axis_forward, axis_up=mytool.fbx_axis_up)
        return {'FINISHED'}