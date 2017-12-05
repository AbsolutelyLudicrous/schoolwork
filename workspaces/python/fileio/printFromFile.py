from sys import argv

script, inputfile = argv
print("Script: ", script, "Input:", inputfile)

f = open(inputfile)
print(f.read())
