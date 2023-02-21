import tkinter as tk
from tkinter import filedialog

class SNESEmulator:
    def __init__(self, master):
        self.master = master
        self.master.title("EMU - SNES Emulator PROUDLY MADE BY FLAMES LLC")
        self.master.geometry("600x400")

        # Create a toolbar
        self.toolbar = tk.Frame(self.master, bg="gray")
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Add a "Open ROM" button to the toolbar
        self.open_rom_button = tk.Button(self.toolbar, text="Open ROM", command=self.open_rom)
        self.open_rom_button.pack(side=tk.LEFT, padx=2, pady=2)

        # Add a "Run" button to the toolbar
        self.run_game_button = tk.Button(self.toolbar, text="Run", command=self.run_game)
        self.run_game_button.pack(side=tk.LEFT, padx=2, pady=2)

        # Add a status bar
        self.status = tk.Label(self.master, text="Welcome to EMU-SNES 0.X.X DEMO!", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def open_rom(self):
        file_path = filedialog.askopenfilename(filetypes=[("SNES ROM Files", "*.smc;*.sfc")])
        if file_path:
            # Load the ROM into memory
            with open(file_path, "rb") as file:
                rom = file.read()

            # Update the status bar
            self.status.config(text=f"ROM loaded: {file_path}")

    def run_game(self):
        # Start the game
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = SNESEmulator(root)
    root.mainloop()
