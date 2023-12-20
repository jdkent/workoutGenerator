from wobot.workouts import TimedWorkout
from wobot.exercises import Rest, ALL_EXERCISES
from wobot.displays import ShellDisplay

SEED = 7

two_exercise_tabata = TimedWorkout(
    on_time=20, off_time=10, round_rest=0, rounds=4, n_exercises=2
)

challenge = TimedWorkout(
    on_time=30, off_time=0, round_rest=20, rounds=1, n_exercises=14,
)

lower_body = ('Quadriceps', 'Hamstrings', 'Glutes', 'Calves', "LowerBack", "Abductors", "Adductors")
upper_body = ("Chest", "MiddleBack", "Lats", "Traps", 'Shoulders')
arms = ('Biceps', 'Triceps', "Forearms")
abs_ = ("Abdominals", "LowerBack")

pushup_exercises = [ex for name, ex in ALL_EXERCISES.items() if 'PushUp' in name]

exclude = []
lower_body_tabata = two_exercise_tabata.init(muscles=lower_body, alt=True, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in lower_body_tabata])))

upper_body_tabata = two_exercise_tabata.init(
    muscles=upper_body, exclude_exercises=exclude, alt=True, seed=SEED,
)
exclude.extend(list(set([ex.__class__ for ex in upper_body_tabata])))

abs_tabata = two_exercise_tabata.init(
    muscles=abs_, exclude_exercises=exclude, alt=True, seed=SEED,
)
exclude.extend(list(set([ex.__class__ for ex in abs_tabata])))

arm_tabata = two_exercise_tabata.init(
    muscles=arms, exclude_exercises=exclude + pushup_exercises, alt=True, seed=SEED,
)
exclude.extend(list(set([ex.__class__ for ex in arm_tabata])))

ab_challenge = challenge.init(
    muscles=("Abdominals",), exclude_exercises=exclude, equipment=(None,), seed=SEED,
)
exclude.extend(list(set([ex.__class__ for ex in ab_challenge])))

lower_body_tabata2 = two_exercise_tabata.init(
    muscles=lower_body, alt=True, exclude_exercises=exclude, seed=SEED
)
exclude.extend(list(set([ex.__class__ for ex in lower_body_tabata2])))

upper_body_tabata2 = two_exercise_tabata.init(
    muscles=upper_body, exclude_exercises=exclude, alt=True, seed=SEED,
)
exclude.extend(list(set([ex.__class__ for ex in upper_body_tabata2])))

abs_tabata2 = two_exercise_tabata.init(
    muscles=abs_, exclude_exercises=exclude, alt=True, seed=SEED,
)
exclude.extend(list(set([ex.__class__ for ex in abs_tabata2])))

arm_tabata2 = two_exercise_tabata.init(
    muscles=arms, exclude_exercises=exclude + pushup_exercises, alt=True, seed=SEED,
)
exclude.extend(list(set([ex.__class__ for ex in arm_tabata2])))


rest = [Rest(10)]
workout = lower_body_tabata + rest + upper_body_tabata + rest + abs_tabata + rest + arm_tabata + rest + ab_challenge + lower_body_tabata2 + rest + upper_body_tabata2 + rest + abs_tabata2 + rest + arm_tabata2

disp = ShellDisplay()

disp.preview(workout)
cont = input("Does this workout look okay?")
disp.display(workout)