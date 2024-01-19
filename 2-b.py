import pandas as pd

# Load the cleaned Excel file
file_path = "C:\\Users\\Hp\\Desktop\\bluejay\\Assignment_Timecard.xlsx"
timecard_data = pd.read_excel(file_path)

# Convert 'Time' and 'Time Out' columns to datetime format
timecard_data['Time'] = pd.to_datetime(timecard_data['Time'])
timecard_data['Time Out'] = pd.to_datetime(timecard_data['Time Out'])

# Sort the DataFrame by 'Employee Name' and 'Time'
timecard_data.sort_values(by=['Employee Name', 'Time'], inplace=True)

# Function to check time between shifts
def check_time_between_shifts(group):
    time_difference = group['Time'].diff().dt.total_seconds() / 3600  # convert seconds to hours
    return (1 < time_difference) & (time_difference < 10)

# Employees who have less than 10 hours of time between shifts but greater than 1 hour
time_between_shifts_mask = timecard_data.groupby('Employee Name').apply(check_time_between_shifts).reset_index(level=0, drop=True)
employees_time_between_shifts = timecard_data.loc[time_between_shifts_mask]

# Display the result
print("Employees who have less than 10 hours of time between shifts but greater than 1 hour:")
print(employees_time_between_shifts[['Employee Name', 'Position ID']])