min_quantity_click = 0

for _ in range(int(input())):
    quantity_space = int(input())
    if (quantity_space + 1) % 4 == 0:
        min_quantity_click += (quantity_space // 4) + 2
    else:
        min_quantity_click += (quantity_space // 4) + (quantity_space % 4)
        
print(min_quantity_click)