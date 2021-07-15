px = -50
x = -49
p = 0

def incfind():
    y1 = px ** 2 + 2 * px + 3
    y2 = x ** 2 + 2 * x + 3

    inc = (y2 - y1) / (x - px)
    print("기울기 : ",inc)
    print("x : ",x, "\n")
        
    if inc == 0:
        return True
    else:
        return False

for i in range(100):
    if incfind():
        print(px, x)
        break
    px += 1
    x += 1
