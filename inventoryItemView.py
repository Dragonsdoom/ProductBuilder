import Tkinter as tk
import ttk

class invItemView():
    root = tk.Tk()

    def __init__(self,controller,model):
        self.controller = controller
        self.model = model
        model.addSubscriber(self)

        self.root.resizable(0,0)
        
        self.iItemNameLabelFrame = ttk.LabelFrame(self.root,text="Gun Name")
        self.iItemNameLabelFrame.grid(row=0, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        self.iItemPhotoImageLabel = ttk.Label(self.iItemNameLabelFrame,text='insertImage')
        self.iItemPhotoImageLabel.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        self.iItemTypeLabelFrame = ttk.LabelFrame(self.root,text="Product")
        self.iItemTypeLabelFrame.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        self.type_option = tk.StringVar(self.root)
        self.iItemTypeOptionMenu = ttk.OptionMenu(self.iItemTypeLabelFrame,self.type_option,'iItem','product','gun')
        self.iItemTypeOptionMenu.pack(expand=1,fill=tk.BOTH)

        self.iItemCreatedLabelFrame = ttk.LabelFrame(self.root,text='Inventory Items Created')
        self.iItemCreatedLabelFrame.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        self.iItemCreatedListBox = tk.Listbox(self.iItemCreatedLabelFrame)
        self.iItemCreatedListBox.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
        self.iItemCreatedListBox.insert(tk.END,'Create a new item')

        self.iItemAddEntry = ttk.Entry(self.iItemCreatedLabelFrame)
        self.iItemAddEntry.grid(row=2, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        self.iItemAddButton = ttk.Button(self.iItemCreatedLabelFrame,text='Add', command=self.create_iitem)
        self.iItemAddButton.grid(row=3, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        self.iItemDeleteButton = ttk.Button(self.iItemCreatedLabelFrame,text='Delete', command=self.delete_iitem)
        self.iItemDeleteButton.grid(row=4, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        self.iItemLoadButton = ttk.Button(self.iItemCreatedLabelFrame,text='Load', command=None)
        self.iItemLoadButton.grid(row=5, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        self.iItemSaveButton = ttk.Button(self.iItemCreatedLabelFrame,text='Save', command=None)
        self.iItemSaveButton.grid(row=6, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        self.iItemClearButton = ttk.Button(self.iItemCreatedLabelFrame,text='Clear', command=self.clear_iitems)
        self.iItemClearButton.grid(row=7, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        self.iItemDescLabelFrame = ttk.LabelFrame(self.root,text="Description")
        self.iItemDescLabelFrame.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        self.iItemDescEntry = tk.Text(self.iItemDescLabelFrame)
        self.iItemDescEntry.pack(fill=tk.BOTH, expand=1)

        self.iItemTraitLabelFrame = ttk.LabelFrame(self.root,text="Traits")
        self.iItemTraitLabelFrame.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        self.iItemTraitScrollbar = ttk.Scrollbar(self.iItemTraitLabelFrame,orient=tk.HORIZONTAL)
        self.iItemTraitScrollbar.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        self.iItemOptionLabelFrame = ttk.LabelFrame(self.root,text="Options")
        self.iItemOptionLabelFrame.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        self.iItemOptionCbox = ttk.Checkbutton(self.iItemOptionLabelFrame)
        self.iItemOptionCbox.pack(side=tk.LEFT)

        self.iItemOptionLabel = ttk.Label(self.iItemOptionLabelFrame,text="Option 1")
        self.iItemOptionLabel.pack(side=tk.LEFT)
        
    def mainLoop(self):
        tk.mainloop()

    def loadLastIItem(self):
        self.iItemNameLabel['text'] = self.controller.getInvItemsCreated()[0].name

    def create_iitem(self):
        name = self.iItemAddEntry.get()
        self.iItemAddEntry.delete(0,tk.END)
        if name:
            self.update_name(name)
            iitem = self.type_option.get()
            #Make an iitem?

    def delete_iitem(self):
        if self.iItemCreatedListBox.size() > 1:
            index = self.iItemCreatedListBox.index(tk.ACTIVE)-1
            self.iItemCreatedListBox.delete(tk.ACTIVE)
        else:
            self.iItemCreatedListBox.insert(tk.END, "Create a new item")
            index = 0
        
        self.iItemCreatedListBox.activate(index)              
        self.iItemNameLabelFrame.config(text=self.iItemCreatedListBox.index(tk.ACTIVE))
            
    def update_name(self,name):
        if name:
            if self.iItemCreatedListBox.index(0) == "Create a new item":
                self.iItemCreatedListBox.delete(0,tk.END)
            self.iItemCreatedListBox.insert(tk.END, name)
            self.iItemNameLabelFrame.config(text=name)
            
    def clear_iitems(self):
        self.iItemCreatedListBox.delete(0,tk.END)
        self.iItemCreatedListBox.insert(tk.END, "Create a new item")
        self.iItemNameLabelFrame.config(text="Create a new item")
        
