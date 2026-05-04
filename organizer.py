import os
import shutil

# 1. Define your base categories and their matching file extensions
CATEGORIES = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    "Documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
    "Code": ['.py', '.js', '.html', '.css', '.cpp', '.json'],
    "Archives": ['.zip', '.rar', '.tar', '.gz'],
    "Media": ['.mp3', '.mp4', '.mkv', '.wav']
}

def organize_directory(source_dir):
    # Check if the path actually exists
    if not os.path.exists(source_dir):
        print(f"Error: The directory '{source_dir}' does not exist.")
        return

    print(f"Scanning directory: {source_dir}...\n")
    
    # 2. Create the category folders if they don't exist yet
    for category in CATEGORIES.keys():
        folder_path = os.path.join(source_dir, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # 3. Iterate through every item in the folder
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        # Skip directories (we only want to move files)
        if os.path.isdir(file_path):
            continue
        
        # Extract the file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        
        moved = False
        
        # 4. Match the extension to a category and move the file
        for category, extensions in CATEGORIES.items():
            if ext in extensions:
                dest_path = os.path.join(source_dir, category, filename)
                
                # Handle filename collisions (if a file with that name already exists in the folder)
                if not os.path.exists(dest_path):
                    shutil.move(file_path, dest_path)
                    print(f"Moved: {filename}  -->  [{category}]")
                else:
                    print(f"Skipped: {filename} (Already exists in {category})")
                
                moved = True
                break
        
        # 5. THE AI HOOK: If the file extension doesn't match our hardcoded rules
        if not moved:
            print(f"Uncategorized: {filename} (This is where your AI API will take over!)")
            # TODO: Pass this filename and extension to OpenAI to dynamically create a folder

    print("\nOrganization Complete!")

# ==========================================
# TEST RUN
# ==========================================
if __name__ == "__main__":
    # WARNING: Test this on a DUMMY folder first, not your actual desktop!
    # Example: target_folder = r"C:\Users\YourName\Desktop\MessyFolder"
    
    target_folder = input("Enter the full path of the folder to organize: ")
    organize_directory(target_folder)