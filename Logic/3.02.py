while True:  
    
    nomeUsuario = input('Usuario: ')
    senhaUsuario = input('Senha: ')   
    
    if nomeUsuario != senhaUsuario:
        print('Login efetuado!')
        break
    else:
        print('Erro! Não e possivel que a senha seja o mesmo que nome de usuario')
        