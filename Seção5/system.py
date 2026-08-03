print("=" * 40)
print(" Sistema de login")
print("=" * 40)

usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if not usuario or not senha:
    print("Erro: O nome de usuário e a senha não podem ser vazios.")
elif usuario == usuario_correto and senha == senha_correta:
    print("Login bem-sucedido!")
else:
    print("Erro: Senha ou usuário incorreto, tente novamente!")
