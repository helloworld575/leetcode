import sys
for line in sys.stdin:
    a = line.split()
    num = int(a[0])
    perMon = float(a[1])
    sumMon = num*perMon
    print(sumMon)
    Sum1 = sumMon*0.7 if num>=3 else sumMon
    if Sum1<40:
        Sum1+=10

    Sum2 = sumMon
    if Sum2>=10:
        Sum2-=2
    if Sum2 < 93:
        Sum2 +=6
    if Sum1-Sum2>0.01 and Sum1-Sum2<=-0.01:
        print(0)
    elif Sum1>Sum2:
        print(2)
    else:
        print(1)
