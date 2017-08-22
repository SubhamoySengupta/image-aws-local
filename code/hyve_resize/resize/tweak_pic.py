from __future__ import division
from PIL import Image
import sys, os

Image.MAX_IMAGE_PIXELS = 1562144000  # ~250MB earlier was ~85 MB


class image_resizer:
    def __init__(self, file_name):
        self.IMAGE = Image.open(file_name)
        self.IMAGE_NAME = file_name
        self.WIDTH, self.HEIGHT = self.IMAGE.size
        self.Extension = file_name.split('.')[1]
        self.ASPECT_RATIO = self.WIDTH / self.HEIGHT
        self.DIR = '/run/user/1000/gvfs/smb-share:server=wdmycloud,share=hyve/hyve-rootwork/'

    def resize(self, input_params):
        # try:
            resized_image = self.IMAGE.resize(self.get_size('4500', 'w'), Image.LANCZOS)
            path = input_params
            if not os.path.exists(path[:path.rfind('/')]):
                os.makedirs(path[:path.rfind('/')])
            resized_image.save(
                                        path,
                                        'jpeg',
                                        optimize=True,
                                        progressive=True,
                                        quality=100
                                      )

    def resize_h(self, input_params):
        # try:
            resized_image = self.IMAGE.resize(self.get_size('4500', 'h'), Image.LANCZOS)
            path = input_params
            if not os.path.exists(path[:path.rfind('/')]):
                os.makedirs(path[:path.rfind('/')])
            resized_image.save(
                                        path,
                                        'jpeg',
                                        optimize=True,
                                        progressive=True,
                                        quality=100
                                      )
        # except:
        #    print 'An error occured while resizing'

    def get_size(self, size, dimension):
        if dimension == 'h':
            return int(int(size) * self.ASPECT_RATIO), int(size)
        elif dimension == 'w':
            return int(size), int(int(size) / self.ASPECT_RATIO)
