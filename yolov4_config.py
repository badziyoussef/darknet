# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:41:08 2020

@author: Quang Nguyen
"""

""" 
Generating custom cfg/yolov4_custom_train.cfg
and cfg/yolov4_custom_test.cfg

"""

classes=17
max_batches=32000
batch=64
subdivisions=64  # instead of 16 to avoid  cuDNN Error: CUDNN_STATUS_BAD_PARAM
width=416
height=416
channels=3
momentum=0.949
decay=0.0005
learning_rate=0.001
steps= (25600,28800)
scales=(0.1,0.1)
