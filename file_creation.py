import os


cwd = os.getcwd()
dir_name = input("Enter Folder name : ")
path = os.path.join(cwd, dir_name)
os.mkdir(path)
os.chdir(path)
versionStart = int(input("Enter the version to start : "))
versionEnd = int(input("Enter the version to end : "))


def file_creation(version):
    filename = f"challenge{version}.py"
    file = open(filename, "a")
    file.write(f"# Welcome to the python challenges of version {version}.")
    file.close()


for i in range(versionStart, versionEnd + 1):
    file_creation(i)
    print(f"file created version : {i} ")
