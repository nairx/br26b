
# from collections import Counter
# wickets = ["John","Amy","Cathy","John","John","Amy"]
# c = Counter(wickets)
# # print(c)
# # print(c.most_common(1))
# print(c.most_common(2))

# from collections import namedtuple
# Price = namedtuple("Price",["Phone","Laptop","Keyboard"])
# items = Price(45,67,87)
# print(items.Phone)

# from collections import defaultdict
# students = defaultdict(int)
# students["John"] = 23
# students["Mike"] = 20
# students["Cathy"] = students["Cathy"] + 4
# print(students)

# from collections import deque
# names = deque(["John","Cathy","Mike","Chastity"])
# # names.append("Joe")
# # names.appendleft("Lisa")
# # print(names)
# # names.extendleft(["Rafeal","Ash"])
# # print(names)
# # names.popleft()
# # print(names)
# names.rotate(2)
# print(names)

from collections import ChainMap
teamA = {"John":2,"Cathy":5}
teamB = {"Mike":1,"Brian":6}
combined = ChainMap(teamA,teamB)
print(combined)
print(combined["John"])
print(combined["Mike"])
for k,v in combined.items():
    print(k,v)
