# -*- coding: UTF-8 -*-

def register(names):
    print 'Type the name:'
    name = raw_input()
    names.append(name)

def list_names(names):
    print 'Printing names:'
    for name in names :
        print name

def remove(names):
    print 'Which name would you like to remove?'
    name = raw_input()
    names.remove(name)

def change(names):
    print 'Which name would you like to change?'
    name_to_change = raw_input()

    if(name_to_change in names):
        position = names.index(name_to_change)
        print 'Type the new name:'
        new_name = raw_input()
        names[posicao] = new_name

def search(names):
    print 'Type the name you would like to search:'
    name = raw_input()
    if(name in names):
        print 'Name %s is registered' % (name)
    else:
        print 'Name %s is not registered' % (name)

def find_regex(names):
    print('Type the regular expression')
    regex = raw_input()
    names_concat = ' '.join(names)
    results = re.findall(regex, names_concat)
    print(results)

def menu():
    names = []
    choice = ''
    while(choice != '0'):
        print 'Type your choice:'
        print '1: To register a new name'
        print '2: To list the names'
        print '3: To remove a name'
        print '4: To change a name'
        print '5: To search a name'
        print '0: To end the program'
        choice = raw_input()

        if(choice == '1'):
            register(names)

        if(choice == '2'):
            list_names(names)

        if(choice == '3'):
            remove(names)

        if(choice == '4'):
            change(names)

        if(choice == '5'):
            search(names)
menu()
