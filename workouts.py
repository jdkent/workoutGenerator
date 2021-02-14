import time
import random
import re

from exercises import ALL_EXERCISES, ALL_EQUIPMENT, Rest
from muscles import ALL_MUSCLES


PATTERN = re.compile(r'(?<!^)(?=[A-Z])')

def opposite_exists(exercise):
    for muscle in exercise.muscles:
        if muscle.opposite:
            return True 
    return False

class Tabata:

    def __init__(self, on_time=25, off_time=5, round_rest=15, rounds=5, n_exercises=4):
        self.on_time = on_time
        self.off_time = off_time
        self.n_exercises = n_exercises
        self.rounds = rounds
        self.round_rest = round_rest
    
    def filter_equipment(self, exercises, equipment=ALL_EQUIPMENT):
        return [exercise for exercise in exercises if set(equipment).intersection(exercise.equipment)]
    
    
    def filter_muscles(self, exercises, muscles):
        return [exercise for exercise in exercises if set(muscles).intersection(exercise.muscles)]


    def init_workout(self, muscles=None, equipment=ALL_EQUIPMENT, alt=False):
        all_exercises = self.filter_equipment(ALL_EXERCISES.values(), equipment)

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
                exercises.extend((exercise, random.choice(opposite_exercises)))
        else:
            exercises = random.sample(all_exercises, self.n_exercises)
        workout = []
        for exercise in exercises:
            for round_ in range(self.rounds):
                workout.append(exercise(self.on_time))
                workout.append(Rest(self.off_time))
            workout.append(Rest(self.round_rest))
        
        self.workout = workout

        return workout

    def display_workout(self, workout=None):
        for exercise in workout:
            name = PATTERN.sub(' ', exercise.__class__.__name__)
            print(name)

    def run_workout(self, workout=None):
        for idx, exercise in enumerate(workout):
            if idx < len(workout) - 1:
                up_next = workout[idx + 1]
            else:
                up_next = None
            exercise.run(up_next=up_next)
              
tabata = Tabata(on_time=5, off_time=1, round_rest=5, rounds=2)  

workout = tabata.init_workout(alt=False, equipment=(None,), muscles=("Chest", "Biceps"))
tabata.display_workout(workout)
time.sleep(10)
tabata.run_workout(workout)
print("done!")        
