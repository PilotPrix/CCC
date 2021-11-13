x = input().split(" ")
start_date = int(x[0])
month_days = int(x[1])

days = 1
a = [0] * 35


for i in range(month_days):
    a[i + start_date - 1] = days
    days += 1

b = a[7:14]
c = a[14:21]
d = a[21:28]
e = a[28:month_days + start_date - 1]
a = a[0: 7]


print("Sun Mon Tue Wed Thr Fri Sat")

p = ""
for i in a:
    if i == 0:
        p += "   "
    elif i < 10:
        p += "  " + str(i)
    else:
        p += " " + str(i)

    p += " "
print(p[0:-1])
p = ""
for i in b:
    if i == 0:
        p += "   "
    elif i < 10:
        p += "  " + str(i)
    else:
        p += " " + str(i)

    p += " "
print(p[0:-1])
p = ""
for i in c:
    if i == 0:
        p += "   "
    elif i < 10:
        p += "  " + str(i)
    else:
        p += " " + str(i)

    p += " "
print(p[0:-1])
p = ""
for i in d:
    if i == 0:
        p += "   "
    elif i < 10:
        p += "  " + str(i)
    else:
        p += " " + str(i)

    p += " "
print(p[0:-1])
p = ""
for i in e:
    if i == 0:
        pass
    elif i < 10:
        p += "  " + str(i)
    else:
        p += " " + str(i)

    p += " "
if e:
    print(p[0:-1])
