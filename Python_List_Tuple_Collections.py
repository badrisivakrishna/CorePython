# Databricks notebook source
v_list = [10,15,20,18,2,4,1,7]
type(v_list)

# COMMAND ----------

v_list_e = [10,15,20,18,2,4,1,7]
print(v_list_e[-5:-1])
print(v_list_e[-5:])

# COMMAND ----------

v_list_m = ["Jan","Feb","Mar","Apr"]

# COMMAND ----------

v_list_m[4] = "May"

# COMMAND ----------

v_list_m.append("May")
print(v_list_m[4])
v_list_m[4] = "Nothing"
print(v_list_m[4])

# COMMAND ----------

help(v_list_m)

# COMMAND ----------

dir(v_list_m)

# COMMAND ----------

help(list)

# COMMAND ----------

v_list_f = ["Apple","Banana","Grapes"]
v_list_f.append(["Orange","Lemon","Pineapple"])

# COMMAND ----------

v_list_f
#If we pass multiple items for append it will treat as list

# COMMAND ----------

v_list_f[3][0]

# COMMAND ----------

v_list_i = ["Jan","Mar","Apr"]
v_list_i.insert(1,"Feb")
print(v_list_i)

# COMMAND ----------

v_list_extend = ["Apple","Banana","Grapes"]
v_list_extend.extend(["Orange","Lemon","Pineapple"])
v_list_extend

# COMMAND ----------

v_list_len = ["Apple","Banana","Grapes"]
len(v_list_len)

# COMMAND ----------

v_list_a = [10,4,5,1,2,8,7,3,6,9]
v_list_a.sort()
print(v_list_a)
v_list_a.sort(reverse=True)
print(v_list_a)

# COMMAND ----------

v_list_abc = ['d','b','e','a','c']
v_list_abc.sort()
print(v_list_abc)
v_list_abc.sort(reverse=True)
print(v_list_abc)

# COMMAND ----------

v_list_rev = [10,7,8,5,2,12,3]
v_list_rev.reverse()
print(v_list_rev)

# COMMAND ----------

v_list_rem = ["Jan","Feb","Mar","Apr"]
v_list_rem.remove("Mar")
print(v_list_rem)

# COMMAND ----------

v_list_pop = ["Jan","Feb","Mar","Apr"]
removed_item = v_list_pop.pop()
print(v_list_pop)
print(removed_item)

# COMMAND ----------

v_list_pop_ind = ["Jan","Feb","Mar","Apr"]
removed_item_ind = v_list_pop_ind.pop(1)
print(v_list_pop_ind)
print(removed_item_ind)

# COMMAND ----------

var = 55
print(var)
del var
print(var)

# COMMAND ----------

v_list_pop_del = ["Jan","Feb","Mar","Apr"]
del v_list_pop_del[1]
print(v_list_pop_del)

# COMMAND ----------

v_list_pop_clr = ["Jan","Feb","Mar","Apr"]
v_list_pop_clr.clear()
print(v_list_pop_clr)

# COMMAND ----------

v_list_hard_copy = ["Jan","Feb","Mar","Apr"]
copy_hard_list = v_list_hard_copy
copy_hard_list.append("May")
print(v_list_hard_copy)
print(copy_hard_list)
v_list_hard_copy.append("Jun")
print(v_list_hard_copy)
print(copy_hard_list)

# COMMAND ----------

v_list_index = ["Jan","Feb","Mar","Apr"]
v_ind = v_list_index.index("Mar")
print(v_ind)

# COMMAND ----------

v_list_ind_pos = ["Siva","Joshika","Sowji","Siva","Deepak","Prakash","Varada","Siva"]
print(v_list_ind_pos.index("Siva",0,len(v_list_ind_pos)))
print(v_list_ind_pos.index("Siva",1,len(v_list_ind_pos)))
print(v_list_ind_pos.index("Siva",4,len(v_list_ind_pos)))

# COMMAND ----------

v_tuple = (1,2,5,5,6,8,1)
print(type(v_tuple))
print(v_tuple)

# COMMAND ----------

v_tuple[:3]

# COMMAND ----------

v_tuple[3] = 5

# COMMAND ----------

v_tuple_two = (2,8,7,3)
add_tuple = v_tuple + v_tuple_two
print(add_tuple)

# COMMAND ----------

v_t = (5,)
print(v_tuple+ v_t)

# COMMAND ----------

i_n = 5
print(v_tuple+ i_n)

# COMMAND ----------

print(v_tuple+ v_t)

# COMMAND ----------

