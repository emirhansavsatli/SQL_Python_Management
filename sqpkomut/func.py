import pypyodbc

db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=.;'
    'Database=asdf;'
    'Trusted_Connection=True;'
)

class SQLManager:
    def __init__(self, server, database):
        self.connection = pypyodbc.connect(
            f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database}"
        )
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):

        column_definitions = []
        for col in columns:
            column_name = col[0]
            data_type = col[1]
            column_definition = f"{column_name} {data_type}"
            column_definitions.append(column_definition)

        column_str = ', '.join(column_definitions)
        query = f"CREATE TABLE {table_name} ({column_str})"

        self.cursor.execute(query)
        self.connection.commit()


    def drop_table(self, table_name):
        query = f"DROP TABLE {table_name}"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_row(self, table_name, values):
        value_placeholders = ', '.join(['?' for _ in values])
        query = f"INSERT INTO {table_name} VALUES ({value_placeholders})"
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_row(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()

    def add_column(self, table_name, column_name, data_type):
        query = f"ALTER TABLE {table_name} ADD {column_name} {data_type}"
        self.cursor.execute(query)
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

