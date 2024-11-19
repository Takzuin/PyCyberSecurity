import os

get_all_drives = lambda: [f"{d}:\\" for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\")]
get_users_in_folder = lambda p: [f for f in os.listdir(p) if os.path.isdir(os.path.join(p, f))]

def find_user_folders():
    users = []
    for drive in get_all_drives():
        for folder in ['Users', 'Usuarios']:
            path = os.path.join(drive, folder)
            if os.path.exists(path):
                try:
                    users += get_users_in_folder(path)
                except PermissionError:
                    pass
                break
    print("\n=== Users Found ===\n" + "\n".join(users) if users else "No users found.")
    return users

if __name__ == "__main__":
    find_user_folders()
