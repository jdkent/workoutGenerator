from wobot.workouts import TimedWorkout, Tabata, NAME_HASHES, Rest
from wobot.exercises import ALL_EQUIPMENT
from wobot.displays import ShellDisplay

SEED = NAME_HASHES["Chris"]
only_equipment = [eq for eq in ALL_EQUIPMENT if eq is not None]
lower_body = ('Quadriceps', 'Hamstrings', 'Glutes', 'Calves', "LowerBack", "Abductors", "Adductors")
upper_body = ("Chest", "MiddleBack", "Lats", "Traps", 'Shoulders')
arms = ('Biceps', 'Triceps', "Forearms")
core = ("Abdominals", "LowerBack")

long_wout = TimedWorkout(on_time=45, off_time=15, round_rest=0, rounds=3, n_exercises=4)
short_tabata = TimedWorkout(on_time=20, off_time=10, round_rest=0, rounds=4, n_exercises=2)
exclude = []

lower_body_wout = long_wout.init(muscles=lower_body, equipment=only_equipment, alt=True, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in lower_body_wout])))

upper_body_wout = long_wout.init(muscles=upper_body, equipment=only_equipment, exclude_exercises=exclude, alt=True, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in upper_body_wout])))

arm_wout = long_wout.init(muscles=arms, equipment=only_equipment, exclude_exercises=exclude, alt=True, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in arm_wout])))

cardio_wout = short_tabata.init(etypes=('cardio',), equipment=(None,), seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in cardio_wout])))

workout = lower_body_wout + [Rest(15)] + upper_body_wout + [Rest(15)] + arm_wout + [Rest(15)] + cardio_wout

disp = ShellDisplay()

disp.preview(workout)
cont = input("Does this workout look okay?")
disp.display(workout)