import tensorflow as tf
from collections import Counter
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#video_record = "./youtube-8m-data/video_level/traina0.tfrecord"
video_record = "./youtube-8m-output/testa0.tfrecord"

def print_examples():
    label_mapping = pd.Series.from_csv('./label_names.csv', header=0).to_dict()
    for example in tf.python_io.tf_record_iterator(video_record):
        tf_example = tf.train.Example.FromString(example)

        print tf_example.features.feature['video_id'].bytes_list.value[0].decode(encoding='UTF-8')
        values = tf_example.features.feature['labels'].int64_list.value
        label = ''
        for value in values:
            label += label_mapping[value]
            label += ','
        print label

print_examples()
