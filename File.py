def file_read_write():
    try:
        
        filename = input("Enter the name of the file to read: ").strip()
        
    
        with open(filename, 'r') as file:
            content = file.readlines()

        
        modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]

    
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_content)

        print(f"File has been successfully read and modified content saved to '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' could not be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    file_read_write()
