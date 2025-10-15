"""
Problem 4: Data Persistence with JSON
Learn to use Python modules (imports) and save data to files using JSON.
"""

import json
# Note: json is a built-in Python module for working with JSON data


def save_to_json(data, filename):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        return True  

    except (OSError, TypeError, ValueError) as e:
        return False  



def load_from_json(filename):

    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return data 

    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        return None 

   


def save_contacts_to_file(contacts, filename="contacts.json"):
    return save_to_json(contacts,filename )




def load_contacts_from_file(filename="contacts.json"):

    result = load_from_json(filename)
    if result == None :
        return []
    else : 
        return result

   

def append_contact_to_file(contact, filename="contacts.json"):
    data = load_contacts_from_file(filename)
    data.append(contact)
    try:
        save_contacts_to_file(data,filename)
        return True 
    except (OSError, TypeError, ValueError) as e:
        return False  


def backup_file(source_filename, backup_filename):
    backup_file = load_from_json(source_filename)
    return save_to_json(backup_file, backup_filename)

def get_file_stats(filename):
    import os
    dict_stat = {}
    data = load_from_json(filename)

    if data == None :
        return None
    else :
        dict_stat["exists"] = os.path.exists(filename)
        data_type = ("list" if isinstance(data, list) else "dict" if isinstance(data, dict) else "other")
        dict_stat["type"]= data_type
        dict_stat["count"]= len(data)
        dict_stat["size_bytes"]= os.path.getsize(filename)
        return dict_stat


def merge_json_files(file1, file2, output_file):
    if not file1 or not file2 : 
        return None
    file_1 = load_from_json(file1)
    file_2 = load_from_json(file2)
    if isinstance(file_1, list) and isinstance(file_2, list):
        list_co = file_1 + file_2
        save_to_json(list_co, output_file)
        return True

def search_json_file(filename, key, value):
    """
    Search a JSON file (containing a list of dicts) for items matching a key-value pair.

    Args:
        filename (str): JSON file to search
        key (str): Key to search for
        value: Value to match

    Returns:
        list: List of matching items

    Example:
        If file has [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
        search_json_file('data.json', 'name', 'Alice')
        returns [{'name': 'Alice', 'age': 25}]
    """

    data = load_from_json(filename)
    if data is None or not isinstance(data, list):
        return []
    results = [item for item in data if key in item and item[key] == value]
    return results


# Test cases
if __name__ == "__main__":
    print("Testing JSON File Operations...")
    print("-" * 50)

    # Test 1: save_to_json and load_from_json
    print("Test 1: save_to_json and load_from_json")
    test_data = {'name': 'Alice', 'age': 25, 'city': 'Paris'}
    save_to_json(test_data, 'test_data.json')
    loaded_data = load_from_json('test_data.json')
    print(f"Saved and loaded: {loaded_data}")
    assert loaded_data == test_data
    print("✓ Passed\n")

    # Test 2: save_contacts_to_file and load_contacts_from_file
    print("Test 2: save and load contacts")
    contacts = [
        {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'},
        {'name': 'Bob', 'phone': '555-0002', 'email': 'bob@email.com'}
    ]
    save_contacts_to_file(contacts, 'test_contacts.json')
    loaded_contacts = load_contacts_from_file('test_contacts.json')
    print(f"Loaded {len(loaded_contacts)} contacts")
    assert len(loaded_contacts) == 2
    assert loaded_contacts[0]['name'] == 'Alice'
    print("✓ Passed\n")

    # Test 3: append_contact_to_file
    print("Test 3: append_contact_to_file")
    new_contact = {'name': 'Charlie', 'phone': '555-0003', 'email': 'charlie@email.com'}
    append_contact_to_file(new_contact, 'test_contacts.json')
    contacts = load_contacts_from_file('test_contacts.json')
    print(f"After append: {len(contacts)} contacts")
    assert len(contacts) == 3
    print("✓ Passed\n")

    # Test 4: backup_file
    print("Test 4: backup_file")
    backup_file('test_contacts.json', 'test_contacts_backup.json')
    backup_data = load_from_json('test_contacts_backup.json')
    print(f"Backup created with {len(backup_data)} items")
    assert len(backup_data) == 3
    print("✓ Passed\n")

    # Test 5: get_file_stats
    print("Test 5: get_file_stats")
    stats = get_file_stats('test_contacts.json')
    print(f"File stats: {stats}")
    assert stats is not None
    assert stats['exists'] == True
    assert stats['type'] == 'list'
    assert stats['count'] == 3
    print("✓ Passed\n")

    # Test 6: merge_json_files
    print("Test 6: merge_json_files")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    save_to_json(list1, 'list1.json')
    save_to_json(list2, 'list2.json')
    merge_json_files('list1.json', 'list2.json', 'merged.json')
    merged = load_from_json('merged.json')
    print(f"Merged list: {merged}")
    assert merged == [1, 2, 3, 4, 5, 6]
    print("✓ Passed\n")

    # Test 7: search_json_file
    print("Test 7: search_json_file")
    results = search_json_file('test_contacts.json', 'name', 'Alice')
    print(f"Search results: {results}")
    assert len(results) == 1
    assert results[0]['name'] == 'Alice'
    print("✓ Passed\n")

    # Cleanup
    print("Cleaning up test files...")
    import os
    for file in ['test_data.json', 'test_contacts.json', 'test_contacts_backup.json',
                 'list1.json', 'list2.json', 'merged.json']:
        if os.path.exists(file):
            os.remove(file)
    print("✓ Cleaned up\n")

    print("=" * 50)
    print("All tests passed! You've mastered JSON file operations!")
