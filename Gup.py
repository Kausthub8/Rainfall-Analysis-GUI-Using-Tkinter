import Tkinter
from Tkinter import *


from Data1 import regression_plot
from stats import stats_column

class Application(Frame):
     def __init(self, master=None):
         super().__init__(master)
         self.master = master
         self.create_widgets()

    
     def create_widgets(self):
         self.winfo_toplevel().title("Gup.py")
         self.l1 = Label(self,master, text = "Fname")
         self.l2 = Label(self.master, text = "X Label")
         self.l3 = Label(self.master, text = "Y Label")

         self.l1.grid(row=0)
         self.l2.grid(row=1)
         self.l3.grid(row=2)


         self.eFname = Entry(self.master, width = 50)
         self.eX = Entry(self.master, width = 50)
         self.eY = Entry(self.master, width = 50)

         self.eFname.grid(row = 0, column = 1, sticky = W)
         self.eX.grid(row = 1, column = 1, sticky = W)
         self.eY.grid(row = 2, column = 1, sticky = W)


         self.txtX = Text(self.master, width = 25)
         self.txtY = Text(self.master, width = 25)


         self.txtX.grid(row = 3, column = 0, sticky = W)
         self.txtY.grid(row = 3, column = 1, sticky = W)
         self.style = Style()
         self.style.map('D.TButton',
         foreground = [('pressed', 'red'), ('active', 'green')],
         background=[('pressed','disabled', 'black'), ('active', 'white')]
         )
         self.btn = Button(self.master, text = "Regression Graph", style="D.TButton")
         self.btn.grid(row = 4, column = 1, sticky = W)


         self.stats = Button(self.master, text= "Stats", style="D.TButton")
         self.stats.grid(row =4, column = 1, sticky = W)

         self.quit = Button(self.master, text="Quit", style = "D.TButton", command = self.master.destroy)
         self.quit.grid(row=4, column=1, sticky = W)
          
      def show_graph(self):
              regression_plot(self.eFname.get(), self.eX.get(), self.eY.get())

      def show_stats(self):
          xstats, ystats = stats_columns(self.eFname.get(), self.eX.get())
          self.txtX.insert(INSERT, xstats)
          self.txtY.insert(INSERT, ystats)   
                       
         root = Tk()

app = Application(master = root)
app.mainloop()
