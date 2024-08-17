"""file = open("file1.txt", "r")
print(file)
lineas = file.readlines()
print(lineas)"""

"""with open("file2.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(lineas.replace("\n", ""))"""

"""with open("file2.txt", "r") as i:
    contenido = i.read()
    lineas = contenido.split("\n")
    print(lineas)"""

with open("file3.txt", "a") as archivo:
    archivo.write("Oscar\nAlejandra\nPedro\n")
    