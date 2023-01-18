arr = {elem[0:elem.find(" ")]: elem[elem.find(" ")+1:len(elem)] for elem in open("text", "r", encoding="UTF-8").read().split("\n")}
print(arr)