from pypboy import BaseModule
from pypboy.modules.radio import radio
import config

class Module(BaseModule):

    label = "RADIO"

    def __init__(self, *args, **kwargs):
        self.submodules = [
            radio.Module(self),
        ]
        super(Module, self).__init__(*args, **kwargs)
        
    def handle_resume(self):
        self.pypboy.topmenu.label = self.label
        self.pypboy.topmenu.title = config.MODULE_TEXT
        self.active.handle_action("resume")
 