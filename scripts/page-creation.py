import os.path
import shutil

template = input("Enter the name of the template you want to use.")
project = input("Enter the name of the project.")

if os.path.exists("../projects/" + project) == False:
	os.makedirs("../projects/" + project)
	print("Creating folder [" + "../projects/" + project + ']')

print("Copying [" + "../templates/" + template + "] to [" + "../projects/" + project + "/" + project + ".html" + "]")
shutil.copyfile("../templates/" + template, "../projects/" + project + "/" + project + ".html")