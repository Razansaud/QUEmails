from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

# function to define database
def Database():
 global con, cursor
 # creating contact database
 con = sqlite3.connect("contact.db")
 cursor = con.cursor()
 # creating members table
 cursor.execute(
 "CREATE TABLE IF NOT EXISTS members (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, fname TEXT, lname TEXT,"
 " Email TEXT)")

# defining function for creating GUI Layout
def Displaywindow():

 # creating window
 display_screen = Tk()
 # setting width and height for window
 display_screen.geometry("760x400")
 # setting title for window
 display_screen.title("@QU")
 global tree
 global SEARCH
 global fname, lname, Email
 SEARCH = StringVar()
 fname = StringVar()
 lname = StringVar()
 Email = StringVar()
 # creating frames for layout
 # topview frame for heading
 TopViewForm = Frame(display_screen, width=600, bd=1)  # for( QU Email) heading
 TopViewForm.pack(side=TOP, fill=X)
 # (first)left frame for members from
 LFrom = Frame(display_screen, width="350", bg="#EAEFF9")
 LFrom.pack(side=LEFT, fill=Y)
 # (2nd)left frame for search form
 LeftViewForm = Frame(display_screen, width=500, bg="#F3F6FC")
 LeftViewForm.pack(side=LEFT, fill=Y)
 # mid frame for displaying lnames record
 MidViewForm = Frame(display_screen, width=600)
 MidViewForm.pack(side=RIGHT)
 # label for heading
 lbl_text = Label(TopViewForm, text="QU Emails", font=("Times", "24", "bold italic"),
                  width=600, bg="#A1C4D8")
 lbl_text.pack(fill=X)
 # creating member form in first left frame
 Label(LFrom, text="First Name ", font=("Arial", 10), bg="#EAEFF9", fg="black").pack(
   side=TOP) # setting of fname above the entry
 Entry(LFrom, font=("Arial", 10), cursor="heart", textvariable=fname).pack(side=TOP, padx=11, fill=X)
 Label(LFrom, text="Last Name ", font=("Arial", 10), bg="#EAEFF9", fg="black").pack(side=TOP)
 Entry(LFrom, font=("Arial", 10), cursor="heart", textvariable=lname).pack(side=TOP, padx=11, fill=X)
 Label(LFrom, text="Email ", font=("Arial", 10), bg="#EAEFF9", fg="black").pack(side=TOP)
 Entry(LFrom, font=("Arial", 10), cursor="heart", textvariable=Email).pack(side=TOP, padx=11, fill=X)
 Button(LFrom, text=" OK", activebackground="#DAA520", relief=FLAT, command=register, activeforeground="red"
 # this attribute for change font color when click
   , bg="#5C9DC0").pack(side=TOP, padx=60, pady=10, fill=X)
 # creating search label and entry in second frame
 lbl_txtsearch = Label(LeftViewForm, text="Enter first name", font=('Arial', 10),
 bg="#F3F6FC")
 lbl_txtsearch.pack()
 # creating search entry
 search = Entry(LeftViewForm, textvariable=SEARCH, cursor="heart", font=('Arial', 12), width=10)
 search.pack(side=TOP, padx=10, fill=X)
 # creating search button
 btn_search = Button(LeftViewForm, text="Search", relief=FLAT, activebackground="#DAA520",
 activeforeground="red"
 , command=SearchRecord, bg="#5C9DC0")
 btn_search.pack(side=TOP, padx=40, pady=10, fill=X)
 # creating view button
 btn_view = Button(LeftViewForm, text="View All", relief=FLAT, activebackground="#DAA520",
 activeforeground="red"
 , command=DisplayData, bg="#5C9DC0")
 btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
 # creating delete button
 btn_delete = Button(LeftViewForm, text="Delete", relief=FLAT, activebackground="#DAA520",
 activeforeground="red"
 , command=Delete, bg="#5C9DC0")
 btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
 # create update button
 btn_delete = Button(LeftViewForm, text="Update", relief=FLAT, activebackground="#DAA520",
 activeforeground="red"
 , command=Update, bg="#5C9DC0")
 btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
 # setting scrollbar
 scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
 scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
 tree = ttk.Treeview(MidViewForm, columns=("Id", "fname", "lname", "Email"),
 selectmode="extended", height=100, yscrollcommand=scrollbary.set,
 xscrollcommand=scrollbarx.set)
 scrollbary.config(command=tree.yview)
 scrollbary.pack(side=RIGHT, fill=Y)
 scrollbarx.config(command=tree.xview)
 scrollbarx.pack(side=BOTTOM, fill=X)
 # setting headings for the columns
 tree.heading('Id', text="Id", anchor=W)
 tree.heading('fname', text="FirstName", anchor=W)
 tree.heading('lname', text="LastName", anchor=W)
 tree.heading('Email', text="Email", anchor=W)
 # setting width of the columns
 tree.column('#0', stretch=NO, minwidth=0, width=0) # from beggning
 tree.column('#1', stretch=NO, minwidth=0, width=30) # for id
 tree.column('#2', stretch=NO, minwidth=0, width=100) # for fname
 tree.column('#3', stretch=NO, minwidth=0, width=100) # for lname
 tree.column('#4', stretch=NO, minwidth=0, width=200) # for email
 tree.pack()
 DisplayData()

def register():
 Database()

 # getting form data
 fname1 = fname.get()
 lname1 = lname.get()
 Email1 = Email.get()
 # applying empty validation
 if fname1 == '' or lname1 == '' or Email1 == '':
     tkMessageBox.showinfo("Warning", "Please, fill the empty field!")
 else:
   # execute query
   con.execute('INSERT INTO members (fname,lname,Email) '
             ' VALUES (?,?,?)', (fname1, lname1, Email1))
   con.commit()
   tkMessageBox.showinfo("Message", "Stored successfully")
   # refresh table data
   DisplayData()
   con.close()

# function to update data into database
def Update():
 Database()
 # getting form data
 fname1 = fname.get()
 lname1 = lname.get()
 Email1 = Email.get()
 # applying empty validation
 if fname1 == '' or lname1 == '' or Email1 == '':
  tkMessageBox.showinfo("Warning", "Please,fill the empty field!")
 else:
  # getting selected data
  curItem = tree.focus()
  contents = (tree.item(curItem))
  selecteditem = contents['values']
  # update query
  con.execute(
   'UPDATE members SET fname=?,lname=?, Email=? WHERE Id = ?',
   (fname1, lname1, Email1, selecteditem[0]))
  con.commit()
  tkMessageBox.showinfo("Message", "Updated successfully")
  # reset form
  Reset()
  # refresh table data
  DisplayData()
  con.close()

def Delete():
  # open database
 Database()
 if not tree.selection():
   tkMessageBox.showwarning("Warning", "Select data to delete")
 else:
  result = tkMessageBox.askquestion('Confirm',
    'Are you sure you want to delete this record?',
     icon="warning")
  if result == 'yes':
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    tree.delete(curItem)
    cursor = con.execute("DELETE FROM members WHERE Id = %d" % selecteditem[0])
    con.commit()
    cursor.close()
    con.close()


def Reset():


    # clear current data from table
    tree.delete(*tree.get_children())
    # refresh table data
    DisplayData()
    # clear search text
    SEARCH.set("")
    fname.set("")
    lname.set("")
    Email.set("")

# function to search data
def SearchRecord():
 # open database
 Database()
 # checking search text is empty or not
 if SEARCH.get() != "":
  # clearing current display data
  tree.delete(*tree.get_children())
  # select query with where clause
  cursor = con.execute("SELECT * FROM members WHERE fname LIKE ?",
  ('%' + str(SEARCH.get()) + '%',))
  # fetch all matching records
  fetch = cursor.fetchall()
  # loop for displaying all records into GUI
  for data in fetch:
    tree.insert('', 'end', values=(data))
  cursor.close()
  con.close()

# defining function to access data from SQLite database
def DisplayData():
 # open database
 Database()
 # clear current data
 tree.delete(*tree.get_children())
 # select query
 cursor = con.execute("SELECT * FROM members")
 # fetch all data from database
 fetch = cursor.fetchall()
 # loop for displaying all data in GUI
 for data in fetch:
  tree.insert('', 'end', values=(data))
  tree.bind("<Double-1>", OnDoubleClick)
 cursor.close()
 con.close()

def OnDoubleClick(self):

 # getting focused item from treeview
 curItem = tree.focus()
 contents = (tree.item(curItem))
 selecteditem = contents['values']
 # set values in the fields
 fname.set(selecteditem[1])
 lname.set(selecteditem[2])
 Email.set(selecteditem[3])
# calling function
Displaywindow()
if __name__ == '__main__':
 # Running Application
 mainloop()




