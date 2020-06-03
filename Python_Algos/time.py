time1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
block1 = ['9:00', '20:00']
time2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
block2 = ['10:00', '18:30']



def convert_to_int(listx):
    listy = []
    for list1 in listx:
        list1 = ([int(x[:-3]) for x in list1])
        listy.append(list1)
    return listy


def convert_blocktoint(listx):
    return [int(x[:-3]) for x in listx]


def create_finalblock(list1, list2):
    return [max(list1[0], list2[0]), min(list1[1], list2[1])]


block1 = convert_blocktoint(block1)
block2 = convert_blocktoint(block2)

final_block = create_finalblock(block1, block2)
print(final_block)


print()
time1 = convert_to_int(time1)
time2 = convert_to_int(time2)

print(time1, "    ",  time2)

time1free = []


# for i, time in enumerate(time1):
#     freespace = time1[i][0]-time1[i-1][1]
#     time1free.append(freespace)
#     print(i)

for i, time in enumerate(time1):
    freespace = [time1[i-1][1], time1[i][0]]
    time1free.append(freespace)

del(time1free[0])

print("XX\n")

time2free = []
for i, time in enumerate(time2):
    freespace = [time2[i-1][1], time2[i][0]]
    time2free.append(freespace)


time2free = [x for x in time2free if x[0]!=x[1]]

del(time2free[0])
print(time1free, "\n", time2free)


print()
finalfreetime = []
for free1, free2 in zip(time1free, time2free):
    if free1[0] >= free2[0] and free1[1] <= free2[1]:
        finalfreetime.append(free1)
    if free2[0] >= free1[0] and free2[1] <= free1[1]:
        finalfreetime.append(free2)

print(finalfreetime)

time1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
block1 = ['9:00', '20:00']
time2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
block2 = ['10:00', '18:30']

x, y = time1[1][1].split(":")
print(x, y)

