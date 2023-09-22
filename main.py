from customtkinter import *

# <-- Program Configurations --> #
root = CTk()
root.title("Time Seclude")
root.geometry("850x600")
root.resizable(False, False)

# <-- Set Globals --> #
employees = ["Natan", "David"]


# <-- Enter New Employee --> #
def enter_new_employee(new_employee):
    global employee_menu_list
    global employees

    if new_employee in employees:
        employee_exists = CTkLabel(root, text_color="red", text="Employee already exists!").grid(row=1, column=1, padx=1, pady=1)
    else:
        employees.append(new_employee)  # Enter the new employee
        employee_menu_list.destroy()  # Destroy the current Options Menu
        employee_menu_list = CTkOptionMenu(root, values=employees)  # Rebuild the Options menu with the updated employees
        employee_menu_list.grid(row=0, column=4, padx=5, pady=5)


def remove_employee(employee_to_remove):
    global employee_menu_list
    global employees

    if employee_to_remove in employees:
        for index, employee in enumerate(employees):
            if employee_to_remove == employees[index]:
                employees.pop(index)
                employee_menu_list.destroy()  # Destroy the current Options Menu
                employee_menu_list = CTkOptionMenu(root, values=employees)  # Rebuilt the Options menu with the updated employees
                employee_menu_list.grid(row=0, column=4, padx=5, pady=5)


employee_entry = StringVar(root)
CTkLabel(root, text="Enter Employee name: ").grid(row=0, column=0, padx=5, pady=5)
CTkEntry(root, textvariable=employee_entry).grid(row=0, column=1, padx=5, pady=5)
CTkButton(root, text="Insert New Employee", command=lambda: enter_new_employee(employee_entry.get())).grid(row=0, column=2, padx=5, pady=5)


# <-- Employee List --> #
CTkLabel(root, text="Employee List:").grid(row=0, column=3, padx=5, pady=5)
employee_menu_list = CTkOptionMenu(root, values=employees)
employee_menu_list.grid(row=0, column=4, padx=5, pady=5)
CTkButton(root, text="Delete Employee", command=lambda: remove_employee(employee_menu_list.get())).grid(row=0, column=5, padx=5, pady=5)


# <--  Employee Frame --> #
CTkLabel(root, text="Table of work").grid(row=1, column=2, padx=2, pady=2)
employee_frame = CTkFrame(root, width=300)


# <-- Main loop --> #
root.mainloop()
