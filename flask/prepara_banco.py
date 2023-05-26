import mysql.connector
from mysql.connector import errorcode

print('Connecting ...')

try:

    conn = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'Tsubasa12'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Usuario ou senha invalida')
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")
cursor.execute("CREATE DATABASE `jogoteca`;")
cursor.execute("USE `jogoteca`;")

#Criando Tabelas

TABLES = {}
TABLES ['Jogos'] = ('''
        CREATE TABLE `jogos` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `nome` varchar(50) NOT NULL,
        `categoria` varchar(40) NOT NULL,
        `plataforma` varchar(20) NOT NULL,
        PRIMARY KEY (`id`)
        )ENGINE =InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_bin;
''')
TABLES ['Usuarios'] = ('''
        CREATE TABLE `usuarios` (
        `nome` varchar(20) NOT NULL,
        `nickname` varchar(8) NOT NULL,
        `senha` varchar(20) NOT NULL,
        PRIMARY KEY (`nickname`)
        )ENGINE =InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_bin;
''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
            print('Creating Table {}'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
             print('Já existe')
        else:
             print(err.msg)
    else:
         print('OK')

# inserindo usuarios

usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
    ('Taz Mania', 'taz', 'a12345'),
    ('Harry Potter', 'potter', 'b12345'),
    ('Marvin Marciano', 'marciano', 'c12345')
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from jogoteca.usuarios')
a= '-'*15
print(f'{a}Usuarios{a}')

for user in cursor.fetchall():
     print(user[1])

# inserindo Jogos

jogos_sql = 'INSERT INTO jogos (nome, categoria, plataforma) VALUES (%s, %s, %s)'
jogos = [
    ('Genshin', "MMORPG", "Multiplataform"),
    ('FF7', 'RPG', 'PS1'),
    ('God of War', 'Hack Slash', 'PS3')
]
cursor.executemany(jogos_sql, jogos)

cursor.execute('select * from jogoteca.jogos')
print(f'{a}Jogos{a}')

for jogo in cursor.fetchall():
     print(jogo[1])

# Commitando se não, nada tem efeito

conn.commit()

cursor.close()
conn.close()


