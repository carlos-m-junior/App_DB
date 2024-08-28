from tkinter import *

from Banco import Banco

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Cidades")

        self.lblidcidade = Label(root, text="Código")
        self.lblidcidade.grid(row=0, column=0)
        self.txtidcidade = Entry(root)
        self.txtidcidade.grid(row=0, column=1)

        self.lblnomecidade = Label(root, text="Nome da Cidade")
        self.lblnomecidade.grid(row=1, column=0)
        self.txtnomecidade = Entry(root)
        self.txtnomecidade.grid(row=1, column=1)

        self.lbluf = Label(root, text="UF")
        self.lbluf.grid(row=2, column=0)
        self.txtuf = Entry(root)
        self.txtuf.grid(row=2, column=1)

        self.lblmsg = Label(root, text="")
        self.lblmsg.grid(row=3, column=0, columnspan=2)

        self.btnBuscar = Button(root, text="Buscar", command=self.buscarCidade)
        self.btnBuscar.grid(row=4, column=0)

        self.btnInsert = Button(root, text="Inserir", command=self.inserirCidade)
        self.btnInsert.grid(row=4, column=1)

        self.btnAlterar = Button(root, text="Alterar", command=self.alterarCidade)
        self.btnAlterar.grid(row=5, column=0)

        self.btnExcluir = Button(root, text="Excluir", command=self.excluirCidade)
        self.btnExcluir.grid(row=5, column=1)

    def buscarCidade(self):
        cidade = Cidades()
        idcidade = self.txtidcidade.get()
        cidade.selectCidade(idcidade)

        if cidade.idcidade:
            self.lblmsg["text"] = "Cidade encontrada!"
            self.txtidcidade.delete(0, END)
            self.txtidcidade.insert(INSERT, cidade.idcidade)
            self.txtnomecidade.delete(0, END)
            self.txtnomecidade.insert(INSERT, cidade.nomecidade)
            self.txtuf.delete(0, END)
            self.txtuf.insert(INSERT, cidade.uf)
        else:
            self.lblmsg["text"] = "Cidade não encontrada."

    def inserirCidade(self):
        cidade = Cidades()
        cidade.idcidade = self.txtidcidade.get()
        cidade.nomecidade = self.txtnomecidade.get()
        cidade.uf = self.txtuf.get()
        self.lblmsg["text"] = cidade.insertCidade()
        self.limparCampos()

    def alterarCidade(self):
        cidade = Cidades()
        cidade.idcidade = self.txtidcidade.get()
        cidade.nomecidade = self.txtnomecidade.get()
        cidade.uf = self.txtuf.get()
        self.lblmsg["text"] = cidade.updateCidade()
        self.limparCampos()

    def excluirCidade(self):
        cidade = Cidades()
        cidade.idcidade = self.txtidcidade.get()
        self.lblmsg["text"] = cidade.deleteCidade()
        self.limparCampos()

    def limparCampos(self):
        self.txtidcidade.delete(0, END)
        self.txtnomecidade.delete(0, END)
        self.txtuf.delete(0, END)


class Cidades:
    def _init_(self):
        self.idcidade = None
        self.nomecidade = None
        self.uf = None

    def selectCidade(self, idcidade):
        if idcidade == "1":
            self.idcidade = "1"
            self.nomecidade = "São Paulo"
            self.uf = "SP"
        else:
            self.idcidade = None

    def insertCidade(self):
        return "Cidade inserida com sucesso!"

    def updateCidade(self):
        return "Cidade atualizada com sucesso!"

    def deleteCidade(self):
        return "Cidade excluída com sucesso!"


root = Tk()
app = App(root)
root.mainloop()