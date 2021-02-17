import time
import random
import re

from exercises import ALL_EXERCISES, ALL_EQUIPMENT, Rest, beep
from muscles import ALL_MUSCLES


PATTERN = re.compile(r'(?<!^)(?=[A-Z])')

def opposite_exists(exercise):
    for muscle in exercise.muscles:
        if muscle.opposite:
            return True 
    return False

class BaseWorkout:

    def filter_type(self, exercises, etypes=('cardio', 'strength')):
        return [exercise for exercise in exercises if exercise.etype in etypes]

    def filter_equipment(self, exercises, equipment=ALL_EQUIPMENT):
        return [exercise for exercise in exercises if set(equipment).intersection(exercise.equipment)]
    
    def filter_muscles(self, exercises, muscles):
        return [exercise for exercise in exercises if set(muscles).intersection(exercise.muscles)]

    def display(self, workout=None):
        total_time = 0
        for exercise in workout:
            name = PATTERN.sub(' ', exercise.__class__.__name__)
            if exercise.reps:
                print(f"{exercise.reps} {name}")
            else:
                print(name)
            total_time += exercise.on_time
        mins, secs = divmod(total_time, 60)
        print(f"\nTotal Time: {mins}:{secs}")

    def run(self, workout=None):
        # start countdown
        t = 3
        while t:
            mins, secs = divmod(t, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") 
            time.sleep(1)
            t -=1

        # run workout
        workout_len = len(workout)
        for idx, exercise in enumerate(workout):
            if idx < workout_len - 1:
                up_next = workout[idx + 1]
            else:
                up_next = None
            exercise.run(up_next=up_next, idx=idx, total=workout_len)

        # finisher
        print("DONE!!!")
        for _ in range(3):
            beep(T=0.5)
            time.sleep(0.3)


class Tabata(BaseWorkout):

    def __init__(self, on_time=25, off_time=5, round_rest=15, rounds=5, n_exercises=4):
        self.on_time = on_time
        self.off_time = off_time
        self.n_exercises = n_exercises
        self.rounds = rounds
        self.round_rest = round_rest


    def init(self, muscles=None, equipment=ALL_EQUIPMENT, exclude_exercises=None, etypes=None, alt=False, seed=None):
        random.seed(seed)
        if exclude_exercises:
            all_exercises = [exercise for ex_name, exercise in ALL_EXERCISES.items() if not re.match(exclude_exercises, ex_name)]
        else:
            all_exercises = list(ALL_EXERCISES.values())
    
        all_exercises = self.filter_equipment(all_exercises, equipment)

        if etypes:
            all_exercises = self.filter_type(all_exercises, etypes)

        if muscles:
            muscles = [ALL_MUSCLES[muscle] for muscle in muscles]
            all_exercises = self.filter_muscles(all_exercises, muscles)

        if alt:
            exercises_with_opposites = [exercise for exercise in all_exercises if opposite_exists(exercise)]
            half_exercises = random.sample(exercises_with_opposites, self.n_exercises // 2)
            exercises = []
            for exercise in half_exercises:
                muscles = exercise.muscles
                opposite_muscles = []
                for muscle in muscles:
                    if muscle.opposite:
                        opposite_muscles.extend(muscle.opposite)
                opposite_exercises = [
                    exercise for exercise in all_exercises if set(exercise.muscles).intersection(opposite_muscles)
                ]
                opposite_exercises = list(set(opposite_exercises) - set(half_exercises).union(exercises))
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


class TimedWorkout(BaseWorkout):

    def __init__(self, on_time=25, off_time=5, round_rest=15, rounds=5, n_exercises=4):
        self.on_time = on_time
        self.off_time = off_time
        self.n_exercises = n_exercises
        self.rounds = rounds
        self.round_rest = round_rest


    def init(self, muscles=None, equipment=ALL_EQUIPMENT, exclude_exercises=None, etypes=None, alt=False, seed=None):
        random.seed(seed)
        if exclude_exercises:
            all_exercises = [exercise for ex_name, exercise in ALL_EXERCISES.items() if not re.match(exclude_exercises, ex_name)]
        else:
            all_exercises = list(ALL_EXERCISES.values())
    
        all_exercises = self.filter_equipment(all_exercises, equipment)

        if etypes:
            all_exercises = self.filter_type(all_exercises, etypes)

        if muscles:
            muscles = [ALL_MUSCLES[muscle] for muscle in muscles]
            all_exercises = self.filter_muscles(all_exercises, muscles)

        if alt:
            exercises_with_opposites = [exercise for exercise in all_exercises if opposite_exists(exercise)]
            half_exercises = random.sample(exercises_with_opposites, self.n_exercises // 2)
            exercises = []
            for exercise in half_exercises:
                muscles = exercise.muscles
                opposite_muscles = []
                for muscle in muscles:
                    if muscle.opposite:
                        opposite_muscles.extend(muscle.opposite)
                opposite_exercises = [
                    exercise for exercise in all_exercises if set(exercise.muscles).intersection(opposite_muscles)
                ]
                opposite_exercises = list(set(opposite_exercises) - set(half_exercises).union(exercises))
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

class EXOX(BaseWorkout):

    def __init__(self, interval=60, difficulty=0.75, rounds=4, n_exercises=3):
        self.interval = interval
        self.difficulty = difficulty
        self.rounds = rounds
        self.n_exercises = n_exercises
    
    def init(self, muscles=None, equipment=ALL_EQUIPMENT, exclude_exercises=None, etypes=None, seed=None):
        random.seed(seed)
        if exclude_exercises:
            all_exercises = [exercise for ex_name, exercise in ALL_EXERCISES.items() if not re.match(exclude_exercises, ex_name)]
        else:
            all_exercises = list(ALL_EXERCISES.values())
    
        all_exercises = self.filter_equipment(all_exercises, equipment)

        all_exercises = [exercise for exercise in all_exercises if exercise.rep_time]
        if etypes:
            all_exercises = self.filter_type(all_exercises, etypes)

        if muscles:
            muscles = [ALL_MUSCLES[muscle] for muscle in muscles]
            all_exercises = self.filter_muscles(all_exercises, muscles)

        exercises = random.sample(all_exercises, self.n_exercises)
        workout = []
        for exercise in exercises:
            # ensure this is a round number
            reps = round((self.interval * self.difficulty) // exercise.rep_time // 2) * 2
            for round_ in range(self.rounds):
                workout.append(exercise(self.interval, reps))
        
        self.workout = workout

        return workout

    
if __name__ == "__main__":             
    tabata = Tabata(on_time=5, off_time=1, round_rest=5, rounds=2)  

    workout = tabata.init_workout(alt=False, equipment=(None,), etypes=('cardio',), muscles=("Chest", "Biceps"))
    tabata.display_workout(workout)
    time.sleep(10)
    tabata.run_workout(workout)
    print("done!")        
