#coding=UTF-8


'''
PARA PROBLEMAS COM CODIFICAÇÃO COMO, P.EX., ASCII, LATIN-1, UTF-8, EM PYTHON
https://www.python.org/dev/peps/pep-0263/
Without encoding comment, Python's parser will assume ASCII text
'''


#isto é uma lista comum, com colchetes, ou seja, uma lista aberta
tipos_convites_lista = ['vip', 'normal', 'meia', 'cortesia'];
tipos_convites_lista.append('penetra');
print(tipos_convites_lista);


#isto(t é uma Tuple, ou seja, uma lista fechada
tipos_convites_tuple = ('vip', 'normal', 'meia', 'cortesia');

'''
para Tuples a função append não pode ser utilizada
ou seja, não podemos adicionar elementos a lista pois ela é fechada
a operação abaixo é proibida num tuple

tipos_convites.append('penetra'); 
'''
print(tipos_convites_tuple[0:2]);



'''
Exemplo de estrutura de dados do tipo DICTIONARY, 
que guarda chaves juntamente com seu valor
Seria praticamente como uma Collection do Java do tipo Map ou HashMap
com uma chave (key) e seu respectivo valor (value).

'''

convites_com_valores = {'vip' : 60 , 'normal' : 40 , 'meia': 30 , 'cortesia':0};

print(convites_com_valores);

print(convites_com_valores['vip']);
print(convites_com_valores['meia']);

#ALTERANDO O VALOR COM BASE NA CHAVE:
convites_com_valores['vip']=80;
convites_com_valores['meia']=40;

print(convites_com_valores['vip']);
print(convites_com_valores['meia']);

'''
print(convites_com_valores[0:1]);
TypeError: unhashable type: 'slice'

print(convites_com_valores[0:1]);
print(convites_com_valores[2:3]);

'''
'''
Sets
Sets are containers that hold unordered data values, 
they cannot contain duplicate values, and they are not indexable. 
This means that the x y notation does not work with a set. 
You must use built in set functions in order to work with a set.
'''


# Define list with a duplicate
positions = ['center','wing','goalie','wing','defensemen'];
# Define a set from that list
myset = set(positions);
print(myset);


'''
Dictionaries

If you've ever worked with set, value pairs in another language then you've 
basically worked with Python dictionaries. These are containers that allow you
to store values in pairs, where you have a key:value notation. Keys must be
unique within any given dictionary, but values can be duplicates. 
As you can see from the examples below, dictionaries can be a 
very useful data container as they provide capabilities which are not available
in lists. You may use any data type you wish as a key as long as it is unique.
Strings and integers are most commonly used for keys, but you could also use a 
tuple since they are immutable. Let's see dictionaries in action...

'''


# Define dictionary
playerPositions = {'juneau':'center', 'nickels':'wing'};

# Add entry into dictionary
playerPositions['smith'] = 'defensemen';
print(playerPositions);

# Remove entry
del playerPositions['juneau'];
print(playerPositions);


# Test membership
#aqui a variável teste é um boolean
teste =  'nickels' in playerPositions;
print(teste);

# List keys
print playerPositions.keys();


'''
Iteration and Conditionals
For Loop:

The "for" loop in Python is just like the shorthand notation of a "for" loop 
which was introduced in Java 1.5. Quite simply, 
a "for" loop is used to iterate through a list of values as such:

'''
#exemplo de um foreach() do Java - iterando por uma lista
for position in playerPositions : print position;

for letter in 'EMMANUEL':
    print(letter);
    
    
listaCompras = ['banana', 'arroz', 'feijão', 'salada'];

for item in listaCompras:
    print item;



'''

If Statement:

No surprise here, the "if" statement evaluates a conditional to a True or False. 
If you want to perform several comparisons, you will follow the first 
"if" statement with an "elif", and the last evaluation should be "else". 
Let's look at the "if" statement in the example below.

'''
#convites_com_valores = {'vip' : 80 , 'normal' : 40 , 'meia': 40 , 'cortesia':0};

for convite in convites_com_valores: 
    print('VERIFICANDO O CONVITE %s COM VALOR = %s' %(convite, convites_com_valores[convite]));
    if convites_com_valores[convite] == 80 : print('Este convite é vip')
    elif convites_com_valores[convite] == 0 : print ('Este convite é uma cortesia')
    else: print('Este convite não é nem vip e nem cortesia');
    
    
'''    
While Statement:
As with other programming languages, the "while" statement will continue to 
loop until a defined condition is met.
'''

# Represent a team wellness report
players = 18
injuries = 1
print('TESTANDO A ESTRUTURA DE CONTROLE WHILE');
while players > 10:
    print('PLAYERS = %d  INJURIES= %d' %(players, injuries))
    players -= injuries
    if players < 13:
          print('Only %d players left, critical number' % players)
    elif players < 10:
          print('Need more players to make a team')
    else:
          print('Team is healthy');
