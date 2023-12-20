from dataclasses import dataclass
import ast
import sys
import inspect
import re
import os

import pandas as pd

import wobot.muscles as ms

# file that contains all the exercise data
DATA_FILE = os.path.join(os.path.dirname(__file__), "exercise_data.tsv")


@dataclass
class BaseExercise:
    on_time: int = 0
    reps: int = 0
    # video: str = None
    # description: str = None

    PATTERN = re.compile(r"(?<!^)(?=[A-Z])")

    def __str__(self):
        return self.PATTERN.sub(" ", self.__class__.__name__)

    def __repr__(self):
        if self.reps:
            quantity = self.reps
            unit = "reps"
        else:
            quantity = self.on_time
            unit = "seconds"
        return f"{quantity} {unit} of {self.PATTERN.sub(' ', self.__class__.__name__)}"


def generate_exercises(exercises_file):
    converters = {
        "muscles": ast.literal_eval,
        "equipment": ast.literal_eval,
    }
    ex_df = pd.read_csv(exercises_file, sep="\t", converters=converters)
    exercises = {}
    for _, row in ex_df.iterrows():
        muscles = tuple(
            [getattr(sys.modules["wobot.muscles"], ms) for ms in row.muscles]
        )
        exercises[row["name"]] = type(
            row["name"],
            (BaseExercise,),
            {
                "muscles": muscles,
                "etype": row.etype,
                "equipment": tuple(row.equipment),
                "rep_time": None if pd.isna(row["rep_time"]) else row.rep_time,
                "video": None if pd.isna(row["video"]) else row.video,
                "description": None if pd.isna(row["description"]) else row.description,
            },
        )

    return exercises


ALL_EXERCISES = generate_exercises(DATA_FILE)


class Rest(BaseExercise):
    muscles = None
    etype = None
    equipment = (None,)
    rep_time = None


ALL_EQUIPMENT = ("kettlebell", "dumbbell", "band", None)

# ALL_EXERCISES = {
#    name: obj for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass) if obj.__module__ is __name__
#    }
# del ALL_EXERCISES['BaseExercise']
# del ALL_EXERCISES['Rest']
