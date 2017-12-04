import tensorflow as tf
from collections import Counter
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#frame_record = "./youtube-8m-data/frame_level/traina2.tfrecord"
frame_record = "./youtube-8m-output/testa0.tfrecord"

def print_examples():
    label_mapping = pd.Series.from_csv('./label_names.csv', header=0).to_dict()
    for example in tf.python_io.tf_record_iterator(frame_record):
        tf_example = tf.train.Example.FromString(example)

        print tf_example.features.feature['video_id'].bytes_list.value[0].decode(encoding='UTF-8')
        values = tf_example.features.feature['labels'].int64_list.value
        label = ''
        for value in values:
            label += label_mapping[value]
            label += ','
        print label

        tf_example_seq = tf.train.SequenceExample.FromString(example)
        num_frames = len(tf_example_seq.feature_lists.feature_list['audio'].feature)
        print num_frames


print_examples()
