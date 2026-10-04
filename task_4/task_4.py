items = [
    ("apple", "fruit"),
    ("banana", "fruit"),
    ("carrot", "vegetable"),
    ("tomato", "vegetable"),
    ("milk", "dairy")
]

groups = {}

for name, category in items:
    if category not in groups:
        groups[category] = []
    groups[category].append(name)

print(groups)