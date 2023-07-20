from tkinter import *
from PIL import Image, ImageTk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
paused = False
started = False
work_sec = WORK_MIN * 60
short_break_sec = SHORT_BREAK_MIN * 60
long_break_sec = LONG_BREAK_MIN * 60
count = 0


# ---------------------------- TIMER PAUSE ------------------------------- #
def pause_timer():
    global paused, started, timer, reps
    if paused:
        return
    started = False
    if timer is not None:
        window.after_cancel(timer)
    title_label.config(text="Paused", fg=PINK)
    paused = True
    reps -= 1


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global started, timer, reps, paused
    started = False
    paused = False
    if timer is not None:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global paused, started
    if started:
        return
    global reps, count, paused
    reps += 1

    if reps % 8 == 0:
        if not paused:
            count = long_break_sec
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        if not paused:
            count = short_break_sec
        title_label.config(text="Break", fg=PINK)
    else:
        if not paused:
            count = work_sec
        title_label.config(text="Work", fg=GREEN)

    paused = False
    started = True
    count_down()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down():
    global count, started

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        count -= 1
        timer = window.after(1000, count_down)
    else:
        started = False
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)

# resize the tomato.png for buttons
img = Image.open("tomato.png")
resized_img = img.resize((40, 40))
resized_tomato_img = ImageTk.PhotoImage(resized_img)

# start button
start_button = Button(borderwidth=0, highlightthickness=0, bg=YELLOW, command=start_timer,
                      text="Start", fg="white", font=(FONT_NAME, 9, "bold"),
                      image=resized_tomato_img, compound="center",)
start_button.grid(column=0, row=2)

# reset button
reset_button = Button(borderwidth=0, highlightthickness=0, bg=YELLOW, command=reset_timer,
                      text="Reset", fg="white", font=(FONT_NAME, 9, "bold"),
                      image=resized_tomato_img, compound="center")
reset_button.grid(column=2, row=2)

# pause button
pause_button = Button(borderwidth=0, highlightthickness=0, bg=YELLOW, command=pause_timer,
                      text="Pause", fg="white", font=(FONT_NAME, 9, "bold"),
                      image=resized_tomato_img, compound="center")
pause_button.grid(column=1, row=2)

# check marks
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
