from feature_extractor import YouTube8MFeatureExtractor
from PIL import Image
import numpy
import os

extractor = YouTube8MFeatureExtractor(model_dir='~/github.com/dennischang/youtube-8m/yt8m-model/')

image_file = os.path.join('../youtube-8m-raw/1200px-Grosser_Panda.JPG')
im = numpy.array(Image.open(image_file))
features = extractor.extract_rgb_frame_features(im)
#print len(features)
print features

