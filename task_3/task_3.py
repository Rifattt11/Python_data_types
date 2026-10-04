list1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
list2 = [{"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]

common = [d for d in list1 if d in list2]
only_in_1 = [d for d in list1 if d not in list2]
only_in_2 = [d for d in list2 if d not in list1]

print("В обоих:", common)
print("Только в list1:", only_in_1)
print("Только в list2:", only_in_2)