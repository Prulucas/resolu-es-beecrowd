linha1 = input().split(" ")
linha2 = input().split(" ")

x1, y1 = linha1
x2, y2 = linha2
dis = (((float(x2) - float(x1)) * (float(x2) - float(x1))) + ((float(y2)-float(y1)) * (float(y2)-float(y1)))) ** (1/2)
print('{:.4f}' .format(dis))