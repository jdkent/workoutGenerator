from flask import Flask
from .workouts import TimedWorkout, Tabata, TimePyramid, TotalRandom, NAME_HASHES, Rest
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


@bp.route('/pyramid', defaults={'seed': None})
@bp.route('/pyramid/<int:seed>')
def pyramid(seed):
    wout = pyramid_workout(seed)
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
