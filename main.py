from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")
#db.print_tables(verbose=True)


#print Name from the table Artist
db.pretty_print("SELECT Name FROM Artist")

#Print all data from the table Invoice where BillingCountry is Germany
db.pretty_print("SELECT * FROM Invoice WHERE BillingCountry = 'Germany' ")

#Count how many albums are in the database
number_of_albums = db.execute("SELECT COUNT(*) FROM Album")
print(number_of_albums[0][0])

#How many customers are from France?
customers_from_france = db.execute("SELECT COUNT(*) FROM Customer WHERE Customer.Country = 'France' ")
print(customers_from_france[0][0])