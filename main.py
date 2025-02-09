import os

for i in range(149,200):
    filename = "file%d" %i
    f = open ("random_files/"+filename, "rb").read(3)
    if f == (b"\xff\xd8\xff"):
        os.rename("random_files/" + filename, "random_files/" + filename + ".jpg")
    else:
        os.remove("random_files/" + filename)