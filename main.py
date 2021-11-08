import pandas
path = input("Please enter the file path: ")
try:
    print("The emails are:")
    print(pandas.read_excel(path)["email"].unique())
except:
    print("An exception occurred")
