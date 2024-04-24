import os
class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_contents(self):
        with open(self.file_path , "r") as fp:
            cont = fp.read()
            print(f"Content of file {self.file_path} is: {cont}")

    def write_contents(self, new_contents):
        with open(self.file_path , "w") as fp:
            fp.write(self.new_contents)
            
    def append_contents(self, new_contents):
        with open(self.file_path , "a") as fp:
            fp.write(self.new_contents)
    
def main():
    file_path = "hello.txt"
    manager = FileManager(file_path)

    manager.read_contents()

    write_content = input("Enter new contents to write in the file")
    manager.write_contents(write_content)

    append_content = input("Enter new contents to append in the file")
    manager.write_contents(append_content)

    manager.read_contents()


if __name__ == "__main__":
    main()



            
    
    
