import json
import os
from tkinter import *
from tkinter.ttk import *
import pprint
# alising

ask = input
pp = pprint.PrettyPrinter(indent=4)


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

jload = json.load

class MyFirstGUI:
    def __init__(self, master):
        self.master = master

        self.programs = os.listdir('programs')
        self.photo = ''
        self.icons = []
        self.commands = []
        print('programs:', self.programs)
        for i, program in enumerate(self.programs):
            print('entered', program)
            jsonpath = 'programs/{}/cmdlaunch.json'.format(program)
            print('opening json path', jsonpath)
            info = jload(open(jsonpath))
            print('info looks like', end='\n\n')
            pretty(info)
            print(end='\n\n')
            photo = PhotoImage(file = 'icons/'+info['icon']) 
            photoimage = photo.subsample(3, 3) 
            self.icons.append(Icon(photoimage, info, program))
            self.commands.append(info['commands'])


        pretty(self.icons)
        for i, icon in enumerate(self.icons):
            print('// entering', icon.program)
            print('icons ... ... ... ...')
            pretty(icon.info, icon.program)
            x = Button(root, text=icon.info['name'] +'\n' + icon.info['version'], 
                        image=icon.photo,
                        compound=LEFT,
                        command=lambda: self.button_exec(icon))
            x.grid(row=0, column=i)

    def button_exec(self, icon):
        os.chdir('programs/'+icon.program)
        for command in icon.info['commands']:
            print(command)
        print(f'''
            The following button with info was clicked:
            program:{icon.program}
            name:{icon.info['name']}
            version:{icon.info['version']}
            icon:{icon.info['icon']}
            commands:{icon.info['commands']}
            ''')
        os.chdir('../..')

my_gui = MyFirstGUI(root)
root.mainloop()