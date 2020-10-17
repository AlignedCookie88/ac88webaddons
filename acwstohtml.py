import ac88web as wb
import yaml

filename = input("Website file: ")
outputf = input("Output file: ")
print("Reading...")
file = open(filename)
data = yaml.load(file, Loader=yaml.FullLoader)
file.close()
print("Converting...")
html = wb.compilecode(data["title"], data["body"], data["font"]).decode('utf-8')
print("Writing...")
file = open(outputf, mode="w+")
file.truncate(0)
file.write(html)
file.close()
print("Done!")
while True:
    pass
