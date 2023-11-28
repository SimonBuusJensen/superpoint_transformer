import numpy as np

TRENCHES = {
    "Area_1": [
        "Area_1_Site_1",
        "Area_1_Site_2",
        "Area_1_Site_3",
        "Area_1_Site_4",
        "Area_1_Site_5",
        "Area_1_Site_6",
        "Area_1_Site_7",
        "Area_1_Site_8",
        "Area_1_Site_9",
        "Area_1_Site_10",
        "Area_1_Site_11",
        "Area_1_Site_12",
        "Area_1_Site_13",
        "Area_1_Site_14",
        "Area_1_Site_15",
        "Area_1_Site_16",
        "Area_1_Site_17",
        "Area_1_Site_18",
        "Area_1_Site_19",
        "Area_1_Site_20",
        "Area_1_Site_21",
        "Area_1_Site_22",
        "Area_1_Site_23",
        "Area_1_Site_24",
        "Area_1_Site_25",
        "Area_1_Site_26",
        "Area_1_Site_27",
        "Area_1_Site_28",
        "Area_1_Site_29",
        "Area_1_Site_30",
        "Area_1_Site_31",
        "Area_1_Site_32",
        "Area_1_Site_33",
        "Area_1_Site_34",
        "Area_1_Site_35",
        "Area_1_Site_36",
        "Area_1_Site_37",
        "Area_1_Site_38",
        "Area_1_Site_39",
        "Area_1_Site_40",
        "Area_1_Site_41",
        "Area_1_Site_42",
        "Area_1_Site_43",
        "Area_1_Site_44",
        "Area_1_Site_45",
        "Area_1_Site_46",
        "Area_1_Site_47",
        "Area_1_Site_48",
        "Area_1_Site_49",
        "Area_1_Site_50"
    ],
    'Area_4': [ 
        "Area_4_Site_1",
        "Area_4_Site_2",
        "Area_4_Site_3",
        "Area_4_Site_4",
        "Area_4_Site_5",
        "Area_4_Site_6",
        "Area_4_Site_7",
        "Area_4_Site_8",
        "Area_4_Site_9",
        "Area_4_Site_10",
        "Area_4_Site_11",
        "Area_4_Site_12",
        "Area_4_Site_13",
        "Area_4_Site_14",
        "Area_4_Site_15",
        "Area_4_Site_16",
        "Area_4_Site_17",
        "Area_4_Site_18",
        "Area_4_Site_19",
        "Area_4_Site_20",
        "Area_4_Site_22",
        "Area_4_Site_23",
        "Area_4_Site_24",
        "Area_4_Site_25",
        "Area_4_Site_26",
        "Area_4_Site_27",
        "Area_4_Site_28",
        "Area_4_Site_29",
        "Area_4_Site_30",
        "Area_4_Site_32",
        "Area_4_Site_33",
        "Area_4_Site_34",
        "Area_4_Site_36",
        "Area_4_Site_37",
        "Area_4_Site_38",
        "Area_4_Site_39",
        "Area_4_Site_40",
        "Area_4_Site_41",
        "Area_4_Site_42",
        "Area_4_Site_43",
        "Area_4_Site_44",
        "Area_4_Site_45",
        "Area_4_Site_46",
        "Area_4_Site_47",
        "Area_4_Site_48",
        "Area_4_Site_50",
        "Area_4_Site_51",
        "Area_4_Site_52",
        "Area_4_Site_53",
        "Area_4_Site_54",
        "Area_4_Site_55",
        "Area_4_Site_56",
        "Area_4_Site_57",
        "Area_4_Site_58",
        "Area_4_Site_59",
        "Area_4_Site_60",
        "Area_4_Site_61",
        "Area_4_Site_62",
        "Area_4_Site_63",
        "Area_4_Site_64",
        "Area_4_Site_66",
        "Area_4_Site_67",
        "Area_4_Site_68",
        "Area_4_Site_69",
        "Area_4_Site_70",
        "Area_4_Site_71",
        "Area_4_Site_73",
        "Area_4_Site_74",
        "Area_4_Site_75",
        "Area_4_Site_76",
        "Area_4_Site_77",
        "Area_4_Site_78",
        "Area_4_Site_79",
        "Area_4_Site_80",
        "Area_4_Site_81",
        "Area_4_Site_82",
        "Area_4_Site_84",
        "Area_4_Site_85",
        "Area_4_Site_86",
        "Area_4_Site_87",
        "Area_4_Site_88"
    ],
    'Area_5': [ 
        "Area_5_Site_1",
        "Area_5_Site_2",
        "Area_5_Site_3",
        "Area_5_Site_4",
        "Area_5_Site_5",
        "Area_5_Site_6",
        "Area_5_Site_7",
        "Area_5_Site_8",
        "Area_5_Site_9",
        "Area_5_Site_10",
        "Area_5_Site_11",
        "Area_5_Site_12",
        "Area_5_Site_13",
        "Area_5_Site_14",
        "Area_5_Site_15",
        "Area_5_Site_16",
        "Area_5_Site_17",
        "Area_5_Site_18",
        "Area_5_Site_19",
        "Area_5_Site_20",
        "Area_5_Site_21",
        "Area_5_Site_22",
        "Area_5_Site_24",
        "Area_5_Site_25",
        "Area_5_Site_27",
        "Area_5_Site_28",
        "Area_5_Site_29",
        "Area_5_Site_30",
        "Area_5_Site_31",
        "Area_5_Site_32",
        "Area_5_Site_33",
        "Area_5_Site_34",
        "Area_5_Site_35",
        "Area_5_Site_36",
        "Area_5_Site_37"
    ]
}

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

