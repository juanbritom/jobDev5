import math


def main():
    nome = 'Juan de Brito Lopes Martins'
    print(reverter(nome))

def reverter(str):
    buff=' '
    dif = 1
    for i in range(math.floor(len(str)/2)):
        str = list(str)
        buff=str[i]
        str[i] = str[len(str)-dif]
        str[len(str)-dif] = buff
        dif+=1

    return "".join(str)
    
        

if __name__ == "__main__":
    main()