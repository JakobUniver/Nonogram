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
        
read=loe_nonogram_sisse("algne.txt")[1]
veerud=loe_nonogram_sisse("algne.txt")[0]

sõne=""

for rida in range(len(pilt)):
    if type(read[rida])==int and read[rida]==len(pilt[rida]):
        sõne+=read[rida]*"*"
        for indeks in range(len(sõne)):
            pilt[rida][indeks]=sõne[indeks]
        sõne=""
    elif type(read[rida])==list and sum(read[rida])+len(read[rida])-1==len(pilt[rida]):
        for element in read[rida]:
            sõne+=element*"*"+" "
        sõne=sõne[0:-1]
        for indeks in range(len(sõne)):
            pilt[rida][indeks]=sõne[indeks]
        sõne=""

for veerg in range(len(pilt[0])):
    if type(veerud[veerg])==int and veerud[veerg]==len(pilt[veerg]):
        sõne+=veerud[veerg]*"*"
        for indeks in range(len(sõne)):
            pilt[indeks][veerg]=sõne[indeks]
        sõne=""
    elif type(veerud[veerg])==list and sum(veerud[veerg])+len(veerud[veerg])-1==len(pilt[veerg]):
        for element in veerud[veerg]:
            sõne+=element*"*"+" "
        sõne=sõne[0:-1]
        for indeks in range(len(sõne)):
            pilt[indeks][veerg]=sõne[indeks]
        sõne=""

for rida in pilt:
    print(rida)