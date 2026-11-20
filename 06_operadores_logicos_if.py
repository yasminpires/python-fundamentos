# EXEMPLO 1 - IF + AND

idade = 20
tem_ingresso = True

if idade >= 18 and tem_ingresso:
    print("Entrada permitida!")
else:
    print("Entrada negada!")

# EXEMPLO 2 - IF + OR

idade = 25
estudante = True

if idade >= 60 or estudante:
    print("Você tem direito ao desconto!")
else:
    print("Você não tem direito ao desconto!")



# EXERCÍCIO 1 - CONTROLE DE ENTRADA

idade = 17
tem_autorizacao = True

# Se a idade for maior ou igual a 18 E tiver autorização:
# Mostre "Entrada permitida!""

#Senão:
# Mostre "Entrada negada!"

if idade >= 18 and tem_autorizacao:
    print("Entrada permitida!")
else:
    print("Entrada negada!")



# EXERCÍCIO 2 - DESCONTO PARA CLIENTES

idade = 25
estudante = True

# Se a idade for maior ou igual a 60 OU for estudante:
# Mostre "Você recebeu desconto!"

# Senão:
# Mostre "Você não tem direito ao desconto!"

if idade >= 60 or estudante:
    print("Você recebeu desconto!")
else:
    print("Você não tem direito ao desconto!")



# EXERCÍCIO 3 - ACESSO AO SISTEMA

idade = 16
senha_valida = False
administrador = True

# Se a idade for maior ou igual a 18 E a senha for válida:
# OU se for administrador:
# Mostre "Acesso autorizado!"

# Senão:
# Mostre "Acesso negado!"

if idade >= 18 and senha_valida or administrador:
    print("Acesso autorizado!")
else:
    print("Acesso negado!")



# EXEMPLO 3 - IF + NOT

tem_bloqueio = False

if not tem_bloqueio:
    print("Acesso permitido!")
else:
    print("Acesso bloqueado!")




# EXERCÍCIO 3 - VERIFICANDO DISPONIBILIDADE

esta_chovendo = False

# Se NÃO estiver chovendo:
# Mostre "Podemos sair!"

# Senão:
# Mostre "Melhor ficar em casa!"

if not esta_chovendo:
    print("Podemos sair!")
else:
    print("Melhor ficar em casa!")



# DESAFIO FINAL - SISTEMA DE ACESSO

idade = 17
tem_ingresso = False
convidado_vip = True
esta_bloqueado = False

# Se tiver 18 anos ou mais E possuir ingresso:
# OU se for convidado VIP E NÃO estiver bloqueado:
# Mostre "Entrada autorizada!"

# Senão:
# Mostre "Entrada negada!"

if idade >= 18 and tem_ingresso or convidado_vip and not esta_bloqueado:
    print("Entrada autorizada!")
else:
    print("Entrada negada!")