import tensorflow as tf
from collections import Counter
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

frame_record = "./youtube-8m-data/frame_level/traina2.tfrecord"

def print_examples():
    label_mapping = pd.Series.from_csv('./label_names.csv', header=0).to_dict()
    for example in tf.python_io.tf_record_iterator(frame_record):
        tf_example = tf.train.SequenceExample.FromString(example)
        num_frames = len(tf_example.feature_lists.feature_list['audio'].feature)

        print tf_example.feature_lists.feature_list['video_id']
        print num_frames

print_examples()
