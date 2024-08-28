from Banco import Banco

class Clientes(object):
    def _init_(self, codigo=0, nome="", endereco="", fone="", cpf="", cid_codigo=0):
        self.info = {}
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.fone = fone
        self.cpf = cpf
        self.cid_codigo = cid_codigo

    def insertCliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO tbl_clientes (nome, endereco, fone, cpf, cid_codigo) VALUES ('" +
                      self.nome + "', '" +
                      self.endereco + "', '" +
                      self.fone + "', '" +
                      self.cpf + "', '" +
                      str(self.cid_codigo) + "')")
            banco.conexao.commit()
            c.close()
            return "Cliente cadastrado com sucesso!"
        except Exception as e:
            return "Ocorreu um erro na inserção do cliente: " + str(e)

    def updateCliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE tbl_clientes SET nome = '" + self.nome +
                      "', endereco = '" + self.endereco +
                      "', fone = '" + self.fone +
                      "', cpf = '" + self.cpf +
                      "', cid_codigo = '" + str(self.cid_codigo) +
                      "' WHERE codigo = " + str(self.codigo) + " ")
            banco.conexao.commit()
            c.close()
            return "Cliente atualizado com sucesso!"
        except Exception as e:
            return "Ocorreu um erro na alteração do cliente: " + str(e)

    def deleteCliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM tbl_clientes WHERE codigo = " + str(self.codigo) + " ")
            banco.conexao.commit()
            c.close()
            return "Cliente excluído com sucesso!"
        except Exception as e:
            return "Ocorreu um erro na exclusão do cliente: " + str(e)

    def selectCliente(self, codigo):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_clientes WHERE codigo = " + str(codigo) + " ")
            for linha in c:
                self.codigo = linha[0]
                self.nome = linha[1]
                self.endereco = linha[2]
                self.fone = linha[3]
                self.cpf = linha[4]
                self.cid_codigo = linha[5]
            c.close()
            return "Busca feita com sucesso!"
        except Exception as e:
            return "Ocorreu um erro na busca do cliente: " + str(e)