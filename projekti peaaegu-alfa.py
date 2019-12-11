def loe_vihjed_sisse(failinimi = 'algne.txt'):
    fail=open(failinimi, encoding="UTF-8")
    järjend=[]
    for rida in fail:
        järjend.append(rida.strip())
    fail.close()
    vihjed=[[],[]]
    reavahetus=järjend.index("")
    for indeks in range(len(järjend)):
        if len(järjend[indeks])==1:
            if indeks<reavahetus:
                vihjed[0].append([int(järjend[indeks])])
            elif indeks>reavahetus:
                vihjed[1].append([int(järjend[indeks])])
        else:
            if indeks<reavahetus:
                abijärjend=[]
                for täht in järjend[indeks]:
                    if täht.isnumeric():
                        abijärjend.append(int(täht))
                vihjed[0].append(abijärjend)
            elif indeks>reavahetus:
                abijärjend=[]
                for täht in järjend[indeks]:
                    if täht.isnumeric():
                        abijärjend.append(int(täht))
                vihjed[1].append(abijärjend)
    return vihjed 

pilt = []
vihjed = loe_vihjed_sisse()
print(vihjed)
for rida in range(len(vihjed[0])):
    pilt.append([])
    for veerg in range(len(vihjed[1])):
        pilt[rida].append(0)

def tee_toorik(vihjed, pilt):
    reanr = 0
    for rida in vihjed[0]:
        abiloendur = 0
        i = 0
        for vihje in rida:
            for j in range(vihje):
                pilt[reanr][i + j] = 1
                abiloendur += 1
            i += abiloendur + 1
        reanr += 1
    return pilt

def veeru_kontroll(indeks, pilt):
    veerg = []
    pikkused = []
    global vihjed
    veeru_vihjed = vihjed[1][indeks]
    for rida in pilt:
        veerg.append(rida[indeks])
    if sum(veerg) != sum(veeru_vihjed):
        return False
    indeks = 0
    i = 0
    while indeks < len(veerg):
        if veerg[indeks] == 1:
            pikkused.append(1)
            indeks += 1
            while 1:
                if veerg[indeks] == 1:
                    pikkused[i] = pikkused[i] + 1
                else:
                    i += 1
                indeks += 1


def prindi(pilt):
    valmis_pilt = ''
    for rida in pilt:
        for ruut in rida:
            if ruut == 1:
                valmis_pilt += u'\u2588'
            else:
                valmis_pilt += u'\u2591'
        valmis_pilt += '\n'
    print(valmis_pilt)

tee_toorik(vihjed, pilt)
for indeks1 in range(len(pilt[0])):
    veeru_kontroll(indeks1, pilt)
prindi(pilt)