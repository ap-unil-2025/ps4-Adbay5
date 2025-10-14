"""
Problem 3: Mini Contact Manager
Build a simple contact manager using lists and dictionaries.
Practice combining data structures and writing functions.
"""


def create_contact(name, phone, email=""):
    dict_1 = {}
    dict_1["name"]= name 
    dict_1["phone"] = phone
    if not email : 
        return dict_1
    else :
        dict_1["email"] = email   
        return dict_1
    

def add_contact(contacts, name, phone, email=""):
    dict_1 = {}
    dict_1["name"]= name 
    dict_1["phone"] = phone
    dict_1["email"] = email   
    
    contacts.append(dict_1)
    return dict_1


def find_contact_by_name(contacts, name):
    for i in contacts :
        if i["name"].lower()== name.lower():
            return i 
        else : return None


def search_contacts(contacts, search_term):
    for i in contacts :
        if search_term.lower() == i["phone"] or  i["name"].lower():
            return i 
        else :
            return None




def delete_contact(contacts, name):
    for index, contact in enumerate(contacts):
        if contact["name"] == name:
            contacts.pop(index)
            return True
    return False 


def count_contacts_with_email(contacts):
    contact_with_mail = []
    for i in contacts:
        if i["email"] != "":
            contact_with_mail.append(i)
    return len(contact_with_mail)


def get_all_phone_numbers(contacts):
    list_phone =[]
    for i in contacts :
        phone = i["phone"]
        list_phone.append(phone)
        
    return list_phone 
    


def sort_contacts_by_name(contacts):
    return sorted(contacts, key=lambda c: c["name"])
   

def contact_exists(contacts, name):
    if find_contact_by_name(contacts, name) == None :
        return False
    else : 
        return True


# Test cases
if __name__ == "__main__":
    print("Testing Mini Contact Manager...")
    print("-" * 50)

    # Create test contacts list
    contacts = []

    # Test 1: create_contact
    print("Test 1: create_contact")
    contact = create_contact("Alice", "555-0001", "alice@email.com")
    print(f"Created: {contact}")
    assert contact == {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'}
    print("✓ Passed\n")

    # Test 2: add_contact
    print("Test 2: add_contact")
    add_contact(contacts, "Alice", "555-0001", "alice@email.com")
    add_contact(contacts, "Bob", "555-0002")
    add_contact(contacts, "Charlie", "555-0003", "charlie@email.com")
    print(f"Added 3 contacts. Total: {len(contacts)}")
    assert len(contacts) == 3
    print("✓ Passed\n")

    # Test 3: find_contact_by_name
    print("Test 3: find_contact_by_name")
    found = find_contact_by_name(contacts, "alice")  # Case-insensitive
    print(f"Found: {found}")
    assert found is not None and found['name'] == 'Alice'
    print("✓ Passed\n")

    # Test 4: search_contacts
    print("Test 4: search_contacts")
    results = search_contacts(contacts, "555-000")
    print(f"Search '555-000' found {len(results)} contacts")
    assert len(results) == 3  # All have 555-000 in phone
    print("✓ Passed\n")

    # Test 5: count_contacts_with_email
    print("Test 5: count_contacts_with_email")
    count = count_contacts_with_email(contacts)
    print(f"Contacts with email: {count}")
    assert count == 2  # Alice and Charlie have emails
    print("✓ Passed\n")

    # Test 6: get_all_phone_numbers
    print("Test 6: get_all_phone_numbers")
    phones = get_all_phone_numbers(contacts)
    print(f"Phone numbers: {phones}")
    assert phones == ['555-0001', '555-0002', '555-0003']
    print("✓ Passed\n")

    # Test 7: sort_contacts_by_name
    print("Test 7: sort_contacts_by_name")
    sorted_contacts = sort_contacts_by_name(contacts)
    names = [c['name'] for c in sorted_contacts]
    print(f"Sorted names: {names}")
    assert names == ['Alice', 'Bob', 'Charlie']
    print("✓ Passed\n")

    # Test 8: contact_exists
    print("Test 8: contact_exists")
    assert contact_exists(contacts, "Alice") == True
    assert contact_exists(contacts, "David") == False
    print("✓ Passed\n")

    # Test 9: delete_contact
    print("Test 9: delete_contact")
    deleted = delete_contact(contacts, "Bob")
    print(f"Deleted Bob: {deleted}, Remaining: {len(contacts)}")
    assert deleted == True and len(contacts) == 2
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Great work on the contact manager!")
