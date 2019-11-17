from math import gcd


import os.path
import array

# Procedure qui doit etre modifiee pour que le systeme fonctionne
def get_masque_8bits(cle):
    masque = 255
    return masque & cle

# Procedure qui doit etre modifiee pour que le systeme fonctionne
def get_cle_modifiee(cle):
    nouvelle_cle = cle >> 8
    return nouvelle_cle

# Procedure qui doit etre modifiee pour que le systeme fonctionne
def chiffre_caractere(caractere,masque):
    nouveau_caractere = caractere ^ masque
    return nouveau_caractere

# Procedure qui doit etre modifiee pour que le systeme fonctionne
def mise_a_jour_cle(tmpcle,cle):
    if tmpcle==0:
        nouvelle_cle = cle
    else:
        nouvelle_cle = tmpcle
    return nouvelle_cle


# Methode de chiffrement / dechiffrement par flux
# La cle est utilisee pour chiffrer le fichier d'entree (fichierin) et produire le fichier de sortie (fichierout)
# Si la cle est plus petite que la taille du fichier, elle doit etre repetee (est-ce une bonne idee?)
def chiffre_flux(cle,fichierin,fichierout):
    tmpcle = cle
    
    # Initialisation des fichiers en lecture et ecriture
    infileobj = open(fichierin,'rb')     # Lecture binaire du fichier
    outfileobj = open(fichierout,'wb')   # Ecriture binaire du fichier
    filesize = os.path.getsize(fichierin)
    
    # Initialisation des tableaux binaires, lecture du fichier d'entree (binaire)
    inbinvalues = array.array('B')
    inbinvalues.fromfile(infileobj, filesize)
    outbinvalues = array.array('B')
    
    # Traitement de tous les caracteres du fichier d'entree, un a la fois
    i = 0
    while (i < filesize):
        # Obtention du masque pour le prochain caractere, chiffrement de ce caractere
        mask = get_masque_8bits(tmpcle)
        tmpcle = get_cle_modifiee(tmpcle)
        newchar = chiffre_caractere(inbinvalues[i], mask)
        # Ecriture du cactere chiffre dans le tampon de sortie
        outbinvalues.append(newchar)
        
        i += 1
        tmpcle = mise_a_jour_cle(tmpcle,cle)

    # Ecriture dans le fichier de sortie, fermeture des fichiers
    infileobj.close()
    outbinvalues.tofile(outfileobj)
    outfileobj.close()


def egcd(a, b):
    x, lastX = 0, 1
    y, lastY = 1, 0
    while (b != 0):
        q = a // b
        a, b = b, a % b
        x, lastX = lastX - q * x, x
        y, lastY = lastY - q * y, y
    return (lastX, lastY)


def phi(*args):
    res = 1
    for p in args:
        res *= (p-1)
    return res


def pollard_p_moins_1(n, maxi):
    m = 2
    for i in range(1, maxi):
        m = m ** i % n
        if gcd(n, m - 1) != 1:
            return gcd(n, m - 1)


def pollards_rho(n):
    x = 2
    y = 2
    d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x-y), n)
    if d != n:
        return d


def break_public_RSA_MM():
    n = 86062381025757488680496918738059554508315544797
    e = 13
    p = pollards_rho(n)
    print('{} = {} * {}'.format(n, p, n//p))

    p = (66405897020462343733, 600000787, 1200001573, 1800002359)
    phin = phi(*p)
    print('phi de n :', phin)

    (d, osef) = egcd(e, phin)
    d = (d + n) % n
    print('d :', d)
    return(n, d)


def break_RSA_encrypts_DH():
    n = 71632723108922042565754944705405938190163585182073827738737257362015607916694427702407539315166426071602596601779609881448209515844638662529498857637473895727439924386515509746946997356908229763669590304560652312325131017845440601438692992657035378159812499525148161871071841049058092385268270673367938496513
    e = 1009
    p = pollard_p_moins_1(n, n)
    print('{} = {} * {}'.format(n, p, n//p))

    q = (p, n//p)
    phin = phi(*q)
    print('phi de n :', phin)

    (d, osef) = egcd(e, phin)
    d = (d + phin) % phin
    print('d :', d)
    return (n, d)



def get_qpg_DH():
    #(n, d) = break_RSA_encrypts_DH()
    (n, d) = (71632723108922042565754944705405938190163585182073827738737257362015607916694427702407539315166426071602596601779609881448209515844638662529498857637473895727439924386515509746946997356908229763669590304560652312325131017845440601438692992657035378159812499525148161871071841049058092385268270673367938496513,
    68154027933166660914890730344092864878649198983935455529422960423721490188331665603876350587274300325806236608234316636462122036878942632337283353153592541640319773342392893703531066563494763814398430222694200307505853252489959059416692855383645323370594713153758488784999568103148728933198795871416131541009)
    
    DH = [70785482415899901219256855373079758876285923471951840038722877622097582944768442919300478197733262514534911901131859013939654902078384994979880540719293485131574905521151256806126737353610928922434810670654618891838295876181905553857594653764136067479449117470741836721372149447795646290103141292761424726007,
    55044587110698448189468021909149190373421069219506981148292634221985403129928367209713497911359302701069378532959510957622709061077384648566361893749771744973388835727259855002207844685526295296408852878202498675158924213264474587673461598376054133832370354928763624202425050121409987087150490459351809040858,
    43089172300844684958445369204000423742543038862350925279569289644298734265625491619486408239703259462606739540181409010715678916496299388069246398890469779970287613357772582024703107603034996120914490203805569384580718393586094166173301167583379300330660182750028000520221960355249560831414918130647224546308]
    
    pc=DH[1]
    p = pow(pc, d, n)
    print(p)
    
    gc=DH[2]
    g = pow(gc, d, n)
    print(g)
    return (p,g)


def break_AES():
    p,g=get_qpg_DH()
    print(p,g)
    k = pow(g,1,p)
    msg = chiffre_flux(k,"salaires.mm","salairedecode.txt")


def break_RSA_salaire():
    mon_fichier = open("salairedecode.txt", "r")
    
    lines = []
    for line in mon_fichier:
        lines.append(line.rstrip('\n').replace('\t',''))
        
    for line in lines[:-3]:
        print(line)
        
    print()
    print()
    fichierout = open("salairedecodeFINAL.txt", "w+")
    
    n, d = break_public_RSA_MM()
    for line in lines[:-3]:
        namefct,code=line.split(':')
        name,fct=namefct.split(',')
        code=int(code)
        salaire=pow(code,d,n)
        print(name,',',fct,',',salaire)
        fichierout.write(name+','+fct+','+str(salaire)+'\n')
        
    mon_fichier.close()
    fichierout.close()

     


break_RSA_salaire()
