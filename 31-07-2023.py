import os
def check(path):
    if not os.path.exists(path):
        print(f"{path} does not exist\n")
        return
    
    try:
        mode = os.stat(path).st_mode
        permissions = {
            'readable': bool(mode & 0o400),
            'writable': bool(mode & 0o200),
            'executable': bool(mode & 0o100)
        }

        print(f"File permissions for '{path}':")
        print(f"Readable: {permissions['readable']}")
        print(f"Writable: {permissions['writable']}")
        print(f"Executable: {permissions['executable']}")
        
    except OSError as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    check(input("Give a path: \n"))
    