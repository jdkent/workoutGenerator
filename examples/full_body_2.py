from wobot.workouts import Tabata, TimedWorkout, EXOX
from wobot.displays import ShellDisplay

ab_burn = TimedWorkout(on_time=30, off_time=0, round_rest=15, rounds=1, n_exercises=6)
tabata = Tabata(on_time=20, off_time=10, round_rest=10, rounds=4, n_exercises=4)
SEED = 86400

lower_body = ('Quadriceps', 'Hamstrings', 'Glutes', 'Calves', "LowerBack", "Abductors", "Adductors")
upper_body = ("Chest", "MiddleBack", "Lats", "Traps", 'Shoulders')
arms = ('Biceps', 'Triceps', "Forearms")

exclude = []
# leg tabata
leg_tabata = tabata.init(muscles=lower_body, etypes=('strength',), alt=True, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in leg_tabata])))
abs1 = ab_burn.init(muscles=("Abdominals",), equipment=(None,), etypes=('strength',), seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in abs1])))

# arm tabata
arm_tabata = tabata.init(muscles=arms, etypes=('strength',), exclude_exercises=exclude, alt=True, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in arm_tabata])))
abs2 = ab_burn.init(muscles=("Abdominals",), equipment=(None,), seed=SEED ** 2)
exclude.extend(list(set([ex.__class__ for ex in abs2])))

# upper body
upper_body = tabata.init(muscles=upper_body, etypes=('strength',), exclude_exercises=exclude, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in upper_body])))
abs3 = ab_burn.init(muscles=("Abdominals",), equipment=(None,), exclude_exercises=exclude, seed=SEED ** 3)
exclude.extend(list(set([ex.__class__ for ex in abs3])))
# cardio tabata
cardio = tabata.init(etypes=('cardio',), exclude_exercises=exclude, seed=SEED)
abs4 = ab_burn.init(muscles=("Abdominals",), equipment=(None,), etypes=('strength',), exclude_exercises=exclude, seed=SEED ** 4)


workout = leg_tabata + abs1 + arm_tabata + abs2 + upper_body + abs3 + cardio + abs4 

disp = ShellDisplay()

disp.preview(workout)
cont = input("Does this workout look okay?")
disp.display(workout)