# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "EasyImport",
    "description": "An addon to simplify and speed up the import of popular file extesions like FBX and OBJ",
    "author" : "Vladislav Ciocoi",
    "description" : "",
    "blender" : (2, 90, 0),
    "version" : (0, 2, 2),
    "location": "File > Import Export",
    "category": "Import Export"
}

if 'bpy' not in locals():
    import bpy
    from bpy.props import PointerProperty
    from . import operators
    from . import properties
    from . import preferences
else:
    import imp
    imp.reload(operators)
    imp.reload(properties)
    imp.reload(preferences)

classes = (
    properties.EI_Properties,
    operators.ImportAnyFile,
    preferences.EI_ImportSettingsPrefs
)
addon_keymaps = []

def register():
    from bpy.utils import register_class

    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')

    kmi = km.keymap_items.new(operators.ImportAnyFile.bl_idname, 'V', 'PRESS', shift=True, ctrl=True)

    addon_keymaps.append((km, kmi))


    for cls in classes:
        register_class(cls)

    bpy.types.Scene.addon_props = PointerProperty(type=properties.EI_Properties)

def unregister():
    from bpy.utils import unregister_class

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    for cls in reversed(classes):
        unregister_class(cls)

    del bpy.types.Scene.addon_props
