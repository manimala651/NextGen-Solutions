print("---TASK 1---")
'create a set'

set={3,5,6,7,8}
print(set)

set.add(9)
print("add the element to the set:",set)


'update the set with new numbers'

set1={13,12,15,7,8}
set.update(set1)

print("updated set:",set)


number=int(input("Enter the number:"))

if number in set:
    print("this number exist in this set")
else:
    print("this number is not present in this set")



'lenght of the set'

print("The length of the set is :",len(set))

print("---TASK 2---")


'''A website records the user IDs of visitors each day. You
need to find out:
Create a two set and print it.
 Unique visitors today.
 Users who visited on both days.
 Users who visited only today (not yesterday).
 Users who visited only yesterday (not today).'''

yesterday_visitor={"ram","harini","ravi","leka","bindhu","murugan","anu"}
today_visitor={"bindhu","anu","hema","kumar","harry","dinesh","santhosh","mohana"}

print("visiter list on yesterday:",yesterday_visitor)
print("vistier list on today:",today_visitor)

print("unique visitor today:",yesterday_visitor|today_visitor)
print("who visited on both days:",yesterday_visitor&today_visitor)
print("who visited only yesterday:",yesterday_visitor-today_visitor)
print("who visited on today:",today_visitor-yesterday_visitor)
print(yesterday_visitor^today_visitor)
