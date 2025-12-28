import os

year = "2025"
start_day = 1
end_day = 2

os.makedirs(year, exist_ok=True)

for i in range(1, end_day + 1):
    folder_name = os.path.join(year, f"Day{i}")
    os.makedirs(folder_name, exist_ok=True)
    
    # Create 2 Python files
    for j in range(1, 3):
        py_file_path = os.path.join(folder_name, f"day{i}_part{j}.py")
        if not os.path.exists(py_file_path):
            with open(py_file_path, "w") as f:
                f.write("# Python file\n")

    # Create 1 text file
    txt_file_path = os.path.join(folder_name, f"day{i}_input.txt")
    if not os.path.exists(txt_file_path):
        with open(txt_file_path, "w") as f:
            f.write("This is a text file.\n")

print("Folders and files created successfully.")
