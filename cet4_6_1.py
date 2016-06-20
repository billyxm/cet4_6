# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 11:07:50 2012

@author: Administrator
"""
import Examinee #导入学生准考证信息类
import Reg      #导入学生注册信息类
import sys      #系统模块
import sqlite3  #pyton连接数据库sqlite3的模块
import datetime #python生成时间的模块
import random   #python生成随机数的模块
#编码转换，以便在命令提示符中以中文显示
reload(sys)
sys.setdefaultencoding('utf8')
#分别代表四六级的数据库中对应的表
table_1 = u"报名信息"
table_3 = u"考场信息"
table_4 = u"考生信息"
#用户类型选择
def showmenu1():
    while True:
        print u"[0]管理员[1]学生[2]退出\n请选择：" #接受键盘输入
        done = False
        while not done:
            chosen = False
            while not chosen:
                try:
                    choice = raw_input().strip()[0].lower()
                except (EOFError,KeyboardInterrupt):
                    choice = 'q'
                print u"\n你的选择：[%s]" % choice
                if choice not in '012q':
                    print u"选择错误，请重新输入"
                else:
                    chosen = True
            if choice == 'q':done = True
            if choice == '0':admin()
            if choice == '1':stu()
            if choice == '2':
                conn.close()
                sys.exit(0)
#定义管理员的函数
def admin():
    print u"请输入你的管理员账号:"
    root_name = raw_input()
    Admin_table = {'root_name':'admin','root_password':'123456'}
    print u"请输入你的密码："
    password = raw_input()
    passwd = Admin_table.get('root_password')
    root = Admin_table.get('root_name')
    if root_name == root:                   #如果账号正确，执行检查密码是否正确
        if password == passwd:              #如果密码不正确，则重新输入账号密码
            print u"\n欢迎管理员",root_name    #如果账号不正确，则重新输入账号密码
            if True:
                showmenu2()                 #登录成功，返回学生整体信息的管理函数
            else:
                admin()                     #否则继续登录，直到登录成功
        else:                               
            print u"你的密码错误,请重新输入"
            admin()
    else:
        print u"账号错误,请重新输入"
        admin()
#学生整体信息的管理
def showmenu2():
    print u"[1]学生报名信息管理\n[2]学生考场信息管理\n[3]考生信息全部查看\n[4]返回上一层菜单\n请选择："
    done = False
    while not done:        
        chosen = False
        while not chosen:
            try:
                choice = raw_input().strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice = 'q'
            print u"\n你的选择：[%s]" % choice
            if choice not in '1234q':
                print u"选择错误，请重新输入"
            else:
                chosen = True
        if choice == 'q':done = True
        if choice == '1':showmenu3()        #报名信息管理函数
        if choice == '2':showmenu4()        #学生考场信息管理 
        if choice == '3':stu_examminee()    #考生信息全部查看
        if choice == '4':showmenu1()        #返回上一个菜单       
#报名信息管理函数
def showmenu3():
    print u"[1]删除报名信息\n[2]更改报名信息\n[3]查看报名信息\n[4]返回上一层菜单\n请选择："
    done = False
    while not done:        
        chosen = False
        while not chosen:
            try:
                choice = raw_input().strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice = 'q'
            print u"\n你的选择：[%s]" % choice
            if choice not in '1234q':
                print u"选择错误，请重新输入"
            else:
                chosen = True
        if choice == 'q':done = True
        if choice == '1':del_stu()                   #删除报名信息的方法
        if choice == '2':update_stu()                #更改报名信息的方法
        if choice == '3':seeStu()                    #查看报名信息的方法
        if choice == '4':showmenu2()                 #返回上一个菜单
       
#学生考场信息管理        
def showmenu4():
    print u"[1]增加考场信息\n[2]删除考场信息\n[3]更改考场信息\n[4]查看考场信息\n[5]返回上一层菜单\n请选择："
    done = False
    while not done:        
        chosen = False
        while not chosen:
            try:
                choice = raw_input().strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice = 'q'
            print u"\n你的选择：[%s]" % choice
            if choice not in '12345q':
                print u"选择错误，请重新输入"
            else:
                chosen = True
        if choice == 'q':done = True
        if choice == '1':addRoom()
        if choice == '2':delRoom()
        if choice == '3':updateRoom()
        if choice == '4':seeRoom()
        if choice == '5':showmenu2()
#查看报名信息的方法                                
def seeStu():
    #数据库sqlite3的连接方法execute()
    cursor = conn.execute("SELECT * FROM 报名信息 ")    #sql语法“查询报名信息表的所有信息”
    print u"姓名     学号(ID)    身份证\t       学校\t          系别    专业   (ID)密码\t性别\n" #此处空格比较多便于好看
    for row in cursor:
        print row[0]," ",row[1]," ",row[2]," ",row[3]," ",row[4]," ",row[5]," ",row[6]," ",row[7],"\n"
    if True:
        print u"报名信息已经显示完毕！是否返回上一个菜单：(y/n)"
        p = raw_input()
        if p in ['Y','y',' ']:    
            showmenu3()             #返回菜单3
        else:
            seeStu()                 
    else:
        print u"报名信息为空！！！！"
#学生管理界面
def stu():
    print u"[1]新用户注册\n[2]用户登录\n[3]返回上页菜单\n请选择："   
    done = False
    while not done:        
        chosen = False
        while not chosen:
            try:
                choice = raw_input().strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice = 'q'
            print u"\n你的选择：[%s]" % choice
            if choice not in '123q':
                print u"选择错误，请重新输入"
            else:
                chosen = True
        if choice == 'q':done = True
        if choice == '1':new_stu()
        if choice == '2':stu_login() 
        if choice == '3':showmenu1()
#新用户注册函数
def new_stu():
    reg = Reg.Reg()
    exam =Examinee.Examinee()
    #学生姓名输入
    while True:
        print u"请输入你的姓名："
        stu_name =raw_input()
        if stu_name:
            reg.setStu_name(stu_name)
            break
        else:
            print u"请重新输入："
            continue 
    #学生学号的注册，包含以后登录用户
    while True:
        print u"请输入你的学号(ID)："
        stu_id = raw_input()
        if True:
            reg.setStu_id(stu_id)
            break
        else:
            print u"学号必须为9位数"
            continue 
    #学生身份证的输入
    while True:
         print u"请输入你的身份证号码："
         stu_indentify = raw_input()
         if True:
            reg.setStu_indentify(stu_indentify)
            break
         else:
            print u"身份证必须为18位数"
            continue 
    #学生的学校信息输入
    while True:
        print u"请输入你的学校信息："
        stu_school = raw_input()
        if stu_school:
            reg.setStu_school(stu_school)
            break
        else:
            print u"请重新输入："
            continue
     #学生的院系的输入   
    while True:
        print u"请输入你的院系："
        stu_institute = raw_input()
        reg.setStu_institute(stu_institute)
        break
    #学生的专业的输入
    while True:
         print u"请输入你的专业："
         stu_major = raw_input()
         if stu_major:
            reg.setStu_major(stu_major)
            break
         else:
            print u"请重新输入："
            continue
    #学生的账号密码的输入
    while True:
        print u"请输入你的账号密码："
        stu_password = raw_input()
        if stu_password:
            reg.setStu_password(stu_password)
            break
        else:
            print u"请重新输入："
            continue
    #学生的性别输入    
    while True:
        print u"请输入你的性别："
        stu_sex = raw_input()
        if stu_sex:
            reg.setStu_sex(stu_sex)
            break
        else:
            print u"请重新输入："
            continue
    #学生的报名信息的显示
    print u"姓名     学号(ID)    身份证\t       学校\t          系别    专业   (ID)密码\t性别\n" #此处空格比较多便于好看    
    print reg.getStu_name()," ",reg.getStu_id()," ",reg.getStu_indentify()," ",reg.getStu_school()," ",reg.getStu_institute()," ",reg.getStu_major()," ",reg.getStu_password()," ",reg.getStu_sex()
    #在sql中增加学生信息中文的输入记住要.decode('gbk')
    conn.execute("insert into "+table_1+" values (?,?,?,?,?,?,?,?)",(reg.getStu_name().decode('gbk') ,reg.getStu_id(),reg.getStu_indentify(),reg.getStu_school().decode('gbk'),reg.getStu_institute().decode('gbk'),reg.getStu_major().decode('gbk'),reg.getStu_password(),reg.getStu_sex().decode('gbk')));
    conn.commit()
    print u"请选择你要报名的科目：\n(1)四级(2)六级"
    exam = Examinee.Examinee()
    nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S");#生成当前时间  
    exam_seat = random.randint(1,25)
    if exam_seat<10:
        exam_seat=str(0)+str(exam_seat);  
    exam.setExam_seat(exam_seat)
    ex = raw_input()
    exam_room_4=random.randint(1,10);
    exam_room_6=random.randint(11,20)
    exam_place = 'buiding 8'
    exam.setExam_major(exam_place)
    if ex == '1':
        print u"你报名的是四级,考场号：",exam_room_4
        exam_major = "cet4"
        exam.setExam_major(exam_major)
        exam.setExam_room(exam_room_4)
        exam_id=str(nowTime)+"Z"+str(exam_room_4)+str(exam_seat);
        exam.setExam_id(exam_id)
        print u"你的准考证号是：",exam.getExam_id()
        print u"你的座位号位：",exam.getExam_seat()
    else: 
        print u"你报名的是六级,考场号：",exam_room_6
        exam_major = "cet6"
        exam.setExam_major(exam_major)
        exam.setExam_room(exam_room_6)
        exam_id=str(nowTime)+"Z"+str(exam_room_6)+str(exam_seat);
        exam.setExam_id(exam_id)
        print u"你的准考证号是：",exam.getExam_id()
        print u"你的座位号位：",exam.getExam_seat()
    exam_place = u"八大楼"
    conn.execute("insert into "+table_4+" values (?,?,?,?,?,?,?,?)",(reg.getStu_name().decode('gbk'),reg.getStu_indentify(),reg.getStu_school().decode('gbk'),exam.getExam_id(),exam_place,exam.getExam_room(),exam.getExam_seat(),exam.getExam_major().decode('gbk')));
    conn.commit()
    print u"注册成功！是否查看自己的准考证信息：(y/n),n返回上一个菜单"
    ou= raw_input()
    #注册成功后显示学生的准考证信息
    if ou in ['Y','y',' ']:
        co =conn.execute("select * from "+table_4+" where exam_id="+"'"+exam.getExam_id()+"'")
        for row in co:
            print u"姓    名:",row[0]
            print u"身 份 证:",row[1]
            print u"学校名称:",row[2]
            print u"准考证号:",row[3]
            print u"考场地点:",row[4]
            print u"考场编号:",row[5]
            print u"座位号码:",row[6]
            print u"科目名称:",row[7]
        print u"准考证信息显示完成是否返回上一个菜单(y/n)"
        op1 = raw_input()
        if op1 in ['Y','y',' ']:           
            stu()
        else:
            stu()
    else:  
        print u"是否退出系统：(y/n)"
        op = raw_input()
        if op == "Y" or op == "y" or op == "":
            sys.exit(0)
            conn.close()
        else:
            showmenu1()
#学生的准考证信息查看方法
def stu_examminee():
     cursor = conn.execute("SELECT * FROM 考生信息 ")
     print u"姓名     学号(ID)    身份证\t       学校\t          系别    专业   (ID)密码\t性别\n" #此处空格比较多便于好看
     for row in cursor:
         print row[0]," ",row[1]," ",row[2]," ",row[3]," ",row[4]," ",row[5]," ",row[6]," ",row[7],"\n"
     print u"准考证信息显示完成是否返回上一个菜单(y/n)"
     op1 = raw_input()
     if op1 in ['Y','y',' ']:
         showmenu2()
     else:
         stu_examminee()
#学生登录立体查看自己的报名信息和准考准考证信息
def stu_login():
    reg = Reg.Reg()
    print u"请输入你的学号"
    stu_id = raw_input()
    temp = conn.execute("select stu_id from "+table_1+" where stu_id="+"'"+stu_id+"'")
    print u"请输入你的密码："
    stu_password= raw_input()
    temp_1 =conn.execute("select stu_password from "+table_1+" where stu_id="+"'"+stu_id+"'")
    temp_new =0
    temp_old =0
    for re in temp:
        temp_new = re[0]
    for re_1 in temp_1:
        temp_old = re_1[0]
    if stu_id == temp_new:
        if stu_password == temp_old:
            print u"欢迎学号",stu_id
            if True:
                reg.setStu_id(stu_id)
                showmenu5(stu_id)
            else:
                stu_login()
        else:
            print u"你的密码错误,请重新输入"
            stu_login()
    else:
        print u"你的学号错误，请重新输入："
        stu_login()
#学生用户信息管理
def showmenu5(stu_id):
    print u"[1]报名信息管理\n[2]准考证信息查看\n[3]返回上页菜单\n请选择："
    done = False
    while not done:        
        chosen = False
        while not chosen:
            try:
                choice = raw_input().strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice = 'q'
            print u"\n你的选择：[%s]" % choice
            if choice not in '123q':
                print u"选择错误，请重新输入"
            else:
                chosen = True
        if choice == 'q':done = True
        if choice == '1':see_bmmess(stu_id)
        if choice == '2':see_ex(stu_id) 
        if choice == '3':stu()   
#报名信息管理
def see_bmmess(stu_id):
    print u"[1]报名信息查询\n[2]报名信息更改\n[3]返回上页菜单\n请选择："
    done = False
    while not done:       
        chosen = False
        while not chosen:
            try:
                choice = raw_input().strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice = 'q'
            print u"\n你的选择：[%s]" % choice
            if choice not in '123q':
                print u"选择错误，请重新输入"
            else:
                chosen = True
        if choice == 'q':done = True
        if choice == '1':see_bm(stu_id)
        if choice == '2':update_bm(stu_id) 
        if choice == '3':showmenu5(stu_id) 
#报名信息的查询
def see_bm(stu_id):
    reg = Reg.Reg()
    reg.setStu_id(stu_id)
    coo =conn.execute("SELECT * FROM "+table_1+" WHERE stu_id="+"'"+reg.getStu_id()+"'")
    print u"姓名     学号(ID)    身份证\t       学校\t          系别    专业   (ID)密码\t性别\n" #此处空格比较多便于好看    
    for row in coo:
        print row[0]," ",row[1]," ",row[2]," ",row[3]," ",row[4]," ",row[5]," ",row[6]," ",row[7],"\n"           
    print u"是否返回上一个菜单(y/n)"
    op1 = raw_input()
    if op1 in ['Y','y',' ']:
        see_bmmess(stu_id)   
    else:
        showmenu3()
#更新报名信息 
def update_bm(stu_id):
    reg = Reg.Reg()
    print u"你要更改学校为："
    stu_school = raw_input()
    reg.setStu_id(stu_id)
    conn.execute("UPDATE "+table_1+" SET stu_school="+"'"+stu_school+"'"+"where stu_id="+"'"+reg.getStu_id()+"'")
    print u"学号为："+reg.getStu_id()+"的学校信息已经更改，是否继续(y/n):"
    op2 = raw_input()
    if op2 == "Y" or op2 == "y":
        update_bm()
    else:
        print u"是否查看学生的报名信息：(y/n)"
        op1 = raw_input()
        if op1 == "Y" or op1 == "y":
            coo =conn.execute("SELECT * FROM "+table_1+" WHERE stu_id="+"'"+reg.getStu_id()+"'")
            print u"姓名     学号(ID)    身份证\t       学校\t          系别    专业   (ID)密码\t性别\n" #此处空格比较多便于好看    
            for row in coo:
                print row[0]," ",row[1]," ",row[2]," ",row[3]," ",row[4]," ",row[5]," ",row[6]," ",row[7],"\n"           
            print u"是否返回上一个菜单(y/n)"
            op1 = raw_input()
            if op1 == "Y" or op1 == "y":
                see_bmmess(stu_id) 
            else:
                update_bm(stu_id)
        else:
            see_bmmess() 
#学生的准考证信息
def see_ex(stu_id):
    reg =Reg.Reg()
    reg.setStu_id(stu_id)
    print u"\n你的准考证信息："
    co =conn.execute("select * from "+table_4+" where stu_name in "+"(select stu_name from "+table_1+" where stu_id="+"'"+reg.getStu_id()+"'"+")")
    for row in co:
        print u"姓    名:",row[0]
        print u"身 份 证:",row[1]
        print u"学校名称:",row[2]
        print u"准考证号:",row[3]
        print u"考场地点:",row[4]
        print u"考场编号:",row[5]
        print u"座位号码:",row[6]
        print u"科目名称:",row[7]
    if True:
        print u"是否返回上一个菜单：(y/n)"
        op1 = raw_input()
        if op1 == "Y" or op1 == "y":
            showmenu5(stu_id)
        else:
            see_ex()   
#删除学生报名信息的方法
def del_stu():        
    print u"你要删除哪位学生信息：(请输入他的学号)"
    stu_id = raw_input()
    conn.execute("delete from "+table_4+" where stu_name in"+"(select stu_name from "+table_1+" where stu_id="+"'"+stu_id+"'"+")")
    conn.commit()    
    conn.execute("delete from "+table_1+" where stu_id="+"'"+stu_id+"'")   
    conn.commit()
    print u"学号为："+stu_id+"的所有报名信息和考生信息已经删除，是否继续(y/n):"
    op = raw_input()
    if op == "Y" or op == "y" or op == "":
        del_stu()
    else:
        print u"是否查看学生的报名信息：(y/n)"
        op1 = raw_input()
        if op1 == "Y" or op1 == "y":
            seeStu()
        else:
            showmenu3()
#更改学生报名信息
def update_stu():
    print u"你要更改哪位学生的学校信息：(请输入他的学号)"
    stu_id = raw_input()
    print u"你要更改学校为："
    stu_school = raw_input()
    conn.execute("UPDATE "+table_1+" SET stu_school="+"'"+stu_school+"'"+"where stu_id="+"'"+stu_id+"'")
    print u"学号为："+stu_id+"的学校信息已经更改，是否继续(y/n):"
    op2 = raw_input()
    if op2 == "Y" or op2 == "y":
        update_stu()
    else:
        print u"是否查看学生的报名信息：(y/n)"
        op1 = raw_input()
        if op1 in ['Y','y']:
            coo =conn.execute("SELECT * FROM "+table_1+" WHERE stu_id="+"'"+stu_id+"'")
            #conn.commit()
            print u"姓名     学号(ID)    身份证\t       学校\t          系别    专业   (ID)密码\t性别\n" #此处空格比较多便于好看    
            for row in coo:
                print row[0]," ",row[1]," ",row[2]," ",row[3]," ",row[4]," ",row[5]," ",row[6]," ",row[7],"\n"           
            print u"是否返回上一个菜单(y/n)"
            po= raw_input()
            if po in ['Y','y']:
                showmenu3()
            else:
                update_stu()
        else:
            print u"是否返回上一个菜单(y/n)"
            po= raw_input()
            if po in ['Y','y']:
                showmenu3()
            else:
                update_stu()
            
 #查看考场信息 
def seeRoom():
    cursor = conn.execute("SELECT * FROM 考场信息 ")
    print u"考场编号\t考场地点\t考试科目"
    for row in cursor:
        print row[0],"\t\t",row[1],"\t\t",row[2]
    print u"是否返回上一个菜单(y/n)"
    po= raw_input()
    if po in ['Y','y']:
        showmenu4()
    else:
        seeRoom()
#增加考场的方法九大楼
def addRoom():
    print u"你要增加考场的编号："
    exam_room = raw_input()
    print u"你要增加考场的地点："
    exam_place = raw_input()
    print u"你要增加考场的科目："
    exam_major = raw_input()
    conn.execute("insert into "+table_3+" values (?,?,?)",(exam_room,exam_place.decode('gbk'),exam_major));
    conn.commit()
    print u"考场信息已经增加，是否查看(y/n),否则返回上一个菜单"
    op2 = raw_input()
    if op2 == "Y" or op2 == "y":
        seeRoom()
        print u"是否继续增加(y/n),否则返回上一个菜单"
        op5 = raw_input()
        if op5 == "Y" or op5 == "y":
            addRoom()
        else:
            showmenu4()
    else:
        showmenu4()
#删除考场方法
def delRoom():
    print u"你要删除哪个考场信息：(请输入考场编号)"
    exam_room = raw_input()
    conn.execute("delete from "+table_3+" where exam_room="+"'"+exam_room+"'")
    conn.commit()
    print u"考场为："+exam_room+"的所有信息已经删除，是否继续(y/n):"
    op = raw_input()
    if op == "Y" or op == "y" or op == "":
        delRoom()
    else:
        print u"是否查看考场信息：(y/n),否则返回上一个菜单"
        op1 = raw_input()
        if op1 == "Y" or op1 == "y":
            seeRoom()
        else:
            showmenu4()
#更改考场信息
def updateRoom():
     print u"你要更改哪个考场信息：(请输入考场编号)"
     exam_room =raw_input()
     print u"你要更改的科目为："
     exam_major= raw_input()
     conn.execute("UPDATE "+table_3+" SET exam_major="+"'"+exam_major+"'"+"where exam_room="+"'"+exam_room+"'")
     print u"考场编号为："+exam_room+"的信息已经更改，是否继续(y/n):"
     op2 = raw_input()
     if op2 == "Y" or op2 == "y":
        updateRoom()
     else:
         print u"是否查看已经更改的考场信息：(y/n)"
         op1 = raw_input()
         if op1 in ['Y','y']:
             coo =conn.execute("SELECT * FROM "+table_3+" WHERE exam_room="+"'"+exam_room+"'")
             print u"考场编号\t考场地点\t考试科目"
             for row in coo:
                 print row[0],"\t\t",row[1],"\t\t",row[2]
             print u"是否返回上一个菜单：(y/n)"
             op0 = raw_input()
             if op0 in ['y','Y']:
                 showmenu4()
             else:
                 updateRoom()
         else:
             print u"是否返回上一个菜单：(y/n)"
             op0 = raw_input()
             if op0 in ['y','Y']:
                 showmenu4()
             else:
                 updateRoom()
if __name__ == '__main__':
    conn = sqlite3.connect('cet4_6.db')
    if True:
        print u"\n欢迎来到四六级报名系统：\n四六级管理系统数据库连接成功！"
    showmenu1()