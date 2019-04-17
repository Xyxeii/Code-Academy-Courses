#Write your function here
def same_values(lst1, lst2):
  newList = [i for i in range(min(len(lst1), len(lst2))) if lst1[i] == lst2[i]]
  return newList

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10]))