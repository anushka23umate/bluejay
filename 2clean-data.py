import pandas as pd

# Load the Excel file
file_path = "C:\\Users\\Hp\\Desktop\\bluejay\\Assignment_Timecard.xlgiysx"
timecard_data = pd.read_excel(file_path)

# Display the shape before any modifications
print("Shape before cleaning:", timecard_data.shape)

# Drop unnecessary columns
columns_to_drop = ['Unnamed: 9', 'Unnamed: 10']
timecard_data = timecard_data.drop(columns=columns_to_drop)

# Drop rows with any null values
timecard_data = timecard_data.dropna()

# Display the shape after cleaning
print("Shape after cleaning:", timecard_data.shape)
