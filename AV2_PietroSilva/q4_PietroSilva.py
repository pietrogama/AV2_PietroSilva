import mysql.connector
from mysql.connector import Error


conectar_bd = (lambda: mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="sua_base_de_dados"
))()


inserir_usuario = (lambda nome, console: (lambda conn: (
    (lambda cursor: cursor.execute(
        "INSERT INTO USUARIOS (nome, console) VALUES (%s, %s)",
        (nome, console))
    )(conn.cursor()),
    conn.commit()
))(conectar_bd))


inserir_jogo = (lambda nome, data_lancamento: (lambda conn: (
    (lambda cursor: cursor.execute(
        "INSERT INTO JOGOS (nome, data_lancamento) VALUES (%s, %s)",
        (nome, data_lancamento))
    )(conn.cursor()),
    conn.commit()
))(conectar_bd))


remover_usuario_por_id = (lambda usuario_id: (lambda conn: (
    (lambda cursor: cursor.execute(
        "DELETE FROM USUARIOS WHERE id = %s",
        (usuario_id,))
    )(conn.cursor()),
    conn.commit()
))(conectar_bd))


remover_jogo_por_id = (lambda jogo_id: (lambda conn: (
    (lambda cursor: cursor.execute(
        "DELETE FROM JOGOS WHERE id = %s",
        (jogo_id,))
    )(conn.cursor()),
    conn.commit()
))(conectar_bd))


consultar_usuarios = (lambda: (lambda conn: (
    (lambda cursor: (lambda rows: [row for row in rows])(cursor.fetchall()))(
        conn.cursor())
))(conectar_bd))


consultar_jogos = (lambda: (lambda conn: (
    (lambda cursor: (lambda rows: [row for row in rows])(cursor.fetchall()))(
        conn.cursor())
))(conectar_bd))


