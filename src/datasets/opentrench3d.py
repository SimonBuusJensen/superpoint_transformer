import os
import os.path as osp
import logging
from src.datasets import BaseDataset
from src.datasets.opentrench3d_config import *

DIR = osp.dirname(osp.realpath(__file__))
log = logging.getLogger(__name__)

__all__ = ['OpenTrench3D']

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
        super().__init__(*args, val_mixed_in_train=True, **kwargs)
    
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
            'train': ['Area_1', 'Area_2', 'Area_3', 'Area_5'],
            'val': ['Area_4'],
            'test': ['Area_4']}
    
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
        return np.load(raw_cloud_path, allow_pickle=True).item()