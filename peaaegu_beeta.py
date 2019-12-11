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
vihjed = loe_vihjed_sisse()

def permutatsioonid(väärtused,rida,vahe=0):
    if len(väärtused)>0 and väärtused[0]>0:
        praegune,*teised=väärtused
        for indeks in range(len(rida)-sum(teised)-len(teised)+1-praegune):
            if 1 not in rida[indeks:indeks+praegune]:
                for edasine in permutatsioonid(teised,rida[indeks+praegune+1:],1):
                    yield [1]*(indeks+vahe) + [2]*praegune + edasine
    else:
        yield []

def lahenda_rida(väärtused,rida):
    kehtivad_permutatsioonid=[]
    for permutatsioon in permutatsioonid(väärtused,rida):
        permutatsioon += [1]*(len(rida)-len(permutatsioon))
        for veerg in range(len(rida)):
            if rida[veerg]>0 and rida[veerg] != permutatsioon[veerg]:
                break
        else:
            kehtivad_permutatsioonid.append(permutatsioon)
    uus_rida=kehtivad_permutatsioonid[0]
    for permutatsioon in kehtivad_permutatsioonid[1:]:
        for indeks in range(len(uus_rida)):
            if uus_rida[indeks] != permutatsioon[indeks]:
                uus_rida[indeks]=0
    return uus_rida

def lahenda(rea_väärtused, veeru_väärtused, maatriks):
    muudetud = True
    while muudetud:
        muudetud = False
        for rea_indeks in range(len(rea_väärtused)):
            rida = lahenda_rida(rea_väärtused[rea_indeks], maatriks[rea_indeks])
            for veeru_indeks in range(len(rida)):
                if maatriks[rea_indeks][veeru_indeks] != rida[veeru_indeks]:
                    muudetud = True
                maatriks[rea_indeks][veeru_indeks] = rida[veeru_indeks]
                    
        for veeru_indeks in range(len(veeru_väärtused)):
            veerg = lahenda_rida(veeru_väärtused[veeru_indeks], [rida[veeru_indeks] for rida in maatriks])
            for rea_indeks in range(len(veerg)):
                if maatriks[rea_indeks][veeru_indeks] != veerg[rea_indeks]:
                    muudetud = True
                maatriks[rea_indeks][veeru_indeks] = veerg[rea_indeks]

def pildi_maatriks(vihjed):
    laius=len(vihjed[0])
    kõrgus=len(vihjed[1])
    veerud=vihjed[0]
    read=vihjed[1]
    maatriks = [[0]*laius for rida in range(kõrgus)]
    lahenda(read, veerud, maatriks)
    for rida in maatriks:
        if 0 in rida:
            print("Nonogram ei ole üheselt lahenduv!")
            return
        else:
            return maatriks

def prindi(pilt):
    if type(pilt)==list:
        valmis_pilt = ''
        for rida in pilt:
            for ruut in rida:
                if ruut == 1:
                    valmis_pilt += u'\u2588'
                else:
                    valmis_pilt += u'\u2591'
            valmis_pilt += '\n'
        print(valmis_pilt)

prindi(pildi_maatriks(vihjed))