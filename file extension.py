filename= input("Enter the file name")
m=filename.split(".")
print(m[1])
if m[1]=='py':
    print("python")
if m[1]=='docx':
    print("word document")
if m[1]=="CRD":
    print("corel draw")


