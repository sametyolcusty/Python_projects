def flatten_list(input_list):
    # We will use a recursive function to flatten nested lists
    def flatten_recursive(lst):
        flattened = []
        for item in lst:
            if isinstance(item, list):
                flattened.extend(flatten_recursive(item))  # Flatten recursively nested lists
            else:
                flattened.append(item)  # Add single elements to list
        return flattened
    
    # Main function takes input_list and flattens nested lists
    return flatten_recursive(input_list)

# Example usage
input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_list = flatten_list(input_list)
print("Input:", input_list)
print("Output:", output_list)
