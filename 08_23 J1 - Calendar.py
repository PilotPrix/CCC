x = input().split(" ")
start_date = int(x[0])
month_days = int(x[1])

# list index of the last item of list
daysIndex = month_days + start_date - 1

days = 1
a = [0] * daysIndex


# assign list a with all the dates
for i in range(month_days):
  a[i + start_date - 1] = days
  days += 1

# convert a into many lists representing rows of the month
b = a[7:14]
c = a[14:21]
d = a[21:28]
e = []
f = []
if daysIndex < 35:
    e = a[28:daysIndex]
else:
    e = a[28:35]
    f = a[35:daysIndex]
a = a[0:7]


dates = [a, b, c, d, e, f]

print("Sun Mon Tue Wed Thr Fri Sat")

# For each calendar row
for date in dates:
  p = ""

  # if the current row exists
  if date:
    # for each day of the month
    for i in date:
      if i == 0:
        p += "   "
      elif i < 10:
        p += "  " + str(i)
      else:
        p += " " + str(i)
    
      p += " "
    print(p[0:-1])