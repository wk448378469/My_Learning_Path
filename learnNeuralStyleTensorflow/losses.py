# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:33:54 2017

@author: kaifeng
"""

from __future__ import print_function
import tensorflow as tf
import nets_factory
import preprocessing_factory
import utils
import os

def gram(layer):
    shape = tf.shape(layer)
    num_images = shape[0]
    width = shape[1]
    height = shape[2]
    num_filters = shape[3]
    filters = tf.reshape(layer,tf.stack([num_images,-1,num_filters]))
    grams = tf.matmul(filters,filters,transpose_a=True) / tf.to_float(width * height * num_filters)
    return grams

def get_style_features(FLAGS):
    # get style image to feature
    with tf.Graph().as_default():
        # generate net
        network_fn = nets_factory.get_network_fn(FLAGS.loss_model,num_classes=1,is_training=False)
        # image preprocessing
        image_preprocessing_fn,image_unprocessing_fn = preprocessing_factory.get_preprocessing(FLAGS.loss_model,is_training=False)
        
        # get the style image data
        size = FLAGS.image_size
        img_bytes = tf.read_file(FLAGS.style_image)
        if FLAGS.style_image.lower().endswith('png'):
            image = tf.image.decode_png(img_bytes)
        else:
            image = tf.image.decode_jpeg(img_bytes)
        
        # add the batch dimension
        images = tf.expand_dims(image_preprocessing_fn(image,size,size),0)
        _ , endpoints_dict = network_fn(images,spatial_squeeze = False)
        features = []
        
        for layer in FLAGS.style_layers:
            feature = endpoints_dict[layer]
            feature = tf.squeeze(gram(feature),[0])
            features.append(feature)
        
        with tf.Session() as sess:
            init_func = utils._get_init_fn(FLAGS)
            init_func(sess)
            # make sure directory
            if os.path.exists('generated') is False:
                os.makedirs('generated')
            # style image path 
            save_file = 'generated/target_style_' + FLAGS.naming + '.jpg'
            # write preprocessed style image 
            with open(save_file,'wb') as f:
                target_image = image_unprocessing_fn(images[0,:])
                value = tf.image.encode_jpeg(tf.cast(target_image,tf.uint8))
                f.write(sess.run(value))
                tf.logging.info('Target style pattern is saved to %s.' % save_file)
            return sess.run(features)

def style_loss(endpoints_dict,style_features_t,style_laryers):
    style_loss = 0
    style_loss_summary = {}
    for style_gram,layer in zip(style_features_t,style_laryers):
        generated_images , _ = tf.split(endpoints_dict[layer],2,0)
        size = tf.size(generated_images)
        layer_style_loss = tf.nn.l2_loss(gram(generated_images) - style_gram) * 2 / tf.to_float(size)
        style_loss_summary[layer] = layer_style_loss
        style_loss += layer_style_loss
    return style_loss,style_loss_summary

def content_loss(endpoints_dict,content_layers):
    content_loss = 0
    for layer in content_layers:
        genetated_images,content_images = tf.split(endpoints_dict[layer],2,0)
        size = tf.size(genetated_images)
        content_loss += tf.nn.l2_loss(genetated_images - content_images) * 2 / tf.to_float(size)
    return content_loss

def total_variation_loss(layer):
    shape = tf.shape(layer)
    height = shape[1]
    width = shape[2]
    y = tf.slice(layer,[0,0,0,0],tf.stack([-1,height-1,-1,-1])) - tf.slice(layer,[0,1,0,0],[-1,-1,-1,-1])
    x = tf.slice(layer,[0,0,0,0],tf.stack([-1,-1,width-1,-1])) -tf.slice(layer,[0,0,1,0],[-1,-1,-1,-1])
    loss = tf.nn.l2_loss(x) / tf.to_float(tf.size(x)) + tf.nn.l2_loss(y)/tf.to_float(tf.size(y))
    return loss
    
    