"""
Problem 1: List Operations and Comprehensions
Practice working with Python lists - creating, modifying, filtering, and transforming them.
"""


def create_number_list(start, end):
    list = []
    for i in range (start, end+1):
        list.append(i)
    return list
    pass


def filter_even_numbers(numbers):
    list = []
    for i in numbers :
        if i %2 == 0:
            list.append(i)

    return list


def square_numbers(numbers):
    list = [i**2 for i in numbers]
    return list


def find_max_min(numbers):
    if not numbers :
        return None
    min_value = min(numbers)
    max_value = max(numbers)
    return (max_value, min_value)


def remove_duplicates(items):
    list = []
    for i in items :
     
        if i not in list :
            list.append(i)
    return list


def merge_lists(list1, list2):
    result = []
    max_len = max(len(list1), len(list2))

    for i in range(max_len):
        if i < len(list1):
            result.append(list1[i])
        if i < len(list2):
            result.append(list2[i])

    return result


def list_statistics(numbers):
 
    if not numbers:
        return None
    dict = {}   
    count = len(numbers)
    sum_nb = sum(numbers)
    dict["sum"]= sum_nb
    dict["average"]= sum_nb/count
    dict ["count"]= count
    dict["max"]= max(numbers)
    dict["min"]= min(numbers)
    return dict 
   


def chunk_list(items, chunk_size):
    chunks = []
    for i in range(0, len(items), chunk_size):
        chunk = items[i:i + chunk_size]
        chunks.append(chunk) 
    return chunks





# Test cases
if __name__ == "__main__":
    print("Testing List Operations...")
    print("-" * 50)

    # Test create_number_list
    print("Test 1: create_number_list(1, 5)")
    result = create_number_list(1, 5)
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5], "Failed!"
    print("✓ Passed\n")

    # Test filter_even_numbers
    print("Test 2: filter_even_numbers([1, 2, 3, 4, 5, 6])")
    result = filter_even_numbers([1, 2, 3, 4, 5, 6])
    print(f"Result: {result}")
    assert result == [2, 4, 6], "Failed!"
    print("✓ Passed\n")

    # Test square_numbers
    print("Test 3: square_numbers([1, 2, 3, 4])")
    result = square_numbers([1, 2, 3, 4])
    print(f"Result: {result}")
    assert result == [1, 4, 9, 16], "Failed!"
    print("✓ Passed\n")

    # Test find_max_min
    print("Test 4: find_max_min([3, 1, 4, 1, 5, 9, 2, 6])")
    result = find_max_min([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"Result: {result}")
    assert result == (9, 1), "Failed!"
    print("✓ Passed\n")

    # Test remove_duplicates
    print("Test 5: remove_duplicates([1, 2, 2, 3, 4, 3, 5])")
    result = remove_duplicates([1, 2, 2, 3, 4, 3, 5])
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5], "Failed!"
    print("✓ Passed\n")

    # Test merge_lists
    print("Test 6: merge_lists([1, 3, 5], [2, 4, 6])")
    result = merge_lists([1, 3, 5], [2, 4, 6])
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5, 6], "Failed!"
    print("✓ Passed\n")

    # Test list_statistics
    print("Test 7: list_statistics([1, 2, 3, 4, 5])")
    result = list_statistics([1, 2, 3, 4, 5])
    print(f"Result: {result}")
    expected = {'sum': 15, 'average': 3.0, 'count': 5, 'max': 5, 'min': 1}
    assert result == expected, "Failed!"
    print("✓ Passed\n")

    # Test chunk_list
    print("Test 8: chunk_list([1, 2, 3, 4, 5, 6, 7], 3)")
    result = chunk_list([1, 2, 3, 4, 5, 6, 7], 3)
    print(f"Result: {result}")
    assert result == [[1, 2, 3], [4, 5, 6], [7]], "Failed!"
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Great work!")
