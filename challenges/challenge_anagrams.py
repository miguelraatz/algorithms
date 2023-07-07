def merge_sort(list_string, start=0, end=None):
    if end is None:
        end = len(list_string)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(list_string, start, mid)
        merge_sort(list_string, mid, end)
        merge(list_string, start, mid, end)


def merge(list_string, start, mid, end):
    left = list_string[start:mid]
    right = list_string[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            list_string[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            list_string[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            list_string[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            list_string[general_index] = right[right_index]
            right_index = right_index + 1


def order(string):
    string_list = list(string)
    merge_sort(string_list)
    return "".join(string_list)


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return ("", "", False)

    first_string_order = order(first_string.lower())
    second_string_order = order(second_string.lower())

    string_is_anagram = first_string_order == second_string_order
    return (first_string_order, second_string_order, string_is_anagram)
