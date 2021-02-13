fopen = open("cedulaspace.txt", mode="r+", encoding="utf-8")

fread = fopen.readlines()


while 1 == 1:
    x = input("Nombre/s o cedula:").upper()
    if x.isdigit():
        for line in fread:
            if x in line:
                print(line)

    else:
        y = input("Apellido/s:").upper()
        for line in fread:

            if x in line and y in line:
                print(line)
