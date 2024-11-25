import re

path_to_file=r"test.txt"
file=open(path_to_file, "r")
tekst=file.read()

dopasowanie=re.findall("[A-Za-z]+[.!?].", tekst)
ilosc_zdan=len(dopasowanie)

#([A-Za-z]+\.)

print(ilosc_zdan)