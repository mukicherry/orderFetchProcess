import os
def walkFile(rootDir):
    fileList = []
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        # for d in dirs:
        #     print os.path.join(root, d)
        for f in files:
            fileList.append(os.path.join(root, f))
    return fileList