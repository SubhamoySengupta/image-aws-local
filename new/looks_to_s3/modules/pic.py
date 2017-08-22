from __future__ import division
from PIL import Image
from PIL import ImageFile


ImageFile.LOAD_TRUNCATED_IMAGES = True

Image.MAX_IMAGE_PIXELS = 262144000  # ~250MB earlier was ~85 MB


class image_resizer:
    def __init__(self, file_name):
        self.IMAGE = Image.open(file_name)
        self.WIDTH, self.HEIGHT = self.IMAGE.size
        self.ASPECT_RATIO = self.WIDTH / self.HEIGHT

    def get_dimensions(self):
            if self.WIDTH > 1500:
                self.DIMENSION = '__w-200-400-600-800-1000-1200-1400__'
            elif self.WIDTH > 1300:
                self.DIMENSION = '__w-200-400-600-800-1000-1200__'
            elif self.WIDTH > 1100:
                self.DIMENSION = '__w-200-400-600-800-1000__'
            elif self.WIDTH > 900:
                self.DIMENSION = '__w-200-400-600-800__'
            elif self.WIDTH > 700:
                self.DIMENSION = '__w-200-400-600__'
            elif self.WIDTH > 500:
                self.DIMENSION = '__w-200-400__'
            elif self.WIDTH > 300:
                self.DIMENSION = '__w-200__'
            else:
                self.DIMENSION = '__w__'
