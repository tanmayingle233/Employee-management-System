import mysql.connector
import tkinter as tk

def connect_to_database():
    """Connects to the MySQL database."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tanmay123",
        database="employee"
    )

def add_employee():
    """Adds an employee to the database."""
    employee_id = entry_id.get()
    employee_name = entry_name.get()
    employee_position = entry_position.get()
    employee_salary = entry_salary.get()

    cursor = connection.cursor()
    sql = "INSERT INTO employees (id, name, position, salary) VALUES (%s, %s, %s, %s)"
    values = (employee_id, employee_name, employee_position, employee_salary)

    cursor.execute(sql, values)
    connection.commit()

    result_label.config(text="Employee added successfully.")

def check_employee():
    """Checks if an employee exists in the database."""
    employee_id = entry_id.get()

    cursor = connection.cursor()
    sql = "SELECT * FROM employees WHERE id = %s"
    values = (employee_id,)

    cursor.execute(sql, values)
    result = cursor.fetchone()

    if result:
        result_label.config(text="Employee exists.")
    else:
        result_label.config(text="Employee does not exist.")

def display_employees():
    """Displays all employees in the database."""
    cursor = connection.cursor()
    sql = "SELECT * FROM employees"
    cursor.execute(sql)
    results = cursor.fetchall()

    display_text = ""
    for employee in results:
        display_text += f"Employee ID: {employee[0]}\n"
        display_text += f"Employee name: {employee[1]}\n"
        display_text += f"Employee position: {employee[2]}\n"
        display_text += f"Employee salary: {employee[3]}\n\n"

    result_label.config(text=display_text)

def delete_employee():
    """Deletes an employee from the database."""
    employee_id = entry_id.get()

    cursor = connection.cursor()
    sql = "DELETE FROM employees WHERE id = %s"
    values = (employee_id,)

    cursor.execute(sql, values)
    connection.commit()

    result_label.config(text="Employee deleted successfully.")



# Initialize the Tkinter window
window = tk.Tk()
window.title("Employee Management")

# Create and configure the database connection
connection = connect_to_database()

# Create and configure Tkinter widgets
label_id = tk.Label(window, text="Employee ID:")
label_name = tk.Label(window, text="Employee Name:")
label_position = tk.Label(window, text="Employee Position:")
label_salary = tk.Label(window, text="Employee Salary:")

entry_id = tk.Entry(window)
entry_name = tk.Entry(window)
entry_position = tk.Entry(window)
entry_salary = tk.Entry(window)

add_button = tk.Button(window, text="Add Employee", command=add_employee)
check_button = tk.Button(window, text="Check Employee", command=check_employee)
display_button = tk.Button(window, text="Display Employees", command=display_employees)
delete_button = tk.Button(window, text="Delete Employee", command=delete_employee)

result_label = tk.Label(window, text="Result will be displayed here.")

# Place the widgets in the window using grid layout
label_id.grid(row=0, column=0)
label_name.grid(row=1, column=0)
label_position.grid(row=2, column=0)
label_salary.grid(row=3, column=0)

entry_id.grid(row=0, column=1)
entry_name.grid(row=1, column=1)
entry_position.grid(row=2, column=1)
entry_salary.grid(row=3, column=1)

add_button.grid(row=4, column=0)
check_button.grid(row=4, column=1)
display_button.grid(row=5, column=0)
delete_button.grid(row=5, column=1)

result_label.grid(row=6, column=0, columnspan=2)

window.mainloop()

# Close the database connection when the Tkinter window is closed
connection.close()
