import datetime

def create_timestamp_file():
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    file_name = f"timestamp_file_{current_timestamp}.txt"

    with open(file_name, 'w') as file:
        file.write(f"Content of the file created at {current_timestamp}")

    print(f"File '{file_name}' created successfully.")

create_timestamp_file()