from dataclasses import dataclass
import sys
import inspect
import time
import re
# import only system from os 
from os import system, name 

import muscles as ms


@dataclass
class BaseExercise:
    count: int

    PATTERN = re.compile(r'(?<!^)(?=[A-Z])')

    # define our clear function 
    def clear(self): 
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
    
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 

    def countdown(self, t): 
        while t: 
            mins, secs = divmod(t, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") 
            time.sleep(1) 
            t -= 1

    def run(self, up_next=None):
        name = self.PATTERN.sub(' ', self.__class__.__name__)
        print(f"Start: {name}")
        if up_next:
            up_next_name = self.PATTERN.sub(' ', up_next.__class__.__name__)
            print(f"Up Next: {up_next_name}")
        self.countdown(self.count)
        self.clear()

class PushUp(BaseExercise):
    muscles = (ms.Chest, ms.Triceps, ms.Shoulders)
    etype = 'strength'
    equipment = (None,)
    rep_time = 2.0

class Crunch(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.0

class BicycleCrunch(Crunch):
    etype = 'cardio'

class HighKnees(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 0.5

class ShoulderTap(BaseExercise):
    muscles = (ms.Shoulders, ms.Abdominals)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 0.75

class Plank(BaseExercise):
    muscles = (ms.Abdominals, ms.Shoulders)
    etype = 'strength'
    equipment = (None,)
    rep_time = None

class Superman(BaseExercise):
    muscles = (ms.LowerBack,)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 1.0

class DeadLift(BaseExercise):
    muscles = (ms.LowerBack, ms.Hamstrings)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.5

class Lunge(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'strength'
    equipment = (None, 'kettlebell', 'dumbbell')
    rep_time = 2.0

class SingleLegDeadLift(DeadLift):
    pass
    
class JumpingJack(BaseExercise):
    muscles = (ms.Shoulders, ms.Calves)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 0.75

class FireHydrant(BaseExercise):
    muscles = (ms.Abductors,)
    etype = 'strength'
    equipment = (None, 'dumbbell')
    rep_time = 1.25

class SidePlank(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None, 'dumbbell')
    rep_time = None

class SquatJump(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 2.0

class Dip(BaseExercise):
    muscles = (ms.Triceps, ms.Chest)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.5

class AnkleTap(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.5

class Bridge(BaseExercise):
    muscles = (ms.LowerBack, ms.Glutes, ms.Hamstrings)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.75

class Squat(BaseExercise):
    muscles = (ms.Quadriceps, ms.Glutes)
    etype = 'strength'
    equipment = (None, 'band', 'kettlebell', 'dumbbell')
    rep_time = 1.0

class BridgePulse(Bridge):
    rep_time = None

class SquatPulse(Squat):
    rep_time = None

class CurtsyLunge(Lunge):
    pass

class FrogPressBridge(BaseExercise):
    muscles = (ms.LowerBack, ms.Abductors)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.75

class SingleLegBridge(Bridge):
    pass


class CalfRaise(BaseExercise):
    muscles = (ms.Calves,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.75

class DownDogPushUp(PushUp):
    pass

class LegLift(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.5

class ShoulderPress(BaseExercise):
    muscles = (ms.Shoulders,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 1.5

class SpiderPlank(Plank):
    rep_time = 1.0

class ReversePlank(BaseExercise):
    muscles = (ms.Shoulders, ms.LowerBack)
    etype = 'strength'
    equipment = (None,)
    rep_time = None

class MountainClimber(BaseExercise):
    muscles = (ms.Abdominals, ms.Quadriceps)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 0.5

class AlternateJack(BaseExercise):
    muscles = (ms.LowerBack, ms.Quadriceps, ms.Calves)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 1.0

class UpDownPlank(Plank):
    muscles = (ms.Abdominals, ms.Shoulders, ms.Triceps,)
    rep_time = 1.5

class InchWorm(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 8.0

class TuckJump(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 1.0

class VUp(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.75

class StarJump(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 1.5

class SkaterJump(BaseExercise):
    muscles = (ms.Quadriceps, ms.Abductors)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 2.0

class ToeTouch(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.5

class Burpee(BaseExercise):
    muscles = (ms.Quadriceps, ms.Chest, ms.Shoulders, ms.Abdominals)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 5.0

class Curl(BaseExercise):
    muscles = (ms.Biceps,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.0

class WoodChopper(BaseExercise):
    muscles = (ms.Abdominals, ms.Shoulders)
    etype = 'strength'
    equipment = ('kettlebell', 'dumbbell')
    rep_time = 2.0

class PistolSquat(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 4.0

class SumoSquat(BaseExercise):
    muscles = (ms.Quadriceps, ms.Adductors)
    etype = 'strength'
    equipment = (None, 'kettlebell', 'dumbbell')
    rep_time = 1.25

class WindshieldWipers(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 2.25

class ChestFlies(BaseExercise):
    muscles = (ms.Chest,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 1.5

class BackFlies(BaseExercise):
    muscles = (ms.MiddleBack,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 1.5

class FlutterKick(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.75

class AccordianCrunches(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.75

class ClappingPushUp(PushUp):
    pass

class NarrowPushUp(PushUp):
    pass

class SquatHold(Squat):
    rep_time = None

class WallSit(Squat):
    rep_time = None

class SquatPress(Squat):
    muscles = (ms.Quadriceps, ms.Shoulders)
    equipment = ('band', 'kettlebell', 'dumbbell')

class HalfBurpee(Burpee):
    rep_time = 4.0

class GobletSquat(Squat):
    equipment = ('kettlebell', 'dumbbell')

class LateralRaises(BaseExercise):
    muscles = (ms.Shoulders,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.0

class ObliqueCrunches(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.75

class BoatHold(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = None

class SwitchLunge(Lunge):
    etype = 'cardio'
    rep_time = 1.5


    
class BandPullApart(BaseExercise):
    muscles = (ms.MiddleBack,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 1.25

class DonkeyKick(BaseExercise):
    muscles = (ms.Quadriceps, ms.Shoulders, ms.Abdominals)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 3.0

class TricepExtension(BaseExercise):
    muscles = (ms.Triceps,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.0

class InnerThighRaises(BaseExercise):
    muscles = (ms.Adductors,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.75

class PlankJack(Plank):
    muscles = (ms.Abdominals, ms.Quadriceps, ms.Shoulders)
    etype = 'cardio'
    rep_time = 1.0

class UprightRow(BaseExercise):
    muscles = (ms.Traps, ms.Shoulders)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 1.25

class BentOverRow(BaseExercise):
    muscles = (ms.MiddleBack,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 1.5

class RussianTwist(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.75

class TeaPot(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 1.75

class DeclinePushUp(PushUp):
    pass

class SumoDeadLift(DeadLift):
    pass

class Wiggle(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.75

class ArnoldPress(BaseExercise):
    muscles = (ms.Shoulders,)
    etype = 'strength'
    equipment = ('kettlebell', 'dumbbell')
    rep_time = 3.0

class SvendPress(BaseExercise):
    muscles = (ms.Shoulders,)
    etype = 'strength'
    equipment = ('kettlebell', 'dumbbell')
    rep_time = 1.5

class JudoRoll(BaseExercise):
    muscles = (ms.Abdominals, ms.Quadriceps)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 4.0


class Rest(BaseExercise):
    muscles = None
    etype = None
    equipment = (None,)
    rep_time = None

ALL_EQUIPMENT = ('kettlebell', 'dumbbell', 'band', None)

ALL_EXERCISES = {
    name: obj for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass) if obj.__module__ is __name__
    }
del ALL_EXERCISES['BaseExercise']
del ALL_EXERCISES['Rest']