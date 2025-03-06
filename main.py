variaveis = {}

print("Bem vindo aocadastro de variáveis")
print("Você pode cadastrar quantas variáveis quiser. Digite 'sair' para finalizar")

while True:
    nome = input("Digite o nome da variável: ")
    
    if nome.lower() == 'sair':
        break
    
    valor = input(f"Digite o valor para {nome}: ")
    
    variaveis[nome] = valor
    
print("\nVariáveis cadastradas:")
for nome, valor in variaveis.items():
    print(f"{nome} = {valor}")
    
print("\nFim do Programa!")
