# Databricks notebook source
v_range = range(100)
list = []
for i in v_range:
    list.append(i)
print(list)

# COMMAND ----------

v_ranges = range(1,50)
for i in v_ranges:
    if i%2 == 0:
        print(i, " : Is even number")
    else:
        print(i, " : Is Odd number")

# COMMAND ----------

x = 10
y = 20

if x > y:
    print("x is greater than y")
elif x < y:
    print("y is greater than x")
else:
    print("y is equal to x")


# COMMAND ----------

# MAGIC %md
# MAGIC Short Hand if conditions

# COMMAND ----------

x = 30
y = 20

if x > y: print("x is greater than y")

# COMMAND ----------

x = 30
y = 20

print("x is greater than y") if x > y else print("y is greater than x")

x = 10
print("x is greater than y") if x > y else print("y is greater than x")

# COMMAND ----------

# MAGIC %md
# MAGIC Python Loops
# MAGIC For Loop and While Loop

# COMMAND ----------

for i in range(1,21,2):
    print(i)

# COMMAND ----------

name = "Sivakrishna Reddy"
for s in name:
    print(s)

# COMMAND ----------

num = 555
for n in num:
    print(n)
#number is not collection or sequence so we can not iterate

# COMMAND ----------

v_fruits = ["apple","banana","cherry","grapes","orange"]

for fruit in v_fruits:
    if fruit == "cherry":
        continue
    print(fruit)

# COMMAND ----------

v_fruits = ["apple","banana","cherry","grapes","orange"]

for fruit in v_fruits:
    if fruit == "cherry":
        break
    print(fruit)

# COMMAND ----------

# continue will use if we want to skip specific item
# break will use if we want to stop loop when the condition match

# COMMAND ----------

for i in range(1,10):
    if i in [2,7,9]:
        continue
    print(i)

# COMMAND ----------

i = 0
while i <10:
    print(i)
    i += 2

# COMMAND ----------

i = 0
while i <10:
    print(i)
    i += 1
    
    if i ==5:
        break

# COMMAND ----------

i = 0
while i <10:
    
    if i ==5:
        continue
    print(i)
    i += 1

# COMMAND ----------

