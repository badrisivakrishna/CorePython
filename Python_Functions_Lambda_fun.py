# Databricks notebook source
lambda_fun = lambda a : a+10
lambda_fun(10)

# COMMAND ----------

lambda_fun_a = lambda a,b : a+b
lambda_fun_a(10,20)

# COMMAND ----------

type(lambda_fun_a)

# COMMAND ----------

lambda_fun_b = lambda a,b : (a+b,a*b)
lambda_fun_b(10,20)

# COMMAND ----------

def fun_sum(a,b):
    return a+b
fun_sum(10,20)

# COMMAND ----------

def fun_noArg():
    print("Hi this function do not have any arg")
fun_noArg()

# COMMAND ----------

def fun_storeRes (a,b):
    print("Sum of two paramers are: ", (a+b))
    return (a+b)
result = fun_storeRes(10,5)
result

# COMMAND ----------

def fun_pos(ename,age):
    print("Employee name is: ",ename)
    print("Employee age is: ",age)
fun_pos("sivakrishna",38)
fun_pos(age= 32, ename="Sowjanya")

# COMMAND ----------

def fun_pos1(ename,age=18):
    print("Employee name is: ",ename)
    print("Employee age is: ",age)
fun_pos1("sivakrishna")
fun_pos1("sivakrishna",38)

# COMMAND ----------

def fun_pos2(ename,sal,age=18):
    print("Employee name is: ",ename)
    print("Employee age is: ",age)
    print("Employee Sal is: ",sal)
fun_pos2(ename="sivakrishna",sal=10000)
fun_pos2("sivakrishna",38,2000)

# COMMAND ----------

def fun_sum_nArg(*args):
    total = 0
    for i in args:
        print(type(i))
        total += sum(i)
    print("Sum of arguments are: ",total)
fun_sum_nArg(1,2,3,4)

# COMMAND ----------

for i in [1,2,3]:
    print(type(i))

# COMMAND ----------

def fun_keyval_arg(**kvargs):
    print(kvargs)
fun_keyval_arg(name="siva",age=30)

# COMMAND ----------

def fun_keyval_arg1(**kvargs):
    for k,v in kvargs.items():
        print("Keys: ",k)
        print("values: ",v)
fun_keyval_arg1(name="siva",age=30)

# COMMAND ----------

