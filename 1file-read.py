import pandas as pd
file_path = "C:\\Users\\Hp\\Desktop\\bluejay\\Assignment_Timecard.xlsx"
readFile = pd.read_excel(file_path)

# Displaying the dataset
print(readFile)