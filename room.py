# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 16:26:20 2012

@author: Administrator
"""

class Room:
   
    exam_room  = ""         #考场编号
    exam_place = ""         #考试地点
    exam_major = ""         #考试科目 
    #set()方法
   
    
    def setExam_room(self,exam_room):
        self.exam_room = exam_room
    #剩下两个方法examinee已经有了
   
    #get()方法    
    def getExam_room(self):
        return self.exam_room
        
