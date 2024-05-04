import math
import random
import time
class femblem(object):
    
    def __init__(self,lv,name):
        self.lv = lv
        self.name = name
        self.wins = 0
        self.hit = 100
        self.evd = 10
        self.evdMtr=0
        self.crithit = 0
        self.critevd = 0
        self.dodgeCnt =0
        self.critCnt =0
        self.wpnCrit = 0
        
    def j(self):
        name = "Joshua"
        self.hp = 21
        self.mt = 7
        self.skl =11
        self.spd = 12
        self.lck = 6
        self.df = 5
        self.res = 2
        self.con = 8
        self.hpGr = .80 * (self.lv-1)
        self.mtGr = .35 * (self.lv-1)
        self.sklGr = .55 * (self.lv-1)
        self.spdGr = .55 * (self.lv-1)
        self.lckGr = .3 * (self.lv-1)
        self.dfGr = .20 * (self.lv-1)
        self.resGr = .20 * (self.lv-1)
        self.wpnTri= "sword"
        self.wpnMt = 5
        self.wpnacc = 80
        self.wmpWt = 3
        #print("owo")
       
        
    def chrom(self):
        self.name = "Chrom"
        self.hp = 20
        self.mt = 7
        self.skl =8
        self.spd = 8
        self.lck = 5
        self.df = 7
        self.res = 1
        self.con = 8
        self.hpGr = (85 * (self.lv-1) / 100)
        self.mtGr = 60 * (self.lv-1) /100
        self.sklGr = 60 * (self.lv-1) /100
        self.spdGr = 60 * (self.lv-1) /100
        self.lckGr = 70 * (self.lv-1) /100
        self.dfGr = 45 * (self.lv-1) /100
        self.resGr = 25 * (self.lv-1) /100
        self.wpnTri= "sword"
        self.wpnMt = 5
        self.wpnacc = 80 #slv swrd acc, change?
        self.wmpWt = 3
        #print("owo")


    def gaius(self):
        self.name = "Gaius"
        self.hp = 19
        self.mt = 5
        self.skl =11
        self.spd = 13
        self.lck = 5
        self.df = 4
        self.res = 2
        self.con = 8
        self.hpGr = 85 * (self.lv-1) / 100
        self.mtGr = 60 * (self.lv-1) / 100 
        self.sklGr = 70 * (self.lv-1) / 100
        self.spdGr = 70 * (self.lv-1) / 100
        self.lckGr = 35 * (self.lv-1) / 100
        self.dfGr = 30 * (self.lv-1) / 100
        self.resGr = 20 * (self.lv-1) / 100
        self.wpnTri= "sword"
        self.wpnMt = 5
        self.wpnacc = 80
        self.wmpWt = 3
        #print("owo")

    def cordelia(self):
        self.name = "Cordelia"
        self.hp = 20
        self.mt = 6
        self.skl =10
        self.spd = 9
        self.lck = 6
        self.df = 5
        self.res = 6
        self.con = 8
        self.hpGr = 90 * (self.lv-1)/100
        self.mtGr = 60 * (self.lv-1)/100
        self.sklGr = 60 * (self.lv-1)/100
        self.spdGr = 60 * (self.lv-1)/100
        self.lckGr = 45 * (self.lv-1)/100
        self.dfGr = 45 * (self.lv-1)/100
        self.resGr = 35 * (self.lv-1)/100
        self.wpnTri= "spear"
        self.wpnMt = 6
        self.wpnacc = 80
        self.wmpWt = 3
        #print("owo")
        print(self.hpGr)

    def owain(self):
        self.name = "Owain"
        self.hp = 11 + 5
        self.mt = 5
        self.skl =6
        self.spd = 7
        self.lck = 10
        self.df = 7
        self.res = 6
        self.con = 8
        self.hpGr = 95 * (self.lv-1)/100
        self.mtGr = 60 * (self.lv-1)/100
        self.sklGr = 60 * (self.lv-1)/100
        self.spdGr = 70 * (self.lv-1)/100
        self.lckGr = 50 * (self.lv-1)/100
        self.dfGr = 35 * (self.lv-1)/100
        self.resGr = 35 * (self.lv-1)/100
        self.wpnTri= "sword"
        self.wpnMt = 5
        self.wpnacc = 80
        self.wmpWt = 3
        #print("owo")

    def panne(self):
        self.name = "Panne"
        self.hp = 23
        self.mt = 5
        self.skl =6
        self.spd = 7
        self.lck = 6
        self.df = 5
        self.res = 1
        self.con = 8
        self.hpGr = 100 * (self.lv-1)/100
        self.mtGr = 60 * (self.lv-1)/100
        self.sklGr = 70 * (self.lv-1)/100
        self.spdGr = 75 * (self.lv-1)/100
        self.lckGr = 40 * (self.lv-1)/100
        self.dfGr = 50 * (self.lv-1)/100
        self.resGr = 40 * (self.lv-1)/100
        self.wpnTri= "stone"
        self.wpnMt = 6
        self.wpnacc = 80
        self.wmpWt = 3

    def hector(self):
        self.name = "Hector"
        self.hp = 19
        self.mt = 7
        self.skl =4
        self.spd = 5
        self.lck = 3
        self.df = 8
        self.res = 0
        self.con = 13
        self.hpGr = 90 * (self.lv-1)/100
        self.mtGr = 60 * (self.lv-1)/100
        self.sklGr = 45 * (self.lv-1)/100
        self.spdGr = 35 * (self.lv-1)/100
        self.lckGr = 30 * (self.lv-1)/100
        self.dfGr = 50 * (self.lv-1)/100
        self.resGr = 25 * (self.lv-1)/100
        self.wpnTri= "axe"
        self.wpnMt = 6
        self.wpnacc = 75
        self.wmpWt = 3

    def marth(self):
        self.name = "Marth"
        self.hp = 18
        self.mt = 5
        self.skl =3
        self.spd = 7
        self.lck = 7
        self.df = 7
        self.res = 0
        self.con = 13
        self.hpGr = 90 * (self.lv-1)/100
        self.mtGr = 50 * (self.lv-1)/100
        self.sklGr = 40 * (self.lv-1)/100
        self.spdGr = 50 * (self.lv-1)/100
        self.lckGr = 70 * (self.lv-1)/100
        self.dfGr = 20 * (self.lv-1)/100
        self.resGr = 0 * (self.lv-1)/100
        self.wpnTri= "sword"
        self.wpnMt = 5
        self.wpnacc = 80
        self.wmpWt = 3

    def alm(self):
        self.name = "Alm"
        self.hp = 28
        self.mt = 10
        self.skl =7
        self.spd = 6
        self.lck = 7
        self.df = 5
        self.res = 4
        self.con = 13
        self.hpGr = 40 * (self.lv-1)/100
        self.mtGr = 50 * (self.lv-1)/100
        self.sklGr = 55 * (self.lv-1)/100
        self.spdGr = 45 * (self.lv-1)/100
        self.lckGr = 35 * (self.lv-1)/100
        self.dfGr = 50 * (self.lv-1)/100
        self.resGr = 0 * (self.lv-1)/100
        self.wpnTri= "sword"
        self.wpnMt = 5
        self.wpnacc = 80
        self.wmpWt = 3

    def kellam(self):
        self.name = "Kellam"
        self.hp = 17
        self.mt = 8
        self.skl =5
        self.spd = 4
        self.lck = 2
        self.df = 12
        self.res = 1
        self.con = 13
        self.hpGr = 100 * (self.lv-1)/100
        self.mtGr = 65 * (self.lv-1)/100
        self.sklGr = 55 * (self.lv-1)/100
        self.spdGr = 45 * (self.lv-1)/100
        self.lckGr = 35 * (self.lv-1)/100
        self.dfGr = 70 * (self.lv-1)/100
        self.resGr = 35 * (self.lv-1)/100
        self.wpnTri= "spear"
        self.wpnMt = 5
        self.wpnacc = 85
        self.wmpWt = 3

    def e1(self):
        self.name = "Edelgard"
        self.hp = 26
        self.mt = 13
        self.skl =5
        self.spd = 8
        self.lck = 5
        self.df = 6
        self.res = 4
        self.con = 8
        self.hpGr = .40 * (self.lv-1)
        self.mtGr = .55 * (self.lv-1)
        self.sklGr = .45 * (self.lv-1)
        self.spdGr = .40 * (self.lv-1)
        self.lckGr = .3 * (self.lv-1)
        self.dfGr = .35 * (self.lv-1)
        self.resGr = .35 * (self.lv-1)
        self.wpnTri= "axe"
        self.wpnMt = 5
        self.wpnacc = 80
        self.wmpWt = 3
        #print("owo")

    def e2(self):
        self.name = "Edelgard"
        self.hp = 26
        self.mt = 13
        self.skl =5
        self.spd = 8
        self.lck = 5
        self.df = 6
        self.res = 4
        self.con = 8
        self.hpGr = .80 * (self.lv-1)
        self.mtGr = .70 * (self.lv-1)
        self.sklGr = .45 * (self.lv-1)
        self.spdGr = .40 * (self.lv-1)
        self.lckGr = .3 * (self.lv-1)
        self.dfGr = .35 * (self.lv-1)
        self.resGr = .35 * (self.lv-1)
        self.wpnTri= "axe"
        self.wpnMt = 5
        self.wpnacc = 80
        self.wmpWt = 3
        #print("owo")

    def p1(self):
        self.name = "Petra"
        self.hp = 25
        self.mt = 9
        self.skl = 7
        self.spd = 10
        self.lck = 7
        self.df = 5
        self.res = 2
        self.con = 8
        self.hpGr = .45 * (self.lv-1)
        self.mtGr = .40 * (self.lv-1)
        self.sklGr = .5 * (self.lv-1)
        self.spdGr = .60 * (self.lv-1)
        self.lckGr = .45 * (self.lv-1)
        self.dfGr = .3 * (self.lv-1)
        self.resGr = .45 * (self.lv-1)
        self.wpnTri= "sword"
        self.wpnMt = 5
        self.wpnacc = 80
        self.wmpWt = 3
        #print("owo")

    def p2(self):
        self.name = "Petra"
        self.hp = 25
        self.mt = 9
        self.skl =7
        self.spd = 10
        self.lck = 7
        self.df = 5
        self.res = 2
        self.con = 8
        self.hpGr = .7 * (self.lv-1)
        self.mtGr = .5 * (self.lv-1)
        self.sklGr = .5 * (self.lv-1)
        self.spdGr = .70 * (self.lv-1)
        self.lckGr = .45 * (self.lv-1)
        self.dfGr = .3 * (self.lv-1)
        self.resGr = .45 * (self.lv-1)
        self.wpnTri= "sword"
        self.wpnMt = 5
        self.wpnacc = 80
        self.wmpWt = 3
        #print("owo")
        
    def dispatcher(self,action):
        d = {
            'joshua': self.j , 'chrom': self.chrom,'gaius': self.gaius, 'cordelia': self.cordelia, "owain": self.owain, "panne": self.panne,"hector": self.hector, "marth": self.marth,"alm": self.alm, "kellam": self.kellam,"petra": self.p1, "petrapromote": self.p2, 'ed': self.e1,"edpromote": self.e2
            }
        return d[action]

    def unitStats(self):
        #dont know how i got this formula self.acc =(self.skl*2) + self.lck + self.wpnacc
        self.hit = math.floor((self.skl*1.5) + (self.lck * .5) + self.wpnacc)
        self.evd =  math.floor((self.spd * 1.5) + (self.lck * .5))
        self.crithit = math.floor(self.skl / 2) + self.wpnCrit
        self.critevd = math.floor(self.lck)
        print("Name: %s"% self.name)
        print("HP: %d"% self.hp)
        print("Mt: %d"% self.mt)
        print("Skl: %d"% self.skl)
        print("Spd: %d"% self.spd)
        print("Lck: %d"% self.lck)
        print("Def: %d"% self.df)
        print("Res: %d"% self.res)
        print("Acc: %d"% self.hit)
        print("Evd: %d"% self.evd)

#end class
def wpnpick(unit,wpnGrabber):
    if (unit.wpnTri =="sword"):
        if(wpnGrabber == "iron"):
            unit.wpnMt = 5
            unit.wpnacc = 90
        if(wpnGrabber == "steel"):
            unit.wpnMt = 8
            unit.wpnacc = 85
        if(wpnGrabber == "silver"):
            unit.wpnMt = 11
            unit.wpnacc = 80       
        if(wpnGrabber == "killer"):
            unit.wpnMt = 6
            unit.wpnacc = 90
            unit.wpnCrit = 30   
    if (unit.wpnTri =="axe"):
        if(wpnGrabber == "iron"):
            unit.wpnMt = 7
            unit.wpnacc = 80
        if(wpnGrabber == "steel"):
            unit.wpnMt = 11
            unit.wpnacc = 70
        if(wpnGrabber == "silver"):
            unit.wpnMt = 15
            unit.wpnacc = 65       
        if(wpnGrabber == "killer"):
            unit.wpnMt = 8
            unit.wpnacc = 90
            unit.wpnCrit = 30
    if (unit.wpnTri =="lance"):
        if(wpnGrabber == "iron"):
            unit.wpnMt = 6
            unit.wpnacc = 85
        if(wpnGrabber == "steel"):
            unit.wpnMt = 9
            unit.wpnacc = 80
        if(wpnGrabber == "silver"):
            unit.wpnMt = 13
            unit.wpnacc = 75       
        if(wpnGrabber == "killer"):
            unit.wpnMt = 7
            unit.wpnacc = 85
            unit.wpnCrit = 30

def unit1Strike(unit1,unit2):
    dodge = False
    unit2.evdMtr = (100 - (unit1.hit - unit2.evd))
    #print(f"{unit2.name} evade chance {unit2.evdMtr}")
    rand = (random.randint(1,100) + random.randint(1,100))/2
    print (rand)
    #print(f"{unit1.crithit - unit2.critevd}")
    #print(rand)
    if(unit2.evdMtr >= rand):
        print("%s dodged"%unit2.name)
        unit2.dodgeCnt = unit2.dodgeCnt + 1
        dodge = True
        rand = (random.randint(1,100) + random.randint(1,100))/2
    #print (unit1.crithit - unit2.critevd)
    #print (rand)
    if (unit1.crithit - unit2.critevd+1 >= rand and dodge == False ):
        #print (f"Critnum{unit1.crithit} rand {rand}")
        print("OH! A CRITICAL HIT!")
        unit1.critCnt = unit1.critCnt + 1
        if((unit1.mt - unit2.df) > 0): 
            unit2.hp = (unit2.hp - (unit1.mt - unit2.df)*3)
            print(f"{unit2.name} takes {(unit1.mt-unit2.df)*3} dmg, hp is now {unit2.hp}")
        else:
            unit2.hp = (unit2.hp - 3)
            print(f"{unit2.name} takes 3 dmg, hp is now {unit2.hp}")
    elif (dodge == False):
        if ((unit1.mt - unit2.df) > 0): 
            unit2.hp = unit2.hp - (unit1.mt - unit2.df)
            print(f"{unit2.name} takes {unit1.mt-unit2.df} dmg, hp is now {unit2.hp}")
        else:
            unit2.hp = (unit2.hp - 1)
            print(f"{unit2.name} takes 1 dmg, hp is now {unit2.hp}")

def unit2Strike(unit1,unit2):
    dodge = False
    unit1.evdMtr = (100 - (unit2.hit - unit1.evd))
    #print(f"{unit1.name} evade chance {unit1.evdMtr}")
    rand = (random.randint(1,100) + random.randint(1,100))/2
    if(unit1.evdMtr >= rand):
        print("%s dodged"%unit1.name)
        unit1.dodgeCnt = unit1.dodgeCnt + 1
        dodge = True
    rand = (random.randint(1,100) + random.randint(1,100))/2
    if (unit2.crithit - unit1.critevd+1 >= rand and dodge == False ):
        print("OH! A CRITICAL HIT!")
        unit2.critCnt = unit2.critCnt + 1
        if((unit2.mt - unit1.df) > 0): 
            unit1.hp = (unit1.hp - (unit2.mt - unit1.df)*3)
            print(f"{unit1.name} takes {(unit2.mt-unit1.df)*3} dmg, hp is now {unit1.hp}")
        else:
            unit1.hp = (unit1.hp - 3)
            print(f"{unit1.name} takes 3 dmg, hp is now {unit1.hp}")
    elif (dodge == False):
        if((unit2.mt - unit1.df) > 0):
            unit1.hp = unit1.hp - (unit2.mt - unit1.df)
            print(f"{unit1.name} takes {unit2.mt-unit1.df} dmg, hp is now {unit1.hp}")
        else:
            unit1.hp = (unit1.hp - 1)
            print(f"{unit1.name} takes 1 dmg, hp is now {unit1.hp}")
#end functions
print("Fire emblem battle simulator")
time.sleep(1)
print("By Hoboayoyo")
time.sleep(2)
print("Pick your character, your options are:")
time.sleep(.5)
print("joshua, chrom, gaius,")
time.sleep(.5)
print ("cordelia, owain, panne,")
time.sleep(.5)
print ("hector, marth, alm and kellam.")
print("")
level = 1
action = 'marth'        
action = input('Character1: - ')
action = action.lower()   
level = int(input('Level: - '))
wpnGrabber = "" #helps declare it early
if(action != "panne"):
    wpnGrabber = (input('Pick weapon type : iron, steel, silver or killer.'))
unit1 = femblem(level,"joshua")
unit1.dispatcher(action)()
wpnpick(unit1,wpnGrabber)
unit1.hp = math.floor(unit1.hp+unit1.hpGr)
unit1.maxhp = unit1.hp
unit1.mt = math.floor(unit1.mt+unit1.mtGr + unit1.wpnMt)
unit1.skl = math.floor(unit1.skl+unit1.sklGr)
unit1.spd = math.floor(unit1.spd+unit1.spdGr)
unit1.lck = math.floor(unit1.lck+unit1.lckGr)
unit1.df = math.floor(unit1.df+unit1.dfGr)
unit1.res = math.floor(unit1.res+unit1.resGr)
print("")


level = 1
action = 'chrom'
action = input('Character2: - ')   
level = int(input('Level: - '))
action = action.lower()
if(action != "panne"):
    wpnGrabber = (input('Pick weapon type : iron, steel, silver or killer.'))
unit2 = femblem(level,"joshua")
unit2.dispatcher(action)()
wpnpick(unit2,wpnGrabber)
unit2.hp=math.floor(unit2.hp+unit2.hpGr)
unit2.maxhp=unit2.hp
unit2.mt = math.floor(unit2.mt+unit2.mtGr + unit2.wpnMt)
unit2.skl = math.floor(unit2.skl+unit2.sklGr)
unit2.spd = math.floor(unit2.spd+unit2.spdGr)
unit2.lck = math.floor(unit2.lck+unit2.lckGr)
unit2.df = math.floor(unit2.df+unit2.dfGr)
unit2.res = math.floor(unit2.res+unit2.resGr)


unit1.unitStats()
print(f"Crit {unit1.crithit - unit2.critevd}")
print("")
unit2.unitStats()
print(f"Crit {unit2.crithit}")
print("")
matches = int(input("how many rounds? - "))
critSwitch = input("enable crits? y/n - ")
if(critSwitch == "n"):
    unit1.crithit =0
    unit2.crithit =0
    unit2.critevd =0
    unit1.critevd = 0
input('As a reminder, each round will go twice, with the first unit going first and then the second unit going first.Press enter to start.')
x=0
while (x!= matches):
    turnCount = 0
    #unit1 strikes 1st
    print(f"{unit1.name} starting {x+1}.")
    while(unit1.hp >0 or unit2.hp > 0):
        unit1Strike(unit1,unit2)
        if(unit2.hp < 1):
            print(unit1.name + " wins")
            unit1.wins += 1
            break
        #unit 2 1st strike
        unit2Strike(unit1,unit2)
        if(unit1.hp < 1):
            print(unit2.name + " wins")
            unit2.wins += 1
            break
        #double hit check
        if(unit1.spd - 4 >= unit2.spd):
            print(f"{unit1.name} strikes again")
            unit1Strike(unit1,unit2)
        if(unit2.hp < 1):
            print(unit1.name + " wins")
            unit1.wins += 1
            break       
        if(unit2.spd - 4 >= unit1.spd):
            print(f"{unit2.name} strikes again")
            unit2Strike(unit1,unit2)
        if(unit1.hp < 1):
            print(unit2.name + " wins")
            unit2.wins += 1
            break        

        turnCount= turnCount + .5
        #print (turnCount)
        #unit 2 2nd strike  
        unit2Strike(unit1,unit2)
        if(unit1.hp < 1):
            print(unit2.name + " wins")
            unit2.wins += 1
            break
        #unit 1 2nd strike
        unit1Strike(unit1,unit2)
        if(unit2.hp < 1):
            print(unit1.name + " wins")
            unit1.wins += 1
            break
        #double hit check
        if(unit1.spd - 4 >= unit2.spd):
            print(f"{unit1.name} strikes again")
            unit1Strike(unit1,unit2)
        if(unit2.hp < 1):
            print(unit1.name + " wins")
            unit1.wins += 1
            break       
        if(unit2.spd - 4 >= unit1.spd):
            print(f"{unit2.name} strikes again")
            unit2Strike(unit1,unit2)
        if(unit1.hp < 1):
            print(unit2.name + " wins")
            unit2.wins += 1
            break            
        turnCount= turnCount + .5
        print (f"turn: {turnCount}")



    #2nd part of the round
    unit1.hp = unit1.maxhp
    unit2.hp = unit2.maxhp
    turnCount=0
    print("")
    print("")
    print(f"{unit2.name} starting {x+1}.")
    while(unit1.hp >0 or unit2.hp > 0):
        #unit 2 1st strike
        unit2Strike(unit1,unit2)
        if(unit1.hp < 1):
            print(unit2.name + " wins")
            unit2.wins += 1
            break
        #unit 1 1st strike
        unit1Strike(unit1,unit2)
        if(unit2.hp < 1):
            print(unit1.name + " wins")
            unit1.wins += 1
            break
        #double hit check
        if(unit1.spd - 4 >= unit2.spd):
            print(f"{unit1.name} strikes again")
            unit1Strike(unit1,unit2)
        if(unit2.hp < 1):
            print(unit1.name + " wins")
            unit1.wins += 1
            break       
        if(unit2.spd - 4 >= unit1.spd):
            print(f"{unit2.name} strikes again")
            unit2Strike(unit1,unit2)
        if(unit1.hp < 1):
            print(unit2.name + " wins")
            unit2.wins += 1
            break        

        turnCount= turnCount + .5
        #print (f"turn: {turnCount}")

        #unit 1 2nd strike
        unit1Strike(unit1,unit2)
        if(unit2.hp < 1):
            print(unit1.name + " wins")
            unit1.wins += 1
            break
        #unit 2 2nd strike
        unit2Strike(unit1,unit2)
        if(unit1.hp < 1):
            print(unit2.name + " wins")
            unit2.wins += 1
            break
                #double hit check
        if(unit1.spd - 4 >= unit2.spd):
            print(f"{unit1.name} strikes again")
            unit1Strike(unit1,unit2)
        if(unit2.hp < 1):
            print(unit1.name + " wins")
            unit1.wins += 1
            break       
        if(unit2.spd - 4 >= unit1.spd):
            print(f"{unit2.name} strikes again")
            unit2Strike(unit1,unit2)
        if(unit1.hp < 1):
            print(unit2.name + " wins")
            unit2.wins += 1
            break               
        turnCount= turnCount + .5
        print (f"turn: {turnCount}")
    x=x+1
print("")
print (f"{unit1.name} wins: {unit1.wins}")
print (f"{unit2.name} wins: {unit2.wins}")
print(f"{unit1.name} crited {unit1.critCnt} times and  dodged {unit1.dodgeCnt} times")
print(f"{unit2.name} crited {unit2.critCnt} times and dodged {unit2.dodgeCnt} times")