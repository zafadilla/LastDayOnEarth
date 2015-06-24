from death import Death        
from lastDayOnEarth import LastDayOnEarth
from exploring import Exploring
from deactivation import Deactivation            
from escape import Escape

class Map(object):

    scenes = {
        'last_day_on_earth': LastDayOnEarth(),
        'death': Death(),
        'exploring':Exploring(),
        'escape':Escape(),
        'deactivation':Deactivation()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        

