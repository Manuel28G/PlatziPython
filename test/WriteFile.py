

def wirteFile():
    with open('numeros.txt','w') as f:
        for i in range(0,9):
            f.write(str(i))


def readFile():
    counter = 0
    with open('aleph.txt') as f:
        for line in f:
            counter += line.lower().count("beatriz")

        print("Beatriz se encuentra {} veces en el cuento".format(counter))

def appendFile():
    with open("numeros.txt","a") as f:
        f.write("Agregando frase final.")
        pass

if __name__ == '__main__':
    appendFile()