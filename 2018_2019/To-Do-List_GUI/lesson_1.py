
#GUI & DICTIONARY EXAMPLE
#Part I: Getting Started

import tkinter

root = tkinter.Tk()
root.title("GUI/DICT EXAMPLE")


albums = {}

#Test Data
albums["Bob Mould"] = "BSOR"
albums["The Smiths"] = "Meat is Murder"
albums["The Cure"] = "Disintegration"


#Function
def show_all():
	# Clear the listbox
	lb_music.delete(0, "end")

	# Iterate through the keys and add to the listbox
	for artist in albums:
		lb_music.insert("end", artist)

def show_one():
	artist = lb_music.get("active") # keys
	album = albums[artist] # values
	msg = artist + " : " + album
	lbl_output["text"] = msg

def add_one():
	info = txt_input.get()
	split_info = info.split(",")
	artist = split_info[0]
	album = split_info[1]
	album[artist] = album
	

#GUI
lbl_output = tkinter.Label(root, text="Ready")
lbl_output.pack()

txt_input = tkinter.Entry(root)
txt_input.pack()

lb_music = tkinter.Listbox(root)
lb_music.pack()

btn_show_all = tkinter.Button(root, text="Show All", command=show_all)
btn_show_all.pack()


btn_show_one = tkinter.Button(root, text="Show one", command=show_one)
btn_show_one.pack()

btn_add_one = tkinter.Button(root, text="Add One", command=add_one)
btn_add_one.pack()


root.mainloop()







