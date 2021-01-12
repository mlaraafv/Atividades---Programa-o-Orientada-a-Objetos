from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="floresta"
) 


myCursor = mydb.cursor() 
myCursor.execute("CREATE DATABASE IF NOT EXISTS poo") 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="floresta",
  database="poo"
) 


myCursor = mydb.cursor()

myCursor.execute("CREATE TABLE IF NOT EXISTS aluno (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), curso VARCHAR(255), idade INT)")


window = Tk()
window.geometry("500x500")
window.title("Atividade 10") 

class Application:   

    def __init__(self, master=None): 
        self.fonte = ("Arial", "12")

        self.container1 = Frame(master)
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5.pack()
        self.container8 = Frame(master)
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9.pack()
        
        
        self.titulo = Label(self.container1, text="Informe os dados :") 
        self.titulo["font"] = ("Calibri", "12", "bold")
        self.titulo.pack()


        
        self.lbidusuario = Label(self.container2,
        text="idUsuario:", font=self.fonte, width=10)
        self.lbidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.seleciona
        self.btnBuscar.pack(side=RIGHT)

        
        self.lbnome = Label(self.container3, text="Nome:",
        font=self.fonte, width=10)
        self.lbnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lbcurso = Label(self.container4, text="Curso:",
        font=self.fonte, width=10)
        self.lbcurso.pack(side=LEFT)

        self.txtcurso = Entry(self.container4)
        self.txtcurso["width"] = 25
        self.txtcurso["font"] = self.fonte
        self.txtcurso.pack(side=LEFT)

        self.lbidade= Label(self.container5, text="Idade:",
        font=self.fonte, width=10)
        self.lbidade.pack(side=LEFT)

        self.txtidade = Entry(self.container5)
        self.txtidade["width"] = 25
        self.txtidade["font"] = self.fonte
        self.txtidade.pack(side=LEFT)

        
        self.bntInsert = Button(self.container8, text="Inserir",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserir
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",
        font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterar
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",
        font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluir
        self.bntExcluir.pack(side=LEFT)

        
        self.lbmsg = Label(self.container9, text="")
        self.lbmsg["font"] = ("Arial", "9")
        self.lbmsg.pack()


    def limparEntry(self): 
        self.txtcurso.delete(0,END)
        self.txtidade.delete(0,END)
        self.txtnome.delete(0,END)

    def checarSeTaVazio(self): 
        nome = self.txtnome.get()
        curso = self.txtcurso.get()
        idade = self.txtidade.get()
        if not nome or  not curso or not idade:
            return True

    def inserir(self):
        if self.checarSeTaVazio(): 
            self.lbmsg["text"] = "Coloque os parametros para inserção" 
            return

        nome = self.txtnome.get()
        curso = self.txtcurso.get()
        try:
            idade = int(self.txtidade.get())
        except ValueError:
            self.lbmsg["text"] = "Coloque um numero na idade!"
            return   
        sql = "INSERT INTO aluno (nome, curso, idade) VALUES (%s, %s, %s)"
        val = (nome,curso,idade)
        myCursor.execute(sql, val) 
        mydb.commit() 

        self.lbmsg["text"] = "Inserido!" 
        self.limparEntry()

    def seleciona(self):
        self.lbmsg["text"] = ""
        sql = "SELECT * FROM aluno where id = %s"
        val = (self.txtidusuario.get(),)
        myCursor.execute(sql,val)
        myresult = myCursor.fetchone() 
        self.limparEntry()
        if myresult == None: 
            self.lbmsg["text"] = "Aluno não encontrado"
            return
        
        self.txtnome.insert(INSERT,myresult[1])
        self.txtcurso.insert(INSERT,myresult[2])
        self.txtidade.insert(INSERT,myresult[3]) 


    def excluir(self):
        if not self.txtidusuario.get():
            self.lbmsg["text"] = "Coloque o id do aluno para exclusão"
            return
        sql = "DELETE FROM aluno where id = %s"
        val = (self.txtidusuario.get(),)
        myCursor.execute(sql,val)
        mydb.commit()
        self.lbmsg["text"] = "Aluno deletado" 
        self.limparEntry() 
    
    def alterar(self):
        if self.checarSeTaVazio(): 
            self.lbmsg["text"] = "Coloque os parametros para alteração"
            return

        if not self.txtidusuario.get():
            self.lbmsg["text"] = "Coloque o id do aluno para exclusão"
            return
        
        nome = self.txtnome.get() 
        curso = self.txtcurso.get()
        try:
            idade = int(self.txtidade.get()) 
        except ValueError:
            self.lbmsg["text"] = "Coloque um numero na idade!"
            return  
        sql = "UPDATE aluno SET nome = %s, curso = %s, idade = %s where id = %s"
        val = (nome,curso,idade, self.txtidusuario.get())
        myCursor.execute(sql,val)
        mydb.commit()
        self.lbmsg["text"] = "Aluno alterado" 
        self.limparEntry() 

Application(window) 
window.mainloop() 







