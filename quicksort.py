def quickSort(list,low,high):
    tmpl = low
    tmph = high
    if tmpl>=tmph:
        return list
    key = list[tmpl]
    while tmpl<tmph:
        while tmpl<tmph and list[tmph]>=key:
            tmph = tmph-1
        list[tmpl] = list[tmph]
        while tmpl<tmph and list[tmpl]<=key:
            tmpl = tmpl+1
        list[tmph] = list[tmpl]
    list[tmpl] = key
    quickSort(list,low,tmpl-1)
    quickSort(list,tmph+1,high)
    return list
print(quickSort([4,3,2,1],0,3))