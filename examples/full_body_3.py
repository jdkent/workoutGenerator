from wobot.workouts import TimedWorkout, DropSet, NAME_HASHES, EXOX, Rest
from wobot.displays import ShellDisplay

SEED = NAME_HASHES["James"]
drop_set = DropSet(on_time=30, off_time=0, round_rest=10, n_exercises=4)
emom = EXOX(difficulty=0.75, rounds=3)
exclude = []
# legs
lower_body = ('Quadriceps', 'Hamstrings', 'Glutes', 'Calves', "LowerBack", "Abductors", "Adductors")

drop_legs = drop_set.init(muscles=lower_body, etypes=('strength'), equipment=(None,), seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in drop_legs])))

emom_legs = emom.init(exclude_exercises=exclude, muscles=lower_body, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in emom_legs])))

# upper body
upper_body = ('Chest', 'Biceps', 'Triceps', 'MiddleBack', 'Shoulders', 'Lats', "Forearms", "Traps")
drop_upper_body = drop_set.init(muscles=upper_body, exclude_exercises=exclude, etypes=("strength",), seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in drop_upper_body])))
emom_upper_body = emom.init(exclude_exercises=exclude, muscles=upper_body, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in emom_upper_body])))
# abs
drop_abs = drop_set.init(muscles=('Abdominals',), exclude_exercises=exclude, equipment=(None,), seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in drop_abs])))
emom_abs = emom.init(exclude_exercises=exclude, muscles=('Abdominals',), seed=SEED)

workout = drop_legs + emom_legs + [Rest(20)] + drop_upper_body + emom_upper_body + [Rest(20)] + drop_abs + emom_abs


disp = ShellDisplay()

disp.preview(workout)
cont = input("Does this workout look okay?")
disp.display(workout)

