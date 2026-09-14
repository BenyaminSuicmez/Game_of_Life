import tkinter as tk
import time as t

def show_menu():

    config = {}

    # Initializing the tkinter window
    root = tk.Tk()
    root.title("")
    root.geometry("700x600")
    root.resizable(False, False)
    root.configure(bg="#E8E6E1")

    # Fine tuning by adding elements:

    # Adding a heading
    heading = tk.Label(root, text="The Game of Life", font=("Times New Roman", 30, "bold"), bg="#E8E6E1", fg="#2A2A28")
    heading.grid(row=0, column=0, pady=80)
    root.grid_columnconfigure(0, weight=1)

    # Adding configuration options for the user
    mode = tk.StringVar(value="infinite")



    gen_entry = tk.Entry(root, state="disabled", highlightthickness=2)
    gen_entry.grid(row=3, column=0)


    # a function that handles the availability of the input field
    def switched_mode():
        if mode.get() == "infinite":
            gen_entry.config(state="normal")
            gen_entry.delete(0, tk.END)
            gen_entry.config(state="disabled")

        if mode.get() == "custom":
            gen_entry.config(state="normal")

    # Creating the two Buttons for selecting the number of generations
    rb1 = tk.Radiobutton(root, text="Infinite Generations",font=("Times New Roman", 18), variable=mode, value="infinite", background="#E8E6E1", command=switched_mode)
    rb1.grid(row=1, column=0)

    rb2 = tk.Radiobutton(root, text="Custom Generation Limit",font=("Times New Roman", 18), variable=mode, value="custom", background="#E8E6E1", command=switched_mode)
    rb2.grid(row=2, column=0, pady=10)

    # Creating a controller so the user can decide how fast the simulation should be
    velocity = tk.Scale(root, from_=20, to=2000, length=300, resolution=10, orient="horizontal", label="Refresh (ms)", bg="#E8E6E1")
    velocity.grid(row=4, column=0, pady=15)

    # Creating the start button and its logic
    def start_game():
        if mode.get() == "infinite":
            gen_entry.config(bg="white")
            gen_entry.config(highlightbackground="white")
            config["generations"] = 100000000000
            config["delay"] = velocity.get()

            root.quit()
            root.destroy()

        if mode.get() == "custom":
            text = gen_entry.get()
            if not text.isdigit() or int(text) <= 0:
                gen_entry.config(bg="#FFCCCC")   # light red background       
                gen_entry.config(highlightbackground="red", highlightthickness=2)   # red frame

            if text.isdigit() and int(text) > 0:
                gen_entry.config(bg="white")
                config["generations"] = int(text)
                config["delay"] = velocity.get()

                root.quit()
                root.destroy()


    start_button = tk.Button(root, text="START", font=("Times New Roman", 20), highlightbackground="#4CAF50", command=start_game)
    start_button.grid(row=5, column=0, pady=40)


    # Giving user notes
    notes = tk.Label(root, text="Note: If selecting 'Custom Generation Limit' input must be an integer greater than 0.", background="#E8E6E1")
    notes.grid(row=6, column=0)

    root.mainloop()
    return config