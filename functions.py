# file reading function
def get_names(filepath='employee_list.txt'):
    with open(filepath, 'r') as file:
        return file.readlines()
