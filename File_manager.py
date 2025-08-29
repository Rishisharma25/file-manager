import os

def create_file(filename):
    """ creates a file with the given filename"""
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename}: Created Successfully!")
    except FileExistsError:
        print(f"File Name {filename} already exists!")
    except Exception as E:
        print(f"An error occurred! {E}")

def view_all_files():
    """ lists all files in the current directory"""
    files = os.listdir('.')
    if not files:
        print("No files found in the current directory.")
    else:
        print("Files in the current directory:")
        for file in files:
            print(file)

def delete_file(filename):
    """ deletes the file with the given filename"""
    try:
        os.remove(filename)
        print(f"File Name {filename}: Deleted Successfully!")
    except FileNotFoundError:
        print(f"File Name {filename} does not exist!")
    except Exception as E:      
        print("An error occurred! {E}")

def read_file(filename):
    """ reads and prints the content of the file with the given filename"""
    try:
        with open('sample.txt', 'r') as f:
            content = f.read()
            print(f"content of the file {filename}:\n{content}  ")
    except FileNotFoundError:
        print(f"File Name {filename} does not exist!")
    except Exception as E:
        print(f"An error occurred! {E}")    

def edit_file(filename):
    """ appends content to the file with the given filename"""
    try:
        with open('sample.txt', 'a') as f:
            content = input("Enter content to append: ")
            f.write(content + '\n')
            print(f"Content appended to file {filename} successfully!")

    except FileNotFoundError:
        print(f"File Name {filename} does not exist!")
    except Exception as E:
        print(f"An error occurred! {E}")

def main():
    while True:
        print("\nFile Manager Application")
        print("1: Create file")
        print("2: View all file ")
        print("3: Delete file" )    
        print("4: Read file")
        print("5: Edit file")       
        print("6: Exit/Stop")

        choice = int(input("Choose your operation(1-6):"))

        if choice == 1:
            filename = input("Enter the filename to create: ")
            create_file(filename)

        elif choice == 2:
            view_all_files()

        elif choice == 3:
            filename = input("Enter the filename to delete: ")
            delete_file(filename)

        elif choice == 4:
            filename = input("Enter the filename to read: ")
            read_file(filename)
        
        elif choice == 5:
            filename = input("Enter the filename to edit: ")
            edit_file(filename)

        elif choice == 6:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid operation (1-6).")
            print("Exiting the application. Goodbye!")

if __name__ == "__main__":
    main()