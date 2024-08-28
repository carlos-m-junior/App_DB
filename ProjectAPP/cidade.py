from Banco import Banco

class Cidades(object):
    def _init_(self, idcidade=0, nome="", uf=""):
        self.idcidade = idcidade
        self.nome = nome
        self.uf = uf

    def insertCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO tbl_cidades (nome, uf) VALUES (?, ?)",
                      (self.nome, self.uf))
            banco.conexao.commit()
            c.close()
            return "Cidade cadastrada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção da cidade: {e}"

    def updateCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE tbl_cidades SET nome = ?, uf = ? WHERE idcidade = ?",
                      (self.nome, self.uf, self.idcidade))
            banco.conexao.commit()
            c.close()
            return "Cidade atualizada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração da cidade: {e}"

    def deleteCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM tbl_cidades WHERE idcidade = ?", (self.idcidade,))
            banco.conexao.commit()
            c.close()
            return "Cidade excluída com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão da cidade: {e}"

    def selectCidade(self, idcidade):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_cidades WHERE idcidade = ?", (idcidade,))
            linha = c.fetchone()
            if linha:
                self.idcidade = linha[0]
                self.nome = linha[1]
                self.uf = linha[2]
            c.close()
            return "Busca feita com sucesso!" if linha else "Cidade não encontrada."
        except Exception as e:
            return f"Ocorreu um erro na busca da cidade: {e}"