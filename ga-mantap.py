import random
import numpy as np

def chrom():
    X = []
    for i in range(8):
        X.append(random.randint(0,7))
    return X


def split_chrom(a_list):  #nilai X1 dan X2
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def encode_func(x, mx, mn):
    up = 0
    dn = 0
    for i in range(len(x)):
        up = (x[i]*10**-i) + up
        dn = (9*10**-i) + dn
    return mn + (((mx-mn)*up)/dn)


def encodechrom(x): #x = get chromosom
    g1,g2 = split_chrom(x)
    x1 = encode_func(g1, 3, -3)
    x2 = encode_func(g2, 2, -2)
    return x1,x2

def calc_func(x1,x2):
    return (4-2*(x1**2)+ (x1**4)/3) * (x1**2+x1*x2+(-4 + 4*(x2**2))*x2**2)



def fitness(chrm): #inputan berupa individu
    x1,x2 = encodechrom(chrm)
    f = calc_func(x1,x2)
    return 1/(f + 0.001)


def populesyen():
    pop = []
    for i in range(10): #banyak populasi = 10
        pop.append(chrom())
    return pop

def populesyen_fitness(pop): #inputan berupa populasi
    fit = []
    for i in range(len(pop)): 
        fit.append(fitness(pop[i]))

    print('       kromosom           |       fitness')
    print('--------------------------|------------------------')
    for j in range(len(pop)):
        print(pop[j],' | ', fit[j]) 
        
    return fit


def parent_sel(pop):  #tournament_selection, menghasilkan 2 indv sebagai parent
    best1 = []
    best2 = []

    for i in range(10):
        krom = pop[random.randint(0,9)]  #generate individu random dari 0-9 (karena ada 10 populasi)
        if len(best1)==0 or fitness(krom) > fitness(best1):
            best1 = krom

    for i in range(10):
        krom = pop[random.randint(0,9)]  #generate individu random dari 0-9 (karena ada 10 populasi)
        if len(best2)==0 or fitness(krom) > fitness(best2) and krom != best1: #cari best2 tapi != best1
            best2 = krom

    return best1,best2


def crossover(p1,p2):
    tipot = random.randint(0,7)
    for i in range(tipot, 8):
        temp = p1[i]
        p1[i] = p2[i]
        p2[i] = temp
    return p1,p2 #child baru

def mutation(c1,c2):
    timut = random.randint(0,7) #titik mutasi
    

#-------------------------------------------------MAIN_PROG-------------------------------------------------#


pop = populesyen()
populesyen_fitness(pop)
best1,best2 = parent_sel(pop)
print("best parent : ",best1, best2)
print("hasil cross :",crossover(best1,best2))
