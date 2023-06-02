import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_932 = tk.Button(root)
        GButton_932["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_932["font"] = ft
        GButton_932["fg"] = "#000000"
        GButton_932["justify"] = "center"
        GButton_932["text"] = "Button"
        GButton_932.place(x=150, y=210, width=70, height=25)
        GButton_932["command"] = self.GButton_932_command

        GCheckBox_802 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_802["font"] = ft
        GCheckBox_802["fg"] = "#333333"
        GCheckBox_802["justify"] = "center"
        GCheckBox_802["text"] = "CheckBox"
        GCheckBox_802.place(x=100, y=100, width=70, height=25)
        GCheckBox_802["offvalue"] = "0"
        GCheckBox_802["onvalue"] = "1"
        GCheckBox_802["command"] = self.GCheckBox_802_command

        GLineEdit_692 = tk.Entry(root)
        GLineEdit_692["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_692["font"] = ft
        GLineEdit_692["fg"] = "#333333"
        GLineEdit_692["justify"] = "center"
        GLineEdit_692["text"] = "Entry"
        GLineEdit_692.place(x=60, y=170, width=70, height=25)

        GMessage_275 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_275["font"] = ft
        GMessage_275["fg"] = "#333333"
        GMessage_275["justify"] = "center"
        GMessage_275["text"] = "Message"
        GMessage_275.place(x=200, y=320, width=80, height=25)

        GListBox_957 = tk.Listbox(root)
        GListBox_957["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_957["font"] = ft
        GListBox_957["fg"] = "#333333"
        GListBox_957["justify"] = "center"
        GListBox_957.place(x=310, y=90, width=80, height=25)

        GLabel_208 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_208["font"] = ft
        GLabel_208["fg"] = "#333333"
        GLabel_208["justify"] = "center"
        GLabel_208["text"] = "Z kreatora"
        GLabel_208.place(x=60, y=40, width=70, height=25)

    def GButton_932_command(self):
        print("command")

    def GCheckBox_802_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
