import mysql.connector

# substitua os valores abaixo pelos detalhes da sua conexão MySQL
conexao = mysql.connector.connect(
    host="seu_host",
    user="seu_usuario",
    password="sua_senha",
    database="sua_base_de_dados"
)

cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS planilha
                (id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                idade INT NOT NULL);''')

def criar_aluno(nome, idade):
    cursor.execute("INSERT INTO planilha (nome, idade) VALUES (%s, %s);", (nome, idade))
    conexao.commit()
    print("Aluno registrado com sucesso.")

def listar_alunos():
    cursor.execute("SELECT * FROM planilha;")
    alunos = cursor.fetchall()
    for aluno in alunos:
        print(aluno)

def atualizar_aluno(id, novo_nome, nova_idade):
    cursor.execute("UPDATE planilha SET nome = %s, idade = %s WHERE id = %s;", (novo_nome, nova_idade, id))
    conexao.commit()
    print("Aluno atualizado com sucesso.")

def remover_aluno(id):
    cursor.execute("DELETE FROM planilha WHERE id = %s;", (id,))
    conexao.commit()
    print("Aluno removido com sucesso.")
