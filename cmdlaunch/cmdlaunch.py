import json
import os
from tkinter import *
from tkinter.ttk import *
import pprint

# aliasing
ask = input
pp = pprint.PrettyPrinter(indent=4)
jload = json.load

def pretty(*args):
    for arg in args:
        pp.pprint(arg)

class Icon:
    def __init__(self, photo, info, program):
        self.photo = photo
        self.info = info
        self.program = program

    def __repr__(self):
        return '\n@object {} {}\n'.format(self.info, self.program)

root = Tk()


class CmdGUI:
    def __init__(self, master):
        self.master = master

        self.programs = os.listdir('programs')
        self.photo = ''
        self.icons = []
        self.commands = []
        #print('programs:', self.programs)
        for i, program in enumerate(self.programs):
            jsonpath = 'programs/{}/cmdlaunch.json'.format(program)
            info = jload(open(jsonpath))
            photo = PhotoImage(file = 'icons/'+info['icon']) 
            photoimage = photo.subsample(3, 3) 
            self.icons.append(Icon(photoimage, info, program))
            self.commands.append(info['commands'])


        # pretty(self.icons)
        # Twice the loop to preserve image reference
        for i, icon in enumerate(self.icons):
            self.x = Button(root, text=icon.info['name'] +'\n' + icon.info['version'], 
                        image=icon.photo,
                        compound=LEFT,
                        command=lambda icon=icon: self.button_exec(icon))
            self.x.grid(row=0, column=i)

    def button_exec(self, icon):
        os.chdir('programs/'+icon.program)
        for command in icon.info['commands']:
            os.system(command)
        
#        print(f'''
#            The following button with info was clicked:
#            program:{icon.program}
#            name:{icon.info['name']}
#            version:{icon.info['version']}
#            icon:{icon.info['icon']}
#            commands:{icon.info['commands']}
#            ''')
        
        os.chdir('../..')

cmdlaunch = CmdGUI(root)
root.mainloop()
