#interface.py
#made by austin wilson.
# uses tkinter to make an interface where you can choose a role and do the
#related functions.
from tkinter import*
import artshackdb

def mainmenuinterface():
    interface= Tk() #create interface
    interface.geometry("750x750") #sets size
    interface.title("Art Shack")#window title
    label=Label(interface,font=("Arial",16,"bold"),justify=CENTER,text='Choose your role')#create the select prompt
    label.grid(row=0, column=0, columnspan=4, pady=100) #pack it into a window #with y padding 100
    #creating buttons
    buyerbutton = Button(interface, text="Buyer",  command=lambda: buyer(interface))  # buyer button
    sellerbutton = Button(interface, text="Seller", command=lambda: seller(interface))  # seller button
    adminbutton = Button(interface, text="Admin", command=lambda: admin(interface))  # admin button
    browserbutton = Button(interface, text="Browser", command=lambda: browser(interface))  # browser button
    # Packing buttons
    buyerbutton.grid(row=1, column=0, padx=10, pady=20)
    sellerbutton.grid(row=1, column=1, padx=10, pady=20)
    adminbutton.grid(row=1, column=2, padx=10, pady=20)
    browserbutton.grid(row=1, column=3, padx=10, pady=20)
        #centers and spaces evenly
    for i in range(4):
        
        interface.grid_columnconfigure(i, weight=1)

    


    interface.mainloop()
#functions for button pressing along with interface definitions
def buyer(interface):
	print("buyer clicked")
	interface.destroy()
	buyerinterface()
def buyerinterface():
    buyerinterface = Tk()
    buyerinterface.geometry("750x750")
    buyerinterface.title("Buyer")
    label = Label(buyerinterface, text="Buyer Interface", font=("Arial", 16, "bold"))
    label.place(x=375,y=20)
    
    #main menu button
    mainbutton=Button(buyerinterface,text="Main Menu", command=lambda: mainmenu(buyerinterface))
    mainbutton.place(x=0,y=0)
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
    label.place(x=375,y=20)
    
    #main menu button
    mainbutton=Button(sellerinterface,text="Main Menu", command=lambda: mainmenu(sellerinterface))
    mainbutton.place(x=0,y=0)
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
    label.place(x=375,y=20)
    
    #main menu button
    mainbutton=Button(admininterface,text="Main Menu", command=lambda: mainmenu(admininterface))
    mainbutton.place(x=0,y=0)
    admininterface.mainloop()

    
def browser(interface):
	print("browser clicked")
	interface.destroy()
	browserinterface()

	
def browserinterface():
    browserinterface = Tk()
    browserinterface.geometry("750x750")
    browserinterface.title("Browser")
    label = Label(browserinterface, text="Browser Interface", font=("Arial", 16, "bold"))
    label.place(x=375,y=20)
    #main menu button
    mainbutton=Button(browserinterface,text="Main Menu", command=lambda: mainmenu(browserinterface))
    mainbutton.place(x=0,y=0)
    browserinterface.mainloop()

    
def mainmenu(interface):
	print("back to main menu")
	interface.destroy()
	mainmenuinterface()


    
mainmenuinterface()
