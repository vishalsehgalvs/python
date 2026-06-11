import os

# ============================================================
# PYTHON OS MODULE - FILE & FOLDER OPERATIONS
# Simple to Complex, explained in plain everyday language
# ============================================================


# ------------------------------------------------------------
# 1. Find out WHERE you currently are (your working folder)
# ------------------------------------------------------------
# Think of this like asking "which room am I in right now?"
cwd = os.getcwd()
print("Current working directory:", cwd)


# ------------------------------------------------------------
# 2. Move to a different folder (change your location)
# ------------------------------------------------------------
# Like walking one room back (going up one folder level)
def show_current_path():
    print("Current working directory:", os.getcwd())

show_current_path()          # print where we are before moving
os.chdir('../')              # go one folder up (like pressing "back")
show_current_path()          # print where we ended up


# ------------------------------------------------------------
# 3. Check if a file or folder EXISTS before doing anything
# ------------------------------------------------------------
# Before opening a drawer, you check if it's actually there
result = os.path.exists("some_file.txt")   # True if it exists, False if not
print("Does the file exist?", result)


# ------------------------------------------------------------
# 4. Check the SIZE of a file (how big is it in bytes?)
# ------------------------------------------------------------
# Like weighing a package before shipping it
# Uncomment and replace "filename" with a real file to try it
# size = os.path.getsize("filename.txt")
# print("Size of the file is", size, "bytes.")


# ------------------------------------------------------------
# 5. See EVERYTHING inside a folder (list its contents)
# ------------------------------------------------------------
# Like opening a drawer and listing everything you see inside
path = "."                            # "." means the current folder
contents = os.listdir(path)
print("Files and folders in current directory:", contents)


# ------------------------------------------------------------
# 6. Create a NEW folder (single level)
# ------------------------------------------------------------
# Like making one new empty drawer/cabinet
new_folder = "my_new_folder"
if not os.path.exists(new_folder):    # only create if it doesn't already exist
    os.mkdir(new_folder)
    print(f"Folder '{new_folder}' created!")
else:
    print(f"Folder '{new_folder}' already exists, skipping.")


# ------------------------------------------------------------
# 7. Create NESTED folders all at once (multiple levels deep)
# ------------------------------------------------------------
# Like building a whole filing cabinet with sections and sub-sections in one go
nested_path = "parent_folder/child_folder/grandchild_folder"
os.makedirs(nested_path, exist_ok=True)   # exist_ok=True means don't crash if it's already there
print(f"Nested folders created at: {nested_path}")


# ------------------------------------------------------------
# 8. Write to a file, then READ it back
# ------------------------------------------------------------
# Like writing a note, putting it in a box, then opening the box to read it
file_name = "my_note.txt"

# Writing to the file
with open(file_name, 'w') as f:
    f.write("Hello from the OS module demo!")

# Reading the file back
with open(file_name, 'r') as f:
    content = f.read()
    print("File contents:", content)


# ------------------------------------------------------------
# 9. RENAME a file (give it a new name)
# ------------------------------------------------------------
# Like crossing out an old label and writing a new one
old_name = "my_note.txt"
new_name = "renamed_note.txt"
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"File renamed from '{old_name}' to '{new_name}'")


# ------------------------------------------------------------
# 10. DELETE a single file (permanently remove it)
# ------------------------------------------------------------
# Like throwing a piece of paper in the trash — it's gone
file_to_delete = "renamed_note.txt"
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"File '{file_to_delete}' deleted.")


# ------------------------------------------------------------
# 11. DELETE an empty folder
# ------------------------------------------------------------
# Like removing an empty drawer from a cabinet
folder_to_delete = "my_new_folder"
if os.path.exists(folder_to_delete):
    os.rmdir(folder_to_delete)   # only works if the folder is completely empty!
    print(f"Folder '{folder_to_delete}' removed.")


# ------------------------------------------------------------
# 12. Safely open a file — handle errors if it doesn't exist
# ------------------------------------------------------------
# Like trying to open a door — if it's locked, handle it gracefully instead of panicking
try:
    f = open("some_file_that_may_not_exist.txt", 'r')
    text = f.read()
    f.close()
    print(text)
except IOError:
    # This runs only if the file was not found or couldn't be read
    print("Oops! Could not find or open the file. It might not exist.")


# ------------------------------------------------------------
# 13. Run a SHELL COMMAND and read its output directly in Python
# ------------------------------------------------------------
# Like typing a command in your terminal and capturing what it prints back
output = os.popen("echo Hello from the shell!").read()
print("Shell output:", output)


# ------------------------------------------------------------
# 14. Build a full file PATH by joining folder + filename safely
# ------------------------------------------------------------
# Instead of typing "folder/subfolder/file.txt" manually,
# let Python build the correct path for your operating system
folder   = "parent_folder"
filename = "my_document.txt"
full_path = os.path.join(folder, filename)
print("Full path built:", full_path)


# ------------------------------------------------------------
# 15. Clean up the nested folders we created earlier
# ------------------------------------------------------------
# Like tidying up after yourself — remove the test folders we made
import shutil   # shutil can delete folders that are NOT empty (os.rmdir can't)
if os.path.exists("parent_folder"):
    shutil.rmtree("parent_folder")
    print("Cleaned up: 'parent_folder' and everything inside it removed.")

