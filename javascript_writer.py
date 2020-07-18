#city writer

year = str(2010)
file = open(year+".txt", "r")
entries = file.readlines()
output = "var data_"+ year +" = ["
for entry in entries:
    entry = entry.replace("\n", "")
    parts = entry.split(";")
    formatted = "new City(\""+parts[1]+"\","+parts[0]+","+parts[2]+","+parts[3]+","+parts[4]+"),"
    output = output + formatted
print(output + "]")

#city location writer

file = open("coords.txt", "r")
entries = file.readlines()
output = "["
for entry in entries:
    entry = entry.replace("\n", "")
    parts = entry.split(";")
    formatted = "new CityLocation(\""+parts[0]+"\","+parts[1]+","+parts[2]+"),"
    output = output + formatted
print(output + "]")
