def isInsidePolygon(pt, poly):
    c = False
    i = -1
    l = len(poly)
    j = l - 1
    while i < l - 1:
        i += 1
        if ((poly[i]["x"] <= pt["x"] and pt["x"] < poly[j]["x"]) or (
                poly[j]["x"] <= pt["x"] and pt["x"] < poly[i]["x"])):
            if (pt["y"] < (poly[j]["y"] - poly[i]["y"]) * (pt["x"] - poly[i]["x"]) / (
                    poly[j]["x"] - poly[i]["x"]) + poly[i]["y"]):
                c = not c
        j = i
    return c
import sys
if __name__ == "__main__":
    n1 = [int(x) for x in sys.stdin.readline().strip().split(" ")[1:]]
    n2 = [int(x) for x in sys.stdin.readline().strip().split(" ")[1:]]
    pt = [{'x':n2[i],'y':n2[i+1]} for i in range(0,len(n2),2)]
    poly = [{'x':n1[i],'y':n1[i+1]} for i in range(0,len(n1),2)]
    num = 0
    for i in pt:
        if(isInsidePolygon(i,poly)):
            num+=1
    print(num)
# 射线法，通过率50%