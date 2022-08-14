from tkinter import *
from cell import Cell
import settings
import utils


# Create the main window
root = Tk()
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Dungeon Game")
root.resizable(False, False)

# Score/Rules area
top_frame = Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=utils.height_prct(17)
)
top_frame.place(x=0,y=0)

# Inventory area
left_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(20),
    height=utils.height_prct(83)
)
left_frame.place(x=0,y=utils.height_prct(17))

# Game area
center_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(80),
    height=utils.height_prct(83)
)
center_frame.place(x=utils.width_prct(20),y=utils.height_prct(17))

for x in range(13):  # change later
    for y in range(settings.GRID_SIZE + 2):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

Cell.create_score_label(top_frame)
Cell.score_count_label.place(x=utils.width_prct(42), y=0)

Cell.create_monster_count_label(top_frame)
Cell.monster_count_label.place(x=utils.width_prct(0), y=0)

Cell.create_treasure_count_label(top_frame)
Cell.treasure_count_label.place(x=utils.width_prct(74), y=0)

Cell.create_hint_label(left_frame)
Cell.hint_label.place(x=0,y=0)

Cell.randomize_monsters()
Cell.randomize_exit()
Cell.randomize_chests()
Cell.randomize_starting_cell()

# Run the main window
root.mainloop()