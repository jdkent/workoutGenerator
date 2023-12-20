from wobot.workouts import TimedWorkout, DropSet, NAME_HASHES, EXOX, Tabata, Rest
from wobot.displays import ShellDisplay

SEED = NAME_HASHES['Balyssa']


def variety_hour(muscle_set1, muscle_set2, seed=None):
    timed_workout = TimedWorkout(on_time=30, off_time=10, round_rest=0, rounds=3, n_exercises=2)
    drop_set = DropSet(on_time=30, off_time=0, round_rest=10, n_exercises=4)
    emom = EXOX(rounds=3)

    exclude = []

    timed_set1 = timed_workout.init(muscles=muscle_set2, alt=True, seed=seed)
    exclude.extend(list(set([eub.__class__ for eub in timed_set1])))
    dset1 = drop_set.init(muscles=muscle_set1, exclude_exercises=exclude, equipment=(None,), seed=seed)
    exclude.extend(list(set([ta.__class__ for ta in dset1])))

    timed_set2 = timed_workout.init(muscles=muscle_set2, alt=True, exclude_exercises=exclude, seed=seed)
    exclude.extend(list(set([eub.__class__ for eub in timed_set2])))
    dset2 = drop_set.init(muscles=muscle_set2, exclude_exercises=exclude, equipment=(None,), seed=seed)
    exclude.extend(list(set([ta.__class__ for ta in dset2])))

    timed_set3 = timed_workout.init(muscles=muscle_set1, alt=True, exclude_exercises=exclude, seed=seed)
    exclude.extend(list(set([ta.__class__ for ta in timed_set3])))
    dset3 = drop_set.init(muscles=muscle_set1, exclude_exercises=exclude, equipment=(None,), seed=seed)
    exclude.extend(list(set([ta.__class__ for ta in dset3])))


    emom_set = emom.init(muscles=muscle_set1 + muscle_set2, exclude_exercises=exclude, seed=seed)

    workout = timed_set1 + dset1 + timed_set2 + dset2 + timed_set3 + dset3 + [Rest(15)] + emom_set

    return workout

arms = ('Biceps', 'Triceps', 'Shoulders', "Forearms")
upper_body = ("Chest", "MiddleBack", "Lats", "Traps")
lower_body = ('Quadriceps', 'Hamstrings', 'Glutes', 'Calves', "LowerBack", "Abductors", "Adductors")
abs_ = ("Abdominals", "LowerBack")

workout = variety_hour(abs_, arms, SEED)

disp = ShellDisplay()

disp.preview(workout)
cont = input("Does this workout look okay?")
disp.display(workout)