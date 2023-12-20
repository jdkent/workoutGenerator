import random
import hashlib

import numpy as np

from .exercises import ALL_EXERCISES, ALL_EQUIPMENT, Rest
from .muscles import ALL_MUSCLES



def str_to_int(s):
    return int(hashlib.sha256(s.encode("utf-8")).hexdigest(), 16) % 10 ** 8


names = [
    "James",
    "Balyssa",
    "Samon",
    "Shris Ti",
    "Kiani",
    "Chandra",
    "Chris",
    "Ianto",
    "Marisol",
    "Yujia",
    "Ka Leigh",
    "Hannah",
]

NAME_HASHES = {n: str_to_int(n) for n in names}


class BaseWorkout:
    """Generator for a list of Exercises."""

    def opposite_exists(self, exercise):
        for muscle in exercise.muscles:
            if muscle.opposite:
                return True
        return False

    def filter_exercise(self, exclude_exercises):
        if isinstance(exclude_exercises, str):
            return [
                exercise
                for ex_name, exercise in ALL_EXERCISES.items()
                if not re.match(exclude_exercises, ex_name)
            ]
        elif isinstance(exclude_exercises, list):
            return sorted(
                list(set(ALL_EXERCISES.values()) - set(exclude_exercises)),
                key=lambda x: x.__name__,
            )
        else:
            raise ValueError("exclude_exercises must be regex or list of exercises")

    def filter_type(self, exercises, etypes=("cardio", "strength")):
        return [exercise for exercise in exercises if exercise.etype in etypes]

    def filter_equipment(self, exercises, equipment=ALL_EQUIPMENT):
        return [
            exercise
            for exercise in exercises
            if set(equipment).intersection(exercise.equipment)
        ]

    def filter_muscles(self, exercises, muscles):
        return [
            exercise
            for exercise in exercises
            if set(muscles).intersection(exercise.muscles)
        ]

    def filter(self, muscles, equipment, exclude_exercises, etypes):
        if exclude_exercises:
            all_exercises = self.filter_exercise(exclude_exercises)
        else:
            all_exercises = list(ALL_EXERCISES.values())

        all_exercises = self.filter_equipment(all_exercises, equipment)

        if etypes:
            all_exercises = self.filter_type(all_exercises, etypes)

        if muscles:
            muscles = [ALL_MUSCLES[muscle] for muscle in muscles]
            all_exercises = self.filter_muscles(all_exercises, muscles)

        return all_exercises


class Tabata(BaseWorkout):
    def __init__(self, on_time=25, off_time=5, round_rest=15, rounds=5, n_exercises=4):
        self.on_time = on_time
        self.off_time = off_time
        self.n_exercises = n_exercises
        self.rounds = rounds
        self.round_rest = round_rest

    def init(
        self,
        muscles=None,
        equipment=ALL_EQUIPMENT,
        exclude_exercises=None,
        etypes=None,
        alt=False,
        seed=None,
    ):
        random.seed(seed)
        all_exercises = self.filter(muscles, equipment, exclude_exercises, etypes)
        if alt:
            exercises_with_opposites = [
                exercise for exercise in all_exercises if self.opposite_exists(exercise)
            ]
            half_exercises = random.sample(
                exercises_with_opposites, self.n_exercises // 2
            )
            exercises = []
            for exercise in half_exercises:
                muscles = exercise.muscles
                opposite_muscles = []
                for muscle in muscles:
                    if muscle.opposite:
                        opposite_muscles.extend(muscle.opposite)
                opposite_exercises = [
                    exercise
                    for exercise in all_exercises
                    if set(exercise.muscles).intersection(opposite_muscles)
                ]
                opposite_exercises = list(
                    set(opposite_exercises) - set(half_exercises).union(exercises)
                )
                exercises.extend((exercise, random.choice(opposite_exercises)))
        else:
            exercises = random.sample(all_exercises, self.n_exercises)
        workout = []
        for exercise in exercises:
            for round_ in range(self.rounds):
                workout.append(exercise(self.on_time))
                if self.off_time > 0:
                    workout.append(Rest(self.off_time))
            if self.round_rest > 0:
                workout.append(Rest(self.round_rest))

        self.workout = workout

        return workout


class DropSet(BaseWorkout):
    def __init__(self, on_time=25, off_time=5, round_rest=15, n_exercises=5):
        self.on_time = on_time
        self.off_time = off_time
        self.n_exercises = n_exercises
        self.round_rest = round_rest

    def init(
        self,
        muscles=None,
        equipment=ALL_EQUIPMENT,
        exclude_exercises=None,
        etypes=None,
        seed=None,
    ):
        random.seed(seed)
        all_exercises = self.filter(muscles, equipment, exclude_exercises, etypes)
        exercises = random.sample(all_exercises, self.n_exercises)
        workout = []
        round_exercises = exercises.copy()
        for round_ in range(self.n_exercises):
            for exercise in round_exercises:
                workout.append(exercise(self.on_time))
                if self.off_time > 0:
                    workout.append(Rest(self.off_time))
            round_exercises.pop()
            if self.round_rest > 0:
                workout.append(Rest(self.round_rest))

        self.workout = workout

        return workout


class TimedWorkout(BaseWorkout):
    def __init__(self, on_time=25, off_time=5, round_rest=15, rounds=5, n_exercises=4):
        self.on_time = on_time
        self.off_time = off_time
        self.n_exercises = n_exercises
        self.rounds = rounds
        self.round_rest = round_rest

    def init(
        self,
        muscles=None,
        equipment=ALL_EQUIPMENT,
        exclude_exercises=None,
        etypes=None,
        alt=False,
        seed=None,
    ):
        random.seed(seed)
        all_exercises = self.filter(muscles, equipment, exclude_exercises, etypes)
        if alt:
            exercises_with_opposites = [
                exercise for exercise in all_exercises if self.opposite_exists(exercise)
            ]
            half_exercises = random.sample(
                exercises_with_opposites, self.n_exercises // 2
            )
            exercises = []
            for exercise in half_exercises:
                muscles = exercise.muscles
                opposite_muscles = []
                for muscle in muscles:
                    if muscle.opposite:
                        opposite_muscles.extend(muscle.opposite)
                opposite_exercises = [
                    exercise
                    for exercise in all_exercises
                    if set(exercise.muscles).intersection(opposite_muscles)
                ]
                opposite_exercises = list(
                    set(opposite_exercises) - set(half_exercises).union(exercises)
                )
                exercises.extend((exercise, random.choice(opposite_exercises)))
        else:
            exercises = random.sample(all_exercises, self.n_exercises)
        workout = []
        for round_ in range(self.rounds):
            for exercise in exercises:
                workout.append(exercise(self.on_time))
                if self.off_time > 0:
                    workout.append(Rest(self.off_time))
            if self.round_rest > 0:
                workout.append(Rest(self.round_rest))

        self.workout = workout

        return workout

class TimePyramid(BaseWorkout):
    def __init__(self, bottom=20, top=60, off_time=0, single_top=True, n_exercises=5):
        self.bottom = bottom
        self.top = top
        self.off_time = off_time
        self.single_top = single_top
        self.n_exercises = n_exercises

    def init(
        self,
        muscles=None,
        equipment=ALL_EQUIPMENT,
        exclude_exercises=None,
        etypes=None,
        seed=None,
    ):
        random.seed(seed)
        all_exercises = self.filter(muscles, equipment, exclude_exercises, etypes)
        exercises = random.sample(all_exercises, self.n_exercises)
        ex_times = list(
            np.hstack([
                np.linspace(self.bottom, self.top, self.n_exercises, dtype=int),
                np.linspace(self.top, self.bottom, self.n_exercises, dtype=int)
            ])
        )
        # add exercises to reversed sample
        exs = exercises + exercises[::-1]

        if self.single_top:
            drop_idx = self.n_exercises
            exs.pop(drop_idx)
            ex_times.pop(drop_idx)

        workout = []
        for exercise, ex_time in zip(exs, ex_times):
            workout.append(exercise(ex_time))
            if self.off_time > 0:
                workout.append(Rest(self.off_time))

        return workout


class EXOX(BaseWorkout):
    def __init__(self, interval=60, difficulty=0.75, rounds=4, n_exercises=3):
        self.interval = interval
        self.difficulty = difficulty
        self.rounds = rounds
        self.n_exercises = n_exercises

    def init(
        self,
        muscles=None,
        equipment=ALL_EQUIPMENT,
        exclude_exercises=None,
        etypes=None,
        seed=None,
    ):
        random.seed(seed)
        all_exercises = self.filter(muscles, equipment, exclude_exercises, etypes)
        all_exercises = [ex for ex in all_exercises if ex.rep_time]
        exercises = random.sample(all_exercises, self.n_exercises)
        workout = []
        for exercise in exercises:
            # ensure this is a round number
            reps = (
                round((self.interval * self.difficulty) // exercise.rep_time // 2) * 2
            )
            for round_ in range(self.rounds):
                workout.append(exercise(self.interval, reps))

        self.workout = workout

        return workout


class TotalRandom(BaseWorkout):
    def __init__(
        self, on_range=(20, 60), off_range=(5, 20), on_prob=0.75, n_exercises=20
    ):
        self.on_range = on_range
        self.off_range = off_range
        self.on_prob = on_prob
        self.n_exercises = n_exercises

    def init(
        self,
        muscles=None,
        equipment=ALL_EQUIPMENT,
        exclude_exercises=None,
        etypes=None,
        seed=None,
    ):
        random.seed(seed)
        all_exercises = self.filter(muscles, equipment, exclude_exercises, etypes)
        exercises = random.sample(all_exercises, self.n_exercises)
        workout = []
        while exercises:
            if len(exercises) == self.n_exercises:
                on_time = random.randrange(self.on_range[0], self.on_range[1], 5)
                workout.append(exercises.pop()(on_time))
            elif random.choices(
                [True, False], weights=[self.on_prob, 1 - self.on_prob]
            )[0]:
                on_time = random.randrange(self.on_range[0], self.on_range[1] + 1, 5)
                workout.append(exercises.pop()(on_time))
            else:
                off_time = random.randrange(self.off_range[0], self.off_range[1] + 1, 5)
                if off_time:
                    workout.append(Rest(off_time))

        self.workout = workout

        return workout
