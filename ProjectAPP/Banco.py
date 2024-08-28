import sqlite3

class Banco():
    def _init_(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists tbl_usuarios(
        idusuario interger primary key autoincrement,
        nome text,
        telefone text,
        email text,
        usuario text,
        senha text)""")
        self.conexao.commit()
        c.close()

        c.execute("""create table if not exists tbl_cidade(
        idcidade interger primary key autoincrement,
        codigo text,
        nome text,
        UF text)""")
        self.conexao.commit()
        c.close()

        c.execute("""create table if not exists tbl_clientes(
        idclientes interger primary key autoincrement,
        cli_codigo text,
        cli_nome text,
        cli_endereco text,
        cli_telefone text,
        cli_email text,
        cli_cid interger,
        FOREIGN KEY (cli_cid) REFERENCES tbl_cidades(idcidade))""")
        self.conexao.commit()
        c.close()