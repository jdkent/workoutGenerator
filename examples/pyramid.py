from wobot.workouts import TimePyramid, NAME_HASHES, Rest
from wobot.displays import ShellDisplay

SEED = NAME_HASHES["Kiani"]

lower_body = ('Quadriceps', 'Hamstrings', 'Glutes', 'Calves', "LowerBack", "Abductors", "Adductors")
upper_body = ("Chest", "MiddleBack", "Lats", "Traps", 'Shoulders', 'Biceps', 'Triceps', "Forearms")
core = ("Abdominals",)
exclude = []

base_pyramid = TimePyramid()

lower_pyramid1 = base_pyramid.init(muscles=lower_body, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in lower_pyramid1])))

upper_pyramid1 = base_pyramid.init(muscles=upper_body, exclude_exercises=exclude, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in upper_pyramid1])))

core_pyramid1 = base_pyramid.init(muscles=core, exclude_exercises=exclude, equipment=(None,), seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in core_pyramid1])))

lower_pyramid2 = base_pyramid.init(muscles=lower_body, exclude_exercises=exclude, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in lower_pyramid2])))

upper_pyramid2 = base_pyramid.init(muscles=upper_body, exclude_exercises=exclude, seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in upper_pyramid2])))

core_pyramid2 = base_pyramid.init(muscles=core, exclude_exercises=exclude, equipment=(None,), seed=SEED)
exclude.extend(list(set([ex.__class__ for ex in core_pyramid2])))


workout = lower_pyramid2 + [Rest(20)] + upper_pyramid2 + [Rest(20)] + core_pyramid2

disp = ShellDisplay()

disp.preview(workout)
cont = input("Does this workout look okay?")
disp.display(workout)