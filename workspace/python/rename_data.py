import requests
import os

def rename(folder_path: str):
    list_file = [name for name in os.listdir(folder_path) if name.endswith('.csv')]
    list_file.sort()
    for name in list_file:
        new_name = '_'.join(name.split('_')[-2:])
        os.rename(
            os.path.join(folder_path, name),
            os.path.join(folder_path, new_name)
        )

if __name__ == '__main__':
    rename('./data')