from fuzzysearch import find_near_matches
fopen = open("cedulaspace.txt", mode="r+", encoding="utf-8")
fread = fopen.readlines()


while 1 == 1:
        y = input("Nombre y Apellido:").upper()
        for line in fread:
                if find_near_matches(y, line, max_l_dist=1):
                        print(line)

