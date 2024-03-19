import os
import shutil

def organize_files(target_dir):
    for item in os.listdir(target_dir):
        if os.path.isfile(os.path.join(target_dir, item)):
            
            file_ext = item.split('.')[-1].lower()


            if file_ext in ['jpg', 'jpeg', 'png', 'gif']:
                dest_dir = os.path.join(target_dir, 'Images')
            elif file_ext in ['doc', 'docx', 'pdf', 'txt']:
                dest_dir = os.path.join(target_dir, 'Documents')
            elif file_ext in ['mp4', 'avi', 'mkv', 'mov']:
                dest_dir = os.path.join(target_dir, 'Videos')
            else:
                dest_dir = os.path.join(target_dir, 'Others')

            
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            
            shutil.move(os.path.join(target_dir, item), dest_dir)

if __name__ == "__main__":
    target_directory = "/path/to/your/target/directory"
    organize_files(target_directory)







