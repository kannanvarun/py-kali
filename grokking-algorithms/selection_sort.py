# Selection sort:

# Simple but inefficient sorting algorithm which works by repeatedly finding the smallest/largest element
# in a list and swapping it with the first element, until the list is fully sorted.

# It has a time complexity of O(n^2), which means its performance significantly worsens
# as the number of elements (n) increases.

def selection_sort(input_array: []):
    for i in range(len(input_array)):
        min_index = i

        for j in range(i+1, len(input_array)):
            if input_array[j] < input_array[min_index]:
                min_index = j

        # swap elements in array
        if i != min_index:
            input_array[min_index], input_array[i] = input_array[i], input_array[min_index]


input = [64, 251, 120, 22, 11, 25]
print("Input array:", input)
selection_sort(input)
print("Sorted array:", input)
