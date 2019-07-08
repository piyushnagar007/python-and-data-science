import tkinter as tk
root=tk.Tk()
main_frame=tk.Frame(root)
label=tk.Label(main_frame,text='Hello iam label',bg='black',fg='white',font=('Times New Roman',24,'bold'))
label.pack()
main_frame.pack()
button= tk.Button(root,text='destroy',command=root.destroy,height=20,width=20,bg='blue')
button.pack()
root.title("My Application")
root.wm_minsize(400,400)
root.wm_maxsize(500,500)
root.geometry("+500+200")

root.mainloop()
