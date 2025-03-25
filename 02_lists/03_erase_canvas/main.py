import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, master):
        self.master = master
        master.title("Eraser App")
        
        # Create a canvas widget
        self.canvas = tk.Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack()
        
        # Draw a grid of blue cells
        self.cells = {}
        self.create_grid()
        
        # Create the eraser rectangle (initially at position 0,0)
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='pink', outline='pink')
        
        # Bind mouse motion to the canvas
        self.canvas.bind("<Motion>", self.mouse_move)
    
    def create_grid(self):
        rows = CANVAS_HEIGHT // CELL_SIZE
        cols = CANVAS_WIDTH // CELL_SIZE
        for row in range(rows):
            for col in range(cols):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='black')
                self.cells[(row, col)] = rect

    def mouse_move(self, event):
        # Update the eraser's position to follow the mouse
        x, y = event.x, event.y
        self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        
        # Erase (set to white) any cell overlapping with the eraser area
        self.erase_cells(x, y)
        
    def erase_cells(self, x, y):
        # Eraser boundaries
        eraser_left, eraser_top = x, y
        eraser_right, eraser_bottom = x + ERASER_SIZE, y + ERASER_SIZE
        
        # Iterate through each cell in the grid
        rows = CANVAS_HEIGHT // CELL_SIZE
        cols = CANVAS_WIDTH // CELL_SIZE
        for row in range(rows):
            for col in range(cols):
                # Get cell coordinates
                cell_x1 = col * CELL_SIZE
                cell_y1 = row * CELL_SIZE
                cell_x2 = cell_x1 + CELL_SIZE
                cell_y2 = cell_y1 + CELL_SIZE
                
                # Check for overlapping rectangles (simple collision detection)
                if not (eraser_right < cell_x1 or eraser_left > cell_x2 or 
                        eraser_bottom < cell_y1 or eraser_top > cell_y2):
                    rect_id = self.cells[(row, col)]
                    self.canvas.itemconfig(rect_id, fill='white')

def main():
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
