import os

base_dir = "2025"
number_of_days = 12

# Create a base directory (optional)
os.makedirs(base_dir, exist_ok=True)

for i in range(1, number_of_days + 1):
    folder_name = os.path.join(base_dir, f"Day{i}")
    os.makedirs(folder_name, exist_ok=True)
    
    # Create 2 Python files
    for j in range(1, 3):
        py_file_path = os.path.join(folder_name, f"day{i}_part{j}.py")
        with open(py_file_path, "w") as f:
            f.write("# Python file\n")

    # Create 1 text file
    txt_file_path = os.path.join(folder_name, f"day{i}_input.txt")
    with open(txt_file_path, "w") as f:
        f.write("This is a text file.\n")

print("Folders and files created successfully.")
