# courtesy from PK # Focus on do one thing and naming
def readAloud(lst):
    new_list = []
    #counter1 reads through the item in the list
    counter1 = 0
    while counter1 < len(lst):
        frequency = 0
        #counter2 reads through the items following counter1 to see how many repeats it has before the item changes
        counter2 = counter1
        while counter2 < len(lst) and lst[counter2] == lst[counter1]:
            frequency += 1
            counter2 += 1
        new_list.extend([frequency, lst[counter1]])
        #counter1 jumps to counter2 so they don't recount the items already counted
        counter1 = counter2
    return new_list
