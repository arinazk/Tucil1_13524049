import time
import threading
import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image

from file_processing import *
from queens_linkedin import *

CURRENT_BOARD = None
LAST_SOLUTION = []

IS_RUNNING = False
SEARCHING_STATUS = None
SEARCHING_TIME = None
CASES_CHECKED = None

DISPLAY_AREA = None
SOLVE_BUTTON = None

SAVE_BUTTON = None
RESET_BUTTON = None
OPT_SWITCH = None


def updateBoardDisplay(solution=[], is_preview=True):
    global CURRENT_BOARD, DISPLAY_AREA, LAST_SOLUTION
    
    if CURRENT_BOARD is not None:
        pil_img = matrixToImage(CURRENT_BOARD, solution, None, color_map)
        LAST_SOLUTION = solution
        

        for child in DISPLAY_AREA.winfo_children():
            child.destroy()

        ctk_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(280, 280))
        
        board_label = ctk.CTkLabel(DISPLAY_AREA, image=ctk_img, text="")
        board_label.place(relx=0.5, rely=0.5, anchor="center")


def importFile():
    global CURRENT_BOARD, SOLVE_BUTTON, SAVE_BUTTON, LAST_SOLUTION, SEARCHING_STATUS, RESET_BUTTON
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
    
    if file_path:
        board = readFile(file_path)
        if isValid(board):
            CURRENT_BOARD = board
            updateBoardDisplay()

            SEARCHING_STATUS.configure(text="Press Solve button to find solution", text_color="white")
            SEARCHING_TIME.configure(text="0")
            CASES_CHECKED.configure(text="0")

            SOLVE_BUTTON.configure(state="normal", fg_color="#7b68ee")
            SAVE_BUTTON.configure(state="normal", text_color="#7b68ee", border_color="#7b68ee")
            RESET_BUTTON.configure(state="normal", text_color="white", border_color="grey")
        else:
            messagebox.showerror("Error", "Board is invalid!")

def solveHandler():
    threading.Thread(target=solveGame, daemon=True).start()

def solveGame():
    global CURRENT_BOARD, SEARCHING_TIME, CASES_CHECKED, SEARCHING_STATUS, SAVE_BUTTON

    if CURRENT_BOARD is None:
        return

    SEARCHING_STATUS.configure(text="Searching for solution...", text_color="#7b68ee")
    
    n = len(CURRENT_BOARD)
    start_time = time.time()

    import queens_linkedin
    queens_linkedin.i = 0 

    queens_linkedin.visual_callback = lambda progress: app.after(0, updateBoardDisplay, progress, False)
    
    stop_monitoring = False

    def monitor():
        while not stop_monitoring:
            elapsed = time.time() - start_time
            current_nodes = queens_linkedin.i 

            SEARCHING_TIME.configure(text=f"{elapsed:.4f} s")
            CASES_CHECKED.configure(text=f"{current_nodes:,}")


    threading.Thread(target=monitor, daemon=True).start()

    is_optimized = OPT_SWITCH.get()
    solution = findFirstSolution(n, CURRENT_BOARD, is_optimized)

    stop_monitoring = True

    final_nodes = queens_linkedin.i
    final_time = time.time() - start_time
    
    SEARCHING_TIME.configure(text=f"{final_time:.4f} s")
    CASES_CHECKED.configure(text=f"{final_nodes:,}") 
    
    queens_linkedin.visual_callback = None

    SAVE_BUTTON.configure(
        state="normal", 
        text_color="#7b68ee", 
        border_color="#7b68ee"
    )
    if solution:
        SEARCHING_STATUS.configure(text="Solution found!", text_color="#2ecc71")
        app.after(0, updateBoardDisplay, solution, False)
    else:
        SEARCHING_STATUS.configure(text="Solution not found.", text_color="#e74c3c")
        app.after(0, updateBoardDisplay, [], True)

def saveResultHandler():
    global CURRENT_BOARD, LAST_SOLUTION
    if CURRENT_BOARD is None: return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        title="Save Solution As"
    )
    
    if file_path:
        matrixToImage(CURRENT_BOARD, LAST_SOLUTION, file_path, color_map)
        messagebox.showinfo("Success", "Image saved successfully!")

def resetHandler(OPT_SWITCH):
    global CURRENT_BOARD, IS_RUNNING, stop_monitoring, SAVE_BUTTON, RESET_BUTTON

    IS_RUNNING = False 
    stop_monitoring = True 
    
    import queens_linkedin
    queens_linkedin.visual_callback = None 
    
    CURRENT_BOARD = None
    SOLVE_BUTTON.configure(state="disabled", fg_color="gray")
    SAVE_BUTTON.configure(state="disabled", text_color="gray", border_color="gray")
    RESET_BUTTON.configure(state="disabled", text_color="gray", border_color="gray")
    if OPT_SWITCH:
        OPT_SWITCH.deselect()
    
    SEARCHING_TIME.configure(text="0")
    CASES_CHECKED.configure(text="0")
    SOLVE_BUTTON.configure(state="disabled", fg_color="gray")

    for child in DISPLAY_AREA.winfo_children():
        child.destroy()
    placeholder = ctk.CTkLabel(DISPLAY_AREA, text="No board loaded yet", text_color="gray", font=("Poppins", 12))
    placeholder.place(relx=0.5, rely=0.5, anchor="center")


    for f in ["input_board.png", "realtime_progress.png"]:
        if os.path.exists(f):
            try: os.remove(f)
            except: pass
    
    if SEARCHING_STATUS:
        SEARCHING_STATUS.configure(text="Upload a file to start searching", text_color="gray")

def header(main_frame): 
    title_label = ctk.CTkLabel(main_frame, text="Queens LinkedIn", font=ctk.CTkFont("Poppins", size=40, weight="bold"))
    title_label.pack(padx=10, pady=(40, 5))
    subtitle_label = ctk.CTkLabel(main_frame, text="Arina Azka - 13524049", font=ctk.CTkFont("Poppins", size=16))
    subtitle_label.pack(padx=0, pady=(0, 20))

def contentSection(main_frame):
    content_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    content_frame.pack(pady=10, padx=20) 

    controlSection(content_frame)
    outputSection(content_frame)

def controlSection(content_frame):
    global SOLVE_BUTTON, OPT_SWITCH, SAVE_BUTTON, RESET_BUTTON
    control_frame = ctk.CTkFrame(content_frame, corner_radius=8, width=280, height=480)
    control_frame.pack(side="right", padx=10, pady=10)
    control_frame.pack_propagate(False)

    upload_label = ctk.CTkLabel(control_frame, text="Upload Board", font=ctk.CTkFont("Poppins", 14, weight="bold"))
    upload_label.pack(pady=(20, 5), padx=20, anchor="w") 
    
    upload_button = ctk.CTkButton(control_frame, text="Import File", 
                                 fg_color="#7b68ee", hover_color="#6a5acd",
                                 font=("Poppins", 14, "bold"), height=32, command=importFile)
    upload_button.pack(padx=20, pady=5, fill="x")
    
    upload_note = ctk.CTkLabel(control_frame, text="* Only accepts .txt files", text_color="gray", font=ctk.CTkFont("Poppins", size=12))
    upload_note.pack(padx=20, pady=(0, 10), anchor="w")

    opt_frame = ctk.CTkFrame(control_frame, fg_color="transparent")
    opt_frame.pack(fill="x", padx=20, pady=(20, 10))
    opt_label = ctk.CTkLabel(
        opt_frame, 
        text="Optimization Settings", 
        font=("Poppins", 14, "bold")
    )
    opt_label.pack(anchor="w")
    OPT_SWITCH = ctk.CTkSwitch(
        opt_frame, 
        text="Enable Optimization", 
        font=("Poppins", 12), 
        progress_color="#7b68ee"
    )
    OPT_SWITCH.pack(pady=(10, 0), anchor="w")
    opt_desc = ctk.CTkLabel(
        opt_frame, 
        text="Brute Force with Pruning", 
        font=("Poppins", 11), 
        text_color="gray"
    )
    opt_desc.pack(anchor="w")

    buttons_frame = ctk.CTkFrame(control_frame, fg_color="transparent")

    SOLVE_BUTTON = ctk.CTkButton(buttons_frame, text="▷ Solve", state="disabled", 
                    fg_color="gray", hover_color="#6a5acd",
                    height=32, font=("Poppins", 14, "bold"), command=solveHandler)
    SOLVE_BUTTON.pack(padx=20, pady=(20, 5), fill="x")

    SAVE_BUTTON = ctk.CTkButton(
        buttons_frame, text="⤓ Save Board as Image", state="disabled", 
        fg_color="transparent", border_width=1, border_color="gray", 
        text_color="white",
        height=32, font=("Poppins", 14), command=saveResultHandler
    )
    SAVE_BUTTON.pack(padx=20, pady=5, fill="x")
    SAVE_BUTTON.bind("<Enter>", lambda e: SAVE_BUTTON.configure(text_color="white", fg_color="#5e4db2") if SAVE_BUTTON.cget("state") == "normal" else None)
    SAVE_BUTTON.bind("<Leave>", lambda e: SAVE_BUTTON.configure(text_color="#7b68ee", fg_color="transparent") if SAVE_BUTTON.cget("state") == "normal" else None)

    RESET_BUTTON = ctk.CTkButton(buttons_frame, text="↺ Reset", state="disabled",
                    fg_color="transparent", hover_color="#7b68ef", border_width=1, border_color = "grey",
                    height=32, font=("Poppins", 14), text_color="gray", command=lambda: resetHandler(OPT_SWITCH))
    RESET_BUTTON.pack(padx=20, pady=5, fill="x")
    
    buttons_frame.pack(side="bottom", fill="x", pady=(0,20))

def outputSection(content_frame):
    output_frame = ctk.CTkFrame(content_frame, fg_color="transparent", width=490, height=480)
    output_frame.pack(side="left", padx=10, pady=10)
    output_frame.pack_propagate(False)
    statsSection(output_frame)
    visualSection(output_frame)

def visualSection(output_frame):
    global DISPLAY_AREA, SEARCHING_STATUS
    visual_frame = ctk.CTkFrame(output_frame, corner_radius=12)
    visual_frame.pack(side="top", fill="both", expand=True, pady=(0, 10))

    ctk.CTkLabel(visual_frame, text="Visualization", font=("Poppins", 15, "bold")).pack(pady=10, padx=25, anchor="w")

    DISPLAY_AREA = ctk.CTkFrame(visual_frame, fg_color="#1E1E1E", corner_radius=10, width=300, height=300)
    DISPLAY_AREA.pack(padx=25, pady=(5, 5))
    DISPLAY_AREA.pack_propagate(False)

    placeholder = ctk.CTkLabel(DISPLAY_AREA, text="No board loaded yet", text_color="gray", font=("Poppins", 12))
    placeholder.place(relx=0.5, rely=0.5, anchor="center")

    SEARCHING_STATUS = ctk.CTkLabel(visual_frame, text="Upload a file to start searching", font=("Poppins", 12), text_color="gray", anchor="w")
    SEARCHING_STATUS.pack()

def statsSection(output_frame):
    global SEARCHING_TIME, CASES_CHECKED

    stats_frame = ctk.CTkFrame(output_frame, corner_radius=12, height=90)
    stats_frame.pack(side="bottom", fill="x")
    stats_frame.pack_propagate(False)

    stats_frame.columnconfigure((0, 1), weight=1)

    t_box = ctk.CTkFrame(stats_frame, fg_color="transparent")
    t_box.grid(row=0, column=0, pady=10)
    ctk.CTkLabel(t_box, text="Execution Time", font=("Poppins", 10, "bold"), text_color="#7b68ee").pack()
    SEARCHING_TIME = ctk.CTkLabel(t_box, text="0", font=("Poppins", 20, "bold"))
    SEARCHING_TIME.pack()

    n_box = ctk.CTkFrame(stats_frame, fg_color="transparent")
    n_box.grid(row=0, column=1, pady=10)
    ctk.CTkLabel(n_box, text="Total Cases Checked", font=("Poppins", 10, "bold"), text_color="#7b68ee").pack()
    CASES_CHECKED = ctk.CTkLabel(n_box, text="0", font=("Poppins", 20, "bold"))
    CASES_CHECKED.pack()

def mainApp():
    main_frame = ctk.CTkFrame(app, fg_color="transparent")

    main_frame.pack(expand=True, fill="both")
    
    center_container = ctk.CTkFrame(main_frame, fg_color="transparent")
    center_container.place(relx=0.5, rely=0.5, anchor="center") 
    
    header(center_container)
    contentSection(center_container)

# PROGRAM UTAMA
app = ctk.CTk()
ctk.set_appearance_mode("dark")
app.geometry("880x800") 
app.title("Queens LinkedIn")

mainApp()

app.mainloop()

