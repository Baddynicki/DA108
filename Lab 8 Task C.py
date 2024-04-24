import csv
class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_contents(self):
        with open(self.file_path , "r") as fp:
            cont = fp.read()
            print(f"Content of file {self.file_path} is: {cont}")

    def write_contents(self, new_contents):
        with open(self.file_path , "w") as fp:
            fp.write(new_contents)
            
    def append_contents(self, new_contents):
        with open(self.file_path , "a") as fp:
            fp.write(new_contents)

class CSVDataManager(FileManager):
    def __init__(self, file_path, delimiter=','):
        super().__init__(file_path)
        self.delimiter = delimiter 
    
    def read_data(self):
        with open(self.file_path, "r") as fp:
            reader = csv.DictReader(fp, delimiter=self.delimiter)
            return [i for i in reader]
    
    def write_data(self, data):
        with open(self.file_path, "w") as fp:
            writer = csv.DictWriter(fp, fieldnames=data[0].keys(), delimiter=self.delimiter)
            writer.writeheader()
            writer.writerows(data)
    
    def append_data(self, data):
        with open(self.file_path, "a") as fp:
            writer = csv.DictWriter(fp, fieldnames=data[0].keys(), delimiter=self.delimiter)
            writer.writerows(data)

def main():
    file_path = "sample.csv"
    manager = CSVDataManager(file_path)
    try:
        initial_data = manager.read_data()
        if initial_data:
            print("Initial Data:")
            for row in initial_data:
                print(row)

                # Writing new data
            write_content = input("Enter new contents to write in the file (e.g., 'Name, Age, City'): ")
            write_content = [dict(zip(initial_data[0].keys(), write_content.split(',')))]
            manager.write_data(write_content)

    # Appending more data
            append_content = input("Enter new contents to append in the file (e.g., 'Alice, 30, New York'): ")
            append_content = [dict(zip(initial_data[0].keys(), append_content.split(',')))]
            manager.append_data(append_content)

    # Reading and printing updated data
            updated_data = manager.read_data()
            print("\nUpdated Data:")
            for row in updated_data:
                print(row)
        else:
            print("File has no contents")

    except FileNotFoundError:
        print("File not found.")
    except Exception as i:
        print(e, "Error occured")


if __name__ == "__main__":
    main()
