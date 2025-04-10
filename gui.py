import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox

n = 0
while n != 20:
    print("\nChoose an option:")
    print("1. Use Label")
    print("2. Use Image in Label")
    print("3. Text on image")
    print("4. Colorized Labels with fonts")
    print("5. Dynamical Content in a Label")
    print("6. Message Widget")
    print("7. Button")
    print("8. Radio Buttons")
    print("9. Indicator")
    print("10. Simple Checkboxes")
    print("11. CheckBox with Button")
    print("12. Button for checking the state of the checkbox")
    print("13. Entry Widgets")
    print("14. Canvas Widgets")
    print("15. Sliders")
    print("16. Text Widgets")
    print("17. Dialogues and Message Boxes")
    print("18. Menu")
    print("19. Event")
    print("20. Exit\n")

    n = int(input("Enter your choice: "))

    if n == 1:
        print("Using Labels")
        root = tk.Tk()
        w = tk.Label(root, text="Hello Tkinter!")
        w.pack()
        root.mainloop()

    elif n == 2:
        print("Using Images in Labels")
        root = tk.Tk()
        try:
            logo = tk.PhotoImage(file="Python-logo-notext.svg.png")
            w1 = tk.Label(root, image=logo)
            w1.pack(side="right")
        except Exception as e:
            print("Error loading image:", e)

        explanation = """At present, only GIF and PPM/PGM formats are supported."""
        w2 = tk.Label(root, justify=tk.LEFT, padx=10, text=explanation)
        w2.pack(side="left")
        root.mainloop()

    elif n == 3:
        print("The text drawn on top of the image")
        root = tk.Tk()
        try:
            logo = tk.PhotoImage(file="Python-logo-notext.svg.png")
            explanation = """At present, only GIF and PPM/PGM formats are supported."""
            w = tk.Label(root, compound=tk.CENTER, text=explanation, image=logo)
            w.pack(side="right")
        except Exception as e:
            print("Error loading image:", e)
        root.mainloop()

    elif n == 4:
        print("Colorized Labels in various fonts")
        root = tk.Tk()
        tk.Label(root, text="Red Text in Times Font", fg="red", font="Times").pack()
        tk.Label(root, text="Green Text in Helvetica Font", fg="light green", bg="dark green", font="Helvetica 16 bold italic").pack()
        tk.Label(root, text="Blue Text in Verdana bold", fg="blue", bg="yellow", font="Verdana 10 bold").pack()
        root.mainloop()

    elif n == 5:
        print("Dynamical Content in a Label")
        counter = 0

        def counter_label(label):
            def count():
                global counter
                counter += 1
                label.config(text=str(counter))
                label.after(1000, count)
            count()

        root = tk.Tk()
        root.title("Counting Seconds")
        label = tk.Label(root, fg="green")
        label.pack()
        counter_label(label)
        button = tk.Button(root, text='Stop', width=25, command=root.destroy)
        button.pack()
        root.mainloop()

    elif n == 6:
        print("Message Widget")
        master = tk.Tk()
        msg = tk.Message(master, text="Whatever you do will be insignificant, but it is very important that you do it.")
        msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        msg.pack()
        master.mainloop()

    elif n == 7:
        print("Button")
        root = tk.Tk()

        def write_slogan():
            print("Tkinter is easy to use!")

        frame = tk.Frame(root)
        frame.pack()
        button = tk.Button(frame, text="QUIT", fg="red", command=root.quit)
        button.pack(side=tk.LEFT)
        slogan = tk.Button(frame, text="Hello", command=write_slogan)
        slogan.pack(side=tk.LEFT)
        root.mainloop()

    elif n == 8:
        print("Radio Buttons")
        root = tk.Tk()
        v = tk.IntVar()
        v.set(1)
        languages = [("Python", 1), ("Perl", 2), ("Java", 3), ("C++", 4), ("C", 5)]

        def ShowChoice():
            print(v.get())

        tk.Label(root, text="Choose your favourite programming language:", justify=tk.LEFT, padx=20).pack()
        for language, val in languages:
            tk.Radiobutton(root, text=language, padx=20, variable=v, command=ShowChoice, value=val).pack(anchor=tk.W)
        root.mainloop()

    elif n == 17:
        print("Dialogues and Message Boxes")

        def answer():
            messagebox.showerror("Answer", "Sorry, no answer available")

        def callback():
            if messagebox.askyesno('Verify', 'Really quit?'):
                messagebox.showwarning('Yes', 'Not yet implemented')
            else:
                messagebox.showinfo('No', 'Quit has been cancelled')

        root = tk.Tk()
        Button(root, text='Quit', command=callback).pack(fill=X)
        Button(root, text='Answer', command=answer).pack(fill=X)
        root.mainloop()

    elif n == 18:
        print("Menu")

        def NewFile():
            print("New File!")

        def OpenFile():
            root.filename = filedialog.askopenfilename(initialdir="/", title="Select file")
            print(root.filename)

        def About():
            print("This is a simple example of a menu")

        root = tk.Tk()
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=NewFile)
        filemenu.add_command(label="Open...", command=OpenFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=About)
        root.mainloop()

    elif n == 19:
        print("Event")

        def hello(event):
            print("Single Click, Button-1")

        def quit_program(event):
            print("Double Click, so let's stop")
            root.quit()

        root = tk.Tk()
        widget = Button(root, text='Mouse Clicks')
        widget.pack()
        widget.bind('<Button-1>', hello)
        widget.bind('<Double-1>', quit_program)
        root.mainloop()

    elif n == 20:
        print("Exiting program.")
        break

    else:
        print("Invalid option! Please try again.")

