tekst="loremipsemsitdolor"
#sprawdzenie ile razy wystapiła literka
slownik={}

liczba=0
for literka in tekst:
    if literka not in slownik:
        slownik[literka]=1
    else:
        slownik[literka]=slownik[literka]+1
print(slownik)                