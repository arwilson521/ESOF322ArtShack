from tkinter import *
import sqlite3
from PIL import Image, ImageTk
import os

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
    buyerinterface = Tk()
    buyerinterface.geometry("750x750")
    buyerinterface.title("Buyer")
    label = Label(buyerinterface, text="Buyer Interface", font=("Arial", 16, "bold"))
    label.place(x=375, y=20)
    
    # Main menu button
    mainbutton = Button(buyerinterface, text="Main Menu", command=lambda: mainmenu(buyerinterface))
    mainbutton.place(x=0, y=0)
    
    # Purchase function (WIP)
    def purchaseart(artpiece):
        print(artpiece)
    
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
    
    # Main menu button
    mainbutton = Button(admininterface, text="Main Menu", command=lambda: mainmenu(admininterface))
    mainbutton.place(x=0, y=0)
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
    cur.execute("SELECT art, price, type FROM art")
    artdata = cur.fetchall()

    def display_art():
        # Create a frame for the images and info labels
        frame = Frame(browserinterface)
        frame.pack(pady=50)  # Add some space around the frame

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
