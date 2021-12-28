from tkinter import *
from tkinter import ttk , filedialog as fd ,messagebox as msg
from hashlib import *
from config_tk import *
import hashlib,binascii
import tkinter.scrolledtext as st
import logging
from cryptography.fernet import Fernet #this for generating the key

def hash_2(mother ,root):
	for widget in mother.winfo_children() :
		widget.destroy()

	root.geometry('500x550')

	try:
	
		with open("key.key" , 'rb') as key_file :
			 key = key_file.read()
		
	except :		

		key= Fernet.generate_key() #generate a new key for encryption
		with open("key.key" , 'wb') as key_file :
			key_file.write(key)

	def hash_options(param):
		f = Fernet(key) 
		if param == 'Enc' :
			msg = input_area.get(0.1 , END) 
			msg_enc = f.encrypt(bytes(msg.encode('utf-8')))
			output_area.delete(0.1, END) 
			output_area.insert(INSERT , msg_enc)
		if param == 'Dec' :
			msg = input_area.get(0.1 , END) 
			msg_dec = f.decrypt(bytes(msg.encode('utf-8')))
			output_area.insert(INSERT , msg_dec)


	k_title = Label(mother , text = "ASymetric Key", font = font, bg= bg , fg =fg )
	k_title.place(relx = 0.05, rely = 0.05 , relheight = 0.07 , relwidth = 0.4)
	message = Text(mother , font= font )
	message.place(relx= 0.05 , rely = 0.12 , relwidth = 0.9 , relheight = 0.12)
	message.insert(INSERT , key)


	i_title = Label(mother , text = "Input area", font = font , bg= bg , fg =fg )
	i_title.place(relx = 0.05, rely = 0.27 , relheight = 0.07 , relwidth = 0.4)	
	input_area = Text(mother , font  = font)
	input_area.place(relx= 0.05 , rely = 0.34 , relwidth = 0.9 , relheight = 0.25)

	o_title = Label(mother , text = "Output area", font = font , bg= bg , fg =fg )
	o_title.place(relx = 0.05, rely = 0.62 , relheight = 0.07 , relwidth = 0.4)
	output_area = Text(mother , font  = font)
	output_area.place(relx= 0.05 , rely = 0.69 , relwidth = 0.9 , relheight = 0.25)

	Encrypt_btn= Button(mother , text = "Encrypt",font = font , bg= bg , fg =fg,
		command =lambda : hash_options('Enc'),
		relief ='flat')
	Encrypt_btn.place(relx= 0.73 , rely = 0.35 , relwidth = 0.2 , relheight = 0.1)

	Decrypt_btn= Button(mother , text = "Decrypt",font = font , bg= bg , fg =fg,
		command =lambda : hash_options('Dec'),
		relief ='flat')
	Decrypt_btn.place(relx= 0.73 , rely = 0.47 , relwidth = 0.2 , relheight = 0.1)
	
	apply_ch([Decrypt_btn , Encrypt_btn , o_title , i_title , k_title ] )




