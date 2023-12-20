from wobot.workouts import Tabata, TimedWorkout, EXOX, NAME_HASHES, TotalRandom, Rest
from wobot.displays import ShellDisplay

SEED = NAME_HASHES['Balyssa']
lower_body = ('Quadriceps', 'Hamstrings', 'Glutes', 'Calves', "LowerBack", "Abductors", "Adductors")
upper_body = ("Chest", "MiddleBack", "Lats", "Traps", 'Shoulders')
arms = ('Biceps', 'Triceps', "Forearms")

exclude = []
# start with tabata
tabata = Tabata(on_time=20, off_time=10, round_rest=10, rounds=4, n_exercises=3)
tabata_workout = tabata.init(muscles=arms + upper_body, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in tabata_workout])))

# arms involved
timed_workout = TimedWorkout(on_time=45, off_time=15, round_rest=0, rounds=3, n_exercises=4)
norm_workout = timed_workout.init(muscles=upper_body + arms, exclude_exercises=exclude, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in norm_workout])))

# end with cardio EMOM
emom = EXOX()
emom_workout = emom.init(etypes=('cardio',), equipment=(None,), exclude_exercises=exclude, seed=SEED)

abs_workout = TimedWorkout(on_time=30, off_time=0, round_rest=0, rounds=1, n_exercises=20)
abs_ = abs_workout.init(equipment=(None,), muscles=("Abdominals",), exclude_exercises=exclude, seed=SEED)
workout = tabata_workout + norm_workout + emom_workout + [Rest(15)] + abs_

disp = ShellDisplay()

disp.preview(workout)
cont = input("Does this workout look okay?")
disp.display(workout)

