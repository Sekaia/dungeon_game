from tkinter import Button, Label
import random

import settings


class Cell:
    all = []
    used = []
    score = 0
    monster_count = settings.MONSTER_COUNT
    treasure_count = settings.TREASURE_COUNT
    monster_count_label = None
    treasure_count_label = None
    score_count_label = None
    hint_label = None
    def __init__(self,x, y, is_monster=False, is_exit=False, is_chest=False):
        self.is_exit = is_exit
        self.is_chest = is_chest
        self.is_monster = is_monster
        self.is_opened = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=8,
            height=4,
            text=f"{self.x}, {self.y}"
        )
        btn.bind("<Button-1>", self.left_click_actions)
        btn.bind("<Button-3>", self.right_click_actions)
        self.cell_btn_object = btn

    @staticmethod
    def create_score_label(location):
        lvl = Label(
            location,
            text=f"Score: {Cell.score}",
            bg="black",
            fg="white",
            width=12,
            height=2,
            font=("consolas",24)
        )
        Cell.score_count_label = lvl

    @staticmethod
    def create_hint_label(location):
        lvl = Label(
            location,
            text="There\nare\nmonsters\nnearby..",
            bg="black",
            fg="orange",
            width=14,
            height=10,
            font=("consolas", 28)
        )
        Cell.hint_label = lvl

    @staticmethod
    def create_monster_count_label(location):
        lbl = Label(
            location,
            text=f"Monsters left: {Cell.monster_count}",
            bg="black",
            fg="white",
            width=20,
            height=2,
            font=("consolas", 24)
        )
        Cell.monster_count_label = lbl

    @staticmethod
    def create_treasure_count_label(location):
        lbl = Label(
            location,
            text=f"Treasure left: {Cell.treasure_count}",
            bg="black",
            fg="white",
            width=20,
            height=2,
            font=("consolas", 24)
        )
        Cell.treasure_count_label = lbl

    def left_click_actions(self, event):
        if self.surrounded_cells_monster > 0:
            if self.surrounded_cells_monster == 1:
                print("There is a monster nearby..")
            else:
                print("There are monsters nearby..")
        if self.surrounded_cells_chest > 0:
            print("There is treasure nearby..")
        if self.surrounded_cells_exit > 0:
            print("The exit is around here..")
        if self.is_monster:
            self.show_monster()
        elif self.is_exit:
            self.show_exit()
        elif self.is_chest:
            self.show_chest()
            for cell_obj in self.reveal_area:  # reveals area around player when they open a chest
                if cell_obj.is_monster:
                    cell_obj.show_monster()
                elif cell_obj.is_exit:
                    cell_obj.show_exit()
                elif cell_obj.is_chest:
                    cell_obj.show_chest()
                else:
                    cell_obj.show_cell()
        else:
            self.show_cell()

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):  # if 1, 1:
        cells = [
            # self.get_cell_by_axis(self.x - 1, self.y - 1),  # 0, 0
            self.get_cell_by_axis(self.x - 1, self.y),  # 0, 1
            # self.get_cell_by_axis(self.x - 1, self.y + 1),  # 0, 2
            self.get_cell_by_axis(self.x, self.y - 1),  # 1, 0
            # self.get_cell_by_axis(self.x + 1, self.y - 1),  # 2, 0
            self.get_cell_by_axis(self.x + 1, self.y),  # 2, 1
            # self.get_cell_by_axis(self.x + 1, self.y + 1),  # 2, 2
            self.get_cell_by_axis(self.x, self.y + 1)  # 1, 2
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def reveal_area(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),  # 0, 0
            self.get_cell_by_axis(self.x - 1, self.y),  # 0, 1
            self.get_cell_by_axis(self.x - 1, self.y + 1),  # 0, 2
            self.get_cell_by_axis(self.x, self.y - 1),  # 1, 0
            self.get_cell_by_axis(self.x + 1, self.y - 1),  # 2, 0
            self.get_cell_by_axis(self.x + 1, self.y),  # 2, 1
            self.get_cell_by_axis(self.x + 1, self.y + 1),  # 2, 2
            self.get_cell_by_axis(self.x, self.y + 1)  # 1, 2
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_monster(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_monster:
                counter += 1
        return counter

    @property
    def surrounded_cells_chest(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_chest:
                counter += 1
        return counter

    @property
    def surrounded_cells_exit(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_exit:
                counter += 1
        return counter

    def show_cell(self):
        self.cell_btn_object.configure(bg="gray")

    def show_monster(self):
        if not self.is_opened:
            Cell.monster_count -= 1
            self.cell_btn_object.configure(bg="red")
            if Cell.monster_count_label:
                Cell.monster_count_label.configure(
                    text=f"Monsters left: {Cell.monster_count}"
                )
        self.is_opened = True

    def show_exit(self):
        self.cell_btn_object.configure(bg="green")

    def show_chest(self):
        if not self.is_opened:
            self.cell_btn_object.configure(bg="yellow")
            Cell.treasure_count -= 1
            if Cell.treasure_count_label:
                Cell.treasure_count_label.configure(
                    text=f"Treasure left: {Cell.treasure_count}"
                )
        self.is_opened = True

    def right_click_actions(self, event):
        print("I am right clicked!")

    @staticmethod
    def randomize_monsters():  # change later
        picked_cells = random.sample(Cell.all, settings.MONSTER_COUNT)
        for cell in picked_cells:
            cell.is_monster = True
            Cell.used.append(cell)
        # print(f"monsters = {picked_cells}")

    @staticmethod
    def randomize_exit():
        picked_cell = random.choice(Cell.all)
        while picked_cell in Cell.used:
            picked_cell = random.choice(Cell.all)
        picked_cell.is_exit = True
        Cell.used.append(picked_cell)
        # print(f"exit = {picked_cell}")

    @staticmethod
    def randomize_chests():  # change later
        chests = []
        for num in range(settings.TREASURE_COUNT):
            picked_cell = random.choice(list(set(Cell.all) - set(Cell.used)))
            Cell.used.append(picked_cell)
            picked_cell.is_chest = True
            chests.append(picked_cell)
            Cell.used.append(picked_cell)
        # print(f"chests = {chests}")

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
