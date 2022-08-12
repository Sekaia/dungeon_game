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

for x in range(settings.GRID_SIZE + 1):
    for y in range(settings.GRID_SIZE + 1):
        c = Cell()
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

c1 = Cell()
c1.create_btn_object(center_frame)
c1.cell_btn_object.grid(column=0, row=0)

c2 = Cell()
c2.create_btn_object(center_frame)
c2.cell_btn_object.grid(column=0, row=1)


# Run the main window
root.mainloop()