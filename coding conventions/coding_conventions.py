import json
import os

def add_student_record(student_id, name, age, grade):
    """Add a new student record to the records JSON file.

    Args:
        student_id (str): Student ID.
        name (str): Student name
        age (int): Student age.
        grade (float): Student grade.
    
    Returns:
        None
    """
    record ={
        "student_id":student_id,
        "name":name,
        "age":age,
        "grade":grade 
    }
    
    if not os.path.exists("records.json"):
        with open("records.json","w") as file:
            json.dump([],file)
    
    with open("records.json","r") as file:
        records = json.load(file)
        
    records.append(record)
    
    with open("records.json","w") as file:
        json.dump(records,file)
        
def search_student_record(identifier):
    """Search for a student record by student_id or name.

    Args:
        identifier (str): Student ID or name to search
    
    Reutrns:
        dict: Student record (age and grade) if found, None
    """
    with open("records.json","r") as file:
        records = json.load(file)
        
    for record in records:
        if record["student_id"] == identifier or record["name"] == identifier:
            return {"name":record["name"],"age":record["age"],"grade":record["grade"]}
        
    return None

def update_student_record(identifier, field, value):
    """
    Update a student's information (age or group) by using student_id or name.

    Args:
        identifier (str): Student ID or name.
        filed (str): Field to update ('age' or 'grade').
        value: New value for the field
        
    Returns:
        bool: True if the record is update, False if the record is not found 
    
    """
    with open("records.json","r") as file:
        records = json.load(file)
        
    found = False
    for record in records:
        if record["student_id"] == identifier or record["name"] == identifier:
            record[field] =value 
            found = True
            break
    
    if found:
        with open("records.json","w") as file:
            json.dump(records,file)
            
    return found

if __name__ == "__main__":
    add_student_record("1001","Rabin Ghimire",20,85.5)
    add_student_record("1002","Shyam Shrestha", 19, 90.0)
    
    result = search_student_record("1001")
    if result:
        print("Student Found:")
        print("Name:",result["name"])
        print("Age:",result["age"])
        print("Grade:",result["grade"])
    else:
        print("Student not found.")
        
    update_student_record("1002","grade",95.5)
    
    result = search_student_record("Shyam Shrestha")
    if result:
        print("\nUpdated Student Found:")
        print("Name:", "Shyam Shrestha")
        print("Age:", result["age"])
        print("Grade:", result["grade"])
    else:
        print("Student not found.")
    
    """Output:
    Student Found:
    Name: Rabin Ghimire
    Age: 20
    Grade: 85.5

    Updated Student Found:
    Name: Shyam Shrestha
    Age: 19
    Grade: 95.5
    
    """
            