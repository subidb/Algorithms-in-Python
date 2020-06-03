class Activity:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return "{} - {}".format(self.start, self.end)


def bubblesort(actlist):
    for i in range(len(actlist)):
        for j in range(len(actlist)-i-1):
            if actlist[j].end > actlist[j+1].end:
                actlist[j], actlist[j+1] = actlist[j+1], actlist[j]
    return actlist


def activity_selector(activity_list):
    final_list = [activity_list[0]]
    i = 0
    j = 1
    count = 1
    for x in range(len(activity_list)-1):
        if activity_list[j].start > activity_list[i].end:
            final_list.append(activity_list[j])
            count += 1
            i = j
        j += 1
    return [final_list, count]


a1 = Activity(1, 4)
a2 = Activity(2, 5)
a3 = Activity(6, 8)
a4 = Activity(5, 10)
a5 = Activity(11, 12)

a_list = [a1, a2, a3, a4, a5]

result = activity_selector(a_list)
print(result)


a_list.append(Activity(5, 6)) 
bubblesort(a_list)

print(a_list)
result2 = activity_selector(a_list)
print(result2)
