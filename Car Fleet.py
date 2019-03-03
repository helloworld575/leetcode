# def carFleet(target, position, speed) -> int:
#     def takePosition(elem):
#         return elem[0]
#     ans = len(position)
#     cars = []
#     for i in range(len(position)):
#         cars.append([position[i],speed[i]])
#     cars.sort(key=takePosition)
#     print(cars)
#     i = 1
#     pre = 0
#     while i< len(position):
#         if pre<0:
#             i+=1
#             pre = i-1
#             continue
#         if cars[pre][0]==cars[i][0]:
#             cars[pre][1] = cars[i][1] = min(cars[pre][1],cars[i][1])
#             ans-=1
#             pre-=1
#             continue
#         if cars[pre][1]>cars[i][1]:
#             time = (target-cars[pre][0])/cars[pre][1]
#             if cars[i][1]*time<=(target-cars[i][0]):
#                 cars[pre][1] = cars[i][1]
#                 ans-=1
#                 pre-=1
#                 continue
#         i+=1
#         pre = i-1
#     return ans

def carFleet(target, position, speed):
    cars = sorted(zip(position, speed))
    times = [float(target - p) / s for p, s in cars]
    ans = 0
    while len(times) > 1:
        lead = times.pop()
        if lead < times[-1]:
            ans += 1  # if lead arrives sooner, it can't be caught
        else:
            times[-1] = lead  # else, fleet arrives at later time 'lead'

    return ans + bool(times)  # remaining car is fleet (if it exists)
print(carFleet(12, [4,0,5,3,1,2], [6,10,9,6,7,2]))
