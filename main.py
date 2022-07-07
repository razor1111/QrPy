from cProfile import label
from cgitb import text
from resizeimage import resizeimage
from distutils.command.config import config
from tkinter import*
import qrcode
from PIL import Image,ImageTk
from turtle import title
class Qr_Generator:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1150x650+200+50")
        self.root.title("  Gerador de Qr Code | Desenvolvido por Antonio Neto")
        self.root.resizable(False,False)
        self.icon_title=PhotoImage(file="images/logo.png")
        title = Label(self.root,text=" Gerador de Qr Code DTI ",image=self.icon_title,compound = LEFT,font=("times new roman",40,"bold"),bg='black',fg='white',anchor = "center").place(x=-150,y=0,relwidth=1,height=100,width=200)

        #======= Variáveis ==============
        self.var_emp_code = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_dep = StringVar()
        self.var_emp_pl = StringVar()


        
        #==== Janela de Detalhes ========
        
        emp_Frame=Frame(self.root,bd=2,relief=RIDGE)
        emp_Frame.place(x=50,y=150,width=500,height=380)

        emp_title = Label(emp_Frame,text="DETALHES",font=("goudy old style",25),bg='#FFA500',fg='white').place(x=0,y=0,relwidth=1)
        lbl_emp_code = Label(emp_Frame,text="Rc/Oc",font=("times new roman",15,'bold')).place(x=20,y=60)
        lbl_emp_name = Label(emp_Frame,text="Nome",font=("times new roman",15,'bold')).place(x=20,y=100)
        lbl_emp_dep = Label(emp_Frame,text="Departamento",font=("times new roman",15,'bold')).place(x=20,y=140)
        lbl_emp_pl = Label(emp_Frame,text="PL",font=("times new roman",15,'bold')).place(x=20,y=180)

        lbl_emp_code = Entry(emp_Frame,font=("times new roman",15,),textvariable=self.var_emp_code,bg='lightyellow').place(x=150,y=60)
        lbl_emp_name = Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_emp_name,bg='lightyellow').place(x=150,y=100)
        lbl_emp_dep = Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_emp_dep,bg='lightyellow').place(x=150,y=140)
        lbl_emp_pl = Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_emp_pl,bg='lightyellow').place(x=150,y=180)

        btn_generate = Button(emp_Frame,text="Gerar QR",command=self.generate,font=("times new roman",18,'bold'),bg="#FFA500",fg='black').place(x='30',y='250',width=180,height=30)
        btn_clear = Button(emp_Frame,text="Limpar",command=self.clear,font=("times new roman",18,'bold'),bg="#FFA500",fg='black').place(x='220',y='250',width=180,height=30)

        self.msg = ""
        self.lbl_msg = Label(emp_Frame,text=self.msg,font=("times new roman",20,'bold'),fg='green')
        self.lbl_msg.place(x=40,y=320)
        #=======Janela do QRCODE==========
       
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE)
        qr_Frame.place(x=580,y=150,width=500,height=380)

        qr_title = Label(qr_Frame,text="QR CODE",font=("goudy old style",25),bg='#FFA500',fg='white').place(x=0,y=0,relwidth=1)
        self.qr_code = Label(qr_Frame,text='QR Code \nNão Gerado',font=('times new roman',10,'bold'),bg='#FFA500',fg='black',bd=1,relief=RIDGE)
        self.qr_code.place(x=175,y=100,width=180,height=180) 

    def generate(self):
        if self.var_emp_code.get()=='' or self.var_emp_name.get()=='' or self.var_emp_dep.get()=='' or self.var_emp_pl.get()=='':
            self.msg = "Campo não pode está vazio!"
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f" Rc/Oc: {self.var_emp_code.get()}\n Nome: {self.var_emp_name.get()} \n Departamento: {self.var_emp_dep.get()} \n PL: {self.var_emp_pl.get()}")
            qr_code = qrcode.make(qr_data)
            print(qr_code)
            qr_code = resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("QR-FUNCIONARIO/Emp_"+str(self.var_emp_name.get())+ '.png')
            
            # ATUALIZAÇÃO DA IMAGEM QR CODE
            self.im = ImageTk.PhotoImage(file = "QR-FUNCIONARIO/Emp_"+str(self.var_emp_name.get())+ '.png')
            self.qr_code.config(image=self.im)
            
            ## ATUALIZAÇÃO DE NOTIFICAÇÃO 
            self.msg = "QR Code Gerado Com Sucesso!"
            self.lbl_msg.config(text=self.msg,fg='green')

    def clear(self):
        self.var_emp_code.set('')
        self.var_emp_name.set('')
        self.var_emp_dep.set('')
        self.var_emp_pl.set('')
        self.msg =''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')
          



root = Tk()
obj = Qr_Generator(root)
root.mainloop()