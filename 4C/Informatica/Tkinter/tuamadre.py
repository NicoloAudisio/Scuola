import tkinter as tk

def main():
    # Creazione della finestra
    window = tk.Tk()

    # Variabile di controllo per i radio button
    selected_option = tk.StringVar()

    # Funzione di gestione della selezione
    def option_selected():
        selected = selected_option.get()
        if selected == "1vs1":
            input_label1.config(text="Giocatore 1:")
            input_label2.config(text="Giocatore 2:")
            entry2.pack()
        elif selected == "1vspc":
            input_label1.config(text="Giocatore:")
            input_label2.config(text="")
            entry2.pack_forget()

    # Creazione dei radio button
    radio1 = tk.Radiobutton(window, text="1vs1", variable=selected_option, value="1vs1", command=option_selected)
    radio2 = tk.Radiobutton(window, text="1vspc", variable=selected_option, value="1vspc", command=option_selected)

    # Posizionamento dei radio button
    radio1.pack()
    radio2.pack()

    # Creazione delle caselle di input
    input_label1 = tk.Label(window, text="Giocatore 1:")
    input_label1.pack()
    entry1 = tk.Entry(window)
    entry1.pack()

    input_label2 = tk.Label(window, text="Giocatore 2:")
    
    # Funzione per nascondere la seconda casella di input all'avvio
    def hide_entry2():
        entry2.pack_forget()

    hide_entry2()

    entry2 = tk.Entry(window)

    # Avvio del main loop
    window.mainloop()

if __name__ == "__main__":
    main()
