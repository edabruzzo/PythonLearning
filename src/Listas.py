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


