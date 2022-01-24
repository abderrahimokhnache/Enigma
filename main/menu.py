from tkinter import *
from main.Hash_ import hash_
from main.Hash_2 import hash_2
from config_tk import *

def run():

	root = Tk() 
	root.geometry(geo)
	root['bg'] = root_bg
	root.title(title)
	root.iconbitmap(icon)
	mother = Frame(root , bg = root_bg)
	mother.place(relx = 0.0 , rely = 0.0 , relwidth  = 1 , relheight = 1)

	Door1 = Button(mother, text = '''Hash 
	Md5 / Sha256 / Sha512''' , font = font , bg = bg , fg= fg  , relief =relief,
	command = lambda :hash_(mother ,root))

	Door1.place(relx = 0.07 , rely = 0.15 , relheight = 0.2 , relwidth = 0.86)

	Door3 = Button(mother, text = '''ASymetric key 
	(Encrypet / Decrypt with the Same key)''' , font = font   ,command = lambda :hash_2(mother , root)
	, bg = bg , fg= fg  , relief =relief)

	Door3.place(relx = 0.07 , rely = 0.45 , relheight = 0.2 , relwidth = 0.86)

	def color_ch(element):
		
		element.bind('<Enter>' , lambda e : element.config(bg = "#3a3a3a"))
		element.bind('<Leave>' , lambda e : element.config(bg = "#111111"))
		element.config(activebackground = '#111111')
		element.config(activeforeground = '#00ffff')

	for element in [Door1 , Door3] :
		color_ch(element)

	root.mainloop()
