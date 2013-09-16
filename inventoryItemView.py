import Tkinter as tk

class invItemView():
    root = tk.Tk()
    def __init__(self,controller,model):
        self.controller = controller
        self.model = model
        model.addSubscriber(self)

        self.iItemNameLabel = tk.Label(self.root,text="testtext")
        self.iItemNameLabel.pack()
        self.iItemLoadButton = tk.Button(self.root,text="Load Last Inventory Item",command=self.loadLastIItem)
        self.iItemLoadButton.pack()
        
    def mainLoop(self):
        tk.mainloop()

    def loadLastIItem(self):
        self.iItemNameLabel['text'] = self.controller.getInvItemsCreated()[0].name
