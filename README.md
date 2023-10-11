# trabalho2
Este é o segundo trabalho da disciplina SEL0456 - Técnicas em Desenvolvimento de Software Livre. Este trabalho é uma classe para controle de usuario, com regras para nome de usuario (não pode haver caracteres especiais, por exemplo). Hash como password (o hash pode ser proveniente de alguma biblioteca. o password nao será guardado), "roles" (niveis de hierarquia): administrador, moderador, usuario, verificação do password (ver se a senha de entrada bate com o hash) e verificação da atribuição (nivel da hierarquia). A entrada será nome de usuario e senha.

O usuário pode possuir qualquer username e senha, sem caracteres especiais
O moderador possui username "mod" (sem aspas) e senha "senha456"
O administrador possui username "admin" e senha "senha789"

Para rodar o programa, execute:
``` shell
python3 ./controle_de_usuarios.py
```
