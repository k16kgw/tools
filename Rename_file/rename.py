import glob
import os

path = './*.pdf'
i = 1

# pdfファイルの取得
flist = glob.glob(path)
print('変更前')
print(flist)

# ファイル名の変更
for file in flist:
    re_file = file
    re_file = re_file.replace(';', '--')
    re_file = re_file.replace(' -', '-')
    re_file = re_file.replace('- ', '-')
    re_file = re_file.replace(' et al', ',etal')
    re_file = re_file.replace(',,', ',')
    re_file = re_file.replace(', ', ',')
    re_file = re_file.replace(' ', '_')
    os.rename(file, re_file)

print(file)