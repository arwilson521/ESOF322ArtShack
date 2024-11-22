from tkinter import *
import sqlite3
from PIL import Image, ImageTk
import os
import random

def mainmenuinterface():
    interface = Tk()  # Create interface
    interface.geometry("750x750")  # Sets size
    interface.title("Art Shack")  # Window title
    label = Label(interface, font=("Arial", 16, "bold"), justify=CENTER, text='Choose your role')  # Create the select prompt
    label.grid(row=0, column=0, columnspan=4, pady=100)  # Pack it into a window with y padding 100
    # Creating buttons
    buyerbutton = Button(interface, text="Buyer", command=lambda: buyer(interface))  # Buyer button
    sellerbutton = Button(interface, text="Seller", command=lambda: seller(interface))  # Seller button
    adminbutton = Button(interface, text="Admin", command=lambda: admin(interface))  # Admin button
    browserbutton = Button(interface, text="Browser", command=lambda: browser(interface))  # Browser button
    # Packing buttons
    buyerbutton.grid(row=1, column=0, padx=10, pady=20)
    sellerbutton.grid(row=1, column=1, padx=10, pady=20)
    adminbutton.grid(row=1, column=2, padx=10, pady=20)
    browserbutton.grid(row=1, column=3, padx=10, pady=20)
    # Centers and spaces evenly
    for i in range(4):
        interface.grid_columnconfigure(i, weight=1)

    interface.mainloop()







def buyer(interface):
    print("buyer clicked")
    interface.destroy()
    buyerinterface()





def buyerinterface():
    buyerinterface=Tk()
    buyerinterface.geometry("750x750")
    buyerinterface.title("Buyer")
    label=Label(buyerinterface,text="Buyer Interface",font=("Arial",16,"bold"))
    label.place(x=375,y=20)
    buttonframe=Frame(buyerinterface)
    buttonframe.place(x=0,y=0)
    mainbutton=Button(buttonframe,text="Main Menu",command=lambda:mainmenu(buyerinterface))
    mainbutton.pack()




    

    def buy(name):
        
        con = sqlite3.connect("ArtShack.db")
        cur = con.cursor()
    
        # Fetch the type of art (e.g., BIN or Auction) from the database
        fullsql = "SELECT type FROM art WHERE art=?"
        result = cur.execute(fullsql, (name,))
        query = result.fetchall()[0][0]  # Get the type of the art
        print(name, query)
    
        # Update the art to 'unapproved' (i.e., set Approved = 0)
        if query == "BIN":
            print("Bought!")
            cur.execute("UPDATE art SET Approved=0 WHERE art=?", (name,))
        else:
            print("You bid $1!")
            fullsql= "SELECT price FROM art WHERE art=?"
            result=cur.execute(fullsql,(name,))
            query=result.fetchall()[0][0]
            print(name,query)
            query=query+1
            query=str(query)
            fullsql="UPDATE art SET price="+query+" WHERE art=?"
            cur.execute(fullsql,(name,))
            ran=random.randint(0,10)
            if ran==5:
                print("You won the auction!")
                cur.execute("UPDATE art SET Approved=0 WHERE art=?", (name,))
                        
    
        con.commit()
        con.close()
        buyerdisplay_art()
        mainmenu(buyerinterface)    
        
    con = sqlite3.connect("ArtShack.db")  # Ensure the database is in the 'Program' folder
    cur = con.cursor()
    cur.execute("SELECT art, price, type FROM art WHERE approved=1")
    artdata = cur.fetchall()


    

    '''
This is just renamed/reused code from admindisplay_art. go check that for comments explaining it.
I only added comments for bits i changed like adding a buybutton.
    '''
    def buyerdisplay_art():
        frame=Frame(buyerinterface)
        frame.pack(pady=50)
        art_directory=("art/")
        for index,art in enumerate(artdata):
            #Buy/bid button
            buybutton=Button(frame,text="Buy/Bid",command=lambda name=art[0]:buy(name))
            buybutton.grid(row=index,column=0,padx=10,pady=10)

            image_filename=art[0]
            image_path=os.path.join(art_directory,image_filename)
            image=Image.open(image_path)
            image=image.resize((150,150))
            photo=ImageTk.PhotoImage(image)
            image_label=Label(frame,image=photo)
            image_label.image=photo
            image_label.grid(row=index,column=1,padx=10,pady=10)
            art_info = f"Price: ${art[1]}\nType: {art[2]}"
            info_label = Label(frame, text=art_info, font=("Arial", 12), justify=LEFT)
            info_label.grid(row=index, column=2, padx=10, pady=10) 
    




    
    buyerdisplay_art()
    # Commit and close connection
    con.commit()
    con.close()
    buyerinterface.mainloop()




def seller(interface):
    print("seller clicked")
    interface.destroy()
    sellerinterface()




def sellerinterface():

    
    sellerinterface = Tk()
    sellerinterface.geometry("750x750")
    sellerinterface.title("Seller")
    label = Label(sellerinterface, text="Seller Interface", font=("Arial", 16, "bold"))
    label.place(x=375, y=20)


    
    #uploading interface
    def uploadinterface():
        sellerinterface.destroy()
        uploadinterface=Tk()
        uploadinterface.geometry("750x750")
        uploadinterface.title("Upload art")


        
        filenamevar=StringVar()
        pricevar=StringVar()
        buytypevar=StringVar()
        
        label = Label(uploadinterface,text="Upload your art",font=("Arial",16,"bold"))
        label.place(x=375,y=20)

        #File name label and entry
        filename=Label(uploadinterface,text="Filename",font=("Arial",16,"bold"))
        filename.place(x=270,y=100)
        nameentry=Entry(uploadinterface,textvariable=filenamevar)
        nameentry.place(x=375,y=110)

        #Price Label and entry
        pricelabel=Label(uploadinterface,text="Price",font=("Arial",16,"bold"))
        pricelabel.place(x=270,y=150)
        priceentry=Entry(uploadinterface,textvariable=pricevar)
        priceentry.place(x=375,y=160)

        #type of entry
        buytype=Label(uploadinterface,text="BIN or Auction",font=("Arial",16,"bold"))
        buytype.place(x=200,y=200)
        buyentry=Entry(uploadinterface,textvariable=buytypevar)
        buyentry.place(x=375,y=210)


        

        #Submittal

        
        def submitfunc():
                   
            if(buytypevar.get()=="BIN" or buytypevar.get()=="Auction"):
                
                con=sqlite3.connect("ArtShack.db")
                cur=con.cursor()
                filename=filenamevar.get()
                price=pricevar.get()
                buytype=buytypevar.get()
                cur.execute("INSERT INTO art VALUES (?,?,?,?)",(0,filename,price,buytype))
        
                con.commit()            
                con.close()
            
            #Debug printing
            print("Uploading the following")
            print("Filename:", filenamevar.get())
            print("Price:", pricevar.get())
            print("Buy Type:", buytypevar.get())


            
        submit=Button(uploadinterface,text="Submit",command=submitfunc)
        submit.place(x=375,y=300)
        print(filenamevar.get(),pricevar.get(),buytypevar.get())


        #main menu button
        mainbutton=Button(uploadinterface,text="Main Menu",command=lambda:mainmenu(uploadinterface))
        mainbutton.place(x=0,y=0)
        uploadinterface.mainloop()

    #promote art
    #tbd, dont wanna do it though

    #upload art
    uploadbutton=Button(sellerinterface, text="Upload art", command=lambda: uploadinterface())
    uploadbutton.place(x=375,y=50)
    
    
    
    # Main menu button
    mainbutton = Button(sellerinterface, text="Main Menu", command=lambda: mainmenu(sellerinterface))
    mainbutton.place(x=0, y=0)
    sellerinterface.mainloop()




def admin(interface):
    print("admin clicked")
    interface.destroy()
    admininterface()




def admininterface():
    admininterface = Tk()
    admininterface.geometry("750x750")
    admininterface.title("Admin")
    label = Label(admininterface, text="Admin Interface", font=("Arial", 16, "bold"))
    label.place(x=375, y=20)


    #main menu button frame to keep mainbutton while using .place and using .grid elsewhere
    buttonframe=Frame(admininterface)
    buttonframe.place(x=0,y=0)
    # Main menu button
    mainbutton = Button(buttonframe, text="Main Menu", command=lambda: mainmenu(admininterface))
    mainbutton.pack()



    
    def approveart(name):
        #print(name)
        con=sqlite3.connect("ArtShack.db")
        cur=con.cursor()
        fullsql=("SELECT approved FROM art WHERE art='"+name+"'")
        #print(fullsql)
        result=cur.execute(fullsql)
        query=(result.fetchall()[0][0])
        
        if(query==1):
            print("Already Approved")
        else:
            print("Approving")
            cur.execute("UPDATE art SET Approved=1 WHERE art=?", (name,))
            print("Art approved")
            
        con.commit()
        con.close()


    
    def unapproveart(name):
        con=sqlite3.connect("ArtShack.db")
        cur=con.cursor()
        fullsql=("SELECT approved FROM art WHERE art='"+name+"'")
        result=cur.execute(fullsql)
        query=(result.fetchall()[0][0])
        if (query==1):
            print("Unapproving")
            cur.execute("UPDATE art SET Approved=0 WHERE art=?", (name,))
            print("Art unapproved")
        else:
            print("Already not approved")
        con.commit()
        con.close()
    #Access DB to display art 
    con = sqlite3.connect("ArtShack.db")  # Ensure the database is in the 'Program' folder
    cur = con.cursor()
    cur.execute("SELECT art, price, type FROM art")
    artdata = cur.fetchall()
    
        
        
    def admindisplay_art():
        # Create a frame for the images and info labels
        frame = Frame(admininterface)
        frame.pack(pady=50)  # Add some space around the frame
        art_directory=("art/")
        for index, art in enumerate(artdata):

            #Approve art buttons
            approve=Button(frame,text="Approve art", command=lambda name=art[0]:approveart(name)) #approval of art
            
            approve.grid(row=index,column=0,padx=10,pady=10)

            #unapprove art button
            unapprove=Button(frame,text="Unapprove art",command=lambda name=art[0]:unapproveart(name))
            unapprove.grid(row=index,column=3,padx=10,pady=10)
            
            image_filename = art[0]  # Get the image file name stored in the database
            image_path = os.path.join(art_directory, image_filename)  # Join the 'art' directory path with the image filename
            image = Image.open(image_path)
            image = image.resize((150, 150))  # Resize the image
            photo = ImageTk.PhotoImage(image)

            # Create a label for the image and display it in the first column
            image_label = Label(frame, image=photo)
            image_label.image = photo  # Keep reference to the image to avoid garbage collection
            image_label.grid(row=index, column=1, padx=10, pady=10)  # Display image in first column
            
            
            # Create a label for the art info (price and type) and display it in the second column
            art_info = f"Price: ${art[1]}\nType: {art[2]}"
            info_label = Label(frame, text=art_info, font=("Arial", 12), justify=LEFT)
            info_label.grid(row=index, column=2, padx=10, pady=10)  # Display text to the right of the image
    
    # Call the function to display the art
    admindisplay_art()

    # Commit and close connection
    con.commit()
    con.close()
    admininterface.mainloop()




def browser(interface):
    print("browser clicked")
    interface.destroy()
    browser_interface()  # Rename function to avoid conflict




def browser_interface():
    browserinterface = Tk()  # Rename the Tk() instance
    browserinterface.geometry("750x750")
    browserinterface.title("Browser")
    
    label = Label(browserinterface, text="Browser Interface", font=("Arial", 16, "bold"))
    label.place(x=375, y=20)
    
    # Main menu button
    mainbutton = Button(browserinterface, text="Main Menu", command=lambda: mainmenu(browserinterface))
    mainbutton.place(x=0, y=0)
    
    # Define the path to the art directory
    art_directory = os.path.join(os.path.dirname(__file__), 'art')  # Get path to the 'art' folder

    # Displaying art
    con = sqlite3.connect("ArtShack.db")  # Ensure the database is in the 'Program' folder
    cur = con.cursor()
    cur.execute("SELECT art, price, type FROM art WHERE approved=1")
    artdata = cur.fetchall()


    
    def display_art():
        # Create a frame for the images and info labels
        frame = Frame(browserinterface)
        frame.pack(pady=50)  # Add some space around the frame
        art_directory=("art/")
        for index, art in enumerate(artdata):
            image_filename = art[0]  # Get the image file name stored in the database
            image_path = os.path.join(art_directory, image_filename)  # Join the 'art' directory path with the image filename
            image = Image.open(image_path)
            image = image.resize((150, 150))  # Resize the image
            photo = ImageTk.PhotoImage(image)

            # Create a label for the image and display it in the first column
            image_label = Label(frame, image=photo)
            image_label.image = photo  # Keep reference to the image to avoid garbage collection
            image_label.grid(row=index, column=0, padx=10, pady=10)  # Display image in first column

            # Create a label for the art info (price and type) and display it in the second column
            art_info = f"Price: ${art[1]}\nType: {art[2]}"
            info_label = Label(frame, text=art_info, font=("Arial", 12), justify=LEFT)
            info_label.grid(row=index, column=1, padx=10, pady=10)  # Display text to the right of the image
    
    # Call the function to display the art
    display_art()

    # Commit and close connection
    con.commit()
    con.close()

    browserinterface.mainloop()




def mainmenu(interface):
    print("back to main menu")
    interface.destroy()
    mainmenuinterface()

mainmenuinterface()
