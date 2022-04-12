# Databricks notebook source
# DBTITLE 1,Python Datatype tutorial from TechLake Youtube Channel -- Ravindaar T
# MAGIC %md
# MAGIC https://www.youtube.com/watch?v=iorae42_LNU&list=PL50mYnndduIHs5KReaz7F7aSelC-zG2zP&index=3

# COMMAND ----------

str = "siva"

# COMMAND ----------

str

# COMMAND ----------

v_range = range(0,10,2)
print(v_range, type(v_range))
list(v_range) #stop value 10 so it will not count

# COMMAND ----------

v_string = 'sivakrishna'
v_string_d = "lucky"
print(v_string,v_string_d)

# COMMAND ----------

v_string_threequote = '''Hello when we use more than one line use 
this three quotes'''
print(v_string_threequote, type(v_string_threequote), type(v_string),type(v_string_d))

# COMMAND ----------

v_int = 70
print('variable value: {0} variable data type:{1} '.format(v_int,type(v_int)))

# COMMAND ----------

v_float = 44.22
print(v_float,type(v_float))

# COMMAND ----------

list = [12,58.2,'Hello',"Siva",True]
print(list, type(list))

# COMMAND ----------

v_tuple = ()
print(type(v_tuple))

# COMMAND ----------

v_set = {}
print(type(v_set)) #by default empty curly brockets are dicttionary

# COMMAND ----------

v_set_values = {1,3,6,8}
print(v_set_values) # these are not in order

# COMMAND ----------

v_set_nodups_allow = {1,2,2,3,5,5}
print(v_set_nodups_allow)

# COMMAND ----------

v_set_values[0] # it is not index based

# COMMAND ----------

v_dict = {"name":"Sivakrishna","qualification":"MBA"}
print(v_dict,type(v_dict))

# COMMAND ----------

v_dict = {"name":"siva","address":{"state":"Hyd","street":"BHEL"}}

# COMMAND ----------

v_dict["address"]["state"]

# COMMAND ----------

v_dict["name"]="Sivakrishna"

# COMMAND ----------

v_dict

# COMMAND ----------

v_frozenset = frozenset({"apple","banana","Grapes"})
print(v_frozenset,type(v_frozenset))

# COMMAND ----------

v_set = {"apple","banana","Grapes"}
v_set[0] = "APPLE"
print(v_set)

# COMMAND ----------

v_frozenset = {"APPLE","banana","Grapes"}

# COMMAND ----------

v_frozenset

# COMMAND ----------

v_bool = False
v_bool_T = True
num_true = 1
print(bool(num_true))
num_false = 0
print(bool(num_false))

# COMMAND ----------

# MAGIC %md
# MAGIC bytes data type

# COMMAND ----------

v_byte = b'Hello this is byte'
print(v_byte)
print(type(v_byte))

# COMMAND ----------

v_byte[-2:]

# COMMAND ----------

v_integer = 55
print(bytes(v_integer))
v_str_b = "Hello"
print(bytes(v_str_b,'utf-8'))
print(bytes(v_str_b,'utf-16'))
print(bytes(v_str_b,'utf-32'))

# COMMAND ----------

import datetime
x_date = datetime.datetime.now()
print(x_date)

# COMMAND ----------

print('date: ',x_date)
print('year: ',x_date.year)
print('month: ',x_date.month)
print('day: ',x_date.day)
print(x_date.strftime("%A"))
print(x_date.strftime("%a"))
print(x_date.strftime("%B"))
print(x_date.strftime("%b"))
print(x_date.strftime("%H"))
print(x_date.strftime("%I"))

# COMMAND ----------

help(datetime)

# COMMAND ----------

