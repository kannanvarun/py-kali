# The binary_search function takes a sorted array and an item.
# If the item is in the array, the function returns its position.

def binary_search(input_array: [],
                  item: int) -> {}:

    input_array = sorted(input_array)
    # print(input_array)
    low = 0
    high = len(input_array) - 1
    steps = 0

    while low <= high:
        mid = int((low + high)/2)
        guess = input_array[mid]

        if guess == item:
            return {"pos": mid, "steps": steps}

        steps += 1

        if guess < item:
            print(f"low={low}")
            low = mid + 1

        elif guess > item:
            high = mid - 1
            print(f"high={high}")

    return {"pos": None, "steps": steps}


search_item = 99
search_out = binary_search([i for i in range(1, 128)], search_item)
print(f"Index of {search_item} is {search_out.get('pos', None)} found in {search_out.get('steps', None)} steps.")
