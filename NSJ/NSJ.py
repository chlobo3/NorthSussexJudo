#!/user/bin/env python3

from tkinter import *
from tkinter import messagebox
from PIL import Image #pillow must be installed on PCs for GUI to work when running code (pip install Pillow)
from tkinter import ttk #for treeview
import sqlite3 #data output

#SQlite3 data table is created:
def create_tables():

        conn =  sqlite3.connect("athlete.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS athlete (name TEXT,weight INTEGER,training_plan TEXT,category TEXT,competition INTEGER,hours INTEGER,total_cost FLOAT)""")
        
        conn.commit()
        conn.close()

create_tables()
print("table created")

#Execte db selection
def query_database():
                
        conn=sqlite3.connect("athlete.db")
        c=conn.cursor()

        c.execute("SELECT * FROM athlete")
        rows = c.fetchall()

        print(rows)
    
        conn.commit()
        conn.close()
        return rows


#main window, info on frame switches is stored here:
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

        username = "coach" #needs better security 
        password = "123"

        if user_entry == username and pass_entry == password:
            controller.show_frame("Menu")                 
        else: 
            messagebox.showerror("Login unsuccessful", "The username or password that you've entered is incorrect")

        self.user_entry.delete(0,END)
        self.pass_entry.delete(0,END)  
    
class Menu(Frame): #Athlete INPUT
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        #GUI
        self.menuimg = PhotoImage(file="menu.png")
        menu_bg=Label(self, image= self.menuimg, width=800, height=700).place(x=0,y=0, relwidth=1,relheight=1)
        self.stickynote = PhotoImage(file="stickynote.png")
        stickynote_img = Label(self, image = self.stickynote, bg='white', width=300, height=300).place(x=460, y=375)

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
                            command = lambda:controller.show_frame("Login"))
        self.log_out.place(x=10, y=660) 
        
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

        comp_entry = Label(self,  
                            text = "Competition Entry:",
                            font = ('serif',10),
                            fg = 'black',       
                            bg = 'white').place(x=250,y=370)

        priv_hr = Label (self,
                            text = "Private Coaching:",
                            font = ('serif',10),
                            fg = 'black',
                            bg = 'white').place(x=250,y=460)
        
        self.hrs = Label(self, text="hrs", font = ('serif', 10 ), bg = 'white',fg = 'black')
        #END OF GUI

#ATHLETE INPUTS:       
    #name
        self.athlete_name = Entry(self,font = ('serif',10),fg='black',width=40)
        self.athlete_name.place(x=250,y=130)
        
    #weight       
        self.athlete_weight = Entry(self,font = ('serif',10),fg='black',width=5)
        self.athlete_weight.place(x=250,y=200) 
        
    #training Plan    
        self.options = StringVar(self)
        self.options.set("Select")
   
        self.athlete_training = OptionMenu(self, self.options,'Beginner', 'Intermediate', 'Elite')
        self.athlete_training.place(x=250, y=265) 

        self.athlete_training.config(bg ='white' , relief='solid', borderwidth=1, width=10,)

    #competition Entry
        self.n = StringVar ()

        self.comp_Yes = Radiobutton(self, text= "Yes", variable = self.n, value=1, command = self.competition)
        self.comp_Yes.place(x = 250, y = 400)
        self.comp_Yes.config(bg= 'white', border = 0)

        self.comp_No = Radiobutton(self, text="No", variable= self.n, value=0,)
        self.comp_No.place(x=350, y= 400)
        self.comp_No.config(bg= 'white', border= 0 )
        self.comp_entry = Entry(self, font = ('serif',10), fg = 'black', width = 5) 
        
    #private hours:
        self.r = StringVar()

        self.private_hours_Y = Radiobutton(self, text= "Yes", variable = self.r , value=1, command=self.private_hours)
        self.private_hours_Y.place(x=250, y=490)
        self.private_hours_Y.config(bg='white',border=0)

        self.private_hours_N = Radiobutton(self, text= "No", variable = self.r , value=0)
        self.private_hours_N.place(x=350, y=490)
        self.private_hours_N.config(bg='white', border=0)

        self.entry_hours = Entry(self,font = ('serif',10),fg='black',width=5)
  
    #data entry:  
        self.enter = Button(self,text = "Enter", font = ('arial',13,'bold'),highlightbackground = 'blue',activeforeground = 'white', activebackground = 'blue', cursor = 'hand1',
                            command = self.save_input)
        self.enter.place(x=250, y=570)

    #weight_category
        self.weight_category = StringVar(self)
        self.weight_category.set("Select")

        self.category = OptionMenu(self, self.weight_category,'Heavyweight', 'Light-Heavyweight', 'Middleweight','Light-Middleweight','Lightweight', 'Flyweight')
        self.category.place(x=250, y=330)
        self.category.config(bg ='white' , relief='solid', borderwidth=1, width=18,)
 
 #string to int manual conversion: 
    def competition(self): 

        radio_value = self.n.get() 

        if radio_value == "1":
  
            self.comp_entry.place(x= 250 , y = 430) 
            
            entry_value = self.comp_entry.get()     
           
            if entry_value != "":
                try: 
                    return int(entry_value)
                except ValueError:
                    return 0 
            
 #private hourly coaching input       
    def private_hours(self): 

        if self.private_hours_Y.cget("text"): #when yes is clicked on the private coaching radiobutton,
            self.entry_hours.place(x=250, y=530) #the entry widget for the input appears
            self.hrs.place(x=300, y=530)
        else:
            return None

    def force_numberHRS(self):
    
        hours_value = self.entry_hours.get() 

        if self.r.get() == 0:
            hours_value = int(hours_value)
            return hours_value
        
        if self.r.get() == 1:   
                
            hours_value >= 5
            messagebox.showerror("Input Error","Only up to 5 hours of coaching is allowed")
            return ValueError
            
        else: 
            return hours_value
        
        
    def force_numberKG(self):
               
        weight_value = self.athlete_weight.get()
        try: 
            weight_value = int(weight_value) #converts the weight values to int
            return weight_value
        except ValueError:
            messagebox.showerror("","Invalid Information") #if another data type is in the input, data invalid
            return None

         
    def total_cost(self):

        private_rate = 9.5 

        self.prices = { #sets the prices for the training plans
                    "Beginner" : 25.0,
                    "Intermediate": 30.0,
                    "Elite": 35.0,
                    }

        key =  self.options.get()
        value = self.prices[key] 
        
        if self.r.get() == "1":

            private_hours = self.entry_hours.get()       
            value = value + (private_rate *float(private_hours))
               
        return value          
                   
    def save_input(self):
    
        data_name = self.athlete_name.get()
        data_weight = self.force_numberKG()
        data_training_plan = self.options.get()
        data_category = self.weight_category.get()
        a_competition =  self.competition()

        data_hours = self.force_numberHRS()
        
        data_total_cost = self.total_cost()
         
        
        conn = sqlite3.connect("athlete.db") #connects to the database 
        with conn: 
            c = conn.cursor() #instructs the database

        c.execute('INSERT INTO athlete (name, weight, training_plan, category, competition, hours, total_cost) VALUES(?, ?, ?, ?, ?, ?, ?)',
                  (data_name, data_weight, data_training_plan, data_category, a_competition, data_hours, data_total_cost))
   
        conn.commit()
        conn.close()
        query_database()

    #clears inputs
        self.athlete_name.delete(0,END) 
        self.athlete_weight.delete(0,END)
        self.entry_hours.delete(0,END)
        self.entry_hours.place_forget()
        self.hrs.place_forget()

        print("works")

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
                                command = lambda:controller.show_frame("Login")).place(x=10, y=660)
        #END OF GUI

#TREE VIEW

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview",
                        background = "#D3D3D3",
                        foreground = "black",
                        rowheight = 25,
                        fieldbackground = "#D3D3D36C")
        style.map('Treeview',
                  background = [('selected','#347083')])
  
        tree_frame = Frame(self)
        tree_frame.place(x=170,y=100)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        self.tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')
        self.tree.pack()
        tree_scroll.config(command=self.tree.yview)

    #defined columns 
        self.tree['columns'] = ("Name", "Weight", "Training Plan", "Category","Competition","Hours", "Total Cost(£)")
        
        self.tree.column("#0", width = 0 , minwidth=0, stretch=NO)
        self.tree.column("Name", width = 90, minwidth=25, anchor=W)
        self.tree.column("Weight", anchor = CENTER, width = 85)
        self.tree.column("Training Plan", anchor= CENTER, width = 130)
        self.tree.column("Category", anchor= CENTER, width=130)
        self.tree.column("Competition", anchor=CENTER, width=50)
        self.tree.column("Hours", anchor=CENTER , width=40)
        self.tree.column("Total Cost(£)", anchor=CENTER , width=80) 

    #headings 
        self.tree.heading("#0", text="", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W )
        self.tree.heading("Weight", text="Weight(kg)", anchor=W)
        self.tree.heading("Training Plan", text ="Training Plan", anchor=CENTER)
        self.tree.heading("Category", text="Weight Category", anchor=CENTER)
        self.tree.heading("Competition", text="Competition" , anchor=CENTER )
        self.tree.heading("Hours", text="Hours", anchor=CENTER)
        self.tree.heading("Total Cost(£)", text="Total Cost", anchor=CENTER)

        self.tree.tag_configure('oddrow', background='white')
        self.tree.tag_configure('evenrow', background='lightblue')

        athlete_delete = Button(self, text="Delete", font=('serif',10), fg='black', command = self.delete_data ) #deletes the user data (front end only)
        athlete_delete.place(x=170, y=380)

        #athlete_edit = Button(self, text="Edit", font=('serif',10), fg='black')
        #athlete_edit.place(x=240, y=380)

        self.refresh = Button(self, text= "Show / Refresh Data", font=('serif', 10), fg= 'black', command = self.insert_treeview)
        self.refresh.place(x=350,y=65)

    def insert_treeview(self):
        
        for item in self.tree.get_children():
            self.tree.delete(item)

        global count
        count = 0
        
        data = query_database()

        for record in data:
            if count % 2 == 0:
                self.tree.insert(parent='', index='end', iid = count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags =('evenrow',))
            else:
                self.tree.insert(parent='', index='end', iid = count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags =('oddrow',))
            count += 1

    #def deleteRecord(self):

        #con = sqlite3.connect("athlete.db")
        #c = con.cursor()
        #c.execute("DELETE FROM athlete WHERE count = ?",(1))
        #con.commit()
        #con.close()
        
    #def save_user(name, weight, training_plan, category, competition, hours, total_cost):

        #con = sqlite3.connect("athlete.db")
        #c = con.cursor()
        
        #c.execute("INSERT INTO athlete VALUES (?, ?, ?, ?, ?, ?, ?)", (name, weight, training_plan, category, competition, hours, total_cost))
        #con.commit()
        #con.close()
     
         
    def delete_data(self):
         
        try: 
            user = self.tree.selection()[0]
            print(user)
            messageDelete = messagebox.askyesno("Please Confirm","Do you want to delete this record?")
            if messageDelete > 0:
                self.tree.delete(user)
                #self.deleteRecord(user)
        except Exception as e:
            print(e)


window = Window()
window.mainloop()
