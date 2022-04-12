# Databricks notebook source
print("this is sample print")

# COMMAND ----------

name ='sivakirshna'
NAME = 'SIVA'

# COMMAND ----------

name, NAME #case sensitive language

# COMMAND ----------

age = 30
print(age)

# COMMAND ----------

name
age

# COMMAND ----------

print(name)
print(age) #use print for multiple outputs

# COMMAND ----------

type(age)

# COMMAND ----------

weight = 85.2
type(weight)

# COMMAND ----------

yes = True
type(yes)

# COMMAND ----------

help(yes)

# COMMAND ----------

list = [1,2,3]
type(list)

# COMMAND ----------

help(list)

# COMMAND ----------

dir(list) #supporting functions related to that element

# COMMAND ----------

True = [1,2,3]

# COMMAND ----------

list_memoryLoc = [50,45,60]
id(list_memoryLoc)

# COMMAND ----------

name_mem_loc = 'sivakrishna'
id(name_mem_loc)

# COMMAND ----------

c= 100
d = 5
id(c), id(d)

# COMMAND ----------

# MAGIC %md
# MAGIC We can write some text here

# COMMAND ----------

total_rec = 100
accept_rec = 90
reject_rec = 10
print('total records: {}, accepted records: {},rejected records: {}'.format(total_rec,accept_rec,reject_rec))

# COMMAND ----------

print(f'total records: {total_rec}, accepted records: {accept_rec},rejected records: {reject_rec}')

# COMMAND ----------

print('total records: {1}, accepted records: {1},rejected records: {0}'.format(total_rec,accept_rec,reject_rec))

# Just checking position

# COMMAND ----------

print(name)
print(name[-2:])

# COMMAND ----------

