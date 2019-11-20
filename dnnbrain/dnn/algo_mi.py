#import some packages needed
import numpy as np
import math
import torch
from PIL import Image

from os.path import join as pjoin

from torch.nn import ReLU
from torch.optim import Adam
from abc import ABC, abstractmethod
from skimage.segmentation import felzenszwalb, slic, quickshift

from dnnbrain.dnn.base import ImageSet
from dnnbrain.dnn.core import Stimulus, Mask

class Algorithm(ABC):
    """ 
    An Abstract Base Classes class to define interface for dnn algorithm 
    """
    def __init__(self, dnn, layer=None, channel=None):
        self.dnn = dnn
        self.layer = layer
        self.channel = channel
        
    def set_layer(self, layer, channel):
        self.layer = layer
        self.channel = channel
        
    @abstractmethod
    def set_params(self):
        """ set parames """
        
    @abstractmethod
    def compute(self, image): 
        """Please implement your algorithm here""" 
        


class MinmalParcelImage(Algorithm):
    """
    A class to generate minmal image for a CNN model using a specific part 
    decomposer and optimization criterion
    """    
    def set_params(self, meth='SLIC', criterion='max'):
        """Set parameter for the estimator"""
        self.meth  = meth
        self.criterion = criterion

    def compute(self, image):
        """Generate minmal image for image listed in stim object """
        pass 

        
class MinmalComponentImage(Algorithm):
    """
    A class to generate minmal image for a CNN model using a specific part 
    decomposer and optimization criterion
    """
    
    def set_params(self,  meth='pca', criterion='max'):
        """Set parameter for the estimator"""
        self.meth = meth
        self.criterion = criterion

    def compute(self, image):
        """Generate minmal image for image listed in stim object """
        pass