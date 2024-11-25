import re

path_to_file=r"D:\AGH\Informatyka\projekty\test.txt"
file=open(path_to_file, "r")
tekst=file.read()

dopasowanie=re.findall("\\.", tekst)
ilosc_zdan=len(dopasowanie)

#([A-Za-z]+\.)

print(ilosc_zdan)