# EXEMPLO 1 - OPERADOR AND

idade = 23

print(idade >=18 and idade <=30)

idade = 16

print(idade >= 18 and idade<=30)

# EXERCÍCIO 1 - OPERADOR AND

idade = 25
salario = 2000

# Verifique se a idade é maior que 18 E o salário é maior que 1500

# Verifique se a idade é menor que 18 E o salário é maior que 1500

print(idade >18 and salario>1500)
print(idade <18 and salario>1500)

# EXEMPLO 2 - OPERADOR OR

idade = 16

print(idade >= 18 or idade <= 16)

# EXERCÍCIO 2 - OPERADOR OR

idade = 17
tem_autorizacao = True

# Verifique se a idade é maior que 18 OU se tem autorização

# Verifique se a idade é maior que 18 OU se tem aultorização

print(idade >=18 or tem_autorizacao)
print(idade >18 or tem_autorizacao)

# EXEMPLO 3 - OPERADOR NOT

tem_autorizacao = True

print(not tem_autorizacao)

# EXERCÍCIO 3 - OPERADOR NOT

tem_carteira = True
esta_chovendo = False

# Inverta o valor de tem_carteira
# Inverta o valor de esta_chovendo

print(not tem_carteira)
print(not esta_chovendo)