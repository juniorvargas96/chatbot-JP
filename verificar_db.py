import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect("database.sqlite3")
cursor = conn.cursor()

# Verificar registros na tabela
cursor.execute("SELECT * FROM statement")
resultados = cursor.fetchall()

# Exibir os dados armazenados
print("Registros no banco de dados:", resultados)

# Fechar conexão
conn.close()
