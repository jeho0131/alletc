start = 0
end = 5
div = 10000

def areaFind(a, b, h):
    area = ((a + b) * h) / 2
    return area

add = 0
for i in range(start * div, end * div):
    add += areaFind((i / div) ** 2, ((i+1) / div) ** 2, 1 / div)

print(add)
