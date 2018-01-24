#!/usr/bin/python
# Python script to convert R  to SparkR
import re
import pandas as pd

r_file_path    = "/home/narendrameenaga3694/tryData/rfile1.R"

r_file       = open(r_file_path,"r")
r_file_str   = r_file.read()

# Assume that all lines are syntactically correct

list_of_stmts = r_file_str.split('\n')
df1 = pd.DataFrame(list_of_stmts,columns=['initial'])
trimmed_strings = []
comments_flag   = []


for index,row in df1.iterrows():
   #print (row['initial'])
   # Trim the strings on both sides
   trimmed_string = row['initial'].strip()
   trimmed_strings.append(trimmed_string)
   #Check  for comments
   print(trimmed_string[:1])
   if (trimmed_string[:1] == '#'): 
      comments_flag.append("YES")
   else:
      comments_flag.append("NO")

df1['trimmed'] = trimmed_strings
df1['comment'] = comments_flag

#print(df['initial'][3])

print(df1)
