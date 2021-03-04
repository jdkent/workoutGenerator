from wobot.workouts import TotalRandom
from wobot.displays import ShellDisplay

SEED = None
total_random = TotalRandom(n_exercises=35)

random_workout = total_random.init(equipment=(None,), seed=SEED)

disp = ShellDisplay()

disp.preview(random_workout)
cont = input("Does this workout look okay?")
disp.display(random_workout)