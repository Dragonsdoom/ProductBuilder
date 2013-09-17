import Tkinter as tk

class invItemView():
    root = tk.Tk()

    def __init__(self,controller,model):
        self.controller = controller
        self.model = model
        model.addSubscriber(self)

        self.iItemNameLabelFrame = tk.LabelFrame(self.root,text="Gun Name")
        self.iItemNameLabelFrame.pack()

        self.iItemTypeLabelFrame = tk.LabelFrame(self.root,text="Product")
        self.iItemTypeLabelFrame.pack()

        typeOption = tk.StringVar(self.root)
        self.iItemTypeOptionMenu = tk.OptionMenu(self.iItemTypeLabelFrame,typeOption, 'iItem','product','gun')
        self.iItemTypeOptionMenu.pack()
        
    def mainLoop(self):
        tk.mainloop()

    def loadLastIItem(self):
        self.iItemNameLabel['text'] = self.controller.getInvItemsCreated()[0].name
