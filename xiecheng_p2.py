import sys
for line in sys.stdin:
    a = line.split()
    s = a[0].split(".")
    if len(s)!=4:
        print("false")
    else:
        flag = True
        for i in s:
            if not(int(i)>=0 and int(i)<=255):
                flag=False
        if flag:
            print("true")
        else:
            print("false")
