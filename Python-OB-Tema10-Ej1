import tkinter
from tkinter import messagebox, ttk

def show_selection():
    option_selection = selection.get()
    messagebox.showinfo(
        message=f"La opción seleccionada es: {option_selection}",
        title="Selección"
    )

def delete_selection():
    main_window.destroy()
    make_window()

def exit():
    main_window.quit()

def make_window():
    main_window = tkinter.Tk()
    main_window.columnconfigure(0, weight=8)
    main_window.title("Elige una opción")
    selection = tkinter.StringVar()
    option_one = ttk.Radiobutton(main_window, text='Me gusta mucho', value='1', variable=selection)
    option_two = ttk.Radiobutton(main_window, text='Me gusta', value='2', variable=selection)
    option_three = ttk.Radiobutton(main_window, text='Ni me gusta ni me disgusta', value='3', variable=selection)
    option_four = ttk.Radiobutton(main_window, text='No me gusta', value='4', variable=selection)
    option_five = ttk.Radiobutton(main_window, text='Me disgusta mucho', value='5', variable=selection)
    option_one.grid(column=0, row=1, sticky=tkinter.W, pady=5, padx=5)
    option_two.grid(column=0, row=2, sticky=tkinter.W, pady=5, padx=5)
    option_three.grid(column=0, row=3, sticky=tkinter.W, pady=5, padx=5)
    option_four.grid(column=0, row=4, sticky=tkinter.W, pady=5, padx=5)
    option_five.grid(column=0, row=5, sticky=tkinter.W, pady=5, padx=5)
    button_show = ttk.Button(text="Mostrar selección", command=show_selection)
    button_show.grid(column=0, row=6, sticky=tkinter.S)
    button_delete = ttk.Button(text="Borrar selección", command=delete_selection)
    button_delete.grid(column=0, row=7, sticky=tkinter.S)
    button_quit = ttk.Button(text="Salir", command=exit)
    button_quit.grid(column=0, row=8, sticky=tkinter.S)


main_window = tkinter.Tk()
main_window.columnconfigure(0, weight=8)
main_window.title("Elige una opción")
selection = tkinter.StringVar()
option_one = ttk.Radiobutton(main_window, text='Me gusta mucho', value='1', variable=selection)
option_two = ttk.Radiobutton(main_window, text='Me gusta', value='2', variable=selection)
option_three = ttk.Radiobutton(main_window, text='Ni me gusta ni me disgusta', value='3', variable=selection)
option_four = ttk.Radiobutton(main_window, text='No me gusta', value='4', variable=selection)
option_five = ttk.Radiobutton(main_window, text='Me disgusta mucho', value='5', variable=selection)
option_one.grid(column=0, row=1, sticky=tkinter.W, pady=5, padx=5)
option_two.grid(column=0, row=2, sticky=tkinter.W, pady=5, padx=5)
option_three.grid(column=0, row=3, sticky=tkinter.W, pady=5, padx=5)
option_four.grid(column=0, row=4, sticky=tkinter.W, pady=5, padx=5)
option_five.grid(column=0, row=5, sticky=tkinter.W, pady=5, padx=5)


button_show = ttk.Button(text="Mostrar selección", command=show_selection)
button_show.grid(column=0, row=6, sticky=tkinter.S)


button_delete = ttk.Button(text="Borrar selección", command=delete_selection)
button_delete.grid(column=0, row=7, sticky=tkinter.S)

button_quit = ttk.Button(text="Salir", command=exit)
button_quit.grid(column=0, row=8, sticky=tkinter.S)

main_window.mainloop()

