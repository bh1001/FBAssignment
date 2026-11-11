#Python Program to Merge Two Lists and Sort it
def merge_list(list_1, list_2):
   merged_list = list_1 + list_2
   merged_list.sort()
   return(merged_list)

list_1 = [20, 18, 9, 51, 48, 31]
list_2 = [28, 33, 3, 22, 15, 20]
print("The first list is :")
print(list_1)
print("The second list is :")
print(list_2)
print(merge_list(list_1, list_2))