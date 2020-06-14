# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Kate Golenkova, 06/13/2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    import ProcessingClasses as FP
    from IOClasses import EmployeeIO as IO
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
file_name = "EmployeeData.txt" # Set variable for file
list_table = [] # List of rows from file
list_of_objects = [] # List of employee objects
emp = [] # List of new employee objects

# Load data from file into a list of employee objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of employee objects
    # Let user add data to the list of employee objects
    # let user save current data to file
    # Let user exit program

try:
    # Load data from file into a list of employee objects when script starts
    list_table = FP.FileProcessor.read_data_from_file(file_name)
    print("Welcome to Assignment 09.")
    print("Please use this program to add new Employee into file.")
    list_of_objects.clear()
    for line in list_table:
        list_of_objects.append(Emp(line[0], line[1], line[2].strip()))
        # While loop to display Menu with options
    while True:
        # Show user a menu of options
        IO.show_menu()
        # Get user's menu option choice
        strChoice = IO.input_menu_choice()
        if strChoice.strip() == '1':
            # Show user current data in the list of employee objects
            IO.show_current_employees(list_of_objects)
            continue
        elif strChoice.strip() == '2':
            # Let user add new employee
            try:
                emp = IO.input_new_employee()
                list_of_objects.append(emp)
            except ValueError as e:
                print(e)
            continue
        elif strChoice.strip() == '3':
            # let user save current data to file
            FP.FileProcessor.save_data_to_file(file_name, list_of_objects)
            continue
        elif strChoice.strip() == '4':
            # Let user exit the program
            print("Goodbye!")
            break
#
except Exception as e:
     print("There was an error!")
     print(e, e.__doc__, type(e), sep='\n')


# Main Body of Script  ---------------------------------------------------- #
