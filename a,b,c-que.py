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

# a) Employees who have worked for 7 consecutive days
consecutive_days_mask = timecard_data.groupby('Employee Name').apply(check_consecutive_days).reset_index(level=0, drop=True)
employees_7_consecutive_days = timecard_data.loc[consecutive_days_mask]

# Display the result for part (a)
print("Employees who have worked for 7 consecutive days:")
print(employees_7_consecutive_days[['Employee Name', 'Position ID']])
print("\n---\n")

# Function to check time between shifts
def check_time_between_shifts(group):
    time_difference = group['Time'].diff().dt.total_seconds() / 3600  # convert seconds to hours
    return (1 < time_difference) & (time_difference < 10)

# b) Employees who have less than 10 hours of time between shifts but greater than 1 hour
time_between_shifts_mask = timecard_data.groupby('Employee Name').apply(check_time_between_shifts).reset_index(level=0, drop=True)
employees_time_between_shifts = timecard_data.loc[time_between_shifts_mask]

# Display the result for part (b)
print("Employees who have less than 10 hours of time between shifts but greater than 1 hour:")
print(employees_time_between_shifts[['Employee Name', 'Position ID', 'Time', 'Time Out']])
print("\n---\n")

# c) Employees who have worked for more than 14 hours
total_hours_worked = (timecard_data['Time Out'] - timecard_data['Time']).dt.total_seconds() / 3600
employees_more_than_14_hours = timecard_data[total_hours_worked > 14]

# Display the result for part (c)
print("Employees who have worked for more than 14 hours:")
print(employees_more_than_14_hours[['Employee Name', 'Position ID', 'Time', 'Time Out']])
