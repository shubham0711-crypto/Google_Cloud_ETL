from faker import Faker
import random
import pandas as pd

# Initialize Faker
fake = Faker()

# Function to generate employee data
def generate_employee_data(num_records=10):
    employee_data = []
    
    for _ in range(num_records):
        employee = {
            "Employee_ID": fake.unique.random_number(digits=5),  # Unique employee ID
            "First_Name": fake.first_name(),
            "Last_Name": fake.last_name(),
            "Email": fake.email(),
            "Phone_Number": fake.phone_number(),
            "Date_of_Birth": fake.date_of_birth(minimum_age=22, maximum_age=65).strftime('%Y-%m-%d'),
            "Address": fake.address(),
            "Position": random.choice(['Software Engineer', 'Data Scientist', 'HR Manager', 'Accountant', 'Marketing Specialist']),
            "Department": random.choice(['IT', 'HR', 'Finance', 'Marketing', 'Operations']),
            "Salary": round(random.uniform(50000, 150000), 2),  # Salary between 50K and 150K
            "SSN": fake.ssn(),  # Social Security Number (PII)
            "Passport_Number": fake.passport_number()  # Passport Number (PII)
        }
        employee_data.append(employee)
    
    return employee_data

# Generate data for 50 employees
num_records = 1000
employee_data = generate_employee_data(num_records)

# Convert to a DataFrame for easy manipulation or saving to file
employee_df = pd.DataFrame(employee_data)

# Save to a CSV file
employee_df.to_csv("employee_data.csv", index=False)

print(f"{num_records} employee records generated and saved to employee_data.csv")
