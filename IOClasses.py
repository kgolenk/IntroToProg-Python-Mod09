# ---------------------------------------------------------- #
# Title: IOClasses Module
# Description: A IO module for Assignment 09
# ChangeLog (Who,When,What):
# Kate Golenkova, 06/11/2020, Created started script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")
else:
    import DataClasses as DC

class EmployeeIO:
    """Perfoms Inputs and Outputs:

        methods:
            show_menu() - show menu to user

            input_menu_choice() - ask user for an option

            show_current_employees(list_of_rows)

            input_new_employee()

        changelog: (When,Who,What)
            Kate Golenkova, 06/11/2020, Modified code to complete assignment 09
        """

    @staticmethod
    def show_menu():  # Display menu
        print('''
                    Choose an Option:
                        1. Show Current Employees 
                        2. Add New Employee
                        3. Save New Data 
                        4. Exit
                ''')

    @staticmethod
    def input_menu_choice():  # Get user choice input
        choice = input("Please enter an Option: ")
        return choice

    @staticmethod
    def show_current_employees(list_of_rows: []):
        """ Print the current data in the Employee rows

        :param list_of_rows: (list) of rows you want to display
        """
        print("******* The current items employees are: *******")
        for row in list_of_rows:
            print(str(row.employee_id) + " | " + row.first_name + " | " + row.last_name)
        print("*******************************************")

    @staticmethod
    def input_new_employee():
        """ Gets data for an employee object

        :return: (employee) object with input data
        """
        emp = []
        try:
            employee_id = input("Please enter employee ID: ")
            first_name = input("Please enter employee first name: ")
            last_name = input("Please enter employee last name: ")
            emp = DC.Employee(employee_id,first_name,last_name)
        except Exception as e:
            print(e)
        print("New employee [" + str(emp) + "] has been addded.")
        return emp

