# ---------------------------------------------------------- #
# Title: TestHarness
# Description: A main module for testing
# ChangeLog (Who,When,What):
# Kate Golenkova, 06/07/2020, Created started script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    from DataClasses import Employee as Emp  # Employee class only!
    import ProcessingClasses as P  # processing classes
    from IOClasses import EmployeeIO as IO # Input/Output classes
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Lue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
# for row in lstTable:
#     print(row.to_string(), type(row))

# Test IO module
IO.show_menu()
print("_______________")
IO.show_current_employees(lstTable)

print(IO.input_new_employee())
print(IO.input_menu_choice())


