# -*- coding:utf-8 -*- 
'''
author: chaihj15
date: 2018/07/09
'''

import numpy as np
import cv2
import uuid

class Camer:
    def __init__(self):
        self.name = 'demo_camer'
        self.cap = cv2.VideoCapture(0)
        self.keyframe = 1

    def diffimage(self, src_1, src_2):
        src_1 = src_1.astype(np.int)
        src_2 = src_2.astype(np.int)
        diff = abs(src_1 - src_2)
        return diff.astype(np.uint8)

    def detect(self):
        ret, lastframe = self.cap.read()
        while(self.cap.isOpened()):
            ret, frame = self.cap.read()
            if not ret:
                break
            if np.sum(self.diffimage(lastframe, frame)) / frame.size > 10:  #设定的阈值
                cv2.imwrite("frameminus" + str(self.keyframe) + ".jpg", frame)
                self.keyframe += 1
            lastframe = frame
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

detect_camer = Camer()
print("begin detect")
detect_camer.detect()
