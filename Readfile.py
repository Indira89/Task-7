def read_and_display_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()

            print("File Content:")
            print(file_content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")

file_to_read = "timestamp_file_2023-12-16_22-39-12.txt"  
read_and_display_file(file_to_read)
