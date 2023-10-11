import bcrypt

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.role = 'Usuario'

    def verificar_senha(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)
    
    def permissoes(self):
        print('Esse usuário tem permissão de ler e escrever mensagens no chat')

class Moderador(Usuario):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.role = 'Moderador'

    def permissoes(self):
        print('Esse usuário tem permissão de apagar mensagens no chat')

class Administrador(Moderador):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.role = 'Administrador'

    def permissoes(self):
        print('Esse usuário tem permissão de banir membros no chat')

def login(usuarios,username,password):
    cadastrado = False
    for user in usuarios:
        if username == user.username:
            cadastrado = True
            if not user.verificar_senha(password):
                print('Senha incorreta')
                return None  
            return user

    if not cadastrado:
        print('Usuário não cadastrado')
        return None
    
user = Usuario('user', 'senha123')
mod = Moderador('mod', 'senha456') #username e password fixos para moderadores e administradores
admin = Administrador('admin', 'senha789')

usuarios=[user,mod,admin]
print('Você deseja se cadastrar ou logar?')
print('1 - Cadastrar')
print('2 - Logar')
cadastro = int(input())
if cadastro ==1:
    print('Criação de nova conta')  #Um novo usuário criado sempre terá a hierarquia de user
    print('Insira seu nome de usuário')
    username = input()
    print('Insira sua senha')
    password = input()
    novo_usuario = Usuario(username, password)
    usuarios.append(novo_usuario)
    cadastro=2      

if cadastro == 2:
    print('Login')
    print('Insira seu nome de usuário')
    username = input()
    print('Insira sua senha')
    password = input()
    current_user = login(usuarios, username, password)
    while current_user == None:
        # Input
        print('Insira seu nome de usuário')
        username = input()
        print('Insira sua senha')
        password = input()
        current_user = login(usuarios, username, password)
        
#O armazenamento de um novo usuário não é persistente
current_user.permissoes()

