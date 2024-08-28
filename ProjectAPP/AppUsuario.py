from tkinter import *
from usuarios import Banco

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Usuários")

        self.lblidusuario = Label(root, text="ID Usuário")
        self.lblidusuario.grid(row=0, column=0)
        self.txtidusuario = Entry(root)
        self.txtidusuario.grid(row=0, column=1)

        self.lblnome = Label(root, text="Nome")
        self.lblnome.grid(row=1, column=0)
        self.txtnome = Entry(root)
        self.txtnome.grid(row=1, column=1)

        self.lbltelefone = Label(root, text="Telefone")
        self.lbltelefone.grid(row=2, column=0)
        self.txttelefone = Entry(root)
        self.txttelefone.grid(row=2, column=1)

        self.lblemail = Label(root, text="Email")
        self.lblemail.grid(row=3, column=0)
        self.txtemail = Entry(root)
        self.txtemail.grid(row=3, column=1)

        self.lblusuario = Label(root, text="Usuário")
        self.lblusuario.grid(row=4, column=0)
        self.txtusuario = Entry(root)
        self.txtusuario.grid(row=4, column=1)

        self.lblsenha = Label(root, text="Senha")
        self.lblsenha.grid(row=5, column=0)
        self.txtsenha = Entry(root, show="*")
        self.txtsenha.grid(row=5, column=1)

        self.lblmsg = Label(root, text="")
        self.lblmsg.grid(row=6, column=0, columnspan=2)

        self.btnBuscar = Button(root, text="Buscar", command=self.buscarUsuario)
        self.btnBuscar.grid(row=7, column=0)

        self.btnInsert = Button(root, text="Inserir", command=self.inserirUsuario)
        self.btnInsert.grid(row=7, column=1)

        self.btnAlterar = Button(root, text="Alterar", command=self.alterarUsuario)
        self.btnAlterar.grid(row=8, column=0)

        self.btnExcluir = Button(root, text="Excluir", command=self.excluirUsuario)
        self.btnExcluir.grid(row=8, column=1)

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.txtidusuario.get()
        user.selectUser(idusuario)

        if user.idusuario:
            self.lblmsg["text"] = "Usuário encontrado!"
            self.txtidusuario.delete(0, END)
            self.txtidusuario.insert(INSERT, user.idusuario)
            self.txtnome.delete(0, END)
            self.txtnome.insert(INSERT, user.nome)
            self.txttelefone.delete(0, END)
            self.txttelefone.insert(INSERT, user.telefone)
            self.txtemail.delete(0, END)
            self.txtemail.insert(INSERT, user.email)
            self.txtusuario.delete(0, END)
            self.txtusuario.insert(INSERT, user.usuario)
            self.txtsenha.delete(0, END)
            self.txtsenha.insert(INSERT, user.senha)
        else:
            self.lblmsg["text"] = "Usuário não encontrado."

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()
        self.lblmsg["text"] = user.insertUser()
        self.limparCampos()

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()
        self.lblmsg["text"] = user.updateUser()
        self.limparCampos()

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.txtidusuario.get()
        self.lblmsg["text"] = user.deleteUser()
        self.limparCampos()

    def limparCampos(self):
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)


class Usuarios:
    def __init__(self):
        self.idusuario = None
        self.nome = None
        self.telefone = None
        self.email = None
        self.usuario = None
        self.senha = None

    def selectUser(self, idusuario):
        if idusuario == "1":
            self.idusuario = "1"
            self.nome = "João"
            self.telefone = "123456789"
            self.email = "joao@example.com"
            self.usuario = "joaouser"
            self.senha = "12345"
        else:
            self.idusuario = None

    def insertUser(self):
        return "Usuário inserido com sucesso!"

    def updateUser(self):
        return "Usuário atualizado com sucesso!"

    def deleteUser(self):
        return "Usuário excluído com sucesso!"


root = Tk()
app = App(root)
root.mainloop()