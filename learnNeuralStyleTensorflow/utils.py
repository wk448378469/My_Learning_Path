# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:33:54 2017

@author: kaifeng
"""

import tensorflow as tf
import yaml

slim = tf.contrib.slim

def _get_init_fn(FLAGS):
    tf.logging.info('Use pretrained model %s ' % FLAGS.loss_model_file) # vgg_16.ckpt
    exclusions = []
    if FLAGS.checkpoint_exclude_scopes:
        exclusions = [scope.strip() for scope in FLAGS.checkpoint_exclude_scopes.split(',')]
    variables_to_restore = []
    for var in slim.get_model_variables():
        excluded = False
        for exclusion in exclusions:
            if var.op.name.startswith(exclusion):
                excluded = True
                break
        if not excluded:
            variables_to_restore.append(var)
    return slim.assign_from_checkpoint_fn(FLAGS.loss_model_file,variables_to_restore,ignore_missing_vars=True)

class Flag(object):
    # a dict object save model parameter
    def __init__(self,**entries):
        self.__dict__.update(entries)

def read_conf_file(conf_file):
    # read model needs parameter
    with open(conf_file) as f:
        FLAGS = Flag(**yaml.load(f))
    return FLAGS

def mean_image_subtraction(image,means):
    pass

if __name__ == '__main__':
    f = read_conf_file('conf/mosaic.yml')
    print (f.loss_model_file)