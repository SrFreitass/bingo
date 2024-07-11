
# from tkinter import *
# from tkinter import ttk
# root = Tk()
# root.title("Bingo")

# mainframe = ttk.Frame(root, padding="3 3 12 12")

# root.mainloop()
from generate_cols import Generate_cols
from generate_nums import Generate_num
from tkinter_interface import Window

def main():
    min_n = 1
    max_n = 75
    letters = {
        "B": [1, 15],
        "I": [16, 30],
        "N": [31, 45],
        "G": [46, 60],
        "O": [61, 75],
    }
    drawn=[]
    matrix=[]
    for x in range(5):
        matrix.append([])
    gen_nums = Generate_num(drawn=drawn, min_n=min_n, max_n=max_n)
    gen_cols = Generate_cols(letters=letters, matrix=matrix)

    for letter in letters:
        gen_cols.execute(letter=letter)

    window = Window(matrix, gen_nums.execute, name="Bingo do Nanael", res="650x500")
    window.execute()
    
    # gen_nums.execute(min_n=min_n, max_n=max_n, drawn=drawn)

if __name__ == "__main__":
    main()