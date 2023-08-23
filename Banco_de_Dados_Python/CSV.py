import pyodbc

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
        LinhaDeTexto VARCHAR(MAX)
    )
"""

# Executa o comando de criação da tabela
cursor.execute(create_table_query)
conn.commit()

# Lê dados do arquivo de texto e insere na tabela
txt_file_path = 'caminho_do_arquivo.txt'  # Substitua pelo caminho do seu arquivo de texto
with open(txt_file_path, 'r', encoding='utf-8') as txtfile:
    for line_id, line in enumerate(txtfile, start=1):
        insert_query = f"INSERT INTO {table_name} (ID, LinhaDeTexto) VALUES (?, ?)"
        cursor.execute(insert_query, (line_id, line.strip()))
        conn.commit()

# Encerra a conexão
cursor.close()
conn.close()

print(f"Tabela '{table_name}' criada e populada com sucesso a partir do arquivo de texto.")
