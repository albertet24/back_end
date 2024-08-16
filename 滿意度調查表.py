# -*- coding: utf-8 -*-
"""
Created on Sat May 18 16:13:55 2024

@author: user
"""
def submit_form():
    name = name_en.get()
    gender = gender_var.get()
    age = age_var.get()
    phone = phone_en.get()
    meals1 = [meals1_list[i] for i in range(len(meals1_list)) if meals1_vars[i].get()]
    meals2 = [meals2_list[i] for i in range(len(meals2_list)) if meals2_vars[i].get()]
    suggestion = suggestion_text.get("1.0", tk.END).strip()
    
    print("姓名:", name)
    print("性別:", gender)
    print("年齡:", age)
    print("聯絡電話:", phone)
    print("今日喜歡餐點:", meals1)
    print("今日不喜歡餐點:", meals2)
    print("建議事項:", suggestion)   
    
    result_lr.config(text=f"姓名: {name}\n性別: {gender}\n年齡: {age}\n聯絡電話: {phone}\n今日喜歡餐點: {meals1}\n今日不喜歡餐點: {meals2}\n建議事項: {suggestion}")
    

import tkinter as tk

ted = tk.Tk()
ted.title("用餐滿意度調查")
ted.geometry("410x450")
ted.resizable(False,False)

store_la = tk.Label(ted,text="歡迎蒞臨本店用餐 您的意見是我們進步的動力!",font=("微軟黑正體", 12),width=100,height=2)
store_la.pack()

frame1 = tk.Frame(ted)
frame1.pack(anchor="w")

name_la = tk.Label(frame1,text="姓名:")
name_la.pack(side="left")

name_en = tk.Entry(frame1,width=10)
name_en.pack(side="left")

gender_La = tk.Label(frame1,text="     性別:")
gender_La.pack(side="left")

gender_var = tk.StringVar()
gender_var.set("男") 

male_ra = tk.Radiobutton(frame1,text="男",value="男",variable=gender_var)
male_ra.pack(side="left")

female_ra = tk.Radiobutton(frame1,text="女",value="女",variable=gender_var)
female_ra.pack(side="left")

phone_la = tk.Label(frame1,text="聯絡電話:")
phone_la.pack(side="left")

phone_en = tk.Entry(frame1,width=14)
phone_en.pack(side="left")

frame2 = tk.Frame(ted)
frame2.pack(anchor="w")

age = tk.Label(frame2,text="年齡:")
age.pack(side="left")

age_var = tk.StringVar()
age_var.set("20歲以下") 

age1 = tk.Radiobutton(frame2,text="20歲以下",value="20歲以下",variable=age_var)
age1.pack(side="left")

age2 = tk.Radiobutton(frame2,text="21-30歲",value="21-30歲",variable=age_var)
age2.pack(side="left")

age3 = tk.Radiobutton(frame2,text="31-40歲",value="31-40歲",variable=age_var)
age3.pack(side="left")

age4 = tk.Radiobutton(frame2,text="41-50歲",value="41-50歲",variable=age_var)
age4.pack(side="left")

age5 = tk.Radiobutton(frame2,text="50歲以上",value="50歲以上",variable=age_var)
age5.pack(side="left")

frame3 = tk.Frame(ted)
frame3.pack(anchor="w")

meals1_la = tk.Label(frame3,text="今日喜歡餐點為(可複選):") 
meals1_la.pack(side="left")

frame4 = tk.Frame(ted)
frame4.pack(anchor="w")

meals1_list = ["開胃菜","沙拉","湯品","主菜","甜點","飲料"]
meals1_vars = [tk.IntVar() for i in range(len(meals1_list))]

for i in range(len(meals1_list)):
    chk1 = tk.Checkbutton(frame4,text=meals1_list[i],variable=meals1_vars[i])
    chk1.pack(side="left")

frame5 = tk.Frame(ted)
frame5.pack(anchor="w")

meals2_la = tk.Label(frame5,text="今日不喜歡餐點為(可複選):") 
meals2_la.pack(side="left")

frame6 = tk.Frame(ted)
frame6.pack(anchor="w")

meals2_list = ["開胃菜","沙拉","湯品","主菜","甜點","飲料"]
meals2_vars = [tk.IntVar() for i in range(len(meals2_list))]

for y in range(len(meals2_list)):
    chk2 = tk.Checkbutton(frame6,text=meals2_list[y],variable=meals2_vars[y])
    chk2.pack(side="left")

frame7 = tk.Frame(ted)
frame7.pack(anchor="w")

suggestion_la = tk.Label(frame7,text="建議事項:")
suggestion_la.pack(side="left")

frame8 = tk.Frame(ted)
frame8.pack(anchor="w")

suggestion_text = tk.Text(frame8,height=5,width=55)
suggestion_text.pack(side="left")

frame9 = tk.Frame(ted)
frame9.pack()

submit_bu = tk.Button(frame9,text="提交",command=submit_form)
submit_bu.pack()

result_fr = tk.Frame(ted,bd=2,relief=tk.GROOVE) 
result_fr.pack(padx=10, pady=10,anchor=tk.CENTER)

result_lr = tk.Label(result_fr,text="",justify="left",anchor=tk.CENTER)
result_lr.pack()

ted.mainloop()