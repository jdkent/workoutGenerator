from wobot.workouts import Tabata, TimedWorkout, EXOX
from wobot.displays import ShellDisplay

SEED = 5
lower_body = ('Quadriceps', 'Hamstrings', 'Glutes', 'Calves', "LowerBack", "Abductors", "Adductors")
upper_body = ("Chest", "MiddleBack", "Lats", "Traps", 'Shoulders')
arms = ('Biceps', 'Triceps', "Forearms")

exclude = []
# start with tabata
tabata = Tabata(on_time=20, off_time=10, round_rest=10, rounds=4, n_exercises=3)
tabata_workout = tabata.init(muscles=lower_body, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in tabata_workout])))

# arms involved
timed_workout = TimedWorkout(on_time=45, off_time=15, round_rest=15, rounds=3, n_exercises=4)
norm_workout = timed_workout.init(muscles=upper_body + arms, exclude_exercises=exclude, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in norm_workout])))

# end with cardio EMOM
emom = EXOX()
emom_workout = emom.init(etypes=('cardio',), equipment=(None,), exclude_exercises=exclude, seed=SEED)

workout = tabata_workout + norm_workout + emom_workout

disp = ShellDisplay()

disp.preview(workout)
cont = input("Does this workout look okay?")
disp.display(workout)

