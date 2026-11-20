# EXEMPLO 1 - IF

idade = 20
if idade >= 18:
    print("Você é maior de idade!")



# EXEMPLO 2 - IF COM CONDIÇÃO FALSA

idade = 16

if idade >= 18:
    print("Você é maior de idade!")



# EXERCÍCIO 1 - VERIFICANDO IDADE

idade = 25

# Se a idade for maior ou igual a 18,
# mostre: "Acesso permitido!"

if idade>= 18:
    print("Acesso permitido!")



#EXEMPLO 3 - IF E ELSE

idade = 16

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")  



# EXERCÍCIO 2 - APROVADO OU REPROVADO 

nota = 6

# Se a nota for maior ou igual a 7:
# Mostre "Aprovado!"

#Senão:
#Mostre "Reprovado!"

if nota >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")   



# EXEMPLO 4 - IF, ELIF E ELSE

nota = 6

if nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação!")
else:        
    print("Reprovado!")



# EXERCÍCIO 3 - CLASSIFICANDO IDADES
 
idade = 15

# Se a idade for maior ou igual a 18: 
# Mostre "Maior de idade!"
 
# Senão se a idade for maior ou igual a 13:
# Mostre "Adolescente!"   

#Senão:
# Mostre "Criança!"

if idade >= 18:
    print("Maior de idade!")
elif idade >= 13:
    print("Adolescente!")
else:
    print("Criança!")



# DESAFIO 4 - SISTEMA DE NOTAS

nota = 8

# Se a nota for maior ou igual a 9:
# Mostre "Excelente!"

# Senão, se a nota for maior ou igual a 7:
# Mostre "Aprovado!"

# Senão, se a nota for maior ou igual a 5:
# Mostre "Recuperação!"

# Senão:
# Mostre "Reprovado!"

if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Aprovado!")
elif nota>= 5:
    print("Recuperação!")    
else:
    print("Reprovado!")    