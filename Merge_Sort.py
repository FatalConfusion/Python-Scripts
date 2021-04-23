def merge_helper(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    
    sorted_list = list()
    left_index = right_index = 0

    left_length = len(left)
    right_length = len(right)

    while len(sorted_list) < left_length + right_length:
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    
        if right_index == right_length:
            sorted_list += left[left_index:]
            break

        if left_index == left_length:
            sorted_list += right[right_index:]
            break

    return sorted_list


def Merge_Sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr)//2
    left_list = Merge_Sort(arr[:middle])
    right_list = Merge_Sort(arr[middle:])
    return merge_helper(left_list, right_list)

random_list = [45, 90, 23, 178, 201, 98, 34, 12, 67]
print(Merge_Sort(random_list))