import shutil
import os


# shutil.copy2(r'D:\Ринат\Сканирование\part1.m3d', r'D:\Ринат\Сканирование\part2.m3d')


print(os.getcwd())

shutil.make_archive(r'D:\Ринат\Сканирование\newdir', 'zip', r'D:\Ринат\Сканирование\newdir')

# pathfile = r'D:\Ринат\Сканирование\newdir\part1.m3d'
pathfile = r'D:\Ринат'

print(os.path.getsize(pathfile))
print(os.path.getctime(pathfile))
print(os.path.getmtime(pathfile))

print(os.listdir(r'D:\Ринат\Оснастка\ИзвариноФарма'))