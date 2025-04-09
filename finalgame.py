from tkinter import*
from PIL import Image, ImageTk 
from tkinter import messagebox, colorchooser
import string
import random
balance=0
current_question = 0
def help():
    messagebox.showinfo("Help", 
       "Welcome to LootVault!\n\n"
        "This application offers:\n"
        "1. Banking Services:\n"
        "   - Deposit Money.\n"
        "   - Withdraw Money.\n"
        "   - Check Account Balance.\n\n"
        "2. Gaming Features:\n"
        "   - Play the KBC Quiz Game.\n"
        "   - Choose Difficulty Levels: Easy, Medium, or Hard.\n"
        "   - Answer questions and earn Rs.\n\n"
        "Follow the on-screen instructions carefully for each action. Enjoy managing your finances and playing games in one integrated application!"
        " \n  - Change the background color of the game window.\n\n"
        "3. Account Management:\n"
        "   - Create a new account by providing details such as Name, Contact, Bank Name, etc.\n"
        "   - Secure your account with a password.\n"
        "   - CAPTCHA verification for additional security.\n"
        "   - Login functionality to access your account.\n\n"
        "    -You can take the rest of the help from Priyanshu Gupta"
        ,parent=new_window)

questions = {
    "Easy": [
        ("1. Which of the following is the correct way\nto create a function in Python?", 
         ["def func():", "function func():", "func() {}", "create func():"], "def func():"),
        ("2. What is the output of 5 + 3?", ["53", "8", "15", "Error"], "8"),
        ("3. Which symbol is used for multiplication in Python?", ["*", "/", "x", "+"], "*"), 
        ("4. Which of the following is the correct way\nto create a function in Python?", ["def func():", "function func():", "func() {}", "create func():"], "def func():"),
        ("5. What is the output of the following code:\nprint('Hello, ' + 'World!')", ["Hello, World!", "Hello, World", "HelloWorld!", "Hello, "], "Hello, World!"),
        ("6. How do you insert comments in Python code?", ["// This is a comment", "# This is a comment", "/* This is a comment */", "<!-- This is a comment -->"], "# This is a comment"),
        ("7. Which data type is used to store\nmultiple items in a single variable in Python?", ["int", "float", "list", "char"], "list"),
        ("8. What is the output of the following code:\nlen(['Python', 'Java', 'C++'])", ["3", "2", "1", "4"], "3"),
        ("9. What is the value of X? Statement I:\nX^2 = 4, Statement II: X^3 = 8", ["2", "3", "4", "5"], "2"),
        ("10. By how many degrees will the hour hand move,\nif the second hand moves 3600 times?", ["360 degree", "25 degree", "30 degree", "45 degree"], "30 degree"),
    ],
    "Medium": [
        ("1. After how much time do the two\nhands of a correct clock coincide?", ["(65+5/11) min", "(56+5/11) min", "60 min", "None of these"], "(65+5/11) min"),
        ("2. At what time between 4 p.m and 5 p.m\nwill the two hands be apart by 5 mins?", ["16 and 4/11 min \npast 4 p.m", "27 and 3/11 \nmin past 4 p.m", "Both (a) \nand (b)", "None of these"], "Both (a) \nand (b)"),
        ("3. The two hands of an incorrect clock\ncoincide after every 70 min.\nHow much does the clock gain\nor lose per hour?", ["0.064 min", "3.896 min", "5 min", "None of these"], "5 min"),
        ("4. If 11th August 2011 was a Sunday, What will be\nthe day on 11th August, 2021?", ["Thursday", "Saturday", "Friday", "Sunday"], "Wednesday"),
        ("5. Last day of the century cannot be a:", ["Monday", "Wednesday", "Tuesday", "Friday"], "Tuesday"),
        ("6. How many Sundays will be there\nin the month of February 2006?", ["3", "4", "5", "None of these"], "4"),
        ("7. 400 students took a mock test: 60% \n of the boys and 80% of the girls cleared \nthe cut-off. If the total  percentage\n of students clearing the cut-off is \n65%,how many girls appeared in the test?", ["100", "120", "150", "300"], "150"),
        ("8. What was the day on 28th May, 2006?", ["Thursday", "Friday", "Sunday", "Saturday"], "Sunday"),
        ("9. Which of the following is used to\ndefine a block of code in Python?", ["Indentation", "Braces {}", "Parentheses ()", "Quotation marks"], "Indentation"),
        ("10. How do you start a for loop in Python?", ["for i in range(10):", "for (i=0; i<10; i++):", "for i=1 to 10", "for i := 1..10"], "for i in range(10):"),
    ],
    "Hard": [
        ("1. What is the correct syntax to import a module\nnamed 'math'?", ["import math", "import Math", "include math", "using math"], "import math"),
        ("2. What is the correct way to handle\n exceptions in Python?", ["try...except", "try...catch", "do...except", "try...finally"], "try...except"),
        ("3. What is the output of the following code:\nprint(type(10))", ["<class 'int'>", "<type 'int'>", "<int>", "<class>"], "<class 'int'>"),
        ("4. What is the time complexity of binary search?", ["O(n)", "O(n^2)", "O(log n)", "O(1)"], "O(log n)"),
        ("5. Which method is called when \n an object is created in Python?", ["__init__", "__del__", "__new__", "__create__"], "__init__"),
        ("6. What is a Python decorator?", ["A function modifier", "A comment", "A loop", "A variable"], "A function modifier"),
        ("7. Which of the following is True \nabout Python's Global Interpreter Lock (GIL)?",
         ["It allows parallel execution of threads in Python",
          "It limits one thread to execute Python bytecode at a time",
          "It removes the need for locks in multi-threaded programs",
          "It is used only in Jupyter Notebooks"], "It limits one thread to execute Python bytecode at a time"),
        ("8. What does the `len()` function do in Python?",
         ["Calculates length of an object", "Deletes an object", "Iterates over an object", "Copies an object"], "Calculates length of an object"),
        ("9. Which of the following keywords \nis used to\ndefine a class in Python?", ["function", "def", "class", "method"], "class"),
    ],
}



def on_exit():
    global balance
    res = messagebox.askquestion("Exit", "If you want to exit, click Yes. However, your winning amount will become zero.", parent=nw)
    if res == "yes":
        balance=0
        nw.destroy()

def check_answer(option):
    global current_question, difficulty,balance
    question, _, correct_answer = questions[difficulty][current_question]
    if option == correct_answer:
        win = (current_question + 1) * 15000
        
        balance+=win
        messagebox.showinfo("Correct Answer!", f"You've earned Rs :{win} !", parent=nw)
    else:
        messagebox.showerror("Wrong Answer!", "That's incorrect. Better luck next time!", parent=nw)
    current_question += 1
    if current_question < len(questions[difficulty]):
        load_question()
    else:
        messagebox.showinfo("Game Over", f"Your total ammount is: Rs:{balance}", parent=nw)

        nw.destroy()


def load_question():
    question, options, _ = questions[difficulty][current_question]
    question_label.config(text=question, bg="black", fg="orange", font=("Arial", 44))

    for i in range(4):
        option_button[i].config(text=options[i], bd=20,command=lambda opt=options[i]: check_answer(opt))

def START_GAME(selected_difficulty):
    global question_label, option_button,nw,difficulty
    difficulty = selected_difficulty
    nw = Toplevel()
    nw.title("KBC Quiz Game")
    
    nw.attributes('-fullscreen',True)
    nw.bind("<Escape>",lambda event: root.attributes('-fullscreen',False))
    nw.configure(bg="violet")
    
    
    question_label=Label(nw,text="",font=("Arial", 16),  bg="lightblue")
    question_label.pack(pady=20)
    
    option_button=[]
    for i in range(4):
        but=Button(nw,text="",font=("Arial", 14), bd=6,width=20, height=2)
        but.pack(pady=5)
        option_button.append(but)
    load_question()
    Button(nw, text="`EXIT`", command=on_exit, font=("Bernard MT Condensed", 25), bg="Silver", fg="red", relief="solid").place(x=30, y=710)
    def change_color():
        chosen_color = colorchooser.askcolor(title="Choose a Background Color")[1]
        if chosen_color:
            nw.config(bg=chosen_color) 


    Button(nw,text="`CHANGE_COLOR`",font=("Bernard MT Condensed", 25), bg="Silver", fg="green", relief="solid",command=lambda:change_color()).place(x=1100,y=710)
    
    nw.mainloop()

def Select_difficulty():
    s_d = Toplevel()


    s_d.title("Select Difficulty")
    

    webp_image = Image.open(r"C:\Users\dell\Desktop\BankBash\screen.webp")
    Timage = ImageTk.PhotoImage(webp_image)
    
    label = Label(s_d, image=Timage)
    label.image = Timage  
    label.place(x=0, y=0)
    
    s_d.geometry("605x260+290+300")
    s_d.resizable( False,False)
    Label(s_d, text="\nSelect\nDifficulty\t\nLevel", font=("Goudy Stout", 12),fg="RED", bg="orange").place(x=182,y=49,width=220,height=120)
    
    Button(s_d, text="Easy ", font=("Arial", 14), bg="green", fg="white", command=lambda: [s_d.destroy(), START_GAME("Easy")]).place(x=180,y=199)
    Button(s_d, text=" Medium ", font=("Arial", 14), bg="blue", fg="white", command=lambda: [s_d.destroy(), START_GAME("Medium")]).place(x=245,y=199)
    Button(s_d, text="Hard ", font=("Arial", 14), bg="red", fg="white", command=lambda: [s_d.destroy(), START_GAME("Hard")]).place(x=340,y=199)


def click(event):
    button_text = event.widget.cget("text")
    Entry_box.config(bg="Blue", fg="red")
    button = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    lb.config(bg="Orange",fg="black")
    if button_text == "C":
        current_text = var.get()
        var.set(current_text[:-1])
    if button_text in button:
        
        current = var.get()
        var.set(current + button_text.strip())
def CheckBalance():
    lb.config(bg="Magenta",fg="Black")
    lb.config(text=f"Your total Balance is\n: ₹{balance}")
def DepositMoney(amount):
    lb.config(bg="Violet",fg="Blue")
    global balance
    if int(amount)>0:
        balance += int(amount)
        lb.config(text=f"Deposited Money: \n₹{amount}\nNew Balance:\n ₹{balance}")
    else:
        lb.config(bg="RED",fg="Black")
        lb.config(text="Invalid \n ammount")
def WithdrawMoney(amount):
    global balance
    lb.config(bg="Green",fg="black")
    if int(amount) <= balance:
        balance -= int(amount)
        lb.config(text=f"Withdrawn_Money: \n₹{amount}\nNew Balance:\n ₹{balance}")
    else:
        lb.config(bg="RED",fg="Black")
        lb.config(text="Invalid \nammount")

    
def validate_transaction(action):
    
    entered_value = var.get()
    if action=="withdraw":
        WithdrawMoney(entered_value)
    elif action=="deposit":
        
        DepositMoney(entered_value)
    elif action == "check_balance":
        CheckBalance()

def Bankservis():
    new_window = Toplevel()
    new_window.title("Pay and Play is start")

    new_window.geometry("900x700+200+10")
    new_window.resizable(False, False)
    image = Image.open(r"C:\Users\dell\Desktop\BankBash\ATM.jpg")
    photo = ImageTk.PhotoImage(image)
    label = Label(new_window, image=photo)
    label.photo = photo
    label.place(x=0, y=0, relwidth=1, relheight=1)

    global var
    var = StringVar()
    var.set(0)
    global Entry_box
    Entry_box = Entry(new_window, font=("Jumble", 20), bg="black", fg="Green", textvariable=var)
    Entry_box.place(x=338, y=390, height=65, width=220)
    
    
    frame = Frame(new_window)
    buttons = [
        "9", "8", "7", "6", "5", "4", "3", "2",
        "C", "1", "0"]
    i = 0

    for b in buttons:
        button = Button(frame, text=b, font=("Copperplate Gothic Bold", 8), bd=10, bg="silver", fg="red", padx=18, pady=2)
        button.grid(row=i // 3, column=i % 3)
        button.bind("<Button-1>", click)
        i += 1

    frame.place(x=310, y=528)
    

    Button(new_window, text="Deposit \n Monay", bd=8,font=("Bernard MT Condensed",12), command=lambda: validate_transaction("deposit"), bg="silver", fg="Magenta").place(x=522, y=528, height=55, width=71)
    Button(new_window, text="Withdraw \nMonay", font=("Bernard MT Condensed",10),command=lambda: validate_transaction("withdraw"), bg="silver", fg="Green", bd=8).place(x=522, y=580, height=55, width=70)
    Button(new_window, text="Check\nBalance",font=("Bernard MT Condensed",12), command=lambda: validate_transaction("check_balance"), bg="silver", bd=8, fg="Indigo").place(x=522, y=633, height=55, width=70)

    Button(new_window, text="Exit", command=new_window.destroy, font=("Bernard MT Condensed",15),bd=8, bg="silver", fg="Red").place(x=450, y=653,width=70,height=35)

    global lb
    lb = Label(new_window, text="Welcome to \nBanking Service ", font=("Arial", 12), bg="light green", fg="brown")
    lb.place(x=368, y=260, height=103, width=173)


def generate_captcha():
    return "".join(random.choices(string.digits+string.ascii_letters+string.digits, k=8))


def detail():
    if Captcha.get() == captcha_text:
        with open("details.txt", "a") as file:
            file.write(f"Name: {Name.get()}\n")
            file.write(f"Contract: {Contract.get()}\n")
            file.write(f"Bank Name: {Bank_name.get()}\n")
            file.write(f"Account: {Account.get()}\n")
            file.write(f"Password: {Password.get()}\n")  # Store password
        messagebox.showinfo("Success", "Details stored and CAPTCHA verified!",parent=window)
        Bankservis()
    else:
        messagebox.showerror("Error", "Invalid CAPTCHA. Please try again.",parent=window)

def Create_new_account():
    global Name, Contract, Bank_name, Account, Captcha, Password, captcha_text,window
    window = Toplevel()
    window.title("Fill Details")
    window.geometry("900x700+200+10")
    window.config(bg="Black")
    window.resizable(False, False)
    
    Name = StringVar()
    Contract = StringVar()
    Bank_name = StringVar()
    Account = StringVar()
    Captcha = StringVar()
    Password = StringVar()

    title_label = Label(window, text="Fill Your Details", font=("Helvetica", 60, "bold"), bg="Black", fg="Blue")
    title_label.pack(pady=20)

    form_frame = Frame(window, bg="#f0f0f0")
    form_frame.pack(pady=10)

    Label(form_frame, text="User Name:", font=("Arial", 16), bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=20, pady=10)
    Entry(form_frame, font=("Arial", 14), textvariable=Name, bd=2, relief="solid").grid(row=0, column=1, padx=20, pady=10)

    Label(form_frame, text="Contract Number:", font=("Arial", 16), bg="#f0f0f0").grid(row=1, column=0, sticky="w", padx=20, pady=10)
    Entry(form_frame, font=("Arial", 14), textvariable=Contract, bd=2, relief="solid").grid(row=1, column=1, padx=20, pady=10)

    Label(form_frame, text="Bank Name:", font=("Arial", 16), bg="#f0f0f0").grid(row=2, column=0, sticky="w", padx=20, pady=10)
    Entry(form_frame, font=("Arial", 14), textvariable=Bank_name, bd=2, relief="solid").grid(row=2, column=1, padx=20, pady=10)

    Label(form_frame, text="Account Number:", font=("Arial", 16), bg="#f0f0f0").grid(row=3, column=0, sticky="w", padx=20, pady=10)
    Entry(form_frame, font=("Arial", 14), textvariable=Account, bd=2, relief="solid").grid(row=3, column=1, padx=20, pady=10)

    Label(form_frame, text="Password:", font=("Arial", 16), bg="#f0f0f0").grid(row=4, column=0, sticky="w", padx=20, pady=10)
    Entry(form_frame, font=("Arial", 14), textvariable=Password, show="*", bd=2, relief="solid").grid(row=4, column=1, padx=20, pady=10)  # Hide password input

    captcha_text = generate_captcha()
    Label(form_frame, text=f"Captcha: {captcha_text}", font=("Arial", 16), bg="#f0f0f0").grid(row=5, column=0, sticky="w", padx=20, pady=10)
    Entry(form_frame, font=("Arial", 14), textvariable=Captcha, bd=2, relief="solid").grid(row=5, column=1, padx=20, pady=10)
    
    Button(window, text="Submit", font=("Arial", 16), bg="#007BFF", fg="#fff", bd=0, relief="solid", command=detail).pack(pady=20)

def login():
    canvas.tag_unbind("all", "<Button-1>")
    canvas2.tag_unbind("all", "<Button-1>")

    
    login_window = Toplevel()
    login_window.title("Login")
    login_window.geometry("600x400+320+170")
    login_window.resizable(False,False)
    login_window.config(bg="#f0f0f0")
    imagep = Image.open(r"C:\Users\dell\Desktop\BankBash\tree.jpg")
    photo = ImageTk.PhotoImage(imagep)
    label = Label(login_window, image=photo)
    label.photo = photo
    label.place(x=30, y=0)

    global login_name, login_password, login_contract
    login_name = StringVar()
    login_password = StringVar()
    login_contract = StringVar()

    Label(login_window, text="Enter Name:", font=("Arial", 16), bg="#f0f0f0").pack()
    Entry(login_window, font=("Arial", 14), textvariable=login_name, bd=2, relief="solid").pack()

    Label(login_window, text="Enter Password:", font=("Arial", 16), bg="#f0f0f0").pack()
    Entry(login_window, font=("Arial", 14), textvariable=login_password, show="*", bd=2, relief="solid").pack()

    Label(login_window, text="Enter Contract Number:", font=("Arial", 16), bg="#f0f0f0").pack()
    Entry(login_window, font=("Arial", 14), textvariable=login_contract, bd=2, relief="solid").pack()

    Button(login_window, text="NEXT", bd=3, font=("Arial", 16), bg="green", fg="black", relief="solid",
           command=lambda: [check_login(), login_window.destroy()]).place(x=480, y=320)


def check_login():
    try:
        with open("details.txt", "r") as file:
            details = file.readlines()

        
        found = False
        for i in range(0, len(details), 5):  
            stored_name = details[i].strip().split(": ")[1]
            stored_contract = details[i + 1].strip().split(": ")[1]
            stored_password = details[i + 4].strip().split(": ")[1]

            
            if (login_name.get() == stored_name and 
                login_contract.get() == stored_contract and 
                login_password.get() == stored_password):
                found = True
                break

        
        if found:
            messagebox.showinfo("Login Success", "Login successful! Welcome!", parent=root1)
            Bankservis()
        else:
            messagebox.showerror("Login Failed", "Name, Contract, or Password does not match!", parent=root1)
    except FileNotFoundError:
        messagebox.showerror("Error", "Details file not found. Please create an account first.", parent=root1)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}",parent=root1)
    finally:
        
        canvas.tag_bind("all", "<Button-1>", lambda e: Create_new_account())
        canvas2.tag_bind("all", "<Button-1>", lambda e: login())



def banklogin():
    global root1
    root1 = Toplevel()
    root1.title("Bank Services")
    root1.geometry("850x700+200+10")
    root1.resizable(False, False)
    root1.config(bg="Violet")
    global canvas, canvas2

   
    image = Image.open(r"C:\Users\dell\Desktop\BankBash\game.jpg")
    resized_image = image.resize((850, 700))  
    photo = ImageTk.PhotoImage(resized_image)

    
    label = Label(root1, image=photo)
    label.photo = photo  
    label.place(x=0, y=0)

   
    canvas = Canvas(root1, width=250, height=80, bg="blue")
    canvas.place(x=460, y=570)
    canvas.create_oval(10, 10, 80, 80, fill="green", outline="")
    canvas.create_oval(170, 10, 240, 80, fill="green", outline="")
    canvas.create_rectangle(45, 10, 205, 80, fill="green", outline="")
    canvas.create_text(125, 45, text="Create new account", fill="black", font=("Arial", 18, "bold"))
    canvas.tag_bind("all", "<Button-1>", lambda e: Create_new_account())

    
    canvas2 = Canvas(root1, width=250, height=80, bg="Blue")
    canvas2.place(x=130, y=570)
    canvas2.create_oval(10, 10, 80, 80, fill="green", outline="")
    canvas2.create_oval(170, 10, 240, 80, fill="green", outline="")
    canvas2.create_rectangle(45, 10, 205, 80, fill="green", outline="")
    canvas2.create_text(125, 45, text="Login", fill="black", font=("Arial", 18, "bold"))
    canvas2.tag_bind("all", "<Button-1>", lambda e: login())

def open_new_window():
    global new_window
    new_window = Toplevel(root)
    new_window.title("LootVault is start")

    new_window.geometry("850x950+200+10")
    new_window.resizable(False, False)
    image = Image.open(r"C:\Users\dell\Desktop\BankBash\photo.jpg")
    photo2 = ImageTk.PhotoImage(image)
    label = Label(new_window, image=photo2)
    label.photo2 = photo2
    label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(new_window, text="", font=("Arial", 20), bg="light gray").place(x=200, y=5)
    Button(new_window,bd=10, text="Back", command=new_window.destroy, font=("Bernard MT Condensed", 25), bg="silver", fg="brown", relief="sunken").place(x=30, y=600)
    Button(new_window,bd=10, text=" HELP ", font=("Bernard MT Condensed", 25), fg="BLUE", bg="silver", relief="sunken", command=help).place(x=30, y=10)
    Button(new_window,bd=10, text="Bank service", font=("Bernard MT Condensed", 25), fg="green", bg="silver", relief="sunken", command=banklogin).place(x=610, y=600)
    Button(new_window, bd=10,text="START GAME", font=("Bernard MT Condensed", 25), fg="yellow", bg="silver", relief="sunken",command=Select_difficulty).place(x=620, y=10)



root = Tk()
root.title("LootVault")

image = Image.open(r"C:\Users\dell\Desktop\BankBash\tree.jpg")
resized_image = image.resize((820, 700))  
photo = ImageTk.PhotoImage(resized_image)


label = Label(root, image=photo)
label.config(bg="black")
label.place(x=0, y=0, relwidth=1, relheight=1)
root.geometry("820x700+200+10")
root.resizable(False, False)
Label(root, text="Welcome to LootVault!", font=("Goudy Stout", 25), bg="gold", fg="black", relief="sunken").place(x=0, y=0)
Button(root, text="~ START ~", bd=20, font=("Bernard MT Condensed", 35), bg="Black", fg="Gold", relief="sunken", command=open_new_window).place(x=550, y=570, width=250, height=100)

root.mainloop()
