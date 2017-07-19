# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:33:54 2017

@author: kaifeng
"""

import tensorflow as tf
from os import listdir
from os.path import isfile,join

def get_image(path,height,width,preprocess_fn):
    png = path.lower().endswith('png')
    img_bytes = tf.read_file(path)
    image = tf.image.decode_png(img_bytes,channels=3) if png else tf.image.decode_jpeg(img_bytes,channels=3)
    return preprocess_fn(image,height,width)

def image(batch_size,height,width,path,preprocess_fn,epochs=2,shuffle=True):
    filenames = [join(path,f) for f in listdir(path) if isfile(join(path,f))]
    if not shuffle:
        filenames = sorted(filenames)
    
    png = filenames[0].lower().endswith('png')
    filename_queue = tf.train.string_input_producer(filenames,shuffle= shuffle,num_epochs=epochs)
    reader = tf.WholeFileReader()
    _ , img_bytes = reader.read(filename_queue)
    image = tf.image.decode_png(img_bytes,channels=3) if png else tf.image.decode_jpeg(img_bytes,channels=3)
    processed_image = preprocess_fn(image,height,width)
    return tf.train.batch([processed_image],batch_size,dynamic_pad=True)