class TableDB:
    def __init__(self):
        self.table_database = []

    def insert(self, table):
        self.table_database.append(table)

    def search(self, table_name):
        for i in range(len(self.table_database)):
            if self.table_database[i].table_name == table_name:
                return i
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
        f"{self.table_name} : {self.table}"











