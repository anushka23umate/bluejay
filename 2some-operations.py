import pandas as pd

# Load the Excel file
file_path = "C:\\Users\\Hp\\Desktop\\bluejay\\Assignment_Timecard.xlsx"
timecard_data = pd.read_excel(file_path)

# Display the names and positions of employees
employee_info = timecard_data[['Employee Name', 'Position ID', 'Position Status']].drop_duplicates()

# Print the result to the console
print("Employee Information:")
print(employee_info)

# Display basic information about the dataset
print("Number of rows and columns:")
print(timecard_data.shape)

# Display the first few rows of the dataset
print("\nFirst few rows:")
print(timecard_data.head())

# Display summary statistics
print("\nSummary statistics:")
print(timecard_data.describe())

# Display information about data types and missing values
print("\nData types and missing values:")
print(timecard_data.info())

# Check for null values in each column
null_values = timecard_data.isnull().sum()
# Display the number of null values for each column
print("Null values in each column:")
print(null_values)

# Get the total count of null values in the entire dataset
total_null_count = timecard_data.isnull().sum().sum()

# Display the total count of null values
print("Total count of null values in the dataset:", total_null_count)
