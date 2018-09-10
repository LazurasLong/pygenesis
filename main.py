import os
import random as ra
import sys
from conf import c, w

def title():

    # The Title ASCII Menu because ASCII shit is cool... 
    print(c.title + """
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    + $$$$$$$             $$$$$$                                          $$               +
    + $$    $$           $$     $$                                                         +
    + $$    $$ $$     $$ $$          $$$$$$  $$$$$$$   $$$$$$    $$$$$$$  $$  $$$$$$$      +
    + $$$$$$$  $$     $$ $$   $$$$  $$    $$ $$    $$ $$    $$  $$        $$ $$            +
    + $$       $$     $$ $$      $$ $$$$$$$$ $$    $$ $$$$$$$$   $$$$$$   $$   $$$$$$      +
    + $$       $$     $$  $$     $$ $$       $$    $$ $$              $$  $$        $$     +
    + $$         $$$$$$$   $$$$$$    $$$$$$$ $$    $$  $$$$$$$  $$$$$$$   $$  $$$$$$$      +
    +                 $$                                                                   +
    +          $$     $$            for WarLite20 (c) Sean Mitchell 2018                   +     
    +            $$$$$$                                                                    +
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """ + c.clear)

def menu():    

    # The Actual Menu Options
    print(c.fair + """
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    + [1]: Generate Kingdom/Region                                    [5]: Generate Potion +
    + [2]: Generate City/Town/Village                                 [6]: Generate Tome   +
    + [3]: Generate NPC/Character                                     [7]: Generate Weapon +
    + [4]: Generate Inn/Tavern                                        [8]: Generate Armor  +
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """ + c.clear)

    # Defining some other objects as to pull more random shit from the list on conf
    r  = ra.choice
    
    # Random Variables for Name Generation with multi-suffix and for sirnames, multi-prefix
    p1 = ra.choice(w.pre)
    s1 = ra.choice(w.suf)
    p2 = ra.choice(w.pre)
    s2 = ra.choice(w.suf)
    s3 = ra.choice(w.suf)
    g1 = ra.choice(w.pre)
    g2 = ra.choice(w.suf)
    gnd = ['Male', 'Female']

    # Stats based off WarLite20 Rulebook(4d6 and the bonus is the total/2 rounded up)
    p_stats = ra.randint(1, 24)

    # The bonus stat is right now set to round down until I find a better way to handle this
    stats_b = p_stats // 2

    # Handles random names for Cities 
    cname = [p1+s1, p1+s1+s2, p1+s1+s2+s3]
    nname = [p1+s1, p1+s1+s2 + ' ' + p2+s3]
    gname = [g1+g2]
    population = [c.poor + 'Poor' + ' ' + str(ra.randint(50, 200)) + c.clear, c.fair + 'Fair'  + ' ' + str(ra.randint(200, 700)) + c.clear, c.rare + 'Good' + ' ' + str(ra.randint(700, 1500)) + c.clear, c.great + 'Great' + ' ' + str(ra.randint(1500, 20000)) + c.clear]
    regions = [c.title + 'Villages: ' + c.clear + str(ra.randint(1, 20)), c.title +'Cities: ' + c.clear + str(ra.randint(1, 20)), c.title + 'Towns: ' + c.clear + str(ra.randint(1, 20))]
    cvt = ['City: ', 'Village: ', 'Town: ']
    options = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # Prompted Input
    gen = input('Please select an option: ')
    
    # Generating a Kingdom with the following options (Name w/ Title, Description, Population, Market, Inns(total), Government)
    if gen == "1": 
        clear()
        print(c.title + 'Kingdom/Region:' + c.clear + ' ' + r(cname) + ' ' +  r(w.tit) + '\n' + c.title + 'Description:' + c.clear + ' ' + r(w.des) + '  ' + r(regions) + '   ' + c.title + 'Rule: ' + c.clear + r(w.gov))
        print(c.title + 'Beliefs: ' + c.clear + r(gname) + ' the ' + r(w.rel1) + ' of ' + r(w.rel2) + '   ' + c.title + 'Known For: ' + c.clear + r(w.mar))
    elif gen == "2":
        clear()
        print(c.title + r(cvt) + c.clear + r(cname) + '   ' + c.title + 'Description:' + c.clear + ' ' + r(w.des) + '\n' + c.title + 'Population: ' + c.clear + r(population) + '   ' + c.title + 'Crime: ' + r(w.cri) + '   ' + c.title + 'Known For: ' + c.clear + r(w.mar))
        print(c.title + 'Strange Events: ' + c.clear + r(w.vic) + ' ' + r(w.vic2) + ' ' + r(w.vic3) + ' has been ' + r(w.vic4) + ' ' + r(w.vic5) + ' ' + r(w.vic6) + ' the case is being handled by ' + r(w.vic7) + ' and are ' + r(w.vic8) + ' solving it, and are ' + r(w.vic9) + ' to share details.' + ' ' + r(w.vic10) + ' a connection to ' + r(w.vic11))
    elif gen == "3":
        clear()
        print(c.title + 'NPC Name: ' + c.clear + r(nname) + '    ' + c.title + 'Race: ' + c.clear + r(gnd) + ' ' + r(w.rac) + '    ' + c.title + 'Class: ' + c.clear + r(w.cla) + '\n' + c.title + 'STR: ' + c.clear + str(p_stats) + c.title + '  Mod: ' + c.clear + c.fair + ' +' + str(stats_b))
        print(c.title + 'Hostility: ' + c.clear + r(w.hos))
    elif gen not in options:
        clear()
        print(c.poor + "Please choose a valid option from the list below!" + c.clear)

    # Clear the screen when an option is selected
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

title()

while True:
    try:
        menu()
    except KeyboardInterrupt:
        sys.exit(0)
    else:
        menu()
