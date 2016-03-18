import pymel.core as pm

class VRayConfig(object):
    """
    This class responsible for linear workflow
    VRaya configurtaion
    """
    def __init__(self):
        pass

    def set_linear_settings(self):

        # Make sure that VRay plugin loaded
        # and render tab set to vray
        pm.mel.loadPlugin('vray')
        current_renderer = pm.Attribute('defaultRenderGlobals.currentRenderer')
        current_renderer.set('vray')

    def linearize_texture(self, file_node):
        pass

    def linearize_all_textures(self):
        pass

def main():
    vr_conf = VRayConfig()
    vr_conf.set_linear_settings()
