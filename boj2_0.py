import random

class Rytir:
    
    def __init__(self, jmeno, HP, ATK, DEF, zbran):
        self.jmeno = jmeno
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.zbran = zbran
    
    def zautoc(self, protivnik):
        if random.randint(1,10) == 5:
            return self.ATK + 100
        elif self.zbran.DUR > 0:
            self.zbran.DUR -= 1
            return self.ATK + self.zbran.ATK - protivnik.DEF
        else:
            return self.ATK - protivnik.DEF      
    
    def __str__(self):
        return f"Jmeno: {self.jmeno}, HP: {self.HP}, durabilita zbrane: {self.zbran.DUR}"
    
    def superutok(self):
        if random.randint(1,10) == 5:
            return 1
        else:
            return 0
        
    def kradeni_zbrani(self):
        if random.randint(1,5) == 3:
            return 1
        else:
            return 0

class Lucistnik(Rytir):
    def __init__(self, jmeno, HP, ATK, DEF, zbran, pocet_sipu):
        super().__init__(jmeno, HP, ATK, DEF, zbran)
        self.pocet_sipu = pocet_sipu

    def zautoc(self, protivnik):
        if super().superutok == 1:
            return self.ATK + 100
        elif self.pocet_sipu > 0 and self.zbran.DUR > 0:
            self.zbran.DUR -= 1
            self.pocet_sipu -= 1
            return self.ATK + self.zbran.ATK - protivnik.DEF
        else:
            return self.ATK - protivnik.DEF

class Uklizecka(Rytir):
    def __init__(self, jmeno, HP, ATK, DEF, zbran, pocet_kostat):
        super().__init__(jmeno, HP, ATK, DEF, zbran)
        self.pocet_kostat = pocet_kostat

    def zautoc(self, protivnik):
        if super().superutok == 1:
            return self.ATK + 100
        elif self.pocet_kostat > 0 and self.zbran.DUR > 0:
            self.zbran.DUR -= 1
            self.pocet_kostat -= 1
            return self.ATK + self.zbran.ATK - protivnik.DEF
        else:
            return self.ATK - protivnik.DEF

class Alkoholik(Rytir):
    def __init__(self, jmeno, HP, ATK, DEF, zbran, pocet_lahvacu):
        super().__init__(jmeno, HP, ATK, DEF, zbran)
        self.pocet_lahvacu = pocet_lahvacu

    def zautoc(self, protivnik):
        if super().superutok == 1:
            return self.ATK + 100
        elif self.pocet_lahvacu > 0:
            self.pocet_lahvacu -= 1
            return self.ATK - ( protivnik.DEF - random.randint(1,4)*10 )
        else:
            return self.ATK - protivnik.DEF
        
class Cikan(Rytir):
    def __init__(self, jmeno, HP, ATK, DEF, zbran):
        super().__init__(jmeno, HP, ATK, DEF, zbran)
        
    def zautoc(self, protivnik):
        if super().superutok == 1:
            return self.ATK + 100
        elif super().kradeni_zbrani == 1:
            return self.ATK + protivnik.zbran.ATK - protivnik.DEF
        elif self.zbran.DUR > 0:
            return self.ATK + self.zbran.ATK - protivnik.DEF
        else:
            return self.ATK - protivnik.DEF
                    
class Prihlizejici:
    def __init__(self, jmeno, vaha):
        self.jmeno = jmeno
        self.vaha = vaha

    def __str__(self):
        return f"Přihlížející: Jméno: {self.jmeno}, váha: {self.vaha}"

    @property
    def vaha(self):
        if self.jmeno == "Karel":
            return "váhu radši ne"

class Zbran:
    
    def __init__(self, jmeno, ATK, DUR):
        self.jmeno = jmeno
        self.ATK = ATK
        self.DUR = DUR
        
class Turnaj:
    
    def __init__(self):
        self.seznam_rytiru = []
        self.seznam_bojovniku = []
    
    def registrace(self, rytir):
        self.seznam_rytiru.append(rytir)
    
    def duel(self):
        r1 = random.choice(self.seznam_rytiru)
        r2 = random.choice(self.seznam_rytiru)

        self.seznam_bojovniku.append(r1)
        self.seznam_bojovniku.append(r2)
        
        print("++++++++++++++++++++++++++")
        print("Bojovníci před zápasem:")
        print(r1)
        print(r2)
        print("++++++++++++++++++++++++++")

        while r1.HP >= 0 and r2.HP >= 0:
            r2.HP -= r1.zautoc(r2)
            r1.HP -= r2.zautoc(r1) 
            if r1.HP == 0 or r1.HP < 0:
                self.seznam_rytiru.remove(r1)
                self.seznam_bojovniku.remove(r1)
            elif r2.HP == 0 or r2.HP < 0:
                self.seznam_rytiru.remove(r2)
                self.seznam_bojovniku.remove(r2)
           
turnaj = Turnaj()

dragon_slayer = Zbran("Dragonslayer", 50, 5)
excalibur = Zbran("Excalibur", 32, 6)
luk = Zbran("Luk", 45, 10)
gbelik = Zbran("Kýbl", 55, 10)
xxx = Zbran("xxx",0,0)
zelezo = Zbran("ukradený železo", 30, 4)

guts = Rytir("Guts", HP=200, ATK=38, DEF=10, zbran=dragon_slayer)
griffith = Rytir("Griffith", HP=170, ATK=31, DEF=25, zbran=excalibur)
pepa = Lucistnik("Pepa", HP=160, ATK=28, DEF=15, zbran=luk, pocet_sipu=4)
hajzlbaba = Uklizecka("Hajzlbaba", HP=190, ATK=69, DEF=48, zbran=gbelik, pocet_kostat=2)
erik = Alkoholik("Erik", HP=170, ATK=32, DEF=22, zbran=xxx, pocet_lahvacu=3)
fero = Cikan("Fero", HP=165, ATK=27, DEF=11, zbran=zelezo)

karel = Prihlizejici("Karel", vaha = 158)

turnaj.registrace(guts)
turnaj.registrace(griffith)
turnaj.registrace(pepa)
turnaj.registrace(hajzlbaba)
turnaj.registrace(erik)
turnaj.registrace(fero)

turnaj.duel()
print("-------------")
print("Výherce:")
for bojovnik in turnaj.seznam_bojovniku:
    print(bojovnik)
print("-------------")

print(karel)