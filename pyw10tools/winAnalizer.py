import os

# Detect all drives available in the system
def get_all_drives():
    drives = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        drive = f"{letter}:\\"
        if os.path.exists(drive):
            drives.append(drive)
    return drives

# Possible folder names for "Users" in English and Spanish
user_folder_names = ['Users', 'Usuarios']

def search_user_folders():
    all_users = []  # To store all found user folders
    drives = get_all_drives()  # Automatically detect available drives

    print("Searching drives:", drives)
    for drive in drives:
        for folder_name in user_folder_names:
            user_folder_path = os.path.join(drive, folder_name)
            print(f"Checking: {user_folder_path}")
            if os.path.exists(user_folder_path):
                print(f"Found user folder: {user_folder_path}")
                # List directories inside the Users/Usuarios folder
                try:
                    folders = os.listdir(user_folder_path)
                    for folder in folders:
                        folder_path = os.path.join(user_folder_path, folder)
                        if os.path.isdir(folder_path):
                            print(f"  User found: {folder}")
                            all_users.append(folder)
                except PermissionError:
                    print(f"  Cannot access folders in {user_folder_path}. Insufficient permissions.")
                break  # Exit loop once a valid user folder is found
        else:
            print(f"No user folder found in {drive}. Moving to the next drive...")

    # Display all users found at the end
    print("\n=== Summary of Users Found ===")
    if all_users:
        for user in all_users:
            print(f"  - {user}")
    else:
        print("No users were found in the detected drives.")
    
    return all_users

if __name__ == "__main__":
    users = search_user_folders()
