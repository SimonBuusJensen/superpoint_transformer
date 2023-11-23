import numpy as np

########################################################################
#                                Labels                                #
########################################################################

OPEN_TRENCH_3D_NUM_CLASSES = 2

INV_OBJECT_LABEL = {
    0: "background",
    1: "pipe"
}

CLASS_NAMES = [INV_OBJECT_LABEL[i] for i in range(OPEN_TRENCH_3D_NUM_CLASSES)] 

CLASS_COLORS = np.asarray([
    [223, 52, 52],    # 'background' ->  red
    [108, 135, 75],   # 'pipe'       ->  dark green
])

OBJECT_LABEL = {name: i for i, name in INV_OBJECT_LABEL.items()}

