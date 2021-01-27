####  add some line in harry.txt file and readline() function use ####

# f=open("harry.txt")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

###################   using tell() function ################
#
# f=open("harry.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# f.close()
################# using seek() function but takeing with argument #################

# f=open("harry.txt")
# f.seek(5)                  ############ seek() function use -- same line print again
# print(f.tell())           ############ tell() function use --- current time where is my file pointer "f" show the no
# print(f.readline())
#
# print(f.readline())
# f.close()