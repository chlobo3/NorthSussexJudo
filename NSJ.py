from tkinter import *
from tkinter import messagebox
from PIL import Image #pillow must be installed on PCs for GUI to work when running code (pip install Pillow)
from tkinter import ttk #for treeview
import sqlite3

def create_tables():

        conn =  sqlite3.connect("athletes.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS athletes (
                    name TEXT,
                    weight INTEGER,
                    training_plan TEXT,
                    category TEXT,
                    hours INTEGER,
                    total_cost FLOAT
              )""")
        
        conn.commit()
        conn.close()


def query_database():

        conn=sqlite3.connect("athletes.db")
        c=conn.cursor()

        c.execute("SELECT * FROM athletes")
        rows = c.fetchall()
        print(rows)
        conn.commit()
        conn.close()
        return rows

#the main window, the info on frame switches is stored here

class Window(Tk):

    def __init__(self):
        super().__init__()

        WIDTH = 800
        HEIGHT = 700

        self.title("North Sussex Judo")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.resizable(False, False) 

        container = Frame(self) #frame holder, this container holds the pages
        container.pack(side="top", fill="both", expand=True) #expand true makes sure that the frames fill the entire window.

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1) 

        self.frames = {} 

        for Page in (Login, Menu, Athlete_Information): #frame switches are stored here, every class has it's own frame with it's own widgets.
            page_name = Page.__name__
            frame = Page(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("Login")

    def show_frame(self, page_name): #show_frame is applied to commands/button binds for the user to switch to a different frame. 
        frame = self.frames[page_name]
        frame.tkraise()

class Login(Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.img = PhotoImage(file="nsjfinal.png") #both login and Menu GUI backgrounds are designed on "https://www.figma.com/". 

        background = Label(self, image = self.img, width = 800, height = 700)
        background.place(x=0, y=0, relwidth=1, relheight=1)


        login_title = Label(self, text="Login", font=('arial',15, 'bold'), fg='blue', bg='white').place(x=370, y=200)
        
        self.user_login = Label(self,
                            text="Username",
                            font=('arial', 12, 'bold'),
                            fg='black',
                            bg='white')
        self.user_login.place(x=250, y=250)

        self.user_entry = Entry(self,
                            font=('arial', 10, 'bold'),
                            fg='black',
                            bg='white')
        self.user_entry.place(x=345, y=250)

        self.password = Label(self,
                            text="Password",
                            font=('arial', 12, 'bold'),
                            fg='black',
                            bg='white')
        self.password.place(x=250, y=285)

        self.pass_entry = Entry(self,
                                font=('arial', 10, 'bold'),
                                fg='black',
                                bg='white',
                                show='*')
        self.pass_entry.place(x=345, y=285)

        Button(self,text="Log in",cursor='hand1',command=lambda: self.check_login(controller,self.user_entry.get(),self.pass_entry.get())).place(x=500, y=280)

    def check_login(self, controller, user_entry, pass_entry):

        username = "coach"
        password = "123"

        if user_entry == username and pass_entry == password:
            controller.show_frame("Menu")                 
        else: 
            messagebox.showerror("Login unsuccessful", "The username or password that you've entered is incorrect")  
    
class Menu(Frame): #Athlete INPUT
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        #GUI
        self.menuimg = PhotoImage(file="menu.png")
        menu_bg=Label(self, image= self.menuimg, width=800, height=700).place(x=0,y=0, relwidth=1,relheight=1)

        self.ath_reg=Label(self,
                          text="Athlete Registration",
                          font=('arial',15, 'bold'),
                          fg='blue',
                          bg='white',
                          cursor='hand2')
        self.ath_reg.place(x= 20,y=105)
        self.ath_reg.bind("<Button-1>", lambda e: controller.show_frame("Menu")) #turns the label into a button + switches frame 

        self.ath_info=Label(self,
                          text="Athlete Information",
                          font=('arial',15, 'bold'),
                          fg='blue',
                          bg='white',
                          cursor='hand2')
        self.ath_info.place(x = 20,y = 178)
        self.ath_info.bind("<Button-1>", lambda e: controller.show_frame("Athlete_Information"))

        self.log_out = Button(self,
                         text="Log Out",
                         font=('arial', 13, 'bold'),
                         fg='black',
                         bg='white',
                         border=0,
                         highlightbackground='blue',
                         activeforeground='white',
                         activebackground='blue',
                         cursor = 'hand1',
                         command = self.exitwindow).place(x=10, y=660) #this DOESN'T WORK, will fix later
        
        ath_title = Label(self,
                          text="Athlete Registration",
                          font=('serif',12,'bold'),
                          fg='blue',
                          bg='white').place(x=250,y=70)
        
        name = Label(self,
                     text = "Name:",
                     font = ('serif',10),
                     fg = 'black',
                     bg = 'white').place(x=250,y=100)
        
        weight = Label(self,
                       text = "Weight:",
                       font = ('serif',10),
                       fg = 'black',
                       bg = 'white').place(x=250,y=170)
        
        KG = Label (self, text = "kg",font = ('serif', 10,'bold'), fg='black', bg='white').place(x=300,y=200)
        
        training = Label(self,  
                        text = "Training Plan:",
                        font = ('serif',10),
                        fg = 'black',
                        bg='white').place(x=250,y=240)

        weight_cat = Label(self,  
                        text = "Weight Category:",
                        font = ('serif',10),
                        fg = 'black',
                        bg = 'white').place(x=250,y=300)

        #comp_entry = Label(self,  
        #           text = "Competition Entry:",
        #           font = ('serif',10),
        #           fg = 'black',       
        #           bg = 'white').place(x=250,y=370)

        priv_hr = Label (self,
                        text = "Private Coaching:",
                        font = ('serif',10),
                        fg = 'black',
                        bg = 'white').place(x=250,y=440)
        
        self.hrs = Label(self, text="hrs", font = ('serif', 10 ), bg = 'white',fg = 'black')
        #END OF GUI

#name
        self.athlete_name = Entry(self,font = ('serif',10),fg='black',width=40)
        self.athlete_name.place(x=250,y=130)
        
#weight       
        self.athlete_weight = Entry(self,font = ('serif',10),fg='black',width=5)
        self.athlete_weight.place(x=250,y=200) 
        
#training plan    
        self.options = StringVar(self)
        self.options.set("Select")
   
        self.athlete_training = OptionMenu(self, self.options,'Beginner', 'Intermediate', 'Elite')
        self.athlete_training.place(x=250, y=265) 

        self.athlete_training.config(bg ='white' , relief='solid', borderwidth=1, width=10,)
       
#private hours
        r = StringVar()

        self.private_hours_Y = Radiobutton(self, text= "Yes", variable = r , value=1, command=self.private_hours)
        self.private_hours_Y.place(x=250, y=470)
        self.private_hours_Y.config(bg='white',border=0)

        self.private_hours_N = Radiobutton(self, text= "No", variable = r , value=0)
        self.private_hours_N.place(x=350, y=470)
        self.private_hours_N.config(bg='white', border=0)

        self.entry_hours = Entry(self,font = ('serif',10),fg='black',width=5)

        self.enter = Button(self,text = "Enter", font = ('arial',13,'bold'),highlightbackground = 'blue',activeforeground = 'white', activebackground = 'blue', cursor = 'hand1',
                            command = self.save_input)
        self.enter.place(x=250, y=550)

#weight_category
        self.weight_category = StringVar(self)
        self.weight_category.set("Select")

        self.category = OptionMenu(self, self.weight_category,'Heavyweight', 'Light-Heavyweight', 'Middleweight', 'Lightweight', 'Flyweight')
        self.category.place(x=250, y=330)
        self.category.config(bg ='white' , relief='solid', borderwidth=1, width=18,)
 
    def private_hours(self): 

        if self.private_hours_Y.cget("text"):
            self.entry_hours.place(x=250, y=500)
            self.hrs.place(x=300, y=500)
        else:
            return None

    def force_numberHRS(self):
       
       if self.private_hours_Y.cget() == 1: 
        hours_value = self.private_hours_Y.get() 
        try:
            hours_value = int(hours_value)
            return hours_value
        except ValueError:
            messagebox.showerror("","Invalid Information")
            return None
        
    def exitwindow(self):
        self.destroy() #doesn't work properly, will fix later
       
    def force_numberKG(self):
               
        weight_value = self.athlete_weight.get()
        try: 
            weight_value = int(weight_value)
            return weight_value
        except ValueError:
            messagebox.showerror("","Invalid Information")
            return None
        
    def total_cost(self):

        private_rate = 9.5 

        self.prices = {
                    "Beginner" : 25.0,
                    "Intermediate": 30.0,
                    "Elite": 35.0,
                    }

        key =  self.options.get()

        #print(f'DEBUG key: {key}')

        value = self.prices[key]

        #print(f'DEBUG value: {value}')
        #print(f'DEBUG cget(): {self.priv_coach_Y.cget("text")}')

        if self.private_hours_Y.cget("text"):
            private_hours =  self.entry_hours.get()
            value = value + (private_rate *float(private_hours))
            return value

    #def input_entry(self):   
                   
    def save_input(self):
    
        name = self.athlete_name.get()
        weight = self.force_numberKG()
        training_plan = self.options.get()
        category = self.weight_category.get()
        hours = 0

        if self.entry_hours.get() != "":
            hours = int(self.entry_hours.get())
        
        total_cost = self.total_cost()
         
        conn = sqlite3.connect("athletes.db")
        c = conn.cursor()

        data = (name,weight,training_plan,category,hours,total_cost)

        for record in data:
            c.execute("INSERT INTO athletes VALUES (:name, :weight, :training_plan, :category, :hours, :total_cost)",)
            {
            'name': record[0],
            'weight': record[1],
            'training_plan': record[2],
            'category': record[3],
            'hours': record[5],
            'total_cost':record[6]
            }
        
        #(name,weight,training_plan,category,hours,total_cost))
   
        conn.commit()
        conn.close()
    
        self.athlete_name.delete(0,END) 
        self.athlete_weight.delete(0,END)
        self.entry_hours.delete(0,END)
        self.entry_hours.place_forget()
        self.hrs.place_forget()

        print("works")
    
 #NOTES/To Do:
        #create an SQLITE file[X]
        #output the info from the entry widgets [X], radio buttons / drop down menus into the SQLITE file [X]
        #from the SQlite3 file output the info into Athlete Information []
        #Assigns INTs to certain variables (Training plan > Prices)[X]

class Athlete_Information(Frame): #Athlete OUTPUT / EDIT existing Athletes
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        #GUI
        self.menuimg = PhotoImage(file="athleteinfo.png")
        menu_bg=Label(self, image= self.menuimg, width=800, height=700).place(x=0,y=0, relwidth=1,relheight=1)
        
        self.ath_regi=Label(self,
                          text="Athlete Reg",
                          font=('arial',15, 'bold'),
                          fg='blue',
                          bg='white',
                          cursor='hand2')
        self.ath_regi.place(x= 20,y=105)
        self.ath_regi.bind("<Button-1>", lambda e: controller.show_frame("Menu"))

        self.ath_info=Label(self,
                          text="Athlete Info",
                          font=('arial',15, 'bold'),
                          fg='blue',
                          bg='white',
                          cursor='hand2')
        self.ath_info.place(x = 20,y = 178)
        self.ath_info.bind("<Button-1>", lambda e: controller.show_frame("Athlete_Information"))

        athlete_title2 = Label(self,
                          text="Athlete Information",
                          font=('serif',12,'bold'),
                          fg='blue',
                          bg='white').place(x=170,y=70)

        log_out = Button(self,
                        text="Log Out",
                        font=('arial', 13, 'bold'),
                        fg='black',
                        bg='white',
                        border=0,
                        highlightbackground='blue',
                        activeforeground='white',
                        activebackground='blue',
                        cursor = 'hand1',
                        command = 'exitwindow').place(x=10, y=660)
        #END OF GUI


        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview",
                        background = "#D3D3D3",
                        foreground = "black",
                        rowheight = 25,
                        fieldbackground = "#D3D3D36C")
        style.map('Treeview',
                  background = [('selected','#347083')])

#TREE VIEW

        tree_frame = Frame(self)
        tree_frame.place(x=170,y=100)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        self.tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')
        self.tree.pack()
        tree_scroll.config(command=self.tree.yview)

        #defined columns 


        self.tree['columns'] = ("Name", "Weight", "Training Plan", "Category", "Hours", "Total Cost")
        
        self.tree.column("#0", width = 0 , minwidth=0, stretch=NO)
        self.tree.column("Name", width = 90, minwidth=25, anchor=W)
        self.tree.column("Weight", anchor = CENTER, width = 85)
        self.tree.column("Training Plan", anchor= CENTER, width = 130)
        self.tree.column("Category", anchor= CENTER, width=130)
        self.tree.column("Hours", anchor=CENTER , width=90)
        self.tree.column("Total Cost", anchor=CENTER , width=80) 

        #headings 

        self.tree.heading("#0", text="", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W )
        self.tree.heading("Weight", text="Weight(kg)", anchor=W)
        self.tree.heading("Training Plan", text ="Training Plan", anchor=CENTER)
        self.tree.heading("Category", text="Weight Category", anchor=CENTER)
        self.tree.heading("Hours", text="Hours", anchor=CENTER)
        self.tree.heading("Total Cost", text="Total Cost", anchor=CENTER)



        self.tree.tag_configure('oddrow', background='white')
        self.tree.tag_configure('evenrow', background='lightblue')

        global count
        count = 0
        data = query_database()
        

        for record in data:
            if count % 2 == 0:
                self.tree.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags =('evenrow',))
            else:
                self.tree.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags =('oddrow',))

            count += 1

        athlete_delete = Button(self, text="Delete", font=('serif',10), fg='black')
        athlete_delete.place(x=170, y=380)

        athlete_edit = Button(self, text="Edit", font=('serif',10), fg='black')
        athlete_edit.place(x=240, y=380)
    
 

#NOTES
        #create a scroll bar and EDIT athlete button [X]
        #when clicking an edit button next to the athlete, the athlete data needs to be outputted back into athelete reg []
        #then removed from the athlete info , and then re-outputted into athlete reg. []


window = Window()
window.mainloop()

window = Window()
window.mainloop()
