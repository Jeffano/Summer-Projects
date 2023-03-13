from zipfile import ZipFile
import os

txtfile = 'randomtext.txt'

f = ZipFile('textcomp.zip', 'w')
f.write(txtfile)

folder = 'randomfolder'
fol = ZipFile('foldercomp.zip', 'w')
for root, dirs, files in os.walk(folder):
    for file in files:
        fol.write(os.path.join(root, file))
fol.close()
f.close()