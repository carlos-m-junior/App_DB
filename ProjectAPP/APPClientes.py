from tkinter import *
from Banco import Banco

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Clientes")

        self.lblcodigo = Label(root, text="Código")
        self.lblcodigo.grid(row=0, column=0)
        self.txtcodigo = Entry(root)
        self.txtcodigo.grid(row=0, column=1)

        self.lblnome = Label(root, text="Nome")
        self.lblnome.grid(row=1, column=0)
        self.txtnome = Entry(root)
        self.txtnome.grid(row=1, column=1)

        self.lblendereco = Label(root, text="Endereço")
        self.lblendereco.grid(row=2, column=0)
        self.txtendereco = Entry(root)
        self.txtendereco.grid(row=2, column=1)

        self.lblfone = Label(root, text="Telefone")
        self.lblfone.grid(row=3, column=0)
        self.txtfone = Entry(root)
        self.txtfone.grid(row=3, column=1)

        self.lblcpf = Label(root, text="CPF")
        self.lblcpf.grid(row=4, column=0)
        self.txtcpf = Entry(root)
        self.txtcpf.grid(row=4, column=1)

        self.lblcidcodigo = Label(root, text="Código da Cidade")
        self.lblcidcodigo.grid(row=5, column=0)
        self.txtcidcodigo = Entry(root)
        self.txtcidcodigo.grid(row=5, column=1)

        self.lblmsg = Label(root, text="")
        self.lblmsg.grid(row=6, column=0, columnspan=2)

        self.btnBuscar = Button(root, text="Buscar", command=self.buscarCliente)
        self.btnBuscar.grid(row=7, column=0)

        self.btnInsert = Button(root, text="Inserir", command=self.inserirCliente)
        self.btnInsert.grid(row=7, column=1)

        self.btnAlterar = Button(root, text="Alterar", command=self.alterarCliente)
        self.btnAlterar.grid(row=8, column=0)

        self.btnExcluir = Button(root, text="Excluir", command=self.excluirCliente)
        self.btnExcluir.grid(row=8, column=1)

    def buscarCliente(self):
        cliente = Clientes()
        codigo = self.txtcodigo.get()
        cliente.selectCliente(codigo)

        if cliente.codigo:
            self.lblmsg["text"] = "Cliente encontrado!"
            self.txtcodigo.delete(0, END)
            self.txtcodigo.insert(INSERT, cliente.codigo)
            self.txtnome.delete(0, END)
            self.txtnome.insert(INSERT, cliente.nome)
            self.txtendereco.delete(0, END)
            self.txtendereco.insert(INSERT, cliente.endereco)
            self.txtfone.delete(0, END)
            self.txtfone.insert(INSERT, cliente.fone)
            self.txtcpf.delete(0, END)
            self.txtcpf.insert(INSERT, cliente.cpf)
            self.txtcidcodigo.delete(0, END)
            self.txtcidcodigo.insert(INSERT, cliente.cid_codigo)
        else:
            self.lblmsg["text"] = "Cliente não encontrado."

    def inserirCliente(self):
        cliente = Clientes()
        cliente.nome = self.txtnome.get()
        cliente.endereco = self.txtendereco.get()
        cliente.fone = self.txtfone.get()
        cliente.cpf = self.txtcpf.get()
        cliente.cid_codigo = self.txtcidcodigo.get()
        self.lblmsg["text"] = cliente.insertCliente()
        self.limparCampos()

    def alterarCliente(self):
        cliente = Clientes()
        cliente.codigo = self.txtcodigo.get()
        cliente.nome = self.txtnome.get()
        cliente.endereco = self.txtendereco.get()
        cliente.fone = self.txtfone.get()
        cliente.cpf = self.txtcpf.get()
        cliente.cid_codigo = self.txtcidcodigo.get()
        self.lblmsg["text"] = cliente.updateCliente()
        self.limparCampos()

    def excluirCliente(self):
        cliente = Clientes()
        cliente.codigo = self.txtcodigo.get()
        self.lblmsg["text"] = cliente.deleteCliente()
        self.limparCampos()

    def limparCampos(self):
        self.txtcodigo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txtfone.delete(0, END)
        self.txtcpf.delete(0, END)
        self.txtcidcodigo.delete(0, END)


class Clientes:
    def _init_(self):
        self.codigo = None
        self.nome = None
        self.endereco = None
        self.fone = None
        self.cpf = None
        self.cid_codigo = None

    def selectCliente(self, codigo):
        if codigo == "1":
            self.codigo = "1"
            self.nome = "Maria"
            self.endereco = "Rua das Flores"
            self.fone = "987654321"
            self.cpf = "123.456.789-00"
            self.cid_codigo = "100"
        else:
            self.codigo = None

    def insertCliente(self):
        return "Cliente inserido com sucesso!"

    def updateCliente(self):
        return "Cliente atualizado com sucesso!"

    def deleteCliente(self):
        return "Cliente excluído com sucesso!"


root = Tk()
app = App(root)
root.mainloop()