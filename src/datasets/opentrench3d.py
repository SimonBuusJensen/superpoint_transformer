import os
import torch
import os.path as osp
import logging
from src.datasets import BaseDataset
from src.data import Data
from src.datasets.opentrench3d_config import *

DIR = osp.dirname(osp.realpath(__file__))
log = logging.getLogger(__name__)

__all__ = ['OpenTrench3D']

def read_opentrench_tile(filepath, is_npy=True):
    data = Data()
    
    fn = osp.basename(filepath)
    if is_npy:
        fn = fn.replace("ply", "npy")  
    dir_name = osp.dirname(filepath) # /home/.../
    area_str = "_".join(fn.split("_")[0:2]) # Area_1_Site_4.npy -> Area_1
    filepath = osp.join(dir_name, area_str, fn) # /home/.../Area_1/Area_1_Site_4.npy
    
    with open(filepath, "rb") as f:
        
        
        
        # Load the npy file
        points = np.load(f)
        
        # Read xyz from column 0, 1, 2
        pos = torch.from_numpy(points[:, :3].astype(np.float32))
        
        # Read rgb from column 3, 4, 5
        rgb = torch.from_numpy(points[:, 3:6].astype(np.uint8))
        
        y = torch.from_numpy(points[:, 6].astype(np.int64))
        
        data = Data(pos=pos, rgb=rgb, y=y)
        
        # data.is_val = torch.ones(data.num_nodes, dtype=torch.bool) if "Area_5" in fn else torch.zeros(data.num_nodes, dtype=torch.bool)
        # print(filepath, data.is_val)
    
    return data

########################################################################
#                           OpenTrench3D                               #
########################################################################
class OpenTrench3D(BaseDataset):
    """OpenTrench3D dataset
    
    Parameters
    ----------
    root : `str`
        Root directory where the dataset should be saved.
    stage : {'train', 'val', 'test', 'trainval'}, optional
    transform : `callable`, optional
        transform function operating on data.
    pre_transform : `callable`, optional
        pre_transform function operating on data.
    pre_filter : `callable`, optional
        pre_filter function operating on data.
    on_device_transform: `callable`, optional
        on_device_transform function operating on data, in the
        'on_after_batch_transfer' hook. This is where GPU-based
        augmentations should be, as well as any Transform you do not
        want to run in CPU-based DataLoaders
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, test_mixed_in_val=True, **kwargs)
    
    @property
    def class_names(self):
        """List of string names for dataset classes. This list may be
        one-item larger than `self.num_classes` if the last label
        corresponds to 'unlabelled' or 'ignored' indices, indicated as
        `-1` in the dataset labels.
        """
        return CLASS_NAMES

    @property
    def num_classes(self):
        """Number of classes in the dataset. May be one-item smaller
        than `self.class_names`, to account for the last class name
        being optionally used for 'unlabelled' or 'ignored' classes,
        indicated as `-1` in the dataset labels.
        """
        return OPEN_TRENCH_3D_NUM_CLASSES
    
    @property
    def all_base_cloud_ids(self):
        """Dictionary holding lists of clouds ids, for each
        stage.

        The following structure is expected:
            `{'train': [...], 'val': [...], 'test': [...]}`
        """
        return {
            'train': TRENCHES['Area_1'],
            'val': TRENCHES['Area_4'],
            'test': TRENCHES['Area_5']
        }
    
    @property
    def raw_file_structure(self):
        return f"""
        {self.root}/
            └── raw/
                └── Area_{{i_area:1>8}}/
                    └── Area_{{i_area:1>8}}_Site_{{i_site:1>50}}.npy
                    └── ...
                """

    def read_single_raw_cloud(self, raw_cloud_path):
        """Read a single raw cloud and return a Data object, ready to
        be passed to `self.pre_transform`.
        Read content from .npy file
        """
        return read_opentrench_tile(raw_cloud_path)
    
    def download_dataset(self):
        return None