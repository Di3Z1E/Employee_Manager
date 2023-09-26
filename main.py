from customtkinter import *
from CTkMessagebox import *
import json


class App(CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("800x600")
        self.title("Employee Organizer")
        self.resizable(False, False)
        self.main_page()  # Display main page
        self.iconbitmap("employee_icon.ico")

    def main_page(self):
        CTkButton(self, text="View Or Edit Employees", command=lambda: self.display_outer_pages("View Employees")).grid(row=1, column=0)

        header = CTkLabel(self, font=("Gisha", 16), text="Employee Organizer", text_color="Green")
        header.grid(row=0, columnspan=6, column=6)

    def display_outer_pages(self, type):
        if type == "View Employees":
            self.employees()  # Display Employee CRUD window on button click

    @staticmethod
    def employees():
        # Create Empty storage for employees
        employees_json = {}
        employee_id_list = []

        # Path to employees JSON file
        employees_json_file_path = os.path.expanduser("~/Documents/Employee List/employees.json")

        # Load employees to the application
        try:
            with open(employees_json_file_path, "r") as file:
                content = json.load(file)

                for employee, role in content["employees"].items():
                    employees_json[employee] = role

        except FileNotFoundError:
            with open(os.path.expanduser("~/Documents/Employee List/employees.json"), "w") as file:
                file.write("""
                  {
                    "employees": {
                    }
                  }
                """)

        # Create the new window
        view_employees_window = CTkToplevel()
        view_employees_window.title("View/Edit Employees")
        view_employees_window.geometry("950x700")
        view_employees_window.resizable(False, False)
        view_employees_window.grab_set()

        # Create the widgets
        employee_list_label = CTkLabel(view_employees_window, font=("Gisha", 20), text="Employee List")
        employee_list_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        employee_list_frame = CTkScrollableFrame(master=view_employees_window, width=920, height=500)
        employee_list_frame.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        employee_id = CTkLabel(employee_list_frame, text="Employee ID:")
        employee_id.grid(row=0, column=0, padx=15, pady=15)

        employee_name = CTkLabel(employee_list_frame, text="Employee First Name:")
        employee_name.grid(row=0, column=1, padx=15, pady=15)

        employee_last_name = CTkLabel(employee_list_frame, text="Employee Last Name:")
        employee_last_name.grid(row=0, column=2, padx=15, pady=15)

        employee_role = CTkLabel(employee_list_frame, text="Employee Role:")
        employee_role.grid(row=0, column=3, padx=15, pady=15)

        employee_category = CTkLabel(employee_list_frame, text="Employee Role Category:")
        employee_category.grid(row=0, column=4, padx=15, pady=15)

        employee_rate = CTkLabel(employee_list_frame, text="Employment Rate:")
        employee_rate.grid(row=0, column=5, padx=15, pady=15)

        # Display Employees
        current_row = 1
        current_column = 0

        for employee_tag, employee_info in employees_json.items():
            for emp_fname, emp_lname in employee_info.items():
                assign_employee = CTkLabel(employee_list_frame, text=emp_lname)
                assign_employee.grid(row=current_row, column=current_column, padx=5, pady=5)

                if emp_fname == "Employee ID":
                    if emp_lname in employee_id_list:
                        pass
                    else:
                        employee_id_list.append(emp_lname)

                current_column += 1
                if current_column > 5:
                    current_column = 0
                    current_row += 1

        def delete_employee_function(employee_to_delete):
            if employee_to_delete != "Select Employee":
                msg = CTkMessagebox(title="Delete Employee?", message=f"Are you sure you want to delete {employee_to_delete} from the employee list?", icon="warning", option_1="No", option_2="Yes")

                if msg.get() == "Yes":
                    # Delete from JSON source file
                    with open(employees_json_file_path, "r") as remove_employee_json_file:
                        json_loaded = json.load(remove_employee_json_file)

                    if 'employees' in json_loaded and employee_to_delete in json_loaded['employees']:
                        del json_loaded['employees'][employee_to_delete]

                        with open(employees_json_file_path, "w") as final_remove_employee_json_file:
                            json.dump(json_loaded, final_remove_employee_json_file, indent=4)

                    # Delete from List
                    employee_id_list.remove(employee_to_delete)

                    CTkLabel(view_employees_window, text_color="green", text="Successfully Deleted Employee").grid(row=4, column=1, columnspan=2, padx=15, pady=15)

        def create_new_employee():
            # Create a new window for the form
            employee_create_window = CTkToplevel()
            employee_create_window.title("Create Employee")
            employee_create_window.geometry("350x300")
            employee_create_window.resizable(False, False)
            employee_create_window.grab_set()


            # Add widgets
            CTkLabel(employee_create_window, font=("Gisha", 17), text_color="light blue", text="Enter Employee Details Form").grid(row=0, column=0, columnspan=2, padx=5, pady=5)

            CTkLabel(employee_create_window, text="Enter Employee First Name:").grid(row=1, column=0, padx=5, pady=5)
            employee_first_name = CTkEntry(employee_create_window)
            employee_first_name.grid(row=1, column=1, padx=5, pady=5)

            CTkLabel(employee_create_window, text="Enter Employee Last Name:").grid(row=2, column=0, padx=5, pady=5)
            employee_last_name = CTkEntry(employee_create_window)
            employee_last_name.grid(row=2, column=1, padx=5, pady=5)

            CTkLabel(employee_create_window, text="Enter Employee Role:").grid(row=3, column=0, padx=5, pady=5)
            employee_role = CTkEntry(employee_create_window)
            employee_role.grid(row=3, column=1, padx=5, pady=5)

            CTkLabel(employee_create_window, text="Enter Employee Category:").grid(row=4, column=0, padx=5, pady=5)
            employee_category = CTkEntry(employee_create_window)
            employee_category.grid(row=4, column=1, padx=5, pady=5)

            CTkLabel(employee_create_window, text="Enter Employee Rate:").grid(row=5, column=0, padx=5, pady=5)
            employee_rate = CTkEntry(employee_create_window)
            employee_rate.grid(row=5, column=1, padx=5, pady=5)

            def print_data():
                print(employee_first_name.get(), employee_last_name.get(), employee_role.get(), employee_category.get(), employee_rate.get())

            CTkButton(employee_create_window, text="Save", fg_color="green", command=print_data).grid(row=6, column=0, padx=7, pady=7)
            CTkButton(employee_create_window, text="Cancel & Exit", fg_color="red", command=employee_create_window.destroy).grid(row=6, column=1, padx=7, pady=7)

        selected_employee_var = StringVar()
        selected_employee_var.set("Select Employee")
        selected_employee = CTkComboBox(view_employees_window, variable=selected_employee_var, values=employee_id_list, state="readonly", justify="center")
        selected_employee.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        new_employee = CTkButton(view_employees_window, fg_color="green", text="New Employee", command=create_new_employee)
        new_employee.grid(row=3, column=0, columnspan=2)

        update_employee = CTkButton(view_employees_window, text="Update Employee")
        update_employee.grid(row=3, column=1, columnspan=2)

        delete_employee = CTkButton(view_employees_window, fg_color="red", text="Delete Employee", command=lambda: delete_employee_function(selected_employee.get()))
        delete_employee.grid(row=3, column=2, columnspan=2)

        action_completed = CTkLabel(view_employees_window, text="")
        action_completed.grid(row=4, column=1, columnspan=2, padx=15, pady=15)

if __name__ == "__main__":
    app = App()
    app.mainloop()
