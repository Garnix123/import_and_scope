'''
Import statements: 
    1. Import the built-in json python package
    2. From employee.py, import the details function and the employee_name, age, title variables
'''
import json
from employee import details, employee_name, age, title


def create_dict(name, age, title):
    """ Creates a dictionary that stores an employee's information """
    return {
        "first_name": str(name),
        "age": int(age),
        "title": str(title)
    }


def write_json_to_file(json_obj, output_file):
    """ Write json string to file """
    newfile = open(output_file, "w")
    newfile.write(json_obj)
    newfile.close()


def main():
    # Print the contents of details() -- This should print the details of an employee
    details()

    # Create employee dictionary
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))

    # Convert dictionary to JSON string
    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))

    # Write out the json object to file
    write_json_to_file(json_object, "employee.json")


if __name__ == "__main__":
    main()

#OUTPUT: Employee name is:  Mario
#        Employee age is:  55
#        Employee title is:  owner
#        employee_dict: {'first_name': 'Mario', 'age': 55, 'title': 'owner'}
#        json_object: {"first_name": "Mario", "age": 55, "title": "owner"}           #