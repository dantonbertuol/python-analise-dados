# Nomeando Variaveis | Exemplo 1
Laranja, Melão, Limão = 1, 2, 3
print(Laranja, Melão, Limão, '\n')

# Nomeando Variaveis | Exemplo 2
Morango = Uva = Kiwi = 100
print(Morango, Uva, Kiwi, '\n')

# Nomeando Variaveis | Exemplo 3
# Criando uma lista
Carros = ['VW', 'GM', 'Ford']

# Nomeando as variaveis com a lista
Marca_01, Marca_02, Marca_03 = Carros
print(Marca_03, '\n')

# Combinando Variaveis | Exemplo 1
Nome = 'Danton'
Sobrenome = 'Jose'
Nome_Completo = Nome + ' ' + Sobrenome
print(Nome_Completo, '\n')

# Combinando Variaveis | Exemplo 2
Dolar = 5.40
Imposto = 0.20
Valor_Liquido = Dolar - (Dolar * Imposto)
print(Valor_Liquido)

# Criando tipos de informações
String = str('Olá Mundo!')
Inteiro = int(10)
Flutuante = float(10.99)
Complex = complex(1j)
Lista = list(('Maça', 'Morango', 'Pera'))
Tupla = tuple(('Maça', 'Morango', 'Pera'))
Range = range(6)
Dicionario = dict(nome='Danton', age=29)
Set = set(('Maça', 'Morango', 'Pera'))
Fronzet = frozenset(('Maça', 'Morango', 'Pera'))
Boleano = bool(5)
Bytes = bytes(5)
ByteArray = bytearray(5)
Memoryview = memoryview(bytes(5))

""" Manipulação de String """
# Imprimindo uma string.
String = 'Olá Mundão!'

# Concatenação
print(String + ' Estou aprendendo Python...')

# Substitui uma substring por alguma outra coisa.
Substituir = String.replace('Mundão', 'Mundo Louco :X')
print(Substituir)

# A string s começa com "Olá"?
print(String.startswith('Olá'))

# A string termina com "mundo"?
print(String.endswith('mundo'))

# Quantas ocorrências da palavra "a" a string possui?
print(String.count('M'))

# Capitalize - Transformar a primeira letra da primeira palavra em maiúscula.
String_02 = 'odemir depieri'
print(String_02.capitalize())

# Verificar se uma string só possui números.
String_03 = '123456789'
String_04 = '123456789ABC'
print(String_03.isdigit())
print(String_04.isdigit())

# Verificar se uma string é alfanumérica (só possui letras e números).
print('12345abc'.isalnum())

# Transformar tudo em Maiusculo
print(String.upper())

# Transformar tudo em Minúsculo
print(String.lower())

# Procurar algo na string
print(String.find('!'))

# Removendo espaçoes antes e fim da palavra
String_05 = ' Olá Mundão! '
print(String_05.strip())

# Removendo espaçoes antes e fim da palavra
String_06 = 'Loja 1 vendou 10, Loja 2 vendou 20, Loja 3 vendou 30 '
print(String_06.split(','))

""" Operadores de Identidade """
String_01 = str('Olá Mundão')
String_02 = str('Olá Mundão')

print(String_01 is String_01)
print(String_01 is String_02)
print(String_01 == String_02)
print(type(String_01) is type(String_02))

""" Manipulação de Listas """
# Manipulando dados dentro das Lista
Lista_Vazia: list = []
print('Lista antes:', Lista_Vazia, '\n')

# Inserindo valores na Lista
Lista_Vazia.append(1)
Lista_Vazia.append(2)
Lista_Vazia.append(3)
print('Lista Depois:', Lista_Vazia, '\n')

# Tamanho da lista
print('Lista contém:', len(Lista_Vazia), 'elementos', '\n')

# Tamanho da lista
print('Acessando o 1º Elemento:', Lista_Vazia[0])
print('Acessando o 2º Elemento:', Lista_Vazia[1])
print('Acessando o último Elemento:', Lista_Vazia[-1])
print('Acessando um periodo:', Lista_Vazia[0:2], '\n')

# Excluindo valor na lista
del Lista_Vazia[1]
print('Depois da exclusão:', Lista_Vazia, '\n')

# Limpando a lista
Lista_Vazia.clear()
print('Depois da Limpeza:', Lista_Vazia, '\n')

# Inserindo um valor com uma posição
Lista_Inserir = ['Posição 1', 'Posição 2', 'Posição 3']
Lista_Inserir.insert(0, 'Posição 4')
print(Lista_Inserir, '\n')

# Inserindo uma lista na outra
Lista_Inserir_01 = ['Posição 1', 'Posição 2', 'Posição 3']
Lista_Inserir_02 = ['Posição 4', 'Posição 5', 'Posição 6']
Lista_Inserir_01.extend(Lista_Inserir_02)
print(Lista_Inserir_01, '\n')

# Removendo itens especifico pelo nome
Lista_Inserir_01.remove('Posição 6')
print(Lista_Inserir_01, '\n')

# Removendo itens pelo index
Lista_Inserir_01.pop(0)
print(Lista_Inserir_01, '\n')

# Ordenar uma lista
Lista_Alfabetica = ['Z', 'C', 'A', 'B', 'L']
Lista_Alfabetica.sort()
print(Lista_Alfabetica, '\n')

# Ordenar uma lista de forma inversa
Lista_Alfabetica.sort(reverse=True)
print(Lista_Alfabetica, '\n')

# Copiar uma Lista
Lista_Alfabetica_02 = Lista_Alfabetica.copy()
print(Lista_Alfabetica_02, '\n')

# Indetificar o Index do elemtno na lista
print(Lista_Alfabetica_02.index('L'), '\n')
