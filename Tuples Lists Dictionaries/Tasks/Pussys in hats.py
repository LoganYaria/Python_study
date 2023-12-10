cats = []
super_cats = []
circles = 1
for pussy in range(100):
    cats.append(1)
print(cats)

while circles != 100:
    for pussy in range(100):
        a = pussy+1
        b = circles + 1
        if a % b == 0:
            if cats[pussy] == 1:
                cats[pussy] = 0
            else:
                cats[pussy] = 1
    circles = circles+1

for indx in range(100):
    if cats[indx] == 1:
        super_cats.append(indx + 1)
print(super_cats)
