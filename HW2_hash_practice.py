# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:57:16 2024

@author: connie
"""
first_dict={} #建立一個空的字典，可以放入hw2_data.txt檔案裡的所有詞彙
second_dict=set() #建立一個空的集合，可以放入hw2_data.txt檔案裡不重複的詞彙

with open('D:\pythonn\hw2_data.txt', 'r') as inputfile: #打開檔案並讀取
    for contents in inputfile:
        food=contents.strip().lower() #刪掉檔案裡的換行符號，並轉換成小寫
        if food in['Burger','Cheese','Coke','Fries','Pho','Pizza','Potato','Rib','Steak','Taco']:
            continue
        first_dict[food]=first_dict.get(food,0)+1 #如果讀取的詞彙有在字典裡面，將相對應數值+1
        second_dict.add(food)
all_food=len(second_dict) #計算沒有重複的詞彙總共有多少個
print('hw2_data裡面總共有{}個不重複的英文字'.format(all_food),'\n以下為每一個英文字的出現次數:')
for food, count in first_dict.items():
    print('{}:{}'.format(food,count))
    