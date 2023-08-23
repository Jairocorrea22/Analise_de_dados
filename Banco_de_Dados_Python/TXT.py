import pyodbc
import csv

# Configurações de conexão local
server = 'localhost'  # Ou o nome da instância do SQL Server local
database = 'seu_banco'  # Substitua pelo nome do banco que você criou
username = 'seu_usuario' 
password = 'sua_senha'

# Estabelece a conexão
conn = pyodbc.connect(f"DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}")

# Cria um cursor
cursor = conn.cursor()

# Nome da tabela
table_name = 'ExemploTabela'

# Comando SQL para criar a tabela
create_table_query = f"""
    CREATE TABLE {table_name} (
        ID INT PRIMARY KEY,
        Nome VARCHAR(255),
        Idade INT
    )
"""

# Executa o comando de criação da tabela
cursor.execute(create_table_query)
conn.commit()

# Lê dados do arquivo CSV e insere na tabela
csv_file_path = 'caminho_do_arquivo.csv'  # Substitua pelo caminho do seu arquivo CSV
with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Pula a linha de cabeçalho
    for row in csvreader:
        insert_query = f"INSERT INTO {table_name} (ID, Nome, Idade) VALUES (?, ?, ?)"
        cursor.execute(insert_query, row)
        conn.commit()

# Encerra a conexão
cursor.close()
conn.close()

print(f"Tabela '{table_name}' criada e populada com sucesso a partir do arquivo CSV.")