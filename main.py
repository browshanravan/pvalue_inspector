from src.utils import read_csv_file


FILE_LOCATION= "/workspaces/data/"
FILE_NAME= "normal_data.csv"


df= read_csv_file(FILE_LOCATION+FILE_NAME)

print(df.head(3))