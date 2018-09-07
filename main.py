import os
import random as ra
import sys
from conf import c, w

def menu():

    #The Title ASCII Menu because ASCII shit is cool... 
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
    
    #The Actual Menu Options
    print(c.fair + """
[1]: Generate Kingdom/Region                                      [5]: Generate Potion
[2]: Generate City/Town/Village                                   [6]: Generate Tome
[3]: Generate NPC/Character                                       [7]: Generate Weapon
[4]: Generate Random Item                                         [8]: Generate Armor
""" + c.clear)

    #Defining some other objects as to pull more random shit from the list on conf
    r  = ra.choice
    p2 = ra.choice(w.pre)
    s2 = ra.choice(w.suf)
    
    #Prompted Input
    gen = input('Please select an option: ')
    
    #Generating a Kingdom with the following options (Name w/ Title, Description, Population, Market, Inns(total), Government)
    if gen == "1":
        clear()
        pop()
        print(c.title + 'Kingdom or Region:' + c.clear + ' ' + r(w.pre) + r(w.suf) + '\n' + c.desc + 'Description:' + c.clear + ' ' + r(w.des))

    #Clear the screen when an option is selected? This still bugs me and doesn't work quite right yet... I'm losing my mind.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
