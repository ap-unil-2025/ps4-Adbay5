"""
Problem 2: Dictionary Operations and Nested Structures
Practice working with Python dictionaries - creating, accessing, modifying, and nesting them.
"""


def create_student_record(name, age, major, gpa):

    dict = {}
    dict["name"] = name
    dict["age"] = age
    dict["major"] = major
    dict["gpa"] = gpa
    return dict 

def get_value_safely(dictionary, key, default=None):
    return dictionary.get(key, default)
   


def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()   
    merged.update(dict2)    
    return merged



def count_word_frequency(text):

    import string
    frequency = {}

    text_cleaned = text.lower().replace(",", "").replace(".","").replace("'"," ")

    words = text.split()

    cleaned = []

    for i in words :
        if i not in string.punctuation :
            cleaned.append(i)
            for i in cleaned :
                frequency[i] = cleaned.count(i)



    return frequency


def invert_dictionary(dictionary):
    inverted = {}
    for key,value in dictionary.items() : 
        inverted[value]= key
    return inverted


def filter_dictionary(dictionary, keys_to_keep):
    new_dict = {}
    for key, value in dictionary.items() :
        if key in keys_to_keep:
            new_dict[key] = value
    return new_dict


def group_by_first_letter(words):
    dict= {}
    list = []
    for mot in words :
        first_letter = mot[0]
        if first_letter not in list :
            list.append(first_letter)
    for i in list :
        for mot in words :
            if mot[0]== i:
                dict.setdefault(i, []).append(mot)
    return dict


def calculate_grades_average(students):
    for i in students.keys():
        values = students[i]
        average = sum(values)/len(values)
        students[i]= round(average,2)
    return students


def nested_dict_access(data, keys):
    if not keys :
        return None
    
    d = data     
    for i in keys :
        if i in d : 
            d = d[i]
        else:
             return None    

    return d    


# Test cases
if __name__ == "__main__":
    print("Testing Dictionary Operations...")
    print("-" * 50)

    # Test create_student_record
    print("Test 1: create_student_record")
    result = create_student_record("Alice", 20, "CS", 3.8)
    print(f"Result: {result}")
    assert result == {'name': 'Alice', 'age': 20, 'major': 'CS', 'gpa': 3.8}
    print("✓ Passed\n")

    # Test get_value_safely
    print("Test 2: get_value_safely")
    d = {'a': 1, 'b': 2}
    assert get_value_safely(d, 'a') == 1
    assert get_value_safely(d, 'c', 'Not found') == 'Not found'
    print("✓ Passed\n")

    # Test merge_dictionaries
    print("Test 3: merge_dictionaries")
    result = merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    print(f"Result: {result}")
    assert result == {'a': 1, 'b': 3, 'c': 4}
    print("✓ Passed\n")

    # Test count_word_frequency
    print("Test 4: count_word_frequency")
    result = count_word_frequency("hello world hello")
    print(f"Result: {result}")
    assert result == {'hello': 2, 'world': 1}
    print("✓ Passed\n")

    # Test invert_dictionary
    print("Test 5: invert_dictionary")
    result = invert_dictionary({'a': 1, 'b': 2, 'c': 3})
    print(f"Result: {result}")
    assert result == {1: 'a', 2: 'b', 3: 'c'}
    print("✓ Passed\n")

    # Test filter_dictionary
    print("Test 6: filter_dictionary")
    result = filter_dictionary({'a': 1, 'b': 2, 'c': 3, 'd': 4}, ['a', 'c'])
    print(f"Result: {result}")
    assert result == {'a': 1, 'c': 3}
    print("✓ Passed\n")

    # Test group_by_first_letter
    print("Test 7: group_by_first_letter")
    result = group_by_first_letter(['apple', 'banana', 'apricot', 'blueberry'])
    print(f"Result: {result}")
    assert result == {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
    print("✓ Passed\n")

    # Test calculate_grades_average
    print("Test 8: calculate_grades_average")
    result = calculate_grades_average({
        'Alice': [90, 85, 88],
        'Bob': [75, 80, 78]
    })
    print(f"Result: {result}")
    assert result == {'Alice': 87.67, 'Bob': 77.67}
    print("✓ Passed\n")

    # Test nested_dict_access
    print("Test 9: nested_dict_access")
    data = {'a': {'b': {'c': 123}}}
    assert nested_dict_access(data, ['a', 'b', 'c']) == 123
    assert nested_dict_access(data, ['a', 'x']) is None
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Excellent work!")
