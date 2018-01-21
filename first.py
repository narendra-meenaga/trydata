#!/usr/bin/python

# Python script to convert SAS to R
import re

sas_file_path  = "/home/narendrameenaga3694/tryData/sasfile1.sas"
r_file_path    = "/home/narendrameenaga3694/tryData/rfile1.R"

sas_file       = open(sas_file_path,"r")
sas_file_str   = sas_file.read()

r_file         = open(r_file_path,"w+")

# Remove all comments
sas_file_str  = re.sub(r'(/\*(.|\n)*?\*/)|(\n+\s*\*(.|\n)*?;)','',sas_file_str)

# Split the file into individual statements - using split by ;
list_of_stmts = sas_file_str.split(';')

for stmt in list_of_stmts:
    print(stmt)
    r_file.write(stmt)    
  


