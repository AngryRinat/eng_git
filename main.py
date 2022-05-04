import os
from datetime import datetime
import shutil
import time

folder_path = r'd:\files'

current_date = time.time()
# current_date = datetime.now().date()

def get_subfolder_paths_list() -> list:
    subfolder_paths = [sp.path for sp in os.scandir(folder_path) if sp.is_dir()]

    return subfolder_paths

def get_file_paths_list() -> list:
    file_paths = [fp.path for fp in os.scandir(folder_path) if not fp.is_dir()]
    print(len(file_paths))
    for f in file_paths:
        t_unix = os.path.getctime(f)
        print(f)
        # print(t_unix)
        # print(datetime.fromtimestamp(t_unix))
        # print(os.path.getsize(f))
        shutil.copy2(f, str (r'd:\files\files_new' + '1'))
    return file_paths

# print(current_date)


get_file_paths_list()

