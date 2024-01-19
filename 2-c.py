import pandas as pd

# Load the cleaned Excel file
file_path = "C:\\Users\\Hp\\Desktop\\bluejay\\Assignment_Timecard.xlsx"
timecard_data = pd.read_excel(file_path)

# Convert 'Time' and 'Time Out' columns to datetime format
timecard_data['Time'] = pd.to_datetime(timecard_data['Time'])
timecard_data['Time Out'] = pd.to_datetime(timecard_data['Time Out'])

# Calculate total hours worked for each employee
timecard_data['Total Hours Worked'] = (timecard_data['Time Out'] - timecard_data['Time']).dt.total_seconds() / 3600

# Identify employees who have worked for more than 14 hours
employees_more_than_14_hours = timecard_data[timecard_data['Total Hours Worked'] > 14]

# Display the result
print("Employees who have worked for more than 14 hours:")
print(employees_more_than_14_hours[['Employee Name', 'Position ID', 'Total Hours Worked']])
