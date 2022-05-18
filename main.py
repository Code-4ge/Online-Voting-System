from tkinter import *
from PIL import ImageTk, Image 
from tkinter import messagebox
from tkinter.ttk import Combobox
from settings import *
import database as model
import webbrowser


root = Tk()
root.geometry("900x500")
root.resizable(0, 0)
root.title("Voting Machine")
root.iconbitmap('./Assets/icon.ico')
root.configure(background="white")


homeImg = ImageTk.PhotoImage(Image.open("./Assets/homeImg.jpg")) 

model.connect()

def voterLogin():
    voterId = StringVar()
    loginFrame = Frame()
    loginFrame.place(x=0, y=0, width="500", height="500")
    loginFrame.configure(background="white")

    label = Label(loginFrame, text="Login to Vote", font=(ARIAL, 20, "bold"), bg="white", fg=HIGHLIGHT_TEXT)
    label.place(x=150, y=50)

    label0 = Label(loginFrame, text="Voter Id ", font=(ARIAL, 12, "normal"), bg="white")
    label0.place(x=100, y=150)
    input0 = Entry(loginFrame, font=(ARIAL, 12), textvariable=voterId, border=0, bg="#f0f0f0")
    input0.place(x=200, y=150, width="200", height="25")

    def Login():
        if(voterId.get() == ""):
            messagebox.showwarning('Voting System Message', 'Field are required')

        else:
            result = model.findByVoterId(voterId.get())
            if(result == None):
                messagebox.showerror('Voting System Message', 'Wrong Credentials')
            else:
                dashboard(voterId.get())

        voterId.set("")

    Login_btn = Button(loginFrame, text="Login", font=(ARIAL, 13, "bold"), command=Login, border=0, bg=HIGHLIGHT_BG, fg="white")
    Login_btn.place(x=200, y=250, width=100, height=50)
    back_btn = Button(loginFrame, text="< Back", font=(ARIAL, 10, "normal"), command=VoterHome, border=0, bg="white", fg="grey")
    back_btn.place(x=0, y=0, width=100, height=50)


def dashboard(voterId):
    poll = StringVar()
    district = StringVar()
    name = StringVar()
    DashboardFrame = Frame()
    DashboardFrame.place(x=0, y=0, width=900, height=500)
    DashboardFrame.configure(background="white")

    result = model.findByVoterId(voterId)
    name.set(result[2])

    IDLabel = Label(DashboardFrame, text=voterId, font=(ARIAL, 13, "normal"), bg="white", fg=HIGHLIGHT_TEXT)
    IDLabel.place(x=10, y=10)

    label = Label(DashboardFrame, text="Your Vote, Your Voice", font=(LUCIDA_CONSOLE, 30, "bold"), bg="white", fg=HIGHLIGHT_BG)
    label.place(x=175, y=50)

    nameLabel = Label(DashboardFrame, text="Hi, "+name.get(), font=(ARIAL, 15, "normal"), bg="white")
    nameLabel.place(x=75, y=150)

    pollLabel = Label(DashboardFrame, text="Select your poll ", font=(ARIAL, 15, "normal"), bg="white")
    pollLabel.place(x=200, y=225)
    pollInput = Combobox(root, values=["BJP", "TMC","SP","AAP"], font=(ARIAL, 13, "normal"), textvariable=poll)
    pollInput.place(x=400, y=225, width=200)
    districtLabel = Label(DashboardFrame, text="Select your Distric", font=(ARIAL, 15, "normal"), bg="white")
    districtLabel.place(x=200, y=275)
    districtInput = Combobox(root, values=["Nashik", "Pune","Mumbai","Jalgaon","Satara"], font=(ARIAL, 13, "normal"), textvariable=district)
    districtInput.place(x=400, y=275, width=200)
    
    def Vote():
        if poll.get()=="" or district.get()=="":
            messagebox.showwarning('Voting System Message','all field are required')

        else:
            result1 = model.findByVoterIdinVote(voterId)
            if(result1 == None):
                if model.submitVote(voterId, poll.get(), district.get()):
                    messagebox.showinfo('Voting System Message', 'Thanks, Vote submited succefully')

                else:
                    messagebox.showwarning('Voting System Message', 'Try again later, Failed to vote')
            
            else:
                messagebox.showwarning('Voting System Message', 'Thanks, but you have voted already')

            poll.set("")
            district.set("")
            name.set("")
            logout()

    Vote_btn = Button(DashboardFrame, text="Vote", font=(ARIAL, 13, "normal"), command=Vote, border=0, bg=HIGHLIGHT_BG, fg="white")
    Vote_btn.place(x=375, y=350, width=150, height=50)
    logOut = Button(DashboardFrame, text="Log Out", font=(ARIAL, 10, "normal"), command=logout, border=0, bg="white", fg="grey")
    logOut.place(x=800, y=0, width=100, height=50)


def voterRegistration():
    voterId = StringVar()
    name = StringVar()
    aadhar = StringVar()
    phone = StringVar()
    gender = StringVar()
    RegistrationFrame = Frame()
    RegistrationFrame.place(x=0, y=0, width="500", height="500")
    RegistrationFrame.configure(background="white")

    label = Label(RegistrationFrame, text="Register to Vote", font=(ARIAL, 20, "bold"), bg="white", fg=HIGHLIGHT_TEXT)
    label.place(x=125, y=50)

    label0 = Label(RegistrationFrame, text="Voter Id ", font=(ARIAL, 12, "normal"), bg="white")
    label0.place(x=30, y=125)
    input0 = Entry(RegistrationFrame, font=(ARIAL, 12), textvariable=voterId, border=0, bg="#f0f0f0")
    input0.place(x=250, y=125, width="200", height="25")

    label1 = Label(RegistrationFrame, text="Full Name ", font=(ARIAL, 12, "normal"), bg="white")
    label1.place(x=30, y=175)
    input1 = Entry(RegistrationFrame, font=(ARIAL, 12), textvariable=name, border=0, bg="#f0f0f0")
    input1.place(x=250, y=175, width="200", height="25")

    label2 = Label(RegistrationFrame, text="Aadhar Card Number", font=(ARIAL, 12, "normal"), bg="white")
    label2.place(x=30, y=225)
    input2 = Entry(RegistrationFrame, font=(ARIAL, 12), textvariable=aadhar, border=0, bg="#f0f0f0")
    input2.place(x=250, y=225, width="200", height="25")

    label3 = Label(RegistrationFrame, text="Mobile Number", font=(ARIAL, 12, "normal"), bg="white")
    label3.place(x=30, y=275)
    input3 = Entry(RegistrationFrame, font=(ARIAL, 12), textvariable=phone, border=0, bg="#f0f0f0")
    input3.place(x=250, y=275, width="200", height="25")

    label4 = Label(RegistrationFrame, text="Gender ", font=(ARIAL, 12, "normal"), bg="white")
    label4.place(x=30, y=325)
    input4=Combobox(RegistrationFrame, values=["Male","Female"], font=(ARIAL, 12, "normal"), textvariable=gender, background="#f0f0f0")
    input4.place(x=250, y=325, width="200", height="25")
    

    def Register():
        if voterId.get() == "" or name.get() == "" or aadhar.get() == "" or phone.get() == "" or gender.get() == "":
            messagebox.showwarning('Voting System Message', 'All field is requird')

        else:
            if len(aadhar.get()) == 12 and len(phone.get()) == 10 and aadhar.get().isdigit() and phone.get().isdigit():
                result = model.findByAadhar(aadhar.get())
                result1 = model.findByVoterId(voterId.get())
                if((result == None) and (result1 == None)):
                    if model.addVoter(voterId.get(), name.get(), aadhar.get(), phone.get(), gender.get()):
                        messagebox.showinfo('Voting System Message', 'Registered as Voter')
                        voterId.set("")
                        name.set("")
                        aadhar.set("")
                        phone.set("")
                        gender.set("")
                        voterLogin()

                    else:
                        messagebox.showwarning('Voting System Message', 'Try again later, Failed to register')

                else:
                    messagebox.showerror('Voting System Message', 'Wrong Credentials')                

            else:
                messagebox.showerror('Voting System Message', 'Aadhar number must be 12 digit and Mobile number must be 10 digit')


    Register_btn = Button(RegistrationFrame, text="Register", font=(ARIAL, 13, "bold"), command=Register, border=0, bg=HIGHLIGHT_BG, fg="white")
    Register_btn.place(x=150, y=390, width=200, height=50)
    back_btn = Button(RegistrationFrame, text="< Back", font=(ARIAL, 10, "normal"), command=VoterHome, border=0, bg="white", fg="grey")
    back_btn.place(x=0, y=0, width=100, height=50)


def AdminRegistration():
    regId = StringVar()
    name = StringVar()
    aadhar = StringVar()
    phone = StringVar()
    gender = StringVar()

    AdminFrame = Frame()
    AdminFrame.place(x=0, y=0, width="500", height="500")
    AdminFrame.configure(background="white")
    label = Label(AdminFrame, text="Register for voting system  ", font=(ARIAL, 20, "bold"), bg="white", fg=HIGHLIGHT_TEXT)
    label.place(x=60, y=50)

    IdLabel = Label(AdminFrame, text="Register Id ", font=(ARIAL, 12, "normal"), bg="white")
    IdLabel.place(x=30, y=125)
    IdInput = Entry(AdminFrame, font=(ARIAL, 12), textvariable=regId, border=0, bg="#f0f0f0")
    IdInput.place(x=250, y=125, width="200", height="25")

    nameLabel = Label(AdminFrame, text="Full Name", font=(ARIAL, 12, "normal"), bg="white")
    nameLabel.place(x=30, y=175)
    nameInput = Entry(AdminFrame, font=(ARIAL, 12), textvariable=name, border=0, bg="#f0f0f0")
    nameInput.place(x=250, y=175, width="200", height="25")

    aadharLabel = Label(AdminFrame, text="Aadhar Card Number", font=(ARIAL, 12, "normal"), bg="white")
    aadharLabel.place(x=30, y=225)
    aadharInput = Entry(AdminFrame, font=(ARIAL, 12), textvariable=aadhar, border=0, bg="#f0f0f0")
    aadharInput.place(x=250, y=225, width="200", height="25")

    phoneLabel = Label(AdminFrame, text="Mobile Number", font=(ARIAL, 12, "normal"), bg="white")
    phoneLabel.place(x=30, y=275)
    phoneInput = Entry(AdminFrame, font=(ARIAL, 12), textvariable=phone, border=0, bg="#f0f0f0")
    phoneInput.place(x=250, y=275, width="200", height="25")

    genderlabel = Label(AdminFrame, text="Gender", font=(ARIAL, 12, "normal"), bg="white")
    genderlabel.place(x=30, y=325)
    genderInput=Combobox(root, values=["Male","Female"], font=("", 12, "normal"), textvariable=gender)
    genderInput.place(x=250, y=325, width="200", height="25")

   
    def Register():
        if regId.get() == "" or name.get() == "" or aadhar.get() == "" or phone.get() == "" or gender.get() == "" :
            messagebox.showwarning('Voting System Message', 'All field is requird')

        else:
            if len(aadhar.get()) == 12 and len(phone.get()) == 10 and aadhar.get().isdigit() and phone.get().isdigit():
                result = model.findByAadharinAdmin(aadhar.get())
                result1 = model.findByRegId(regId.get())
                if((result == None) and (result1 == None)):
                    if(model.addAdmin(regId.get(), name.get(), aadhar.get(), phone.get(), gender.get())):
                        messagebox.showinfo('Voting System Message', 'Registered as Admin')
                        regId.set("")
                        name.set("")
                        aadhar.set("")
                        phone.set("")
                        gender.set("")
                        AdminLogin()

                    else:
                        messagebox.showwarning('Voting System Message', 'Try again later, unable to register admin')

                else:
                    messagebox.showerror('Voting System Message', 'Aadhar number is already register')

            else:
                messagebox.showwarning('Voting System Message', 'Aadhar number must be 12 digit and Mobile number must be 10 digit')

    

    Register_btn = Button(AdminFrame, text="Register", font=(ARIAL, 13, "bold"), command=Register, border=0, bg=HIGHLIGHT_BG, fg="white")
    Register_btn.place(x=175, y=400, width=150, height=50)
    back_btn = Button(AdminFrame, text="< Back", font=(ARIAL, 10, "normal"), command=AdminHome, border=0, bg="white", fg="grey")
    back_btn.place(x=0, y=0, width=100, height=50)


def VoterHome():
    voterFrame = Frame()
    voterFrame.place(x=0, y=0, width="900", height="500")
    voterFrame.configure(background="white")
    login_btn = Button(voterFrame, text="Login", font=(ARIAL, 13, "bold"),command=voterLogin, relief=FLAT, border=0, bg=HIGHLIGHT_BG, fg="white")
    login_btn.place(x=150, y=150, width=150, height=50)
    btn_border = LabelFrame(voterFrame, bd = 0, bg = HIGHLIGHT_BG)
    btn_border.place(x=150, y=250, width=150, height=50)
    reg_btn = Button(btn_border, text="Register", font=(ARIAL, 13, "bold"), command=voterRegistration, relief=FLAT, border=0, bg="white", fg=HIGHLIGHT_BG)
    reg_btn.place(x=1, y=1, width=148, height=48)
    back_btn = Button(voterFrame, text="< Back", font=(ARIAL, 10, "normal"), command=Home, border=0, bg="white", fg="grey")
    back_btn.place(x=0, y=0, width=100, height=50)
    label = Label(voterFrame, text="Your Vote,\nYour Voice", font=(LUCIDA_CONSOLE, 30, "bold"), bg=HIGHLIGHT_BG, fg="white")
    label.place(x=500, y=0, width=400, height=500)



def AdminHome():
    adminFrame = Frame()
    adminFrame.place(x=0, y=0, width="900", height="500")
    adminFrame.configure(background="white")
    login_btn = Button(adminFrame, text="Login", font=(ARIAL, 13, "bold"),command=AdminLogin, relief=FLAT, border=0, bg=HIGHLIGHT_BG, fg="white")
    login_btn.place(x=150, y=150, width=150, height=50)
    btn_border = LabelFrame(adminFrame, bd = 0, bg = HIGHLIGHT_BG)
    btn_border.place(x=150, y=250, width=150, height=50)
    reg_btn = Button(btn_border, text="Register", font=(ARIAL, 13, "bold"), command=AdminRegistration, relief=FLAT, border=0, bg="white", fg=HIGHLIGHT_BG)
    reg_btn.place(x=1, y=1, width=148, height=48)
    back_btn = Button(adminFrame, text="< Back", font=(ARIAL, 10, "normal"), command=Home, border=0, bg="white", fg="grey")
    back_btn.place(x=0, y=0, width=100, height=50)
    label = Label(adminFrame, text="Lorem Ipsum,\nLorem Ipsum", font=(LUCIDA_CONSOLE, 30, "bold"), bg=HIGHLIGHT_BG, fg="white")
    label.place(x=500, y=0, width=400, height=500)

def Home():
    homeFrame = Frame()
    homeFrame.place(x=0, y=0, width="900", height="500")
    homeFrame.configure(background="white")
    photo = Label(homeFrame, image = homeImg)
    photo.place(x=300, y=80, width=600, height=350) 
    label = Label(homeFrame, text="Vote for the Future", font=(LUCIDA_CONSOLE, 30, "bold"), bg="white", fg=HIGHLIGHT_TEXT)
    label.place(x=20, y=100)
    voter_btn = Button(homeFrame, text="Voter ", font=(ARIAL, 13, "normal"), command=VoterHome, relief=FLAT, border=0, bg=HIGHLIGHT_BG)
    voter_btn.place(x=100, y=200, width=150, height=50)
    btn_border = LabelFrame(homeFrame, bd = 0, bg = HIGHLIGHT_BG)
    btn_border.place(x=100, y=300, width=150, height=50)
    admin_btn = Button(btn_border, text="Admin", font=(ARIAL, 13, "normal"), command=AdminHome, relief=FLAT, border=0, bg="white")
    admin_btn.place(x=1, y=1, width=148, height=48)
    about = Label(homeFrame, text="💠", font=(LUCIDA_CONSOLE, 18, "normal"), bg="white", fg="grey")
    about.place(x=860, y=460)
    about.bind("<Button-1>", open_browser)
    


def AdminLogin():
    regId = StringVar()
    LoginFrame = Frame()
    LoginFrame.place(x=0, y=0, width="500", height="500")
    LoginFrame.configure(background="white")

    label = Label(LoginFrame, text="Login to Voting System", font=(ARIAL, 20, "bold"), bg="white", fg=HIGHLIGHT_TEXT)
    label.place(x=100, y=50)

    IdLable = Label(LoginFrame, text="Register Id", font=(ARIAL, 12, "normal"), bg="white")
    IdLable.place(x=100, y=150)
    IdInput = Entry(LoginFrame, font=(ARIAL,12,"normal"), textvariable=regId, border=0, bg="#f0f0f0")
    IdInput.place(x=200, y=150, width="200", height="25")

    def Login():
        if regId.get() == "":
            messagebox.showwarning('Voting System Message', 'Field are required')

        else:
            result = model.findByRegId(regId.get())
            if(result == None):
                messagebox.showerror('Voting System Message', 'Wrong Credentials')
            else:
                AdminDashboard(regId.get())

        regId.set("")

    Login_btn = Button(LoginFrame, text="Login", font=(ARIAL, 13, "bold"), command=Login, border=0, bg=HIGHLIGHT_BG, fg="white")
    Login_btn.place(x=200, y=250, width=100, height=50)
    back_btn = Button(LoginFrame, text="< Back", font=(ARIAL, 10, "normal"), command=AdminHome, border=0, bg="white", fg="grey")
    back_btn.place(x=0, y=0, width=100, height=50)


def AdminDashboard(regId):

    dashboardFrame = Frame()
    dashboardFrame.place(x=0, y=0, width=900, height=500)
    dashboardFrame.configure(background="white")

    admin_name = model.findByRegId(regId)

    menu_bar = Frame(dashboardFrame)
    menu_bar.place(x=0, y=0, width=249, height=500)
    menu_bar.configure(background="#f0f0f0")

    section = Frame(dashboardFrame)
    section.place(x=249, y=0, width=651, height=500)
    section.configure(background="grey")
    votingResults()

    admin = Frame(menu_bar)
    admin.place(x=0, y=0, width=249, height=100)
    admin.configure(background=HIGHLIGHT_BG)

    label = Label(admin, text=regId, font=(ARIAL, 15, "bold", UNDERLINE), bg=HIGHLIGHT_BG, fg="white")
    label.place(x=10, y=25)

    label = Label(admin, text=admin_name[2], font=(LUCIDA_CONSOLE, 13, "normal"), bg=HIGHLIGHT_BG, fg="white")
    label.place(x=10, y=60)

    update_btn = Button(menu_bar, text="Dashboard", font=(ARIAL, 13, "normal"), command=votingResults, border=0, bg="white", fg="grey", anchor="w", padx=30)
    update_btn.place(x=0, y=100, width=249, height=50)

    delete_btn = Button(menu_bar, text="All Record", font=(ARIAL, 13, "normal"), command=showAllRecord, border=0, bg="white", fg="grey", anchor="w", padx=30)
    delete_btn.place(x=0, y=151, width=249, height=50)

    search_btn = Button(menu_bar, text="Search User", font=(ARIAL, 13, "normal"), command=searchUser, border=0, bg="white", fg="grey", anchor="w", padx=30)
    search_btn.place(x=0, y=202, width=249, height=50)

    data_btn = Button(menu_bar, text="Update User Records", font=(ARIAL, 13, "normal"),command=updateUser, border=0, bg="white", fg="grey", anchor="w", padx=30)
    data_btn.place(x=0, y=253, width=249, height=50)

    result_btn = Button(menu_bar, text="Delete User", font=(ARIAL, 13, "normal"),command=deleteUser, border=0, bg="white", fg="grey", anchor="w", padx=30)
    result_btn.place(x=0, y=304, width=249, height=50)

    logOut_btn = Button(menu_bar, text="Log Out", font=(ARIAL, 13, "normal"), command=Home, border=0, bg="white", fg="grey", anchor="w", padx=30)
    logOut_btn.place(x=0, y=355, width=249, height=50)

    space = Label(menu_bar, bg="white")
    space.place(x=0, y=406, width=249, height=100)


def votingResults():
  
    resultFrame = Frame()
    resultFrame.place(x=250, y=0, width=650, height=500)
    resultFrame.configure(background="white")

    total=Label(resultFrame,text="Total vote",font=(LUCIDA_CONSOLE,15,"bold"),bg="white",fg=HIGHLIGHT_TEXT)
    total.place(x=150,y=50)
    party1=Label(resultFrame,text="BJP",font=(LUCIDA_CONSOLE,15,"normal"),bg="white",fg="grey")
    party1.place(x=150,y=150)
    party2=Label(resultFrame,text="TMC",font=(LUCIDA_CONSOLE,15,"normal"),bg="white",fg="grey")
    party2.place(x=150,y=200)
    party3=Label(resultFrame,text="SP",font=(LUCIDA_CONSOLE,15,"normal"),bg="white",fg="grey")
    party3.place(x=150,y=250)
    party4=Label(resultFrame,text="AAP",font=(LUCIDA_CONSOLE,15,"normal"),bg="white",fg="grey")
    party4.place(x=150,y=300)
    
    result = model.getTotalCount()
    t_user = model.getTotalUserCount()
    totalCount=Label(resultFrame,text="{}  /  {}".format(result[0], t_user[0]),font=("",15,"bold"), bg="white")
    totalCount.place(x=400,y=50)

    result1 = model.getPartyCount("BJP")
    count1=Label(resultFrame,text=result1, font=("",15,"bold"),bg="white")
    count1.place(x=400,y=150)

    result1 = model.getPartyCount("TMC")
    count2=Label(resultFrame,text=result1, font=("",15,"bold"),bg="white")
    count2.place(x=400,y=200)

    result1 = model.getPartyCount("SP")
    count3=Label(resultFrame,text=result1, font=("",15,"bold"),bg="white")
    count3.place(x=400,y=250)

    result1 = model.getPartyCount("AAP")
    count4=Label(resultFrame,text=result1, font=("",15,"bold"),bg="white")
    count4.place(x=400,y=300)


def showAllRecord():
    DataFrame = Frame()
    DataFrame.place(x=250, y=0, width=650, height=500)
    DataFrame.configure(background="white")
    name=Label(DataFrame,text="Name",font=(LUCIDA_CONSOLE,13,"bold"),bg="white",fg=HIGHLIGHT_TEXT)
    name.place(x=20,y=20)
    phone=Label(DataFrame,text="Phone No.",font=(LUCIDA_CONSOLE,13,"bold"),bg="white",fg=HIGHLIGHT_TEXT)
    phone.place(x=220,y=20)
    gender=Label(DataFrame,text="Gender",font=(LUCIDA_CONSOLE,13,"bold"),bg="white",fg=HIGHLIGHT_TEXT)
    gender.place(x=365,y=20)
    address=Label(DataFrame,text="Locality",font=(LUCIDA_CONSOLE,13,"bold"),bg="white",fg=HIGHLIGHT_TEXT)
    address.place(x=495,y=20)

    result = model.getallVoters()

    x=20
    y=75
    for r in result:
        nameValue=Label(DataFrame,text=r[0],font=(ARIAL,12,"normal"),bg="white")
        nameValue.place(x=x,y=y)
        x+=200
        phoneValue=Label(DataFrame,text=r[1],font=(ARIAL,12,"normal"),bg="white")
        phoneValue.place(x=x,y=y)
        x+=160
        genderValue=Label(DataFrame,text=r[2],font=(ARIAL,12,"normal"),bg="white")
        genderValue.place(x=x,y=y)
        x+=125
        addressValue=Label(DataFrame,text=r[3],font=(ARIAL,12,"normal"),bg="white")
        addressValue.place(x=x,y=y)
        y+=50
        x=20


def searchUser():
    aadhar = StringVar()
    SearchFrame = Frame()
    SearchFrame.place(x=250, y=0, width=650, height=500)
    SearchFrame.configure(background="white")
    aadharLabel = Label(SearchFrame, text="Aadhar Card Number", font=("", 13, "normal"), bg="white")
    aadharLabel.place(x=50, y=55, height=30)
    aadharInput = Entry(SearchFrame, textvariable=aadhar,font=("",12,"normal"), bg="#f0f0f0", border=0)
    aadharInput.place(x=230, y=55, width=170, height=30)
    def search():
        if aadhar.get() == "" or len(aadhar.get()) != 12 or not aadhar.get().isdigit():
            messagebox.showwarning('Voting System Message', '🎱 Field is requird\n🎱 Aadhar number length must be 12 digit')

        else:
            user = model.getUserByAadhar(aadhar.get())
            if(user == None):
                messagebox.showinfo('Voting System Message', 'No such User')

            else:
                DataFrame = Frame(SearchFrame)
                DataFrame.place(x=150, y=150, width=500, height=200)
                DataFrame.configure(background="white")
                name = Label(DataFrame, text="Name :", font=(ARIAL, 13, "bold"), bg="white")
                name.place(x=0, y=0, height=30)
                nameValue = Label(DataFrame, text=user[0], font=(ARIAL, 12, "normal"), bg="white")
                nameValue.place(x=150, y=0, height=30)
                phone = Label(DataFrame, text="Mobile Number :", font=(ARIAL, 13, "bold"), bg="white")
                phone.place(x=0, y=50, height=30)
                phoneValue = Label(DataFrame, text=user[1], font=(ARIAL, 12, "normal"), bg="white")
                phoneValue.place(x=150, y=50, height=30)
                gender = Label(DataFrame, text="Gender :", font=(ARIAL, 13, "bold"), bg="white")
                gender.place(x=0, y=100, height=30)
                genderValue = Label(DataFrame, text=user[2], font=(ARIAL, 12, "normal"), bg="white")
                genderValue.place(x=150, y=100, height=30)
                locality = Label(DataFrame, text="Locality :", font=(ARIAL, 13, "bold"), bg="white")
                locality.place(x=0, y=150, height=30)
                localityValue = Label(DataFrame, text=user[3], font=(ARIAL, 12, "normal"), bg="white")
                localityValue.place(x=150, y=150, height=30)
                    

    search_btn = Button(SearchFrame, text="SEARCH", font=(ARIAL, 12, "bold"), command=search, border=0, bg=HIGHLIGHT_BG, fg="white")
    search_btn.place(x=450, y=50, width=150, height=40)



def updateUser():
    aadhar = StringVar()
    name = StringVar()
    phone = StringVar()
    gender = StringVar()

    UpdateFrame = Frame()
    UpdateFrame.place(x=250, y=0, width=650, height=500)
    UpdateFrame.configure(background="white")
    aadharLabel = Label(UpdateFrame, text="Aadhar Card Number", font=("", 13, "normal"), bg="white")
    aadharLabel.place(x=50, y=55, height=30)
    aadharInput = Entry(UpdateFrame, textvariable=aadhar,font=("",12,"normal"), bg="#f0f0f0", border=0)
    aadharInput.place(x=230, y=55, width=170, height=30)
    def search():
        if aadhar.get() == "" or len(aadhar.get()) != 12 or not aadhar.get().isdigit():
            messagebox.showwarning('Voting System Message', '🎱 Field is requird\n🎱 Aadhar number length must be 12 digit')

        else:
            user = model.findByAadhar(aadhar.get())
            if(user == None):
                messagebox.showinfo('Voting System Message', 'No such User')

            else:
                DataFrame = Frame(UpdateFrame)
                DataFrame.place(x=150, y=150, width=500, height=350)
                DataFrame.configure(background="white")

                name.set("")
                phone.set("")
                gender.set("")

                nameLabel = Label(DataFrame, text="Name ", font=(ARIAL, 13, "bold"), bg="white")
                nameLabel.place(x=0, y=0, height=30)
                nameValue = Entry(DataFrame, font=(ARIAL, 12, "normal"), textvariable=name, border=0, bg="#f0f0f0")
                nameValue.insert(0, user[2])
                nameValue.place(x=150, y=0, width=200, height=30)

                phoneLabel = Label(DataFrame, text="Mobile Number ", font=(ARIAL, 13, "bold"), bg="white")
                phoneLabel.place(x=0, y=50, height=30)
                phoneValue = Entry(DataFrame, font=(ARIAL, 12, "normal"), textvariable=phone, border=0, bg="#f0f0f0")
                phoneValue.insert(0, user[4])
                phoneValue.place(x=150, y=50, width=200, height=30)

                genderLabel = Label(DataFrame, text="Gender ", font=(ARIAL, 13, "bold"), bg="white")
                genderLabel.place(x=0, y=100, height=30)
                genderValue = Combobox(DataFrame, values=["Male","Female"], font=(ARIAL, 12, "normal"), textvariable=gender)
                genderValue.insert(0, user[5])
                genderValue.place(x=150, y=100, width=200, height=30)
                
                def update():
                    if name.get() == "" or phone.get() == "" or gender.get() == "" or len(phone.get()) != 10 or not phone.get().isdigit() :
                        messagebox.showwarning('Voting System Message', '🎱 Field is requird\n🎱 Mobile number length must be 10 digit')

                    else:
                        if(model.updateUserByAadhar(name.get(), phone.get(), gender.get(), aadhar.get())):
                            messagebox.showinfo('Voting System Message', 'Updated Successfully!!')
                        else:
                            messagebox.showwarning('Voting System Message', 'Try again later, unable to update user')

                        name.set("")
                        phone.set("")
                        gender.set("")
                        aadhar.set("")

                update_btn = Button(DataFrame, text="Update", font=(ARIAL, 12, "normal"), command=update, border=0, bg=HIGHLIGHT_BG, fg="white")
                update_btn.place(x=150, y=175, width=100, height=40)

    search_btn = Button(UpdateFrame, text="SEARCH", font=(ARIAL, 12, "bold"), command=search, border=0, bg=HIGHLIGHT_BG, fg="white")
    search_btn.place(x=450, y=50, width=150, height=40)


def deleteUser():
    aadhar = StringVar()
    DeleteFrame = Frame()
    DeleteFrame.place(x=250, y=0, width=650, height=500)
    DeleteFrame.configure(background="white")
    aadharLabel = Label(DeleteFrame, text="Aadhar Number", font=(ARIAL, 13, "bold"), bg="white")
    aadharLabel.place(x=100, y=150, height=30)
    aadharValue = Entry(DeleteFrame, textvariable=aadhar,font=(ARIAL,12,"normal"), bg="#f0f0f0", border=0)
    aadharValue.place(x=275, y=150, width=250, height=30)
    def delete():
        if aadhar.get() == "" or len(aadhar.get()) != 12 or not aadhar.get().isdigit():
            messagebox.showwarning('Voting System Message', '🎱 Field is requird\n🎱 Aadhar number length must be 12 digit')

        else:
            userResult = model.findByAadhar(aadhar.get())
            if(userResult == None):
                messagebox.showinfo('Voting System Message', 'No such User')

            else:
                if(model.deleteUserByAadhar(aadhar.get())):
                    messagebox.showinfo('Voting System Message', 'User Deleted')
                else:
                    messagebox.showwarning('Voting System Message', 'Try again later, unable to delete user')

            aadhar.set("")

    delete_btn = Button(DeleteFrame, text="Delete", font=(ARIAL, 13, "normal"), command=delete, border=0, bg=HIGHLIGHT_BG, fg="white")
    delete_btn.place(x=250, y=230, width=150, height=40)


def logout():
    Home()


def open_browser(e):
    webbrowser.open_new("https://code-4ge.github.io/")


Home()

root.mainloop()
