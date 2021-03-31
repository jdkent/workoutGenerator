from abc import ABCMeta, abstractmethod
import time
from os import system, name

import numpy as np
import simpleaudio as sa
import numpy as np


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class BaseDisplay(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def preview(self, workout):
        """Preview the workout."""
        pass

    @abstractmethod
    def display(self, workout):
        """Display the workoout on a medium."""
        pass


class ShellDisplay(BaseDisplay):
    def __init__(self):
        pass

    def _clear(self):
        # for windows
        if name == "nt":
            _ = system("cls")

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system("clear")

    def _beep(self, freq=880, T=1.0):
        sample_rate = 44100
        t = np.linspace(0, T, int(T * sample_rate), False)

        note = np.sin(freq * t * 2 * np.pi)

        note *= 32767 / np.max(np.abs(note))

        note = note.astype(np.int16)

        play_obj = sa.play_buffer(note, 1, 2, sample_rate)

        play_obj.wait_done()

    def _countdown(self, t):
        first_t = t
        while t:
            try:
                mins, secs = divmod(t, 60)
                timer = "{:02d}:{:02d}".format(mins, secs)
                print(timer, end="\r")
                if first_t == t:
                    self._beep()
                else:
                    time.sleep(1)
                t -= 1
            except KeyboardInterrupt:
                end = input("Paused, type 'quit' to end program")
                if end == "quit":
                    raise KeyboardInterrupt
                else:
                    continue

    def preview(self, workout):
        total_time = 0
        for exercise in workout:
            print(repr(exercise))
            total_time += exercise.on_time
        mins, secs = divmod(total_time, 60)
        print(f"\nTotal Time: {mins}:{secs}")

    def _run_exercise(self, exercise, up_next=None, idx=None, total=None):
        self._clear()
        if exercise.reps:
            name = repr(exercise)
        else:
            name = str(exercise)
        print(
            f"\n\n\n{bcolors.OKGREEN}{bcolors.BOLD}{bcolors.UNDERLINE}Now: {name}{bcolors.ENDC}\n\n\n"
        )

        if up_next:
            up_next_name = repr(up_next)
            print(f"{bcolors.FAIL}Up Next: {up_next_name}{bcolors.ENDC}")

        print(f"{bcolors.OKBLUE}Progress: {idx}/{total}{bcolors.ENDC}")
        self._countdown(exercise.on_time)
        self._clear()

    def display(self, workout):
        # start countdown
        t = 3
        while t:
            mins, secs = divmod(t, 60)
            timer = "{:02d}:{:02d}".format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

        # run workout
        workout_len = len(workout)
        for idx, exercise in enumerate(workout):
            if idx < workout_len - 1:
                up_next = workout[idx + 1]
            else:
                up_next = None
            self._run_exercise(
                exercise, up_next=up_next, idx=idx + 1, total=workout_len
            )

        # finisher
        print("DONE!!!")
        for _ in range(3):
            self._beep(T=0.5)
            time.sleep(0.3)
