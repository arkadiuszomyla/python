filename = input("Enter filename: ")
print("The file name is: %s" % filename)

#filesize = input("Enter the max file size: ")
#print("The max size is %d" % (filesize))
#input to zawsze napis

while True:
    filesizeStr = input("Enter the max file size (MB): ")

    if filesizeStr.isdecimal():
        fileSizeInt = int(filesizeStr)
        break

print("the max sie in %d" % fileSizeInt)
print("Size in KB is %d" % fileSizeInt*1024)