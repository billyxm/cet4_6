# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 15:55:41 2012

@author: Administrator
"""
 
class Reg:  
    stu_name = ""       #姓名
    stu_id = ""         #学号
    stu_indentify = ""  #身份证
    stu_school = ""     #学校  
    stu_institute = ""  #院系
    stu_major = ""      #专业
    stu_password = ""   #密码
    stu_sex = ""        #性别
      
    #set ID   
    def setStu_name(self,stu_name):  
        self.stu_name = stu_name  
      
    def setStu_id(self,stu_id):  
        self.stu_id = stu_id  
      
    def setStu_indentify(self,stu_indentify):  
        self.stu_indentify= stu_indentify  
          
    def setStu_school(self,stu_school):  
        self.stu_school = stu_school
    
    def setStu_institute(self,stu_institute):
        self.stu_institute = stu_institute
        
    def setStu_major(self,stu_major):
        self.stu_major = stu_major
        
    def setStu_password(self,stu_password):
        self.stu_password = stu_password
    
    def setStu_sex(self,stu_sex):
        self.stu_sex = stu_sex
     #get()方法 
    def getStu_name(self):  
        return self.stu_name 
      
    def getStu_id(self):  
        return self.stu_id 
      
    def getStu_indentify(self):  
        return self.stu_indentify 
      
    def getStu_school(self):  
        return self.stu_school
        
    def getStu_institute(self):
        return self.stu_institute
        
    def getStu_major(self):
        return self.stu_major
        
    def getStu_password(self):
        return self.stu_password
        
    def getStu_sex(self):
        return self.stu_sex
        