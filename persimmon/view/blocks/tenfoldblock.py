from persimmon.view.util import EmptyContent, InputPin, OutputPin
from persimmon.view.blocks import Block

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from sklearn.model_selection import KFold


Builder.load_file('view/blocks/tenfoldblock.kv')

class TenFoldBlock(Block):
    #in_1 = ObjectProperty()
    out_1 = ObjectProperty()

    def function(self):
        self.out_1.val = KFold(n_splits=10)
