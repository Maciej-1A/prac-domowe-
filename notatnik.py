
def notatnik():
    file_name = input("> Podaj nazwę notatki :3 : ")
    file_name = file_name + ".txt"
    while True:
        content = input("> podaj coski ktore maja byc w notatce (wpisz kys aby zakończyć): ")
        
        if content.lower() == 'kys':
            break
        with open(file_name, 'a') as plik:
            plik.writelines(content + '\n')
notatnik()

