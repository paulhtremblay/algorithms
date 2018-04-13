def binary_search(the_list, target):
    if len(the_list) == 0:
        return False
    half_way = len(the_list)//2
    if the_list[half_way] == target:
        return True
    else:
        if target < the_list[half_way]:
            return binary_search(the_list[:half_way], target)
        else:
            return binary_search(the_list[half_way + 1:], target)

def find_rotation_point(the_list, start, end):
    half_way = (end - start) //2 + start
    first = the_list[half_way]
    second = the_list[half_way + 1]
    if second < first:
        return half_way
    elif the_list[end] < the_list[half_way]:
        return find_rotation_point(the_list, half_way, end)
    return find_rotation_point(the_list, start, half_way)



for l in [
        [3, 4, 5, 6, 7, 8, 9, 0, 2],
        [9, 10, 2, 3, 4, 5, 6],
        [1, 0]
        ]:
    rotation_point = find_rotation_point(l, 0, len(l) - 1)
    print("roatation point for l {0} is {1}".format(l, rotation_point))
    found = False
    found = item_in_list = binary_search(l[0:rotation_point], 2)
    if not found:
        found = item_in_list = binary_search(l[rotation_point:], 2)
    print("2 is in list is {0}".format(found))
