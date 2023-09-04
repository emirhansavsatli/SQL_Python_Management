from func import SQLManager

if __name__ == "__main__":
    db_manager = SQLManager("ID", "VERİ")


    columns = [("id", "INT"), ("name", "VARCHAR(255)")]
    db_manager.create_table("yenitablo", columns)


    db_manager.drop_table("yenitablo")


    values = [1, "İSİM GİR"]
    db_manager.insert_row("yenitablo", values)


    db_manager.add_column("yenitablo", "age", "INT")

    condition = "id = 1"
    db_manager.delete_row("yenitablo", condition)




