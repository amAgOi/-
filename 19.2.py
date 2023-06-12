def f(x, y, k):
    if k == 4 and x + y >= 77:
        return 1
    elif k == 4 and x + y < 77:
        return 0
    elif x + y >= 77 and k < 4:
        return 0
    else:
        if k % 2 != 0:
            return f(x + 1, y, k + 1) or f(x, y + 1, k + 1) or f(x * 2, y, k + 1) or f(x, y * 2, k + 1)   
        else:
            return f(x + 1, y, k + 1) and f(x, y + 1, k + 1) and f(x * 2, y, k + 1) and f(x, y * 2, k + 1) 
 
for x in range(1, 70):
    if f(x, 7, 1) == 1:
        print(x)
