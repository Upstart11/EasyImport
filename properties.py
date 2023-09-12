from bpy.props import (BoolProperty,
                       FloatProperty,
                       EnumProperty,
                       )

from bpy.types import PropertyGroup

class EI_Properties(PropertyGroup):

    fbx_import_scale : FloatProperty(
    name = "FBX Import Scale",
    description="Scale factor of the importet FBX Mesh",
    default = 1.0,
    min = 0.001,
    max = 1000
    )
    fbx_apply_transform : BoolProperty(
    name="Apply Transform",
    description="Bake space transform into object data",
    default = False
    )
    fbx_use_custom_normals : BoolProperty(
    name="Custom Normals",
    description="Import custom normals, if available",
    default = True
    )
    fbx_use_image_search : BoolProperty(
    name="Image Search",
    description="Search subdirs for any associated images (WARNING: may be slow)",
    default = True
    )
    fbx_use_alpha_decals : BoolProperty(
    name="Alpha Decals",
    description="Treat materials with alpha as decals (no shadow casting)",
    default = True
    )
    fbx_decal_offset : FloatProperty(
    name = "Decal offset",
    description="Scale factor of the importet FBX Mesh",
    default = 0.0,
    min = 0.0,
    max = 1
    )
    fbx_use_anim : BoolProperty(
    name="Import Animation",
    description="Import FBX animation",
    default = True
    )
    fbx_anim_offset : FloatProperty(
    name = "Animation Offset",
    description="Offset to apply to animation during import, in frames",
    default = 1.0,
    min = -1000,
    max = 1000
    )
    fbx_use_subsurf : BoolProperty(
    name="Subdivision Data",
    description="Import FBX subdivision information as subdivision surface modifiers",
    default = False
    )
    fbx_use_custom_props : BoolProperty(
    name="Custom Properties",
    description="Import user properties as custom properties",
    default = True
    )
    fbx_use_custom_props_enum_as_string : BoolProperty(
    name="Import Enums As Strings",
    description="Store enumeration values as strings",
    default = True
    )
    fbx_ignore_leaf_bones : BoolProperty(
    name="Ignore Leaf Bones",
    description="Ignore the last bone at the end of each chain (used to mark the length of the previous bone)",
    default = False
    )
    fbx_force_connect_children : BoolProperty(
    name="Force Connect Children",
    description="Force connection of children bones to their parent, even if their computed head/tail positions do not match (can be useful with pure-joints-type armatures)",
    default = False
    )
    fbx_use_manual_orientation : BoolProperty(
    name="Manual Orientation",
    description="Specify orentation and scale",
    default = False
    )
    fbx_axis_forward : EnumProperty(
    items = [('X','X','X'), 
             ('Y','Y','Y'),
             ('Z','Z','Z'),
             ('-X','-X','-X'),
             ('-Y','-Y','-Y'),
             ('-Z','-Z','-Z')],
    name = "Forward",
    description="Forward Axis",
    default = '-Z'

    )
    
    fbx_axis_up : EnumProperty(
    items = [('X','X','X'), 
             ('Y','Y','Y'),
             ('Z','Z','Z'),
             ('-X','-X','-X'),
             ('-Y','-Y','-Y'),
             ('-Z','-Z','-Z')],
    name = "UP",
    description="UP Axis",
    default = 'Y'

    )
    obj_use_smooth_groups : BoolProperty(
    name="Smooth Groups",
    description="Surround smooth groups by sharp edges",
    default = True
    )
    obj_use_split_objects : BoolProperty(
    name="OBJ Objects",
    description="Import OBJ Objects into Blender Objects",
    default = True
    )
    obj_use_split_groups : BoolProperty(
    name="OBJ Groups",
    description="Import OBJ Groups into Blender Objects",
    default = False
    )
    obj_use_image_search : BoolProperty(
    name="Image Search",
    description="Search subdirs for any associated images (Warning, may be slow)",
    default = True
    )
    obj_axis_forward : EnumProperty(
    items = [('X','X','Z'), 
             ('Y','Y','Y'),
             ('Z','Z','Z'),
             ('-X','-X','-X'),
             ('-Y','-Y','-Y'),
             ('-Z','-Z','-Z')],
    name = "Forward",
    description="Forward Axis",
    default = '-Z'

    )
    obj_axis_up : EnumProperty(
    items = [('X','X','X'), 
             ('Y','Y','Y'),
             ('Z','Z','Z'),
             ('-X','-X','-X'),
             ('-Y','-Y','-Y'),
             ('-Z','-Z','-Z')],
    name = "UP",
    description="UP Axis",
    default = 'Y'

    )