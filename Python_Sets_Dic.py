# Databricks notebook source
v_set = {1,5,5,2,3,5,10,2,1,8}
print(v_set)

# COMMAND ----------

v_set.add(11)
print(v_set)

# COMMAND ----------

#to add multiple items
v_set.update([15,20,18,19])
print(v_set)

# COMMAND ----------

len(v_set)

# COMMAND ----------

v_set_rem = {"Apple","Banana","Grapes","Orange"}

# COMMAND ----------

v_set_rem.remove("Bananaaaa")

# COMMAND ----------

_set_rem.remove("Banana")

# COMMAND ----------

v_set_rem.discard("Bananaaaa")
#If you use remove and that item not present it will throgh an exception. If you do not want throght an exption then use discard

# COMMAND ----------

v_set_rem

# COMMAND ----------

pop_item = v_set_rem.pop()
print(pop_item)
#pop will not remove last element but will remove randomly from the set

# COMMAND ----------

set1 = {1,2,3,5,6,7}
set2 = {7,2,3,15}
print(set1.intersection(set2))
print(set1)
print(set2)

# COMMAND ----------

print(set1.union(set2))

# COMMAND ----------

print(set1.difference(set2))

# COMMAND ----------

dict = {"key1":"Value1","key2":"Value2"}
print (dict)

# COMMAND ----------

for k,v in dict.items():
    print(k)
    print(v)

# COMMAND ----------

dict.items()

# COMMAND ----------

