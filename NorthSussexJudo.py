from tkinter import *
from tkinter import messagebox

WIDTH = 800
HEIGHT = 700

#window = Tk()


#window.title("Welcome")
#window.resizable(False, False)
#window.geometry(f'{WIDTH}x{HEIGHT}')

#Window GUI
#icon = PhotoImage(file='nsj_logo.png')
#window.iconphoto(True,icon) 
#window.config(background='white')
#photo = PhotoImage(file='nsjfinal.png')
#label = Label(window,
              #image=photo,
              #compound='bottom')
#label.place(x=0, y=0)


#Login page GUI


window = Tk()

class window:
        def __init__(window, self):
            super().__init__()

            self.title("North Sussex Judo")
            self.resizable(False, False)
            self.geometry(f'{WIDTH}x{HEIGHT}')


            self.config(background='white')

            self.photo = PhotoImage(file='nsjfinal.png')
            self.label = Label(self,image=self.photo)
            self.label.place(x=0, y=0)

            self.login_page = LoginPage(self)
            self.menu_page = MainMenu(self)

            #self.athlete = AthletePage(self)
            #self.registration = EditInfo(self)

        def login_page(self):
            self.menu_page.pack_forget()
            self.login_page.pack(fill='both', expand=True)

        def show_MainMenu(self):
             self.login_page.pack_forget()
             self.menu_page.pack(fill='both',expand=True)


class login_page (Frame)
            def __init__(self):
            super().__init__(self)

#.place(x=375, y=200)
            Label(self, NSJ,
                        text="Log in",
                        font=('Serif',14,'bold'),
                        fg='black',
                        bg='white',).pack(side="top")
            
#.place(x= 250, y=250)
            Label(self,
                        text= "Username",
                        font=('serif',10, 'bold'),
                        fg='black',
                        bg='white').pack()
#.place(x= 340, y=250)
            self.name_entry=Entry(self, 
                            font=('serif', 13,'normal'),
                            fg='black',
                            bg='white').pack()
#.place(x= 250, y=285)
            Label(self, 
                        text = "Password",
                        font=('serif',10,'bold'),
                        fg='black',
                        bg='white').pack()
#.place(x= 340, y=285)
            self.pass_entry=Entry(self,                      
                            font=('serif', 13, 'normal'),
                            fg='black',
                            bg='white',
                            show='*').pack()
#.place(x= 370, y=335)
            Button(self, 
                        text = "Enter",
                        font=('serif', 10, 'normal'),
                        bg='white',
                        padx= 20,
                        pady= 0,
                        command = self.login).pack()

#Login input for the client to proceed to the main menu
            
        def login(self): 
                
            username = "coach"
            password = "123"

            if self.name_entry.get() == username and self.pass_entry.get() == password:
                self.MainMenu()
            else: 
                messagebox.showerror(title="Login unsuccessful", message ="Please try again")
                
            
          
class MainMenu(Frame):
        def __init__(self, master):
            super().__init__(master)

            self.MM_img = PhotoImage(file='menu.png')
            self.menu_img = Label(self,
                        image = self.MM_img, 
                        compound = 'bottom')
            self.menu_img.place(x=0, y=0)

#runs the program
NSJ = NSJ ()
NSJ.mainloop()