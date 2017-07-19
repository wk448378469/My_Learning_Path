# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:33:54 2017

@author: kaifeng
"""

from __future__ import print_function
import tensorflow as tf
import preprocessing_factory
import reader
import model
import os

tf.app.flags.DEFINE_string('loss_model', 'vgg_16', 'The name of the architecture to evaluate. '
                           'You can view all the support models in nets_factory.py')
tf.app.flags.DEFINE_integer('image_size', 256, 'Image size to train.')
tf.app.flags.DEFINE_string("model_file", "models.ckpt", "")
tf.app.flags.DEFINE_string("image_file", "a.jpg", "")

FLAGS = tf.app.flags.FLAGS

def main(_):
    # get image height , width
    height = 0
    width = 0
    with open(FLAGS.image_file,'rb') as img:
        with tf.Session().as_default() as sess:
            if FLAGS.image_file.lower().endswith('png'):
                image = sess.run(tf.image.decode_png(img.read()))
            else:
                image = sess.run(tf.image.decode_jpeg(img.read()))
            height = image.shape[0]
            width = image.shape[1]
    
    with tf.Graph().as_default():
        with tf.Session().as_default() as sess:
            
            # read image data
            image_preprocessing_fn , _ = preprocessing_factory.get_preprocessing(FLAGS.loss_model,is_training=False)
            image = reader.get_image(FLAGS.image_file,height,width,image_preprocessing_fn)
            
            # add batch dimension
            image = tf.expand_dims(image,0)
            
            generated = model.net(image,training=False)
            generated = tf.cast(generated,tf.uint8)
            generated = tf.squeeze(generated,[0])
            
            # restore model variables
            saver = tf.train.Saver(tf.global_variables(),write_version=tf.train.SaverDef.V1)
            sess.run([tf.global_variables_initializer(),tf.local_variables_initializer()])
            
            FLAGS.model_file = os.path.abspath(FLAGS.model_file)
            saver.restore(sess,FLAGS.model_file)
            
            # directory exits
            generated_file = 'generated/res.jpg'
            if os.path.exists('generated') is False:
                os.makedirs('generated')
            
            # generate and write image data to file
            with open(generated_file,'wb') as img:
                img.write(sess.run(tf.image.encode_jpeg(generated)))

if __name__ == '__main__':
    tf.app.run()
