from wobot.workouts import TimedWorkout, DropSet, EXOX, Tabata, Rest
from wobot.displays import ShellDisplay

SEED = 10

def variety_hour(muscle_set1, muscle_set2, seed=None):
    tabata = Tabata(on_time=20, off_time=10, round_rest=10)
    timed_workout = TimedWorkout(on_time=45, off_time=15, round_rest=0, rounds=3, n_exercises=4)
    drop_set = DropSet(on_time=30, off_time=0, round_rest=10, n_exercises=4)
    emom = EXOX()

    exclude = []
    tabata_set1 = tabata.init(muscles=muscle_set1, alt=True, seed=seed)
    exclude.extend(list(set([ta.__class__ for ta in tabata_set1])))

    emom_set2 = emom.init(muscles=muscle_set2, exclude_exercises=exclude, seed=seed)
    exclude.extend(list(set([eub.__class__ for eub in emom_set2])))

    timed_workout_set1 = timed_workout.init(muscles=muscle_set1, exclude_exercises=exclude, seed=seed)
    exclude.extend(list(set([twa.__class__ for twa in timed_workout_set1])))

    drop_set_set2 = drop_set.init(muscles=muscle_set2, exclude_exercises=exclude, seed=seed)

    workout = tabata_set1 + emom_set2 + [Rest(15)] + timed_workout_set1 + drop_set_set2

    return workout

arms = ('Biceps', 'Triceps', 'Shoulders', "Forearms")
upper_body = ("Chest", "MiddleBack", "Lats", "Traps")
lower_body = ('Quadriceps', 'Hamstrings', 'Glutes', 'Calves', "LowerBack", "Abductors", "Adductors")
abs_ = ("Abdominals", "LowerBack")

workout = variety_hour(arms + upper_body, abs_, SEED)

disp = ShellDisplay()

disp.preview(workout)
cont = input("Does this workout look okay?")
disp.display(workout)