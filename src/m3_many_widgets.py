import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (4 pts)
#
#   Now, we are going to practice all of our widgets.
#
#   First, create two different frames.
#
#   Next, place widgets in both frames. Your frames should have these widgets
#   in them:
#
#       - Frame 1
#           - Label
#           - Button
#           - Single Line Text Entry
#       - Frame 2
#           - Label
#           - Multi Line Text Entry
#
#   You choose what text to have in the labels and button.
#
#   Make sure you call the pack method on all your widgets and that each widget
#   is in the proper frame.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()

frame1 = tk.Frame()
label1 = tk.Label(master=frame1, text="Frame #1")
label1.pack()
button1 = tk.Button(master=frame1, text="SELF DESTRUCT BUTTON", bg="red", fg="black")
button1.pack()
entry1 = tk.Entry(master=frame1, width=55)
entry1.insert(0, "This is the self destruct button, please do NOT press it.")
entry1.pack()
frame1.pack()

frame2 = tk.Frame()
label2 = tk.Label(master=frame2, text="Frame #2")
label2.pack()
text2 = tk.Text(master=frame2, width=45, fg="red")
text2.insert("1.0", "I want to press the self destruct button!", "2.0", "\nRIGHT NOW!!!")
text2.pack()
frame2.pack()

window.mainloop()
