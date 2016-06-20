# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 16:33:44 2012

@author: Administrator
"""

class Examinee:
    stu_name = ""       #姓名 
    stu_indentify = ""  #身份证
    stu_school = ""     #学校 
    exam_major = ""     #报考科目
    exam_id = ""        #准考证号
    exam_room = ""      #考场编号
    exam_seat = ""      #座位
    exam_place =""      #考试地点
    def setStu_name(self,stu_name):  
        self.stu_name = stu_name
     
    def setExam_seat(self,exam_seat):
        self.exam_seat = exam_seat
    
        
    def setStu_indentify(self,stu_indentify):  
        self.stu_indentify= stu_indentify  
        
    def setStu_school(self,stu_school):  
        self.stu_school = stu_school
        
    def setExam_major(self,exam_major):
        self.exam_major =exam_major
        
    def setExam_id(self,exam_id):
        self.exam_id = exam_id
        
    def setExam_room(self,exam_room):
        self.exam_room = exam_room
        
    def setExam_place(self,exam_place):
        self.exam_place = exam_place
    #get()    
    def getStu_name(self):  
        return self.stu_name 
    
    def getExam_seat(self):
        return self.exam_seat

    
    def getStu_indentify(self):  
        return self.stu_indentify
        
    def getStu_school(self):  
        return self.stu_school
        
    def getExam_major(self):
        return self.exam_major
        
    def getExam_id(self):
        return self.exam_id
    
    def getExam_room(self):
        return self.exam_room
        
    def getExam_place(self):
        return self.exam_place