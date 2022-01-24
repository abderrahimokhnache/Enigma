from tkinter import *
from tkinter import ttk
from hashlib import *
from config_tk import *
import binascii, logging
from cryptography.fernet import Fernet #this for generating the key


Log_format = "%(levelname)s - %(asctime)s - %(message)s"
logging.basicConfig(filename = 'History.txt' , level = logging.DEBUG,
	format = Log_format )#filemode = 'w' to overwrite 




def hash_(mother , root):
	for widget in mother.winfo_children() :
		widget.destroy()

	root.geometry("500x500")
	logger = logging.getLogger()

	def crypt_options(param):
		msg = 'Algorithm : {} - Password : {} '.format(cb.get() , PW.get())
		logger.info(msg)

		if param == 'Normal':
			crypt = cb.get()
			if crypt == "SHA512":
				crypt = sha512()
			elif crypt == "SHA1":
				crypt = sha1()
			elif crypt == "SHA256":
				crypt = sha256()
			elif crypt == "SHA224":
				crypt = sha224()
			elif crypt == "SHA384":
				crypt = sha384()
			else:
				crypt = md5()
			Name=PW.get()
			crypt.update(Name.encode('utf-8'))
			PW.delete(0,END)
			txt.delete(0.0,END)
			txt.insert(INSERT,crypt.hexdigest())
			with open('History.log' , 'a') as History_file :
				log_data = (Name  ,  crypt.hexdigest())
				History_file.write(str(log_data) + '\n')

		elif param == 'Advance':

			algorithm = cb.get()
			password = PW.get()
			keys = Key.get()
			times = Times.get()
			dk = pbkdf2_hmac(algorithm ,bytes( password , encoding ="utf-8")
				, bytes( keys, encoding ="utf-8"),int(times))
			txt.insert(INSERT,binascii.hexlify(dk))

	def Advance():
		global Key
		global Times
		global bt2
		TimesL = Label(mother , text = "Times ", font = font , bg= bg , fg =fg )
		TimesL.place(relx= 0.03 , rely = 0.52)
		Times= Entry(mother , font= font )
		Times.place(relx= 0.17 , rely = 0.5 , relwidth = 0.25 , relheight = 0.1)

		KeyL = Label(mother , text = "Key ", font = font , bg= bg , fg =fg )
		KeyL.place(relx= 0.45 , rely = 0.52)
		Key= Entry(mother , font= font )
		Key.place(relx= 0.545 , rely = 0.5 , relwidth = 0.2 , relheight = 0.1)
		bt2= Button(mother , text = "Encrypt",font = font , bg= '#111111' , fg =fg
			,relief ='flat' , command =lambda : crypt_options('Advance'))
		bt2.place(relx= 0.78 , rely = 0.5 , relwidth = 0.2 , relheight = 0.1)


	PW= ttk.Entry(mother , font= font )
	PW.place(relx= 0.05 , rely = 0.2 , relwidth = 0.9 , relheight = 0.1)
	cb1= StringVar()
	cb = ttk.Combobox(mother ,font = font)

	cb["values"] = ('--Algorithms--','SHA1', 'SHA224', 'SHA384',  'SHA256', 'SHA512', 'MD5')
	cb.current(0)
	cb.place(relx= 0.05 , rely = 0.35 , relwidth = 0.4 , relheight = 0.1)
	bt1= Button(mother , text = "Encrypt",font = font , bg= '#111111' , fg =fg,
		relief ='flat' , command = lambda : crypt_options('Normal'))
	bt1.place(relx= 0.45 , rely = 0.35 , relwidth = 0.2 , relheight = 0.1)


	txt=Text(mother , font  = font)
	txt.place(relx= 0.05 , rely = 0.65 , relwidth = 0.9 , relheight = 0.3)

	Advancebu = Button(mother , text = 'Advance',command = Advance ,font = font ,
	 bg= bg , fg =fg,relief ='flat' )
	Advancebu.place(relx= 0.661 , rely = 0.35 , relwidth = 0.19 , relheight = 0.1)

	apply_ch([Advancebu , bt1 ,] )


	mother.mainloop()


