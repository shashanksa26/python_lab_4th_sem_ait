# gettting partial output:
import zipfile
import glob
with zipfile.ZipFile('sample.zip', 'w') as f:
    for file in glob.glob('my own/*'):
        f.write(file)
print("Directry created and files inserted into it")