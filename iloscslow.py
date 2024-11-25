import re

path_to_file=r"D:\AGH\Informatyka\projekty\test.txt"
file=open(path_to_file, "r")
tekst=file.read()

dopasowanie=re.findall(r"[A-Za-z]+ ", tekst)
ilosc_zdan=len(dopasowanie)

print(ilosc_zdan)