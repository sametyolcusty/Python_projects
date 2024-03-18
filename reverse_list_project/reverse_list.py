def reverse_list(lst):
    return [reverse_list(sublst) if isinstance(sublst, list) else sublst for sublst in reversed(lst)]

# Example used
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_list(input_list)
print(output_list)
