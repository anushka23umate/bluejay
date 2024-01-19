import pandas as pd

# Load the cleaned Excel file
file_path = "C:\\Users\\Hp\\Desktop\\bluejay\\Assignment_Timecard.xlsx"
timecard_data = pd.read_excel(file_path)

# Convert 'Time' and 'Time Out' columns to datetime format
timecard_data['Time'] = pd.to_datetime(timecard_data['Time'])
timecard_data['Time Out'] = pd.to_datetime(timecard_data['Time Out'])

# Sort the DataFrame by 'Employee Name' and 'Time'
timecard_data.sort_values(by=['Employee Name', 'Time'], inplace=True)

# Function to check consecutive days
def check_consecutive_days(group):
    return group['Time'].diff().dt.days == 1

# Employees who have worked for 7 consecutive days
consecutive_days_mask = timecard_data.groupby('Employee Name').apply(check_consecutive_days).reset_index(level=0, drop=True)
employees_7_consecutive_days = timecard_data[consecutive_days_mask]

# Display the name and position of employees who have worked for 7 consecutive days
result = employees_7_consecutive_days[['Employee Name', 'Position ID']]
print(result)
