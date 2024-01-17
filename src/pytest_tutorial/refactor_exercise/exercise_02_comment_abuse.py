def filter_them_with_comment(the_list: List[List[int]]) -> List[List[int]]:
    list1 = list() # construct return list
    for x in the_list:
        if x[0] == 4: # get the status code and check if it is invalid
            list1.append(x) # if invalid append to return value
    return list1 # return list of invalid items
