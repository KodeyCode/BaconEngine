from tkinter import *

class window:
	def up(e):
		display.move(spr,0,-20)
	def down(e):
		display.move(spr,0,20)
	def left(e):
		display.move(spr,-20,0)
	def right(e):
		display.move(spr,20,0)
	def __init__(self,title,hw):
		self.title = title
		global root
		root = Tk()
		root.title(self.title)
		root.bind('<Up>',window.up)
		root.bind('<Down>',window.down)
		root.bind('<Left>',window.left)
		root.bind('<Right>',window.right)
	def tweak(self,title,hw):
		self.title = title
		root.title(self.title)
		root.geometry(hw.replace(':','x'))
	def run(self):
		root.mainloop()
class screen:
	def __init__(self,hw,bg):
		self.height = hw.split(':')[0]
		self.width = hw.split(':')[1]
		self.bg = bg
		global display
		display = Canvas(height=self.height,width=self.width,bg=self.bg)
		display.pack()
	def tweak(self,hw):
		self.height = hw.split(':')[0]
		self.width =  hw.split(':')[1]
def getCoor(event)
class obj:
    def skin(self,img,name):
        self.img = PhotoImage(file=img)
        self.sprname = name
    def add(self,hw):
    	global spr
        global obcount
    	spr = display.create_image(hw.split(':')[0],hw.split(':')[1],image=self.img)
        obcount +=1
    def tele(self,xy):
        x = xy.split(':')[0]
        y = xy.split(':')[1]
        display.move(spr,abs(display.coords(spr),x),abs(display.coords(spr),y)
