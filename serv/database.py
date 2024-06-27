import pyodbc


server = 'LARAARAUJO'
database = 'CRUDDB'
username = 'LARAARAUJO\lara-'
password = ''
conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Trusted_Connection=yes')
cursor = conn.cursor()
