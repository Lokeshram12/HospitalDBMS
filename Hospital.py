from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


def fun(args):
    print(args)

# main window frame with title

class Hospital:



    def __init__(self,root):

        ### variables ###

        self.root=root
        self.Pat_ID=StringVar()
        self.Pat_ID2=StringVar()
        self.Name=StringVar()
        self.Diagnosis=StringVar()
        self.Address=StringVar()
        self.Doc_ID=StringVar()
        self.Hosp_ID=StringVar()
        self.Checkup_Date=StringVar()
        self.Gender=StringVar()
        self.Rel_Name=StringVar()
        self.Phone=StringVar()
        self.Relation=StringVar()

        self.Doc_ID=StringVar()
        self.Doc_Name=StringVar()
        self.Qual=StringVar()
        self.Salary=StringVar()

        self.MCode=StringVar()
        self.qty=StringVar()

        
            

    def home_page(self):
        
        self.root.title("Hospital Management System")
        self.root.geometry("1540x780+0+0")
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="purple",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        


        ##################### buttons frame ###########

        Buttonframe = Frame(self.root,bd=20,relief=RIDGE,bg="cyan")
        Buttonframe.place(x=0,y=130,width=1540,height=650)

        b1 = Button(Buttonframe, text = "Admin",
                    background = "red", fg = "white",font=("times new roman",50,"bold"),command=lambda: [lbltitle.destroy(),Buttonframe.destroy(),self.admin_page_2()])
        b1.pack(side = TOP, expand = True, fill = BOTH,pady=5,padx=5)

        # Button 2
        b2 = Button(Buttonframe, text = "Reception",
                    background = "blue", fg = "white",font=("times new roman",50,"bold"),command=lambda: [lbltitle.destroy(),Buttonframe.destroy(),self.rec_page_2()])
        b2.pack(side = TOP, expand = True, fill = BOTH,pady=5,padx=5)
        
        # Button 3
        b3 = Button(Buttonframe, text = "Exit",
                    background = "green", fg = "white",font=("times new roman",50,"bold"),command=self.root.destroy)
        b3.pack(side = TOP, expand = True, fill = BOTH,pady=5,padx=5)




    def admin_page_2(self):
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Admin System",fg="purple",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

         ########### Data Frame #############
        Dataframe = Frame(self.root,bd=20,relief=RIDGE,bg="cyan")
        Dataframe.place(x=0,y=130,width=1540,height=650)

        ############ Button Frame ###########
        
        Buttonframe = Frame(Dataframe,bd=5,relief=RAISED,bg="brown")
        Buttonframe.place(x=0,y=0,width=100,height=50)

        ########### Back Button #############

        b1 = Button(Buttonframe, text = "< Back",
        background = "red", fg = "white",font=("times new roman",10,"bold"),command=lambda: [lbltitle.destroy(),Buttonframe.destroy(),self.home_page()])
        b1.pack(fill=BOTH,side=BOTTOM)

        ########### Admin Login Form #############

        usernameLabel = Label(Dataframe, text="Admin User Name",background = "red", fg = "white",font=("times new roman",10,"bold")).place(x=480,y=150)
        username = StringVar()
        usernameEntry = Entry(Dataframe, textvariable=username).place(x=600,y=150)  

        passwordLabel = Label(Dataframe,text="Admin Password",background = "red", fg = "white",font=("times new roman",10,"bold")).place(x=480,y=180)  
        password = StringVar()
        passwordEntry = Entry(Dataframe, textvariable=password, show='*').place(x=600,y=180)  

        #login button
        loginButton = Button(Dataframe, text="Login",background = "red", fg = "white",font=("times new roman",10,"bold"), command=lambda:self.validateLogin(username,password)).place(x=500,y=210)




    def admin_page_3(self):

        ##################### buttons frame ###########

        Buttonframe = Frame(self.root,bd=20,relief=RIDGE,bg="cyan")
        Buttonframe.place(x=0,y=130,width=1540,height=650)

        # Button 1

        b1 = Button(Buttonframe, text = "Add Doctor Details",
                    background = "red", fg = "white",font=("times new roman",40,"bold"),command=lambda: [Buttonframe.destroy(),self.rec_adddoc()])
        b1.pack(side = TOP, expand = True, fill = BOTH,pady=5,padx=5)

        # Button 2

        b2 = Button(Buttonframe, text = "Generate Prescription/Bills",
                    background = "red", fg = "white",font=("times new roman",40,"bold"),command=lambda: [Buttonframe.destroy(),self.rec_bill()])
        b2.pack(side = TOP, expand = True, fill = BOTH,pady=5,padx=5)
        
        # Button 3
        
        b3 = Button(Buttonframe, text = "Log Out",
                    background = "green", fg = "white",font=("times new roman",40,"bold"),command=lambda: [Buttonframe.destroy(),self.home_page()])
        b3.pack(side = TOP, expand = True, fill = BOTH,pady=5,padx=5)




    def rec_page_2(self):

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Reception",fg="purple",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

         ########### Data Frame #############
        Dataframe = Frame(self.root,bd=20,relief=RIDGE,bg="cyan")
        Dataframe.place(x=0,y=130,width=1540,height=650)

        ############ Button Frame ###########
        
        Buttonframe = Frame(Dataframe,bd=5,relief=RAISED,bg="brown")
        Buttonframe.place(x=0,y=0,width=100,height=50)

        ########### Back Button #############

        b1 = Button(Buttonframe, text = "< Back",
        background = "red", fg = "white",font=("times new roman",10,"bold"),command=lambda: [lbltitle.destroy(),Buttonframe.destroy(),self.home_page()])
        b1.pack(fill=BOTH,side=BOTTOM)

        ########### Staff Login Form #############

        usernameLabel = Label(Dataframe, text="Staff User Name",background = "red", fg = "white",font=("times new roman",10,"bold")).place(x=480,y=150)
        username = StringVar()
        usernameEntry = Entry(Dataframe, textvariable=username).place(x=600,y=150)  

        passwordLabel = Label(Dataframe,text="Staff Password",background = "red", fg = "white",font=("times new roman",10,"bold")).place(x=480,y=180)  
        password = StringVar()
        passwordEntry = Entry(Dataframe, textvariable=password, show='*').place(x=600,y=180)  

        #login button
        loginButton = Button(Dataframe, text="Login",background = "red", fg = "white",font=("times new roman",10,"bold"), command=lambda:[lbltitle.destroy(),Dataframe.destroy(),self.validateLogin2(username,password)]).place(x=500,y=210)




    def rec_page_3(self):

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Reception",fg="purple",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        ##################### buttons frame ###########

        Buttonframe = Frame(self.root,bd=20,relief=RIDGE,bg="cyan")
        Buttonframe.place(x=0,y=130,width=1540,height=650)

        b1 = Button(Buttonframe, text = "Show All",
                    background = "red", fg = "white",font=("times new roman",40,"bold"),command=lambda: [Buttonframe.destroy(),self.rec_showtable()])
        b1.pack(side = TOP, expand = True, fill = BOTH,pady=5,padx=5)

        # Button 2
        b2 = Button(Buttonframe, text = "Add New Patient",
                    background = "red", fg = "white",font=("times new roman",40,"bold"),command=lambda: [Buttonframe.destroy(),self.rec_addnew()])
        b2.pack(side = TOP, expand = True, fill = BOTH,pady=5,padx=5)
        
        # Button 3
        b3 = Button(Buttonframe, text = "Find",
                    background = "red", fg = "white",font=("times new roman",40,"bold"),command=lambda: [Buttonframe.destroy(),self.rec_find()])
        b3.pack(side = TOP, expand = True, fill = BOTH,pady=5,padx=5)

        # Button 5
        b5 = Button(Buttonframe, text = "Log Out",
                    background = "green", fg = "white",font=("times new roman",40,"bold"),command=lambda: [Buttonframe.destroy(),self.home_page()])
        b5.pack(side = TOP, expand = True, fill = BOTH,pady=5,padx=5)
        


    def rec_showtable(self):

        ########### Data Frame #############

        Dataframe = Frame(self.root,bd=20,relief=RIDGE,bg="cyan")
        Dataframe.place(x=0,y=130,width=1540,height=650)

        ############ Button Frame ###########
        
        Buttonframe = Frame(Dataframe,bd=5,relief=RAISED,bg="brown")
        Buttonframe.place(x=0,y=0,width=100,height=50)

        ########### Back Button #############

        b1 = Button(Buttonframe, text = "< Back",
        background = "red", fg = "white",font=("times new roman",10,"bold"),command=lambda: [Buttonframe.destroy(),self.rec_page_3()])
        b1.pack(fill=BOTH,side=BOTTOM)

        ########### Scroll Bar #############

        scroll_x=ttk.Scrollbar(Dataframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Dataframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Dataframe,column=("Pat_ID","Name","Diagnosis","Address","Hosp_ID","Doc_ID","Checkup_Date","Gender"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("Pat_ID",text="Patient ID")
        self.hospital_table.heading("Name",text="Patient Name")
        self.hospital_table.heading("Diagnosis",text="Diagnosis")
        self.hospital_table.heading("Address",text="Address")
        self.hospital_table.heading("Hosp_ID",text="Hospital ID")
        self.hospital_table.heading("Doc_ID",text="Doctor ID")
        self.hospital_table.heading("Checkup_Date",text="Checkup Date")
        self.hospital_table.heading("Gender",text="Gender")

        self.hospital_table["show"]="headings"
        self.hospital_table.place(x=0,y=50,width=1485,height=540)

        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM PATIENT")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()



    ######## patient and dependents page ########

    def rec_addnew(self):

        ########### Data Frame #############

        Dataframe1 = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe1.place(x=0,y=130,width=770,height=650)

        ########### Data Frame #############

        Dataframe2 = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe2.place(x=770,y=130,width=770,height=650)

        ############ Button Frame ###########
        
        Buttonframe = Frame(Dataframe1,bd=5,relief=RAISED,bg="brown")
        Buttonframe.grid(row=0,column=1)

        ########### Back Button #############

        b1 = Button(Buttonframe, text = "< Back",
        background = "red", fg = "white",font=("times new roman",10,"bold"),command=lambda: [Dataframe1.destroy(),Dataframe2.destroy(),self.rec_page_3()])
        b1.pack(fill=BOTH,side=BOTTOM)

        ########### Add new record form ##########

        lblPatID=Label(Dataframe1,text="Patient ID",font=("arial",12,"bold"),padx=2,pady=6).grid(row=0,column=5)
        txtPatID=Entry(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.Pat_ID).grid(row=0,column=6,sticky=W)

        lblName=Label(Dataframe1,text="Patient Name",font=("arial",12,"bold"),padx=2,pady=6).grid(row=1,column=5)
        txtName=Entry(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.Name).grid(row=1,column=6,sticky=W)

        lblName=Label(Dataframe1,text="Diagnosis",font=("arial",12,"bold"),padx=2,pady=6).grid(row=2,column=5)
        txtDiagnosis=Entry(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.Diagnosis).grid(row=2,column=6,sticky=W)

        lblName=Label(Dataframe1,text="Address",font=("arial",12,"bold"),padx=2,pady=6).grid(row=3,column=5)
        txtAddress=Entry(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.Address).grid(row=3,column=6,sticky=W)

        lblName=Label(Dataframe1,text="Hospital ID",font=("arial",12,"bold"),padx=2,pady=6).grid(row=4,column=5)
        txtHosp_ID=Entry(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.Hosp_ID).grid(row=4,column=6,sticky=W)

        lblName=Label(Dataframe1,text="Doctor ID",font=("arial",12,"bold"),padx=2,pady=6).grid(row=5,column=5)
        txtDoc_ID=Entry(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.Doc_ID).grid(row=5,column=6,sticky=W)

        lblName=Label(Dataframe1,text="Checkup Date",font=("arial",12,"bold"),padx=2,pady=6).grid(row=6,column=5)
        txtCheckup_Date=Entry(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.Checkup_Date).grid(row=6,column=6,sticky=W)

        lblName=Label(Dataframe1,text="Gender",font=("arial",12,"bold"),padx=2,pady=6).grid(row=7,column=5)
        comGender=ttk.Combobox(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.Gender)
        comGender["values"]=("M","F")
        comGender.grid(row=7,column=6,sticky=W)

        b2 = Button(Dataframe1, text = "Submit",
        background = "red", fg = "white",font=("times new roman",10,"bold"),command=lambda: [Buttonframe.destroy(),self.insert1()])
        b2.grid(row=8,column=6,sticky=W)

        b3 = Button(Dataframe1, text = "Update",
        background = "red", fg = "white",font=("times new roman",10,"bold"),command=lambda: [Buttonframe.destroy(),self.rec_update()])
        b3.grid(row=8,column=7,sticky=W)

        ########## Add Relatives of Patient ###########

        lblPatID2=Label(Dataframe2,text="Patient ID",font=("arial",12,"bold"),padx=2,pady=6).grid(row=0,column=8)
        txtPatID2=Entry(Dataframe2,font=("arial",12,"bold"),width=33,textvariable=self.Pat_ID2).grid(row=0,column=9,sticky=W)

        lblName2=Label(Dataframe2,text="Relative Name",font=("arial",12,"bold"),padx=2,pady=6).grid(row=1,column=8)
        txtName2=Entry(Dataframe2,font=("arial",12,"bold"),width=33,textvariable=self.Rel_Name).grid(row=1,column=9,sticky=W)

        lblPhone=Label(Dataframe2,text="Phone",font=("arial",12,"bold"),padx=2,pady=6).grid(row=2,column=8)
        txtPhone=Entry(Dataframe2,font=("arial",12,"bold"),width=33,textvariable=self.Phone).grid(row=2,column=9,sticky=W)

        lblRelation=Label(Dataframe2,text="Relation",font=("arial",12,"bold"),padx=2,pady=6).grid(row=3,column=8)
        txtRelation=Entry(Dataframe2,font=("arial",12,"bold"),width=33,textvariable=self.Relation).grid(row=3,column=9,sticky=W)

        b4 = Button(Dataframe2, text = "Submit",
        background = "red", fg = "white",font=("times new roman",10,"bold"),command=lambda: [Buttonframe.destroy(),self.insert2()])
        b4.grid(row=4,column=9,sticky=W)




    #### contains actual sql query for patient insertion operation ####

    def insert1(self):

        if self.Name.get()=="" or self.Address.get()=="" or self.Diagnosis.get() =="" or self.Gender.get()=="" or self.Hosp_ID.get()=="" or self.Pat_ID.get()=="" or self.Checkup_Date.get()=="" or self.Doc_ID.get()=="":
            messagebox.showerror("Error","One or More Fields are empty !")
        else:    
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="project")
            my_cursor=conn.cursor()
            try:
                my_cursor.execute("INSERT INTO PATIENT VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(self.Pat_ID.get(),self.Name.get(),self.Diagnosis.get(),self.Address.get(),self.Hosp_ID.get(),self.Doc_ID.get(),self.Checkup_Date.get(),self.Gender.get()))
            except:
                messagebox.showerror("Sql Error","Duplicate / constraint violation !")
            finally:
                self.rec_addnew()
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for i in rows:
                    self.hospital_table.insert("",END,values=i)
            conn.commit()
            messagebox.showinfo("Success","Inserted !")
            self.rec_showtable()
            conn.close()
            self.clearBuffer()
        
    


    ##### contains actual query for relative record insertion ####

    def insert2(self):

        if self.Pat_ID2.get() =="" or self.Rel_Name.get() =="" or self.Phone.get() =="" or self.Relation.get() =="":
            messagebox.showerror("Error","One or More Fields are empty in the dependents form !")
        else:    
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="project")
            my_cursor=conn.cursor()
            try:
                my_cursor.execute("INSERT INTO RELATIVE VALUES(%s,%s,%s,%s)",(self.Pat_ID2.get(),self.Rel_Name.get(),self.Phone.get(),self.Relation.get()))
            except:
                messagebox.showerror("Sql Error","Duplicate / constraint violation !")
            finally:
                self.addnew()
            conn.commit()
            my_cursor.execute("SELECT * FROM RELATIVE WHERE PAT_ID = %s AND RELATIVENAME = %s",(self.Pat_ID2.get(),self.Rel_Name.get()))
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                messagebox.showinfo("Success","Inserted")
            else:
                messagebox.showerror("Error","Patient does not exist or referencial contraint clash")
            conn.commit()
            conn.close()
            self.clearBuffer()
        self.rec_addnew()




    #### find a patient's detail ####

    def rec_find(self):

        ########### Data Frame #############

        Dataframe1 = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe1.place(x=0,y=130,width=1540,height=200)

        ########### Data Frame #############

        Dataframe2 = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe2.place(x=0,y=215,width=1540,height=650)

        ############ Button Frame ###########
        
        Buttonframe = Frame(Dataframe1,bd=5,relief=RAISED,bg="brown")
        Buttonframe.grid(row=0,column=1)

        ########### Back Button #############

        b1 = Button(Buttonframe, text = "< Back",
        background = "red", fg = "white",font=("times new roman",10,"bold"),command=lambda: [Buttonframe.destroy(),self.rec_page_3()])
        b1.pack(fill=BOTH,side=BOTTOM)

        ########### find by patient id #######

        lblPatID=Label(Dataframe1,text="Enter Patient ID",font=("arial",12,"bold"),padx=2,pady=6).grid(row=0,column=2)
        txtPatID=Entry(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.Pat_ID).grid(row=0,column=3,sticky=W)
        b2 = Button(Dataframe1, text = "Submit",
        background = "red", fg = "white",font=("times new roman",10,"bold"),command=lambda: [self.findPatient()])
        b2.grid(row=0,column=4,sticky=W)

        ########### Scroll Bar #############

        scroll_x=ttk.Scrollbar(Dataframe2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Dataframe2,orient=VERTICAL)
        self.hospital_table2=ttk.Treeview(Dataframe2,column=("Pat_ID","Name","Diagnosis","Address","Hosp_ID","Doc_ID","Checkup_Date","Gender","Relative_Name","Phone","Relation"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=TOP,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table2.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table2.yview)

        self.hospital_table2.heading("Pat_ID",text="Patient ID")
        self.hospital_table2.heading("Name",text="Patient Name")
        self.hospital_table2.heading("Diagnosis",text="Diagnosis")
        self.hospital_table2.heading("Address",text="Address")
        self.hospital_table2.heading("Hosp_ID",text="Hospital ID")
        self.hospital_table2.heading("Doc_ID",text="Doctor ID")
        self.hospital_table2.heading("Checkup_Date",text="Checkup Date")
        self.hospital_table2.heading("Gender",text="Gender")
        self.hospital_table2.heading("Relative_Name",text="Relative Name")
        self.hospital_table2.heading("Phone",text="Phone")
        self.hospital_table2.heading("Relation",text="Relation")

        self.hospital_table2["show"]="headings"
        self.hospital_table2.place(x=0,y=50,width=1485,height=540)


            

    ######## Contains query to update an exisiting patient detail ########

    def rec_update(self):
        
        if self.Name.get()=="" or self.Address.get()=="" or self.Diagnosis.get() =="" or self.Gender.get()=="" or self.Hosp_ID.get()=="" or self.Pat_ID.get()=="" or self.Checkup_Date.get()=="" or self.Doc_ID.get()=="":
            messagebox.showerror("Error"," Cant update null values (one or more fields are empty) !")
            self.rec_addnew()
        else:   
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="project")
            my_cursor=conn.cursor()
            try:
                my_cursor.execute("UPDATE PATIENT SET NAME=%s,DIAGNOSIS=%s,ADDRESS=%s,CHECKUP_DATE=%s,GENDER=%s WHERE PAT_ID=%s",(self.Name.get(),self.Diagnosis.get(),self.Address.get(),self.Checkup_Date.get(),self.Gender.get(),self.Pat_ID.get()))
            except:
                messagebox.showerror("Sql Error"," Duplicate / constraint violation !")
            finally:
                self.rec_addnew()
            rows=my_cursor.rowcount
            print(rows)
            if (rows) == 0 or (rows) == -1:
                messagebox.showerror("Error"," Does not exist !")
            else:
                messagebox.showinfo("Success","Updated !")
                conn.commit()
                conn.close()
            self.clearBuffer()
            self.rec_addnew()
            ## to check ... WIP ... not working at the moment !! ##




    #### Query to handle the find page ####

    def findPatient(self):

        if self.Pat_ID.get() == "":
            messagebox.showerror("Error","Please Enter Something")
            self.rec_find()
        
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="project")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT P.*,R.RELATIVENAME,R.PHONE,R.RELATION FROM PATIENT P,RELATIVE R WHERE P.PAT_ID = R.PAT_ID AND P.PAT_ID = %s",[self.Pat_ID.get()])
            rows=my_cursor.fetchall()
            if len(rows) != 0:
                messagebox.showinfo("Success","Found !")
                if len(rows)!=0:
                    self.hospital_table2.delete(*self.hospital_table2.get_children())
                    for i in rows:
                        self.hospital_table2.insert("",END,values=i)                 
                conn.commit()
                conn.close()
            else:
                messagebox.showerror("Error","Patient does not exist or relatives not found ")
                self.rec_find()
                




    #### to clear variables values after insertion / update or find
    
    def clearBuffer(self):
        
        self.Name.set("")
        self.Address.set("")
        self.Diagnosis.set("")
        self.Gender.set("")
        self.Hosp_ID.set("")
        self.Pat_ID.set("")
        self.Pat_ID2.set("")
        self.Checkup_Date.set("")
        self.Doc_ID.set("")
        self.Rel_Name.set("")
        self.Phone.set("")
        self.Relation.set("")
        self.Doc_ID.set("")
        self.Doc_Name.set("")
        self.Qual.set("")
        self.Salary.set("")
        self.MCode.set("")
        self.qty.set("")


    
    #### validates reception staff ####

    def validateLogin2(self,username,password):

        if username.get()=="staff" and password.get()=="s" :
            messagebox.showinfo("Success !","Welcome "+ username.get())
            self.rec_page_3()

        else:
            self.rec_page_2()
            messagebox.showerror("Error","The credentials are incorrect or unauthorized access")



    #### validates admin ####

    def validateLogin(self,username,password):
        
        if username.get()=="ps" and password.get()=="6" :
            messagebox.showinfo("Success !","Admin has been authenticated successfully")
            self.admin_page_3()

        else:
            self.admin_page_2()
            messagebox.showerror("Error","The credentials are incorrect")



    #### doctor details form ####

    def rec_adddoc(self):
        
        ########### Data Frame #############

        Dataframe1 = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe1.place(x=0,y=130,width=770,height=650)

        ########### Data Frame #############

        Dataframe2 = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe2.place(x=770,y=130,width=770,height=650)

        ############ Button Frame ###########
        
        Buttonframe = Frame(Dataframe1,bd=5,relief=RAISED,bg="brown")
        Buttonframe.grid(row=0,column=1)

        ########### Back Button #############

        b1 = Button(Buttonframe, text = "< Back",
        background = "red", fg = "white",font=("times new roman",10,"bold"),command=lambda: [Dataframe1.destroy(),Dataframe2.destroy(),self.admin_page_3()])
        b1.pack(fill=BOTH,side=BOTTOM)

        ########### Add new doctor ##########

        lblDocID=Label(Dataframe1,text="Doctor ID",font=("arial",12,"bold"),padx=2,pady=6).grid(row=0,column=5)
        txtDocID=Entry(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.Doc_ID).grid(row=0,column=6,sticky=W)

        lblDoc=Label(Dataframe1,text="Doctor Name",font=("arial",12,"bold"),padx=2,pady=6).grid(row=1,column=5)
        txtDoc=Entry(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.Doc_Name).grid(row=1,column=6,sticky=W)

        lblQual=Label(Dataframe1,text="Qualification",font=("arial",12,"bold"),padx=2,pady=6).grid(row=2,column=5)
        txtQual=ttk.Combobox(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.Qual)
        txtQual["values"]=("Surgeon","ENT Specialist","Dermatoligist","Pediatrician")
        txtQual.grid(row=2,column=6,sticky=W)

        lblSalary=Label(Dataframe1,text="Salary",font=("arial",12,"bold"),padx=2,pady=6).grid(row=3,column=5)
        txtSalary=Entry(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.Salary).grid(row=3,column=6,sticky=W)

        lblHosp_ID=Label(Dataframe1,text="Hospital ID",font=("arial",12,"bold"),padx=2,pady=6).grid(row=4,column=5)
        txtHosp_ID=Entry(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.Hosp_ID).grid(row=4,column=6,sticky=W)

        b2 = Button(Dataframe1, text = "Submit",
        background = "red", fg = "white",font=("times new roman",10,"bold"),command=lambda: [Buttonframe.destroy(),self.insert3()])
        b2.grid(row=8,column=6,sticky=W)

        #### show all doctors on side pane ####

        ########### Scroll Bar #############

        scroll_x=ttk.Scrollbar(Dataframe2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Dataframe2,orient=VERTICAL)
        self.doc_table=ttk.Treeview(Dataframe2,column=("Doc_ID","Doc_Name","Qual","Salary","Hosp_ID","Bonus"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.doc_table.xview)
        scroll_y=ttk.Scrollbar(command=self.doc_table.yview)

        self.doc_table.heading("Doc_ID",text="Doctor ID")
        self.doc_table.heading("Doc_Name",text="Doctor Name")
        self.doc_table.heading("Qual",text="Qualification")
        self.doc_table.heading("Salary",text="Salary")
        self.doc_table.heading("Hosp_ID",text="Hospital ID")
        self.doc_table.heading("Bonus",text="Bonus")

        self.doc_table["show"]="headings"
        self.doc_table.place(x=0,y=50,width=710,height=540)

        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM DOCTORS")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.doc_table.delete(*self.doc_table.get_children())
            for i in rows:
                self.doc_table.insert("",END,values=i)
            conn.commit()
        conn.close()



    ##### for handling prescriptions / bills #####

    def  rec_bill(self):

        ########### Data Frame #############

        Dataframe1 = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe1.place(x=0,y=130,width=770,height=650)

        ########### Data Frame #############

        Dataframe2 = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe2.place(x=770,y=130,width=770,height=330)

        ########### Data Frame #############

        Dataframe3 = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe3.place(x=770,y=460,width=770,height=650)

        ############ Button Frame ###########
        
        Buttonframe = Frame(Dataframe1,bd=5,relief=RAISED,bg="brown")
        Buttonframe.grid(row=0,column=1)

        ########### Back Button #############

        b1 = Button(Buttonframe, text = "< Back",
        background = "red", fg = "white",font=("times new roman",10,"bold"),command=lambda: [Dataframe1.destroy(),Dataframe2.destroy(),self.admin_page_3()])
        b1.pack(fill=BOTH,side=BOTTOM)

        ########## form to generate bills #########

        lblPatID=Label(Dataframe1,text="Patient ID",font=("arial",12,"bold"),padx=2,pady=6).grid(row=0,column=5)
        txtPatID=Entry(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.Pat_ID).grid(row=0,column=6,sticky=W)

        lblMed=Label(Dataframe1,text="Medicine Code",font=("arial",12,"bold"),padx=2,pady=6).grid(row=1,column=5)
        txtMed=Entry(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.MCode).grid(row=1,column=6,sticky=W)

        lblQty=Label(Dataframe1,text="Quantity",font=("arial",12,"bold"),padx=2,pady=6).grid(row=3,column=5)
        txtQty=Entry(Dataframe1,font=("arial",12,"bold"),width=33,textvariable=self.qty).grid(row=3,column=6,sticky=W)

        b2 = Button(Dataframe1, text = "Generate",
        background = "red", fg = "white",font=("times new roman",10,"bold"),command=lambda: [Buttonframe.destroy(),self.insert4()])
        b2.grid(row=8,column=6,sticky=W)


        ##### display medicine stock on right upper pane ####

        ########### Scroll Bar #############

        scroll_x=ttk.Scrollbar(Dataframe2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Dataframe2,orient=VERTICAL)
        self.med_table=ttk.Treeview(Dataframe2,column=("MCode","MName","Expiry","MPrice"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=TOP,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.med_table.xview)
        scroll_y=ttk.Scrollbar(command=self.med_table.yview)

        self.med_table.heading("MCode",text="Medicine Code")
        self.med_table.heading("MName",text="Medicine Name")
        self.med_table.heading("Expiry",text="Expiry")
        self.med_table.heading("MPrice",text="Price")

        self.med_table["show"]="headings"
        self.med_table.pack()

        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM MEDICINE")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.med_table.delete(*self.med_table.get_children())
            for i in rows:
                self.med_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        ##### display all bills on right below plane ####

        ########### Scroll Bar #############

        scroll_x=ttk.Scrollbar(Dataframe3,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Dataframe3,orient=VERTICAL)
        self.bill_table=ttk.Treeview(Dataframe3,column=("Pat_ID","MCode","Dosage","to_pay"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=TOP,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.bill_table.xview)
        scroll_y=ttk.Scrollbar(command=self.bill_table.yview)

        self.bill_table.heading("Pat_ID",text="Patient ID")
        self.bill_table.heading("MCode",text="Medicine Code")
        self.bill_table.heading("Dosage",text="Dosage")
        self.bill_table.heading("to_pay",text="Total Amount")

        self.bill_table["show"]="headings"
        self.bill_table.pack()

        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM BILL")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.bill_table.delete(*self.bill_table.get_children())
            for i in rows:
                self.bill_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    ###### insert query handler for doctors records ######

    def insert3(self):

        if self.Doc_ID.get() == "" or self.Doc_Name.get() == "" or self.Qual.get() == "" or self.Salary.get() == "" or self.Hosp_ID.get() == "":
            messagebox.showerror("Error","One or More Fields are empty !")
        else:    
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="project")
            my_cursor=conn.cursor()
            try:
                my_cursor.execute("INSERT INTO DOCTORS(DOC_ID,DNAME,QUALIFICATION,SALARY,HOSP_ID) VALUES(%s,%s,%s,%s,%s)",(self.Doc_ID.get(),self.Doc_Name.get(),self.Qual.get(),self.Salary.get(),self.Hosp_ID.get()))
            except:
                messagebox.showerror("SQL Error","Duplicate / constraint violation !")
            finally:
                self.rec_adddoc()
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                messagebox.showerror("SQL Error","Query not executed !")
            else:
                conn.commit()
                messagebox.showinfo("Success","Inserted !")
        self.rec_adddoc()
        conn.close()
        self.clearBuffer()



    ###### query handler function for bill insertion ######

    def insert4(self):

        if self.Pat_ID.get() == "" or self.MCode.get() == "" or self.qty.get() == "":
            messagebox.showerror("Error","One or More Fields are empty !")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="project")
            my_cursor=conn.cursor()
            try:
                my_cursor.execute("CALL PRO(%s,%s,%s)",(self.Pat_ID.get(),self.MCode.get(),self.qty.get()))
            except:
                messagebox.showerror("Sql Error","Duplicate / Constraint violation !")
            finally:
                self.rec_bill()
            rows=my_cursor.fetchall()
            conn.commit()
            messagebox.showinfo("Success","Inserted !")
        self.rec_bill()
        conn.close()
        self.clearBuffer()









########## Driver Code ##########    

def main():
    root=Tk()
    ob=Hospital(root)
    ob.home_page()
    root.mainloop()


if __name__ == "__main__":
    main()
