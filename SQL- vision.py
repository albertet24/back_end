import pymysql
conn= pymysql.connect(host= "localhost", user="albertet24", passwd="sahtysle24", db= 'test', charset= "utf8")
cur=conn.cursor()

import tkinter as tk

import hashlib
md5= hashlib.md5()

ac_staff=tk.Tk()
ac_staff.title("login system")
#變數
staff_account= tk.StringVar()
staff_pwd = tk.StringVar()
ac_staff.geometry('500x500')

#--------register-------------

    
def reg_page():
    ac_staff.withdraw()
    reg_page =tk.Toplevel(ac_staff)
    reg_page.geometry('500x500')
    reg_page.title=("註冊帳號")
    line_1= tk.Label(reg_page, text="------------------------------------------")
    line_2= tk.Label(reg_page, text="------------------------------------------")
    title_label= tk.Label(reg_page, text="註冊新帳號", font=15)
    line_1.pack()
    title_label.pack()
    line_2.pack()
    
    def back_index():
        def back():
                reg_page.destroy()
                back_index.destroy()
                ac_staff.deiconify()
            
        reg_page.withdraw()
        back_index=tk.Toplevel(ac_staff)
        back_index.geometry("500x100")
        
        reg_oklab=tk.Label(back_index,text="註冊完成")
        reg_ok_btn=tk.Button(back_index, text="返回登入", command=back)
        reg_oklab.pack(pady=10)
        reg_ok_btn.pack(pady=10)
        
        
    def Insert_info():
        new_name=name_entry.get()
        new_acc= acc_entry.get()
        new_pwd=pwd_entry.get()
        check_sql="SELECT sf_account FROM staff_info WHERE sf_account='"+new_acc+"' AND sf_del='0' "
        cur.execute(check_sql)
        chk_acc=cur.fetchone()
        '''md5.update(new_pwd.encode('utf-8'))
        #獲取MD5十六進制表示
        pwd_value = md5.hexdigest()'''
        if not chk_acc == None:
            #print("{}帳號已存在".format(new_acc))
            result_label.config(text=f'{new_acc}已註冊，請使用其他帳號')
        else:
            chk_sql2= "INSERT INTO staff_info (sf_name, sf_account, sf_pwd, create_user, update_user) VALUES('"+new_name+"','"+new_acc+"' ,'"+new_pwd+"', '"+new_acc+"', 'SYSTEM')"
            print(chk_sql2)
            cur.execute(chk_sql2)
            conn.commit()
            #print("{}註冊成功".format(new_acc))
            back_index()
        
       
            
    
    reg_frame1=tk.Frame(reg_page,bd=20)
    reg_frame1.pack(side='top', anchor=tk.CENTER)
    reg_name=tk.Label(reg_frame1, text="請輸入姓名: ")
    reg_name.pack(side="left")
    name_entry=tk.Entry(reg_frame1)
    name_entry.pack(side='left')
    
    reg_frame2=tk.Frame(reg_page,bd=10)
    reg_frame2.pack(side='top', anchor=tk.CENTER)
    reg_acclab=tk.Label(reg_frame2, text="請輸入帳號: ")
    reg_acclab.pack(side="left")
    acc_entry=tk.Entry(reg_frame2, )
    acc_entry.pack(side="left")
    
    reg_frame2=tk.Frame(reg_page,bd=10)
    reg_frame2.pack(side="top",anchor=tk.CENTER)
    reg_pwdlab=tk.Label(reg_frame2, text="請輸入密碼: ")
    reg_pwdlab.pack(side="left")
    pwd_entry=tk.Entry(reg_frame2)
    pwd_entry.pack(side="left")
    
    result_frame=tk.Frame(reg_page,bd=10)
    result_label=tk.Label(result_frame, text="")
    result_frame.pack(padx=10,pady=10, anchor="w")
    result_label.pack()
    
    
    
    reg_btn=tk.Button(reg_page, text="註冊帳號",command=Insert_info)
    reg_btn.pack()

#------------------------功能選單------------------

def index2_page():
    def seach_result():
        get_acc= seach_box.get()
        check_sql="SELECT sf_account FROM staff_info WHERE sf_account='"+get_acc+"' AND sf_del='0' "
        cur.execute(check_sql)
        chk_acc=cur.fetchone()
        #print(chk_acc)
        if chk_acc is None:
            #print("帳號密碼錯誤")
            seach_result_lab.config(text=f'{get_acc}無此帳號')
        else:
            seach_sql="SELECT sf_pk, sf_name, sf_account, sf_pwd, sf_level FROM staff_info WHERE sf_account='"+get_acc+"'AND sf_del='0' "
            #print(seach_sql)
            cur.execute(seach_sql)
            gotacc=cur.fetchone()
            seach_result_lab.config(text=f"{get_acc}資料--編號{gotacc[0]} 使用者名稱為{gotacc[1]} 系統層級為 {gotacc[4]} ")
    def destroy():
        index2_page.destroy()
        ac_staff.deiconify()
        
    #-------------------更改密碼--------------------
    def chg_pwd():
        chk_block=seach_box.get()
        chk_sql4="SELECT sf_account FROM staff_info WHERE sf_account= '"+chk_block+"' AND sf_del='0'"
        cur.execute(chk_sql4)
        chk_sql_result=cur.fetchone()
        #print(chk_sql_result)
        #------------------結束選單
        def back_index2():
            def back():
                    pwd_page.destroy()
                    back_index2.destroy()
                    index2_page.deiconify()
                
            pwd_page.withdraw()
            back_index2=tk.Toplevel(index2_page)
            back_index2.geometry("500x100")
            
            pwd_oklab=tk.Label(back_index2,text="修改完成")
            pwd_ok_btn=tk.Button(back_index2, text="返回選單", command=back)
            pwd_oklab.pack(pady=10)
            pwd_ok_btn.pack(pady=10)
            
        if chk_block == "":
            result_label2.config(text="請先輸入帳號資料")
        elif chk_sql_result is None:
            result_label2.config(text=f'{chk_block}無此帳號')

        else:
            pwd_page=tk.Toplevel(index2_page)
            def change_pwd():
                new_passwd=chg_pwdbox.get()
                chk_passwd=chg_pwdbox2.get()
                if new_passwd != chk_passwd:
                    result_label3.config(text="密碼不相同")
                else:
                    change_sql1="UPDATE staff_info SET sf_pwd='"+new_passwd+"' WHERE sf_account='"+chk_block+"' "
                    #print(change_sql1)
                    cur.execute(change_sql1)
                    conn.commit()
                    back_index2()
                    
            
            chg_pwd_frame=tk.Frame(pwd_page, bd=20)
            chg_pwd_frame.pack(side="top", anchor=tk.CENTER)
            chg_pwd_frame2=tk.Frame(pwd_page, bd=20)
            chg_pwd_frame2.pack(side="top", anchor=tk.CENTER)
            chg_pwdlab=tk.Label(chg_pwd_frame, text="請輸入要更改的密碼: ")
            chg_pwdbox=tk.Entry(chg_pwd_frame)
            chg_pwdlab2=tk.Label(chg_pwd_frame2, text="請再次確認密碼:     ")
            chg_pwdbox2=tk.Entry(chg_pwd_frame2)
            chg_pwdlab.pack(side="left")
            chg_pwdbox.pack(side="left")
            chg_pwdlab2.pack(side="left")
            chg_pwdbox2.pack(side="left")
            chg_pwd_btn=tk.Button(pwd_page, text="確認", command=change_pwd)
            chg_pwd_btn.pack(pady=10)
            result_frame3=tk.Frame(pwd_page, bd=0)
            result_frame3.pack(padx=10,pady=10, anchor=tk.CENTER)
            result_label3=tk.Label(result_frame3, text="", anchor="w", justify=tk.LEFT)
            result_label3.pack()
        #-----------------------更改姓名    
    def chg_name():
        chk_block=seach_box.get()
        chk_sql4="SELECT sf_account FROM staff_info WHERE sf_account= '"+chk_block+"' AND sf_del='0'"
        cur.execute(chk_sql4)
        chk_sql_result=cur.fetchone()
        
        #------------------結束選單
        def back_index2():
            def back():
                back_index2.destroy()
                index2_page.deiconify()
                
            name_page.withdraw()
            back_index2=tk.Toplevel(index2_page)
            back_index2.geometry("500x100")
            
            name_oklab=tk.Label(back_index2,text="修改完成")
            name_ok_btn=tk.Button(back_index2, text="返回選單", command=back)
            name_oklab.pack(pady=10)
            name_ok_btn.pack(pady=10)
            
        if chk_block == "":
            result_label2.config(text="請先輸入帳號資料")
        elif chk_sql_result is None:
            result_label2.config(text=f"{chk_block}查無此帳號")
        else:
            name_page=tk.Toplevel(index2_page)
            def change_name():
                new_name=chg_namebox.get()
                change_sql2="UPDATE staff_info SET sf_name='"+new_name+"' WHERE sf_account='"+chk_block+"' "
                #print(change_sql2)
                cur.execute(change_sql2)
                conn.commit()
                back_index2()
                
            
            chg_name_frame=tk.Frame(name_page, bd=20)
            chg_name_frame.pack(side="top", anchor=tk.CENTER)
            chg_namelab=tk.Label(chg_name_frame, text="請輸入要更改的姓名: ")
            chg_namebox=tk.Entry(chg_name_frame)
            chg_namelab.pack(side="left")
            chg_namebox.pack(side="left")
            chg_name_btn=tk.Button(name_page, text="確認", command=change_name)
            chg_name_btn.pack(pady=10)
            result_frame3=tk.Frame(name_page, bd=0)
            result_frame3.pack(padx=10,pady=10, anchor=tk.CENTER)
            result_label3=tk.Label(result_frame3, text="", anchor="w", justify=tk.LEFT)
            result_label3.pack()            
    def chg_level ():
        chk_acc= acckeyin.get()
        target_acc=seach_box.get()
        chk_sql4="SELECT sf_account FROM staff_info WHERE sf_account= '"+target_acc+"' AND sf_del='0'"
        cur.execute(chk_sql4)
        chk_sql_result=cur.fetchone()
        if target_acc == "":
            result_label2.config(text="請先輸入帳號資訊")
        elif chk_sql_result is None:
            result_label2.config(text=f"{target_acc}查無此帳號")
        else:
            chk_sql3="SELECT sf_level FROM staff_info WHERE sf_account= '%s' AND sf_del='0'"
            values=(chk_acc) 
            #print(chk_sql3 % values)
            cur.execute(chk_sql3 % values)
            chk_result=cur.fetchone()
            level_result=int(chk_result[0])
            #print(level_result)
            if (level_result) <= 2:
                result_label2.config(text="使用者系統層級不足")
            else:
                level_page=tk.Toplevel(index2_page)
                level_page.geometry("500x200")
                
                def chk_level():
                    chk_page=tk.Toplevel(level_page)
                    chk_page.geometry("500x100")
                    var_level=level_vars.get()
                    var_acc=seach_box.get()
                    def back():
                        level_page.destroy()
                        chk_level.destroy()
                        index2_page.deiconify()
                        
                        
                    level_sql="UPDATE staff_info SET sf_level='"+var_level+"' WHERE sf_account='"+var_acc+"' "
                    print(level_sql)
                    cur.execute(level_sql)
                    conn.commit()
                    level_chk_label=tk.Label(chk_page, text=f"修改完成\n{target_acc}目前層級為 {var_level}")
                    level_chk_label.pack()
                    level_chk_btn=tk.Button(chk_page, text="返回選單", command=back)
                    level_chk_btn.pack()
                    
                    
                
                chk_sql3="SELECT sf_level FROM staff_info WHERE sf_account= '%s' AND sf_del='0'"
                values=(target_acc) 
                #print(chk_sql3 % values)
                cur.execute(chk_sql3 % values)
                target_result=cur.fetchone()
                target_vars=target_result[0]
                
                level_label=tk.Label(level_page,text="請選擇要修改的層級")
                level_label.pack()
                
                level_vars=tk.StringVar()
                level_vars.set(target_vars)
                level_list=["1", "2","3","0"]
                level_item=tk.OptionMenu(level_page, level_vars, *level_list)
                level_item.pack()
                level_btn=tk.Button(level_page, text="確認",command=chk_level)
                level_btn.pack()
                print(level_item)
                
            
            
        
    ac_staff.withdraw()
    index2_page = tk.Toplevel(ac_staff)
    index2_page.geometry('500x600')
    index2_page.title("功能選單")
    line_1= tk.Label(index2_page, text="------------------------------------------")
    line_2= tk.Label(index2_page, text="------------------------------------------")
    title_label= tk.Label(index2_page, text="功能選單", font=15)
    line_1.pack()
    title_label.pack()
    line_2.pack()
    
    seach_frame=tk.Frame(index2_page,bd=10)
    seach_frame.pack(side="top", anchor=tk.CENTER)
    seach_label=tk.Label(seach_frame, text="1. 員工帳號資料: ")
    seach_box=tk.Entry(seach_frame)
    seach_label.pack(side=("left"))
    seach_box.pack(side=("left"))
    seach_btn=tk.Button(seach_frame,text="查詢", command=seach_result)
    seach_btn.pack(side="left", padx=5)
    seach_result_frame=tk.Frame(index2_page, bd=10)
    seach_result_frame.pack(side="top",anchor=tk.CENTER)
    seach_result_lab=tk.Label(seach_result_frame, text="", justify=tk.LEFT, anchor="w")
    seach_result_lab.pack()
    index2_label = tk.Label(index2_page, text="請輸入要執行的項目")
    index2_label.pack()
    
    choice_frame=tk.Frame(index2_page, bd=10)
    choice_frame.pack(side="top" , anchor=tk.CENTER)
    choice_btn1=tk.Button(choice_frame, text="1. 修改密碼",command=chg_pwd)
    choice_btn2=tk.Button(choice_frame, text="2. 修改姓名",command=chg_name)
    choice_btn3=tk.Button(choice_frame, text="3. 修改層級",command=chg_level)
    choice_btn4=tk.Button(choice_frame, text="4. 離開系統", command=destroy)
    choice_btn1.pack(side="top",pady=20)
    choice_btn2.pack(side="top",pady=20)
    choice_btn3.pack(side="top",pady=20)
    choice_btn4.pack(side="top",pady=20)
    result_frame2=tk.Frame(index2_page, bd=0)
    result_frame2.pack(padx=10,pady=10, anchor=tk.CENTER)
    result_label2=tk.Label(result_frame2, text="", anchor="w", justify=tk.LEFT)
    result_label2.pack()
    
    
    
    
def login():      
        check_acc= acckeyin.get()
        check_pwd= pwdkeyin.get()
        if check_acc =="":
            print("帳號不可為空")
            return
        sql_acc="SELECT sf_pk, sf_account, sf_pwd FROM staff_info where sf_account='"+check_acc+"' AND sf_del='0'"
        cur.execute(sql_acc)
        tar_acc= cur.fetchone()
        #print(tar_acc)
        
        if tar_acc is None:
            #print("帳號密碼錯誤")
            result_label.config(text=f'{check_acc}無此帳號')
        mypwd = tar_acc[2]
        #print(mypwd)
        if check_pwd != mypwd:
            #print("帳號密碼錯誤")
            result_label.config(text=f'{check_acc}，密碼錯誤')
            return
        else:
            print("登入成功")
            index2_page()
            
            
        
#------------------登入系統----------------------------

line_1= tk.Label(ac_staff, text="------------------------------------------")
line_2= tk.Label(ac_staff, text="------------------------------------------")
title_label= tk.Label(ac_staff, text="管理員登入系統", font=15)
line_1.pack()
title_label.pack()
line_2.pack()

frame_1=tk.Label(ac_staff,bd=0)
frame_1.pack(side="top",anchor=tk.CENTER,pady=30)

loginlabel=tk.Label(frame_1,text="請輸入帳號:  ", font=1)
loginlabel.pack(side="left")
acckeyin= tk.Entry(frame_1 )
acckeyin.pack(side="left")

frame_2=tk.Label(ac_staff, bd=0)
frame_2.pack(side="top", anchor=tk.CENTER)
loginlabel_2=tk.Label(frame_2, text="請輸入密碼: ",font=1)
pwdkeyin=tk.Entry(frame_2)
loginlabel_2.pack(side="left")
pwdkeyin.pack(side="left")

reg_frame=tk.Frame(ac_staff, bd=10)
reg_frame.pack()

check_btn_1=tk.Button(ac_staff, text="登入", command= login)
check_btn_1.pack()

reg_btn=tk.Button(reg_frame,text="註冊帳號",command=reg_page)
reg_btn.pack()

result_frame = tk.Frame(ac_staff, bd=0)
result_frame.pack(padx=10, pady=10, anchor=tk.CENTER)
    
result_label = tk.Label(result_frame, text="", justify=tk.LEFT, anchor="w")
result_label.pack()

ac_staff.mainloop()
cur.close()
conn.close()