
cadastrar_usuario = (lambda: open("usuarios.txt", "a").write(input("Digite o login: ") + " " + input("Digite a senha: ") + "\n"))


fazer_login = (lambda: print("SUCESSO") if any((lambda login, senha: login + " " + senha)(input("Digite o login: "), input("Digite a senha: ")) in line for line in open("usuarios.txt")) else print("FRACASSO"))


opcoes = {
    "1": cadastrar_usuario,
    "2": fazer_login,
    "3": (lambda: None)  
}


while True:
    print("1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Sair")
    opcao = input("Escolha a opção: ")

   
    match opcao:
        case "1":
            opcoes["1"]()
        case "2":
            opcoes["2"]()
        case "3":
            opcoes["3"]()
        case _:
            print("Opção inválida. Tente novamente.")
