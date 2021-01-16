from tkinter import *
import userdata, RSA, pickle, importlib
from PIL import Image, ImageTk

class MenuBar:
    def __init__(self,root):
        self.toolbar=Frame(root,bd=1,relief=RAISED,bg=user.toolbar_bg)

        compose_img=Image.open('./Assets/plus.jpg')
        inbox_img=Image.open('./Assets/Inbox.png')
        logout_img=Image.open('./Assets/logout.png')
        group_img=Image.open('./Assets/Group.png')
        clear_img=Image.open('./Assets/clear.jpg')
        settings_img=Image.open('./Assets/settings.png')

        compose_icon=ImageTk.PhotoImage(compose_img)
        inbox_icon=ImageTk.PhotoImage(inbox_img)
        logout_icon=ImageTk.PhotoImage(logout_img)
        group_icon=ImageTk.PhotoImage(group_img)
        clear_icon=ImageTk.PhotoImage(clear_img)
        settings_icon=ImageTk.PhotoImage(settings_img)

        compose_button = Button(self.toolbar,image=compose_icon,command = send_window)
        inbox_button = Button(self.toolbar,image=inbox_icon,command = check_inbox)
        logout_button = Button(self.toolbar,image=logout_icon,command = loginScreen)
        group_button = Button(self.toolbar,image=group_icon,command = doNothing)
        clear_button = Button(self.toolbar,image=clear_icon,command = clearMessages)
        settings_button = Button(self.toolbar,image=settings_icon,command = SELECTION)

        compose_button.image=compose_icon
        inbox_button.image=inbox_icon
        logout_button.image=logout_icon
        group_button.image=group_icon
        clear_button.image=clear_icon
        settings_button.image=settings_icon

        compose_button.pack(side=LEFT, padx=2, pady=2)
        inbox_button.pack(side=LEFT, padx=2, pady=2)
        group_button.pack(side=LEFT, padx=2, pady=2)
        clear_button.pack(side=LEFT, padx=2, pady=2)

        logout_button.pack(side=RIGHT, padx=2, pady=2)
        settings_button.pack(side=RIGHT, padx=2, pady=2)

        self.toolbar.pack(side=TOP,fill=X)
    
    def destroy(self):
        self.toolbar.destroy()

class TUTORIAL:
    def __init__(self):
        self.state=0
        self.explainCompose()
    def explainCompose(self):
        self.compose_label=Label(side_frame,text='COMPOSE',font=(None,8))
        self.compose_label.grid(row=0,column=0)
        self.compose_label.bind('<Button-1>',lambda e: self.explainInbox())
    def explainInbox(self):
        self.compose_label['text']=''
        self.compose_label.config(background='bisque')
        self.inbox_label=Label(side_frame,text='CHECK INBOX',font=(None,8)).grid(row=0,column=1)

class SELECTION:
    def __init__(self):

        global mainframe
        mainframe.destroy()
        mainframe = Frame(root,width=800,height=600)
        mainframe.pack_propagate(0)
        mainframe.pack()
        
        self.select_window=Frame(mainframe,bd=1,relief=RAISED,bg='light blue')

        red_img=Image.open('./Assets/red.png')
        blue_img=Image.open('./Assets/blue.png')
        green_img=Image.open('./Assets/green.png')
        yellow_img=Image.open('./Assets/yellow.png')
        bisque_img=Image.open('./Assets/bisque.png')
        lightgreen_img=Image.open('./Assets/lightgreen.png')
        tick_img=Image.open('./Assets/tick.png')

        red_icon=ImageTk.PhotoImage(red_img)
        blue_icon=ImageTk.PhotoImage(blue_img)
        green_icon=ImageTk.PhotoImage(green_img)
        yellow_icon=ImageTk.PhotoImage(yellow_img)
        bisque_icon=ImageTk.PhotoImage(bisque_img)
        lightgreen_icon=ImageTk.PhotoImage(lightgreen_img)
        tick_icon=ImageTk.PhotoImage(tick_img)

        red_button=Button(self.select_window,image=red_icon,command= lambda : self.change_colour('red'))
        blue_button=Button(self.select_window,image=blue_icon,command= lambda : self.change_colour('blue'))
        green_button=Button(self.select_window,image=green_icon,command= lambda : self.change_colour('green'))
        yellow_button=Button(self.select_window,image=yellow_icon,command= lambda : self.change_colour('yellow'))
        bisque_button=Button(self.select_window,image=bisque_icon,command= lambda : self.change_colour('bisque'))
        lightgreen_button=Button(self.select_window,image=lightgreen_icon,command= lambda : self.change_colour('light green'))
        tick_button=Button(self.select_window,image=tick_icon,command= lambda : self.finalise())

        red_button.image=red_icon
        blue_button.image=blue_icon
        green_button.image=green_icon
        yellow_button.image=yellow_icon
        bisque_button.image=bisque_icon
        lightgreen_button.image=lightgreen_icon
        tick_button.image=tick_icon

        red_button.pack(side=LEFT, padx=2, pady=2)
        blue_button.pack(side=LEFT, padx=2, pady=2)
        green_button.pack(side=LEFT, padx=2, pady=2)
        yellow_button.pack(side=LEFT, padx=2, pady=2)
        bisque_button.pack(side=LEFT, padx=2, pady=2)
        lightgreen_button.pack(side=LEFT, padx=2, pady=2)
        tick_button.pack(side=RIGHT, padx=2, pady=2)

        self.select_window.pack(side=TOP,fill=X)

        self.select_screen()

    def select_screen(self):
        self.t=Frame(mainframe,width=800,height=24,bg=user.toolbar_bg)
        self.t.pack(side=TOP)
        self.s=Frame(mainframe,height=550,width=280,bg=user.side_frame_bg)
        self.s.pack(side=LEFT)
        self.b=Frame(mainframe,height=550,width=520,bg=user.body_frame_bg)
        self.b.pack(side=RIGHT)
        self.select_changing_frame(self.t)
        self.colour_d={self.t:user.toolbar_bg,self.s:user.side_frame_bg,self.b:user.body_frame_bg}
        self.t.bind('<Button-1>',lambda e: self.select_changing_frame(self.t))
        self.s.bind('<Button-1>',lambda e: self.select_changing_frame(self.s))
        self.b.bind('<Button-1>',lambda e: self.select_changing_frame(self.b))


    def select_changing_frame(self,frame):
        self.t.config(highlightbackground=None)
        self.t.config(highlightthickness=0)
        self.s.config(highlightbackground=None)
        self.s.config(highlightthickness=0)
        self.b.config(highlightbackground=None)
        self.b.config(highlightthickness=0)
        frame.config(highlightbackground='black')
        frame.config(highlightthickness=1)
        self.changing_frame=frame

    def change_colour(self,colour):
        self.changing_frame.config(background=colour)
        self.colour_d[self.changing_frame] = colour

    def finalise(self):
        with open('userdata.py','a') as f:
            f.write(f"\n{user.username}.toolbar_bg = '{self.colour_d[self.t]}'")
            f.write(f"\n{user.username}.side_frame_bg = '{self.colour_d[self.s]}'")
            f.write(f"\n{user.username}.body_frame_bg = '{self.colour_d[self.b]}'")
        importlib.reload(userdata)
        usermenu(username)
    def destroy(self):
        self.select_window.destroy()

def hazh(x):
    sume=sumo=suma=pr4=pr3=0
    ods=evs=prall=1
    for i in range(0,len(x),2):
        sume += ord(x[i])
    for i in range(1,len(x),2):
        sumo += ord(x[i])
    for i in range(len(x)):
        prall *= ord(x[i])+i
    for i in range(0,len(x),4):
        pr4 += (ord(x[i]) * ord(x[i-1]) * ord(x[i-2]) * ord(x[i-3]))
    for i in range(0,len(x),3):
        pr3 += (ord(x[i]) * ord(x[i-1]) * ord(x[i-2]))
    for i in range(1,len(x),2):
        ods *= ord(x[i])
    for i in range(0,len(x),2):
        evs *= ord(x[i])
    prs = hex(sume*sumo)[-1:-3:-1]
    suma = (sume+sumo)*len(x) - sume
    suma = hex(suma)[-1:-3:-1]
    if ods>evs: oediff = ods-evs
    else: oediff = ods + evs
    while not oediff%16: oediff//=16
    oediff = hex(oediff)[-1:-3:-1]
    while not prall%16: prall//=16
    prall = hex(prall)[-1:-5:-1]
    pr43 = hex(pr4%pr3)[-1:-3:-1]
    result = prall+suma+oediff+prs+pr43

    return result

def doNothing(*args): 
    return

def create_account(user_name_entry,user_pass_entry1,user_pass_entry2,msg):
    username=user_name_entry.get()
    if username in userdata.userDict:
        msg.config(text='Username already taken')
        return
    else:
        password1=user_pass_entry1.get()
        password2=user_pass_entry2.get()
        if password1!=password2:
            user_pass_entry1.delete(0,'end')
            user_pass_entry2.delete(0,'end')
            msg.config(text='Passwords do not match')
            return
        password=hazh(password1)
        with open("userdata.py",'a') as f:
            f.write(f"\n{username} = USERS('{username}','{password}')")
            f.write(f"\nuserDict['{username}'] = {username}")
        importlib.reload(userdata)

        inbox_filename="./UserfilesInbox/"+username+".dat"
        outbox_filename="./UserfilesOutbox/"+username+".dat"
        inbox_userfile=open(inbox_filename,'w')
        inbox_userfile.close()
        outbox_userfile=open(outbox_filename,'w')
        outbox_userfile.close()
        usermenu(username)

def create_account_screen(rframe):
    Label(rframe,width=15,height=5,text='Username',font=('arial',10),bg='light green').grid(row=1,column=1)
    user_name_entry=Entry(rframe,width=20)
    user_name_entry.grid(row=1,column=2)
    Label(rframe,width=15,height=5,text='Set Password',font=('arial',10),bg='light green').grid(row=2,column=1)
    user_pass_entry1=Entry(rframe,width=20,show="*")
    user_pass_entry1.grid(row=2,column=2)
    Label(rframe,width=15,height=5,text='Confirm Password',font=('arial',10),bg='light green').grid(row=3,column=1)
    user_pass_entry2=Entry(rframe,width=20,show='*')
    user_pass_entry2.grid(row=3,column=2)
    msg = Label(rframe,fg='#f00',bg='light green')
    msg.grid(row=4,column=1,columnspan=2)
    rframe.bind('<Return>',lambda x: create_account(user_name_entry,user_pass_entry1,user_pass_entry2,msg))
    submit=Button(rframe,text='Create Account',command = lambda : create_account(user_name_entry,user_pass_entry1,user_pass_entry2,msg))
    submit.grid(row=5,column=1,columnspan=2)

def send(receiver_entry,message_entry,msg):
    receiver=receiver_entry.get()
    receiver=userdata.userDict[receiver]
    
    if receiver in userdata.userDict.values():
        receiver_file=receiver.inbox_file
        sender_file=user.outbox_file
        message=message_entry.get("1.0", "end-1c")
        message = f"From: {user.username}\nTo: {receiver.username}\n{message}"
        KEY_r=receiver.password
        KEY_s=user.password
        message_r=RSA.rsa(message,RSA.keys(KEY_r,True)[0],RSA.keys(KEY_r,True)[1],True)
        print(message_r)
        with open(receiver_file,'ab') as f:
            pickle.dump(message_r,f)
        message_s=RSA.rsa(message,RSA.keys(KEY_s,True)[0],RSA.keys(KEY_s,True)[1],True)
        with open(sender_file,'ab') as f:
            pickle.dump(message_s,f)
        msg.config(text="Message sent")
        message_entry.delete('1.0',END)
    
    elif receiver in userdata.groupDict.values():
        group_password=input("Enter the password of the group: ")
        group_password=hazh(group_password)
        
        if userdata.groupDict[receiver] == group_password:
            receiver_file="./Groups/"+receiver+".dat"
            sender_file="./UserfilesOutbox/"+username+".dat"
            message=username+": "+message_entry.get("1.0", "end-1c")
            with open(receiver_file,'ab') as f:
                message1=RSA.rsa(message,RSA.keys(group_password,True)[0],RSA.keys(group_password,True)[1],True)
                pickle.dump(message1,f) 
            
            KEY=userdata.userDict[username]

            with open(sender_file,'ab') as f:
                message2=RSA.rsa(message,RSA.keys(KEY,True)[0],RSA.keys(KEY,True)[1],True)
                pickle.dump(message2,f)
            msg.config(text="Message sent")
        else:
            msg.config(text="Incorrect password")

    else:
        msg.config(text="This receiver does not exist.")

def check_inbox():
    global body_frame, side_frame
    body_frame.destroy()
    body_frame=Frame(mainframe,height=600,width=520,background=user.body_frame_bg)
    body_frame.pack(side=RIGHT)
    body_frame.grid_propagate(0)
    side_frame.destroy()
    side_frame=Frame(mainframe,height=600,width=280,background=user.side_frame_bg)
    side_frame.pack(side=LEFT)
    side_frame.grid_propagate(0)
    usermenu(username)
    Label(body_frame,text='INBOX',bg=user.body_frame_bg).pack(side=TOP)
    output=Text(body_frame,height=40,bg='green')
    output.pack(side=LEFT)
    
    filename=user.inbox_file
    KEY=user.password
    with open(filename,'rb') as f:       
        try:
            while True:
                messagelist=pickle.load(f)
                messagelist=RSA.rsa(messagelist,RSA.keys(KEY,False)[0],RSA.keys(KEY,False)[1],False)
                output.insert(END,messagelist)
                output.insert(END,'\n'+"_"*20+'\n')
        except:
            pass

    output.config(state=DISABLED)

def group_messages(group):
    global body_frame, side_frame
    body_frame.destroy()
    body_frame=Frame(mainframe,height=600,width=520,background=user.body_frame_bg)
    body_frame.pack(side=RIGHT)
    body_frame.grid_propagate(0)
    side_frame.destroy()
    side_frame=Frame(mainframe,height=600,width=280,background=user.side_frame_bg)
    side_frame.pack(side=LEFT)
    side_frame.grid_propagate(0)
    usermenu(username)
    Label(body_frame,text='INBOX',bg=user.body_frame_bg).pack(side=TOP)
    output=Text(body_frame,height=40,bg='green')
    output.pack(side=LEFT)

    filename=group.chatfile
    KEY=group.password
    with open(filename,'rb') as f:       
        try:
            while True:
                messagelist=pickle.load(f)
                messagelist=RSA.rsa(messagelist,RSA.keys(KEY,False)[0],RSA.keys(KEY,False)[1],False)
                output.insert(END,messagelist)
                output.insert(END,'\n'+"_"*20+'\n')
        except:
            pass
    output.config(state=DISABLED)

def send_window():
    global body_frame,msg
    body_frame.destroy()
    body_frame=Frame(mainframe,height=600,width=520,background=user.body_frame_bg)
    body_frame.pack(side=RIGHT)
    body_frame.grid_propagate(0)
    msg = Label(body_frame,bg=user.body_frame_bg)
    msg.grid(row=1,column=1)
    topframe = Frame(body_frame,width=520,height=50,bg=user.body_frame_bg)
    topframe.pack_propagate(0)
    topframe.grid(row=2,column=1)
    Label(topframe,text='To:',bg=user.body_frame_bg).grid(row=1,column=1)
    receiver_entry=Entry(topframe)
    receiver_entry.grid(row=1,column=2)
    message_entry=Text(body_frame,height=10,bg='green')
    message_entry.grid(row=3,column=1)
    send_button=Button(body_frame,text='SEND',command = lambda: send(receiver_entry,message_entry,msg))
    send_button.grid(row=4,column=1)

def reset_pass(old,new,conf,msg):
    if hazh(old.get()) != userdata.userDict[username].password:
        msg.config(text='Current password entered is incorrect')
        old.delete(0,'end')
    else:
        if new.get() == conf.get():
            filename=user.outbox_file
            KEY=user.password
            messagelist = []
            with open(filename,'rb') as f:     
                try:
                    while True:
                        messagelist.append(RSA.rsa(pickle.load(f),RSA.keys(KEY,False)[0],RSA.keys(KEY,False)[1],False))
                except: pass
            with open("userdata.py",'a') as f:
                f.write(f"\n{username}.password = '{hazh(new.get())}'")
            importlib.reload(userdata)
            with open(filename,'wb') as f:     
                for i in messagelist:
                    pickle.dump(messagelist,f)
        else:
            msg.config(text='Passwords do not match')
            new.delete(0,'end')
            conf.delete(0,'end')

def reset_pass_screen():
    global body_frame,msg
    body_frame.destroy()
    body_frame=Frame(mainframe,height=600,width=520,background=user.body_frame_bg)
    body_frame.pack(side=RIGHT)
    body_frame.grid_propagate(0)
    re_enter = Entry(body_frame,show='*')
    new_pass = Entry(body_frame,show='*')
    confirm_ = Entry(body_frame,show='*')

    Label(body_frame,text='Current password ',bg=user.body_frame_bg).grid(row=1,column=1)
    Label(body_frame,text='New password ',bg=user.body_frame_bg).grid(row=2,column=1)
    Label(body_frame,text='Confirm new password ',bg=user.body_frame_bg).grid(row=3,column=1)
    re_enter.grid(row=1,column=2)
    new_pass.grid(row=2,column=2)
    confirm_.grid(row=3,column=2)
    msg = Label(body_frame,bg=user.body_frame_bg,fg='#f00')
    msg.grid(row=4,column=1,columnspan=2)
    Button(body_frame,text='Reset',command=lambda: reset_pass(re_enter,new_pass,confirm_,msg),bg=user.body_frame_bg).grid(row=5,column=1,columnspan=2)

def clearMessages():
    filename="./UserfilesInbox/"+username+".dat"
    with open(filename,'wb') as f:
        pickle.dump('',f)
    check_inbox()

def checkOutbox():
    global body_frame, side_frame
    body_frame.destroy()
    body_frame=Frame(mainframe,height=600,width=520,background='light green')
    body_frame.pack(side=RIGHT)
    body_frame.grid_propagate(0)
    side_frame.destroy()
    side_frame=Frame(mainframe,height=600,width=280,background='bisque')
    side_frame.pack(side=LEFT)
    side_frame.grid_propagate(0)
    usermenu(username)
    output=Text(body_frame,height=40,bg='green')
    output.pack(side=LEFT)

    filename=user.outbox_file
    KEY=user.password
    with open(filename,'rb') as f:       
        try:
            while True:
                messagelist=pickle.load(f)
                messagelist=RSA.rsa(messagelist,RSA.keys(KEY,False)[0],RSA.keys(KEY,False)[1],False)
                output.insert(END,messagelist)
                output.insert(END,'\n'+"_"*20+'\n')
        except:
            pass
    output.config(state=DISABLED)

def createGroup(admin,group_name,group_password,msg,members):
    members.append(admin)
    if group_name.get() in userdata.groupDict:
        msg.config(text="This group name already exists, try choosing a different one")
        group_name.delete(0,'end')
        return
    group_name = group_name.get()
    if len(group_password.get()) < 8:
        msg.config(text='Password too small')
        return
    group_password_text=group_password.get()
    group_password=hazh(group_password.get())

    with open("userdata.py",'a') as f:
        f.write(f"\n{group_name} = GROUP('{group_name}','{group_password}','{admin}')\ngroupDict['{group_name}'] = '{group_password}'")

    for i in members:
        if i not in userdata.userDict:
            msg.config(text=msg['text']+'\nNo user named '+i+' exists.')
            continue
        user_file=f"./UserfilesInbox/{i}.dat"
        message=f"{admin} has added you to a group {group_name}. The group password is {group_password_text}.\nIf you forget group password you will not be able to send/receive group messages."
        KEY=userdata.userDict[i].password
        message=RSA.rsa(message,RSA.keys(KEY,True)[0],RSA.keys(KEY,True)[1],True)
        with open(user_file,'ab') as f:
            pickle.dump(message,f)
        with open('userdata.py','a') as f:
            f.write(f"{group_name}.memberslist.append({i})")
    
    group_path=f"./Groups/{group_name}.dat"
    with open(group_path,'wb') as f:
        message=f"New group {group_name} has been created by {admin}"
        message=RSA.rsa(message,RSA.keys(group_password,True)[0],RSA.keys(group_password,True)[1],True)
        pickle.dump(message,f)

    check_group_inbox(group_name,True)

def createGroupScreen():
    global body_frame
    body_frame.destroy()
    body_frame=Frame(mainframe,height=600,width=520,background=user.body_frame_bg)
    body_frame.pack(side=RIGHT)
    body_frame.grid_propagate(0)
    Label(body_frame,bg=userdata.userDict[username].body_frame_bg, text='Usernames of individuals in the group separated by a ;').grid(row=1,column=1,columnspan=2)
    Label(body_frame,text='Name of group',bg=userdata.userDict[username].body_frame_bg).grid(row=2,column=1)
    group_name_entry = Entry(body_frame)
    group_name_entry.grid(row=2,column=2)
    Label(body_frame,text='Password of group',bg=userdata.userDict[username].body_frame_bg).grid(row=3,column=1)
    group_pass_entry = Entry(body_frame,show='*')
    group_pass_entry.grid(row=3,column=2)
    member_entry=Text(body_frame,height=10,width=64,bg='#090')
    member_entry.grid(row=4,column=1,columnspan=2)
    msg = Label(body_frame,bg=userdata.userDict[username].body_frame_bg,fg="#f00")
    msg.grid(row=6,column=1,columnspan=2)
    create_group_button=Button(body_frame,text='CREATE',command = lambda: createGroup(username,group_name_entry,group_pass_entry,msg,member_entry.get("1.0", "end-1c").split(';')))
    create_group_button.grid(row=5,column=1,columnspan=2)

def usermenu(userx):
    global tools, mainframe, body_frame, side_frame, username,user
    username = userx
    user=userdata.userDict[username]
    mainframe.destroy()
    mainframe = Frame(root,width=800,height=600)
    mainframe.pack_propagate(0)
    mainframe.pack()
    tools=MenuBar(mainframe)
    side_frame=Frame(mainframe,height=600,width=280,background=user.side_frame_bg)
    side_frame.pack_propagate(0)
    side_frame.pack(side=LEFT)
    side_frame.grid_propagate(0)
    #tutorial=TUTORIAL()
    body_frame=Frame(mainframe,height=600,width=520,background=user.body_frame_bg)
    body_frame.pack_propagate(0)
    body_frame.pack(side=RIGHT)
    body_frame.grid_propagate(0)
    root.bind('<Return>',doNothing)
    l1=Label(side_frame,text="SENT",bg='light blue',font=(None,20))
    l1.grid(row=1,column=1,pady=10)
    l2=Label(side_frame,text="Create a group",bg='light blue',font=(None,20))
    l2.grid(row=3,column=1,pady=10)
    l3=Label(side_frame,text="Check your group inbox",bg='light blue',font=(None,20))
    l3.grid(row=5,column=1,pady=10)
    l4=Label(side_frame,text='Change Password',bg='light blue',font=(None,20))
    l4.grid(row=6,column=1,pady=10)

    l1.bind('<Button-1>',lambda e: checkOutbox())
    l2.bind('<Button-1>',lambda e: createGroupScreen())
    l4.bind('<Button-1>',lambda e: reset_pass_screen())

def login(user_name_entry,user_pass_entry,msg):
    username=user_name_entry.get()
    password=user_pass_entry.get()
    password=hazh(password)
    if username not in userdata.userDict.keys(): msg.config(text='User does not exist')
    elif userdata.userDict[username].password == password: usermenu(username)
    else: msg.config(text='Incorrect password')

def loginScreen():
    global mainframe
    mainframe.destroy()
    mainframe=Frame(root,height=600,width=800)
    mainframe.pack()
    mainframe.pack_propagate(0)
    lframecontainer = Frame(mainframe,height=600,width=300,bg='bisque')
    rframecontainer = Frame(mainframe,height=600,width=500,bg='light green')
    lframecontainer.pack_propagate(0)
    rframecontainer.pack_propagate(0)
    lframecontainer.pack(side=LEFT)
    rframecontainer.pack(side=RIGHT)
    lframe = Frame(lframecontainer,height=600,width=300,bg='bisque')
    rframe = Frame(rframecontainer,height=600,width=500,bg='light green')
    lframe.pack_propagate(0)
    rframe.pack_propagate(0)
    lframe.pack(side=LEFT)
    rframe.pack(side=LEFT)
    Label(lframe,width=15,height=5,text='Username',font=('arial',10),bg='bisque').grid(row=1,column=1)
    user_name_entry=Entry(lframe,width=20)
    user_name_entry.grid(row=1,column=2)
    Label(lframe,width=15,height=5,text='Password',font=('arial',10),bg='bisque').grid(row=2,column=1)
    user_pass_entry=Entry(lframe,width=20,show="*")
    user_pass_entry.grid(row=2,column=2)
    msg = Label(lframe,fg='#f00',bg='bisque')
    msg.grid(row=3,column=1,columnspan=2)
    user_pass_entry.bind('<Return>',lambda x: login(user_name_entry,user_pass_entry,msg))
    submit=Button(lframe,text='Login',command=lambda: login(user_name_entry,user_pass_entry,msg))
    submit.grid(row=4,column=2)
    new = Label(lframe,text='New? Sign up.',fg='#02a',cursor='hand2',bg='bisque')
    new.grid(row=4,column=1)
    new.bind('<Button-1>',lambda x: create_account_screen(rframe))

root=Tk()
root.geometry('800x600')
root.title('DPS MAIL')
mainframe = Frame(root,width=800,height=600)
mainframe.pack_propagate(0)
mainframe.pack()
loginScreen()
root.mainloop()
