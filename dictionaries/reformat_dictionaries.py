"""
You have a nested dictionary containing information about employees in various departments of a company.
The dictionary is structured as follows:

employees = {
    "Engineering": {
        "Alice": {"age": 29, "role": "Software Engineer"},
        "Bob": {"age": 35, "role": "DevOps Engineer"}
    },
    "Marketing": {
        "Charlie": {"age": 25, "role": "Content Strategist"},
        "Dana": {"age": 30, "role": "SEO Specialist"}
    },
    "HR": {
        "Eve": {"age": 45, "role": "HR Manager"},
        "Frank": {"age": 50, "role": "Recruiter"}
    }
}

Your task is to write a Python function reformat_employees that takes this nested dictionary as input and
returns a new dictionary structured by employee names as keys and their details (department, age, and role) as values.

The output dictionary should look like this:

{
    "Alice": {"department": "Engineering", "age": 29, "role": "Software Engineer"},
    "Bob": {"department": "Engineering", "age": 35, "role": "DevOps Engineer"},
    "Charlie": {"department": "Marketing", "age": 25, "role": "Content Strategist"},
    "Dana": {"department": "Marketing", "age": 30, "role": "SEO Specialist"},
    "Eve": {"department": "HR", "age": 45, "role": "HR Manager"},
    "Frank": {"department": "HR", "age": 50, "role": "Recruiter"}
}

"""


def reformat_employees(nested_dict):
    """
    Reformats a nested dictionary of employees by department into a flat dictionary
    of employees by name with their details including department.

    Args:
        nested_dict (dict): The input nested dictionary with departments as keys
                            and dictionaries of employee details as values.

    Returns:
        dict: A dictionary with employee names as keys and dictionaries of their
              details (department, age, role) as values.
    """
    reformatted_dict = {}
    for department, employees in nested_dict.items():
        for name, details in employees.items():
            reformatted_dict[name] = {
                "department": department,
                "age": details["age"],
                "role": details["role"]
            }
    return reformatted_dict


if __name__ == "__main__":
    employees = {
        "Engineering": {
            "Alice": {"age": 29, "role": "Software Engineer"},
            "Bob": {"age": 35, "role": "DevOps Engineer"}
        },
        "Marketing": {
            "Charlie": {"age": 25, "role": "Content Strategist"},
            "Dana": {"age": 30, "role": "SEO Specialist"}
        },
        "HR": {
            "Eve": {"age": 45, "role": "HR Manager"},
            "Frank": {"age": 50, "role": "Recruiter"}
        }
    }

    reformatted_employees = reformat_employees(employees)
    print(reformatted_employees)
