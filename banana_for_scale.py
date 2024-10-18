import os
import bpy

bl_info = {
    "name": "Banana For Scale",
    "author": "CaptainAweYeah",
    "version": (1, 0),
    "blender": (4, 00, 0),
    "location": "View3D > Add Banana",
    "description": "Inserts banana at 3d cursor for scale purposes",
    "category": "3D View",
}

# banana button class
class TEST_OT_material_init(bpy.types.Operator):
    bl_idname = 'test.material_init'
    bl_label = 'Banana For Scale'
    
    # Execute banana function
    def execute(self, context):
        # Find banana
        cwd = os.getcwd()
        N = len(cwd)
        ver = cwd[N - 3 :]
        bD = '/scripts/addons/Banana For Scale/Banana.blend'
        banana_path = cwd + '/' + ver + bD

        # Link the external Banana
        with bpy.data.libraries.load(banana_path, link=True) as (data_from, data_to):
            # Specify the banana
            data_to.objects = ['Banana']
            
        # Access the banana object
        linked_banana = bpy.data.objects['Banana']
        
        # Insert banana
        linked_banana.location = bpy.context.scene.cursor.location
        bpy.context.collection.objects.link(linked_banana)
        return {'FINISHED'}
    
# Register banana button
bpy.utils.register_class(TEST_OT_material_init)

def menu_item_draw_func(self, context):
    self.layout.separator()
    self.layout.operator('test.material_init', icon='MATERIAL')
    
bpy.types.VIEW3D_MT_object_context_menu.append(menu_item_draw_func)

# Register banana button
def register():
    bpy.utils.register_class(TEST_OT_material_init)
    
def unregister():
    bpy.utils.unregister_class(TEST_OT_material_init)

if __name__ == "__main__":
    register()
