import os
import shutil
import time

def copy_or_cut_files(base_dir, dest_dir, operation):
    print(dest_dir)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            source_path = os.path.join(root, file)
            dest_path = os.path.join(dest_dir, file)
            print(source_path)
            try:
                start_time = time.time()

                if operation.lower() == 'copy':
                    shutil.copy(source_path, dest_path)
                    print(f"Copied: {source_path} to {dest_path}")
                elif operation.lower() == 'cut':
                    # shutil.move(source_path, dest_path)
                    shutil.copy(source_path, dest_path)
                    os.remove(source_path)
                    print(f"Cut: {source_path} to {dest_path}")
                else:
                    print("Invalid operation. Please choose 'copy' or 'cut'.")
                    return
                end_time = time.time()
                elapsed_time = end_time - start_time

                if elapsed_time > 7:
                    print(f"Skipped: {source_path} - Took longer than 10 seconds to {operation}")
                    continue

            except Exception as e:
                print(source_path, 'didnt work')
                print(f"Error processing {source_path}: {str(e)}")

    print(f"All files {operation} to {dest_dir}")

if __name__ == "__main__":
    default = input("enter if default or not 1/0")
    if not default:
        base_directory = input("Enter the base directory path: ")
        destination_directory = input("Enter the destination directory path: ")

    else:
        base_directory = r"F:\DCIM\Camera"
        destination_directory = r"C:\Users\raf-k\Desktop\DCIM\Camera" #r"C:\Users\raf-k\Desktop\test\output"

    operation = input("Do you want to copy or cut? (copy/cut): ")

    copy_or_cut_files(base_directory, destination_directory, operation)


