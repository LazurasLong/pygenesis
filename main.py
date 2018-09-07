import os
import random as ra
import sys
from conf import c, w

def menu():
    print(c.title + """
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 $$$$$$$             $$$$$$                                          $$ 
 $$    $$           $$     $$                                       
 $$    $$ $$     $$ $$          $$$$$$  $$$$$$$   $$$$$$    $$$$$$$  $$  $$$$$$$
 $$$$$$$  $$     $$ $$   $$$$  $$    $$ $$    $$ $$    $$  $$        $$ $$     
 $$       $$     $$ $$      $$ $$$$$$$$ $$    $$ $$$$$$$$   $$$$$$   $$   $$$$$$
 $$       $$     $$  $$     $$ $$       $$    $$ $$              $$  $$        $$
 $$         $$$$$$$   $$$$$$    $$$$$$$ $$    $$  $$$$$$$  $$$$$$$   $$  $$$$$$$
                 $$ 
           $$    $$            for WarLite20 (c) Sean Mitchell 2018       
            $$$$$$                                                                 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""" + c.clear)
    print(c.fair + """
[1]: Generate Kingdom/Region                                      [5]: Generate Potion
[2]: Generate City/Town/Village                                   [6]: Generate Tome
[3]: Generate NPC/Character                                       [7]: Generate Weapon
[4]: Generate Random Item                                         [8]: Generate Armor
""" + c.clear)
    r  = ra.choice
    p2 = ra.choice(w.pre)
    s2 = ra.choice(w.suf)
    gen = input('Please select an option: ')
    if gen == "1":
        clear()
        pop()
        print(c.title + 'Kingdom or Region:' + c.clear + ' ' + r(w.pre) + r(w.suf) + '\n' + c.desc + 'Description:' + c.clear + ' ' + r(w.des))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pop():
    p = ra.choice(w.pop)
    if p == "Poor":
        print(c.poor + 'Population:' + c.clear + ' ' + p + ': ' + ra.randint(1, 100))
    if p == "Fair":
        print(c.fair + 'Population:' + c.clear + ' ' + p + ': ' + ra.randint(100, 500))
    if p == "Good":
        print(c.good + 'Population:' + c.clear + ' ' + p + ': ' + ra.randint(599, 1500))
    if p == "Great":
        print(c.great + 'Population:' + c.clear + ' ' + p + ': ' + ra.randint(2500, 20000))

while True:
    try:
        menu()
    except KeyboardInterrupt:
        print('\n')
        sys.exit(0)
