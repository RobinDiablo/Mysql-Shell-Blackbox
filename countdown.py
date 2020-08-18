import tkinter as tk

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('200x90')
        self.label = tk.Label(self, text="",font=("Courier", 50), width=300,height=200,bd=10,bg='sky blue')
        self.label.place(height=90,width=200)
        self.remaining = 0
        self.countdown(9)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="Time's up!",font=("Courier", 25),width=300,height=200,bd=10,bg='sky blue')
        else:
            self.label.configure(text="%d" % self.remaining,width=300,height=200,bd=10,bg='sky blue')
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

if __name__ == "__main__":
    app = ExampleApp()
    app.after(12000, lambda: app.destroy())
    app.mainloop()

'''import tkinter as tk
import datetime

class Countdown(tk.Frame):
    #A Frame with label to show the time left, an entry to input the seconds to count
    #down from, and a start button to start counting down.
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 0
        self._timer_on = False

    def show_widgets(self):

        self.label.pack()
        self.entry.pack()
        self.start.pack()

    def create_widgets(self):

        self.label = tk.Label(self, text="00:00:00")
        self.entry = tk.Entry(self, justify='center')
        self.entry.focus_set()
        self.start = tk.Button(self, text="Start", command=self.start_button)

    def countdown(self):
        #Update label based on the time left.
        self.label['text'] = self.convert_seconds_left_to_time()

        if self.seconds_left:
            self.seconds_left -= 1
            self._timer_on = self.after(1000, self.countdown)
        else:
            self._timer_on = False

    def start_button(self):
        #Start counting down.
        self.seconds_left = int(self.entry.get())   # 1. to fetch the seconds
        self.stop_timer()                           # 2. to prevent having multiple
        self.countdown()                            #    timers at once

    def stop_timer(self):
        #Stops after schedule from executing.
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False

    def convert_seconds_left_to_time(self):

        return datetime.timedelta(seconds=self.seconds_left)


if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False, False)

    countdown = Countdown(root)
    countdown.pack()

    root.mainloop()'''