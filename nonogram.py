def loe_nonogram_sisse(failinimi):
    fail=open(failinimi, encoding="UTF-8")
    järjend=[]
    for rida in fail:
        järjend.append(rida.strip())
    fail.close()
    nonogram=[[],[]]
    reavahetus=järjend.index("")
    for indeks in range(len(järjend)):
        if len(järjend[indeks])==1:
            if indeks<reavahetus:
                nonogram[0].append(int(järjend[indeks]))
            elif indeks>reavahetus:
                nonogram[1].append(int(järjend[indeks]))
        else:
            if indeks<reavahetus:
                abijärjend=[]
                for täht in järjend[indeks]:
                    if täht.isnumeric():
                        abijärjend.append(int(täht))
                nonogram[0].append(abijärjend)
            elif indeks>reavahetus:
                abijärjend=[]
                for täht in järjend[indeks]:
                    if täht.isnumeric():
                        abijärjend.append(int(täht))
                nonogram[1].append(abijärjend)
    return nonogram
pilt=[]
for rida in range(len(loe_nonogram_sisse("algne.txt")[1])):
    pilt.append([])
    for veerg in range(len(loe_nonogram_sisse("algne.txt")[0])):
        pilt[rida].append(" ")
for rida in pilt:
    print(rida)