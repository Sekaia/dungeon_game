from tkinter import Button

class Cell:
    def __init__(self, is_monster=False):
        self.is_monster = is_monster
        self.cell_btn_object = None

    def create_btn_object(self, location):
        btn = Button(
            location,
            text="Text"
        )
        btn.bind("<Button-1>")
        self.cell_btn_object = btn
