import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

class TableDB:
    def __init__(self):
        self.table_database = []

    def insert(self, table):
        self.table_database.append(table)

    def search(self, table_name):
        for table in self.table_database:
            if table.table_name == table_name:
                return table
        return None

class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        filtered_list = [item for item in self.table if condition(item)]
        return filtered_list

    def aggregate(self, aggregation_function, aggregation_key):
        if not self.table:
            return None

        col_val = []
        for item in self.table:
            if aggregation_key in item:
                col_val.append(float(item[aggregation_key]))

        return aggregation_function(col_val) if col_val else None

    def __str__(self):
        return f"{self.table_name} : {self.table}"

#Print the min and max temperatures for cities in EU that do not have coastlines
eu_country_items = []
eu_no_coastline = filter(lambda x: x["coastline"] == "no" and x["EU"] == "yes", countries)
for item in eu_no_coastline:
    eu_country_items.append(item["country"])

temp = []
cities_eu = filter(lambda x: x["country"], cities)
for i in cities_eu:
    if i["country"] in eu_country_items:
        temp.append(float(i["temperature"]))

min_temp_eu_no_coastline = min(temp)
max_temp_eu_no_coastline = max(temp)
print(f"The min temperatures for cities in EU that do not have coastlines : {min_temp_eu_no_coastline}")
print(f"The max temperatures for cities in EU that do not have coastlines : {max_temp_eu_no_coastline}")
print()

#Print the min and max latitude for cities in every country
latitude_list = []
a = filter(lambda x: x["latitude"], cities)
for item in a:
    latitude_list.append(float(item["latitude"]))

min_latitude = min(latitude_list)
max_latitude = max(latitude_list)
print(f"The min latitude for cities in every country : {min_latitude}")
print(f"The max latitude for cities in every country : {max_latitude}")
