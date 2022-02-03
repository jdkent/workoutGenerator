import ast
import re

from flask import Flask, request, make_response
from .workouts import (
    TimedWorkout, Tabata, EXOX, TotalRandom, 
    DropSet, TimePyramid, NAME_HASHES, Rest
)
from .exercises import ALL_EQUIPMENT

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'


    app.register_blueprint(bp)
    app.add_url_rule('/', endpoint='index')

    return app


from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


bp = Blueprint('workout', __name__)


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/create')
def create_workout():
    return render_template('generate.html')


@bp.route('/run-workout', methods=['POST', "GET"], defaults={'seed': None})
@bp.route('/run-workout/<int:seed>', methods=["GET"])
def run_workout(seed):
    if request.method == 'POST':
        res = make_response()
        WOUT_CODE = request.form['data']
        res.set_cookie("WOUT_CODE", value=WOUT_CODE)
        return (res, 204)
    elif request.method == 'GET':
        WOUT_CODE = request.cookies.get('WOUT_CODE')
        if WOUT_CODE:
            if seed and "seed" in WOUT_CODE:
                old_seed = re.search(r"seed=([0-9]+)", WOUT_CODE).groups()[0]
                WOUT_CODE = WOUT_CODE.replace(f".init(seed={old_seed}, ", f".init(seed={seed}, ")
            elif seed:
                WOUT_CODE = WOUT_CODE.replace(".init(", f".init(seed={seed}, ")

            block = ast.parse(WOUT_CODE, mode='exec')
        
            # assumes last node is an expression
            last = ast.Expression(block.body.pop().value)
            _locals = {}
            exec(compile(block, '<string>', mode='exec'), globals(), _locals)
            wout = eval(compile(last, '<string>', mode='eval'), globals(), _locals)
            total_time = [sum([ex.on_time for ex in wout])]
            return render_template('workout.html', exercises=wout, total_time=total_time, repr=repr, str=str)
    else:
        print("WATTT")

@bp.route('/weighty-wednesday', defaults={'seed': None})
@bp.route('/weighty-wednesday/<int:seed>')
def weighty(seed):
    wout = weighty_wednesday(seed)
    total_time = [sum([ex.on_time for ex in wout])]
    return render_template('workout.html', exercises=wout, total_time=total_time, repr=repr, str=str)


@bp.route('/thirty-thursday', defaults={'seed': None})
@bp.route('/thursday-thirty', defaults={'seed': None})
@bp.route('/thirty-thursday/<int:seed>')
@bp.route('/thursday-thirty/<int:seed>')
def thirty(seed):
    wout = thirty_thursday(seed)
    total_time = [sum([ex.on_time for ex in wout])]
    return render_template('workout.html', exercises=wout, total_time=total_time, repr=repr, str=str)


@bp.route('/only-abs', defaults={'seed': None})
@bp.route('/only-abs/<int:seed>')
def abs_(seed):
    wout = only_abs(seed)
    total_time = [sum([ex.on_time for ex in wout])]
    return render_template('workout.html', exercises=wout, total_time=total_time, repr=repr, str=str)


@bp.route('/pyramid', defaults={'seed': None})
@bp.route('/pyramid/<int:seed>')
def pyramid(seed):
    wout = pyramid_workout(seed)
    total_time = [sum([ex.on_time for ex in wout])]
    return render_template('workout.html', exercises=wout, total_time=total_time, repr=repr, str=str)


@bp.route('/variety-hour', defaults={'seed': None})
@bp.route('/variety-hour/<int:seed>')
def variety(seed):
    wout = variety_hour(seed)
    total_time = [sum([ex.on_time for ex in wout])]
    return render_template('workout.html', exercises=wout, total_time=total_time, repr=repr, str=str)


@bp.route('/emomonday', defaults={'seed': None})
@bp.route('/emomonday/<int:seed>')
def emoms(seed):
    wout = emomonday(seed)
    total_time = [sum([ex.on_time for ex in wout])]
    return render_template('workout.html', exercises=wout, total_time=total_time, repr=repr, str=str)


@bp.route('/tabata', defaults={'seed': None})
@bp.route('/tabata/<int:seed>')
def tabatas(seed):
    wout = all_tabata(seed)
    total_time = [sum([ex.on_time for ex in wout])]
    return render_template('workout.html', exercises=wout, total_time=total_time, repr=repr, str=str)


@bp.route('/for-samon', defaults={'seed': None})
@bp.route('/for-samon/<int:seed>')
def for_samon(seed):
    wout = samon_preferred(seed)
    total_time = [sum([ex.on_time for ex in wout])]
    return render_template('workout.html', exercises=wout, total_time=total_time, repr=repr, str=str)


def weighty_wednesday(seed=None):
    SEED = seed
    only_equipment = [eq for eq in ALL_EQUIPMENT if eq is not None]
    lower_body = ('Quadriceps', 'Hamstrings', 'Glutes', 'Calves', "LowerBack", "Abductors", "Adductors")
    upper_body = ("Chest", "MiddleBack", "Lats", "Traps")
    arms = ('Biceps', 'Triceps', "Forearms", 'Shoulders')
    core = ("Abdominals", "LowerBack")

    long_wout = TimedWorkout(on_time=45, off_time=15, round_rest=0, rounds=3, n_exercises=4)
    short_tabata = TimedWorkout(on_time=20, off_time=10, round_rest=0, rounds=4, n_exercises=2)
    exclude = []

    lower_body_wout = long_wout.init(muscles=lower_body, equipment=only_equipment, alt=True, seed=SEED)
    exclude.extend(list(set([ex.__class__ for ex in lower_body_wout])))

    upper_body_wout = long_wout.init(muscles=upper_body, equipment=only_equipment, exclude_exercises=exclude, alt=True, seed=SEED)
    exclude.extend(list(set([ex.__class__ for ex in upper_body_wout])))

    arm_wout = long_wout.init(muscles=arms, equipment=only_equipment, exclude_exercises=exclude, seed=SEED)
    exclude.extend(list(set([ex.__class__ for ex in arm_wout])))

    cardio_wout = short_tabata.init(etypes=('cardio',), equipment=(None,), seed=SEED)
    exclude.extend(list(set([ex.__class__ for ex in cardio_wout])))

    return lower_body_wout + [Rest(15)] + upper_body_wout + [Rest(15)] + arm_wout + [Rest(15)] + cardio_wout


def thirty_thursday(seed=None):
    SEED = seed

    total_random = TotalRandom(n_exercises=35)

    random_workout = total_random.init(equipment=(None,), seed=SEED)

    return random_workout


def only_abs(seed=None):
    SEED = seed
    core = ("Abdominals",)

    total_random = TotalRandom(n_exercises=35)
    abs_workout = total_random.init(muscles=core, etypes=("strength",), seed=SEED)

    return abs_workout


def pyramid_workout(seed=None):
    SEED = seed
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


    return lower_pyramid1 + [Rest(20)] + upper_pyramid1 + [Rest(20)] + core_pyramid1 + [Rest(20)] + lower_pyramid2 + [Rest(20)] + upper_pyramid2 + [Rest(20)] + core_pyramid2


def variety_hour(seed=None):
    arms = ('Biceps', 'Triceps', 'Shoulders', "Forearms")
    upper_body = ("Chest", "MiddleBack", "Lats", "Traps")
    lower_body = ('Quadriceps', 'Hamstrings', 'Glutes', 'Calves', "LowerBack", "Abductors", "Adductors")
    abs_ = ("Abdominals",)

    timed_workout = TimedWorkout(
        on_time=45, off_time=15, round_rest=0, rounds=2, n_exercises=4,
    )
    tabata = Tabata(on_time=20, off_time=10, round_rest=0, rounds=4, n_exercises=3)
    emom = EXOX(rounds=3, n_exercises=2)
    drop_set = DropSet(n_exercises=4, on_time=30, off_time=0, round_rest=10)
    rand = TotalRandom(n_exercises=10)
    pyramid = TimePyramid(n_exercises=5)

    wout = []
    exclude = []

    wout += timed_workout.init(
        muscles=arms+upper_body, equipment=("dumbbell", "kettlebell", "band"), etypes=("strength",), seed=seed,
    )
    wout += [Rest(15)]
    exclude = list(set([ex.__class__ for ex in wout]))

    wout += tabata.init(muscles=lower_body, exclude_exercises=exclude, alt=True, seed=seed)
    wout += [Rest(15)]
    exclude = list(set([ex.__class__ for ex in wout]))

    wout += drop_set.init(muscles=abs_, exclude_exercises=exclude, equipment=(None,), seed=seed)
    wout += [Rest(15)]
    exclude = list(set([ex.__class__ for ex in wout]))

    wout += emom.init(muscles=arms+upper_body, exclude_exercises=exclude, seed=seed)
    wout += [Rest(15)]
    exclude = list(set([ex.__class__ for ex in wout]))

    wout += pyramid.init(muscles=lower_body, exclude_exercises=exclude, seed=seed)
    wout += [Rest(15)]
    exclude = list(set([ex.__class__ for ex in wout]))

    wout += rand.init(muscles=abs_, exclude_exercises=exclude, equipment=(None,))

    return wout


def emomonday(seed=None):
    arms = ('Biceps', 'Triceps', 'Shoulders', "Forearms")
    upper_body = ("Chest", "MiddleBack", "Lats", "Traps")
    lower_body = ('Quadriceps', 'Hamstrings', 'Glutes', 'Calves', "LowerBack", "Abductors", "Adductors")
    abs_ = ("Abdominals",)

    wout = []
    exclude = []

    emom = EXOX(rounds=3, n_exercises=3)
    fake_tabata = TimedWorkout(
        on_time=20, off_time=10, round_rest=0, rounds=3, n_exercises=2
    )

    # lower body
    wout += fake_tabata.init(muscles=lower_body, seed=seed)
    wout += [Rest(15)]
    exclude = list(set([ex.__class__ for ex in wout]))

    wout += emom.init(muscles=lower_body, exclude_exercises=exclude, seed=seed)
    wout += [Rest(15)]
    exclude = list(set([ex.__class__ for ex in wout]))

    # upper body
    wout += fake_tabata.init(muscles=upper_body + arms, exclude_exercises=exclude, seed=seed)
    wout += [Rest(15)]
    exclude = list(set([ex.__class__ for ex in wout]))

    wout += emom.init(muscles=upper_body + arms, exclude_exercises=exclude, seed=seed)
    wout += [Rest(15)]
    exclude = list(set([ex.__class__ for ex in wout]))

    # abs
    wout += fake_tabata.init(muscles=abs_, exclude_exercises=exclude, seed=seed)
    wout += [Rest(15)]
    exclude = list(set([ex.__class__ for ex in wout]))

    wout += emom.init(muscles=abs_, exclude_exercises=exclude, seed=seed)

    return wout


def all_tabata(seed=None):
    arms = ('Biceps', 'Triceps', 'Shoulders', "Forearms")
    upper_body = ("Chest", "MiddleBack", "Lats", "Traps")
    lower_body = ('Quadriceps', 'Hamstrings', 'Glutes', 'Calves', "LowerBack", "Abductors", "Adductors")
    abs_ = ("Abdominals",)

    wout = []
    exclude = []

    tabata = Tabata(rounds=4, n_exercises=6, on_time=20, off_time=10, round_rest=10)

    # lower body
    wout += tabata.init(muscles=lower_body, seed=seed)
    exclude = list(set([ex.__class__ for ex in wout]))

    # upper body
    wout += tabata.init(muscles=upper_body + arms, exclude_exercises=exclude, seed=seed)
    exclude = list(set([ex.__class__ for ex in wout]))


    # abs
    wout += tabata.init(muscles=abs_, exclude_exercises=exclude, seed=seed)

    return wout


def samon_preferred(seed=None):
    SEED = seed
    muscles = ('Biceps', "Triceps")
    equipment = [eq for eq in ALL_EQUIPMENT if eq is not None]
    long_wout = TimedWorkout(on_time=45, off_time=15, round_rest=0, rounds=3, n_exercises=10)

    wout = long_wout.init(muscles=muscles, equipment=equipment, alt=True, seed=SEED)

    return wout