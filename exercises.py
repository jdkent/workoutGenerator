from dataclasses import dataclass
import sys
import inspect
import time
import re
# import only system from os 
from os import system, name 

import numpy as np
import simpleaudio as sa

import muscles as ms


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def beep(freq=880, T=1.0):
    sample_rate = 44100
    t = np.linspace(0, T, int(T * sample_rate), False)

    note = np.sin(freq * t * 2 * np.pi)

    note *= 32767 / np.max(np.abs(note))

    note = note.astype(np.int16)

    play_obj = sa.play_buffer(note, 1, 2, sample_rate)

    play_obj.wait_done()


@dataclass
class BaseExercise:
    on_time: int = 0
    reps: int = 0

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
        first_t = t
        while t:
            try:
                mins, secs = divmod(t, 60) 
                timer = '{:02d}:{:02d}'.format(mins, secs) 
                print(timer, end="\r") 
                if first_t == t:
                    beep()
                else:
                    time.sleep(1)
                t -= 1
            except KeyboardInterrupt:
                end = input("Paused, type 'quit' to end program")
                if end == 'quit':
                    raise KeyboardInterrupt
                else:
                    continue


    def run(self, up_next=None, idx=None, total=None):
        self.clear()
        name = self.PATTERN.sub(' ', self.__class__.__name__)
        if self.reps > 0:
            print(f"{bcolors.OKGREEN}{bcolors.BOLD}{bcolors.UNDERLINE}Start: {self.reps} {name}{bcolors.ENDC}")
        else:
            print(f"{bcolors.OKGREEN}{bcolors.BOLD}{bcolors.UNDERLINE}Start: {name}{bcolors.ENDC}")
        if up_next:
            up_next_name = self.PATTERN.sub(' ', up_next.__class__.__name__)
            if up_next.reps > 0:
                print(f"{bcolors.FAIL}Up Next: {up_next.reps} {up_next_name}{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}Up Next: {up_next_name}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Progress: {idx}/{total}{bcolors.ENDC}")
        self.countdown(self.on_time)
        self.clear()

class PushUp(BaseExercise):
    muscles = (ms.Chest, ms.Triceps, ms.Shoulders)
    etype = 'strength'
    equipment = (None,)
    rep_time = 2.25

class TPushUp(PushUp):
    rep_time = 3.0

class ChaturangaPushUp(PushUp):
    pass

class DiveBombPushUp(PushUp):
    rep_time = 5.0


class Crunch(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.0

class SitUp(Crunch):
    rep_time = 1.75

class StraightLegSitUp(SitUp):
    pass

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
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = None


class PlankWithHipRotation(Plank):
    rep_time = 1.0
class Superman(BaseExercise):
    muscles = (ms.LowerBack,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.75

class DeadLift(BaseExercise):
    muscles = (ms.LowerBack, ms.Hamstrings)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.8

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
    rep_time = 1.0

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

class SidePlankDip(SidePlank):
    rep_time = 1.1


class SidePlankRotations(SidePlank):
    rep_time = 2.25

class SquatJump(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 1.75

class SquatJump180(SquatJump):
    pass

class Dip(BaseExercise):
    muscles = (ms.Triceps, ms.Chest)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.8

class AnkleTap(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.5

class Bridge(BaseExercise):
    muscles = (ms.LowerBack, ms.Glutes, ms.Hamstrings)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.25

class Squat(BaseExercise):
    muscles = (ms.Quadriceps, ms.Glutes)
    etype = 'strength'
    equipment = (None, 'band', 'kettlebell', 'dumbbell')
    rep_time = 1.5

class BridgePulse(Bridge):
    rep_time = None

class SquatPulse(Squat):
    rep_time = None

class CurtsyLunge(Lunge):
    rep_time = 3.25

class FrogPressBridge(BaseExercise):
    muscles = (ms.LowerBack, ms.Abductors)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.25

class SingleLegBridge(Bridge):
    rep_time = 1.5


class CalfRaise(BaseExercise):
    muscles = (ms.Calves,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.5

class DownDogPushUp(PushUp):
    muscles = (ms.Shoulders,)
    rep_time = 2.5

class LegLift(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 2.0

class FigureEightLegLift(LegLift):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 6.0

class ShoulderPress(BaseExercise):
    muscles = (ms.Shoulders,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.25

class SpiderPlank(Plank):
    rep_time = 1.75

class StarPlank(Plank):
    pass


class ReverseCrunch(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 3.0

class DeadBug(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.25

class BirdDog(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.85

class HollowBodyRock(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = None

class LSit(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = None

class BeastPoseHold(BaseExercise):
    muscles = (ms.Abdominals, ms.Quadriceps, ms.Shoulders)
    etype = 'strength'
    equipment = (None,)
    rep_time = None

class ReversePlank(BaseExercise):
    muscles = (ms.Shoulders, ms.LowerBack)
    etype = 'strength'
    equipment = (None,)
    rep_time = None

class MountainClimber(BaseExercise):
    muscles = (ms.Abdominals, ms.Quadriceps, ms.Shoulders)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 0.5

class MountainClimberTwist(BaseExercise):
    muscles = (ms.Abdominals, ms.Quadriceps, ms.Shoulders)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 0.5

class AlternateJack(BaseExercise):
    muscles = (ms.LowerBack, ms.Quadriceps, ms.Calves)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 1.8

class UpDownPlank(Plank):
    muscles = (ms.Abdominals, ms.Shoulders, ms.Triceps,)
    rep_time = 2.5

class InchWorm(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 5.0

class TuckJump(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 2.0

class RenegadePushUp(BaseExercise):
    muscles = (ms.Chest, ms.Triceps, ms.Shoulders, ms.MiddleBack)
    etype = 'strength'
    equipment = ('dumbbell', 'kettlebell')
    rep_time = 4.0

class SpiderManPushUp(PushUp):
    muscles = (ms.Chest, ms.Triceps, ms.Shoulders, ms.Abdominals)
    rep_time = 3.00

class StarCrunch(Crunch):
    rep_time = 1.25
class VUp(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.75

class StarJump(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 2.50

class ProneLegLift(BaseExercise):
    muscles = (ms.LowerBack,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 2.25

class SkaterHop(BaseExercise):
    muscles = (ms.Quadriceps, ms.Abductors)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 1.75

class ToeTouch(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.0

class BusDriver(BaseExercise):
    muscles = (ms.Shoulders,)
    etype = 'strength'
    equipment = ('dumbbell',)
    rep_time = None
class Burpee(BaseExercise):
    muscles = (ms.Quadriceps, ms.Chest, ms.Shoulders, ms.Abdominals)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 3.0

class LungeBurpee(Burpee):
    rep_time = 3.75

class YTWL(BaseExercise):
    muscles = (ms.MiddleBack, ms.Shoulders)
    etype = 'strength'
    equipment = (None,)
    rep_time = 4.0


class SurferBurpee(Burpee):
    rep_time = 3.5

class DoubleJumpBurpee(Burpee):
    rep_time = 4.0

class Curl(BaseExercise):
    muscles = (ms.Biceps,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.0

class OutwardCurl(Curl):
    pass

class HighCurl(Curl):
    muscles = (ms.Biceps, ms.Shoulders)

class OutAndInCurl(Curl):
    rep_time = None
class HammerCurl(Curl):
    pass

class ForearmCurl(Curl):
    pass

class CurlPulse(Curl):
    rep_time = None

class WoodChopper(BaseExercise):
    muscles = (ms.Abdominals, ms.Shoulders)
    etype = 'strength'
    equipment = ('kettlebell', 'dumbbell')
    rep_time = 2.25

class PistolSquat(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 4.0

class SumoSquat(BaseExercise):
    muscles = (ms.Quadriceps, ms.Adductors)
    etype = 'strength'
    equipment = (None, 'kettlebell', 'dumbbell')
    rep_time = 1.8

class WindshieldWipers(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 2.75

class ChestFly(BaseExercise):
    muscles = (ms.Chest,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.25

class BackFly(BaseExercise):
    muscles = (ms.MiddleBack,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.25

class FlutterKick(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.30

class AccordianCrunch(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.25

class ClappingPushUp(PushUp):
    rep_time = 3.0

class NarrowPushUp(PushUp):
    pass

class SquatHold(Squat):
    rep_time = None

class WallSit(Squat):
    rep_time = None

class SquatPress(Squat):
    muscles = (ms.Quadriceps, ms.Shoulders)
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.5

class HalfBurpee(Burpee):
    rep_time = 2.5

class GobletSquat(Squat):
    equipment = ('kettlebell', 'dumbbell')
    rep_time = 2.25

class LateralRaise(BaseExercise):
    muscles = (ms.Shoulders,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 3.0

class FrontRaise(LateralRaise):
    pass

class LatPullDown(BaseExercise):
    muscles = (ms.Lats,)
    etype = 'strength'
    equipment = ('band',)
    rep_time = 1.5

class ButterflyCrunch(Crunch):
    pass

class PushUpJackTap(PushUp):
    muscles = (ms.Chest, ms.Triceps, ms.Shoulders, ms.Quadriceps)
    etype = 'cardio'
    rep_time = 2.75

class ObliqueCrunch(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.0

class BoatHold(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = None

class FigureEightBoatHold(BoatHold):
    equipment = ("dumbbell", "kettlebell")


class SwitchLunge(Lunge):
    etype = 'cardio'
    rep_time = 1.5


class SideLunge(Lunge):
    rep_time = 2.5

class BandPullApart(BaseExercise):
    muscles = (ms.MiddleBack,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.75

class MuleKick(BaseExercise):
    muscles = (ms.Quadriceps, ms.Shoulders, ms.Abdominals)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 2.75


class DonkeyKick(BaseExercise):
    muscles = (ms.Glutes,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.75

class DonkeyPulse(DonkeyKick):
    rep_time = None


class DonkeyKneeToElbow(DonkeyKick):
    rep_time = 2.5

class DonkeyRainbow(DonkeyKick):
    rep_time = 2.5


class OverheadTricepExtension(BaseExercise):
    muscles = (ms.Triceps,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.0


class SkullCrusher(BaseExercise):
    muscles = (ms.Triceps,)
    etype = 'strength'
    equipment = ('kettlebell', 'dumbbell')
    rep_time = 2.25

class BentOverTricepExtension(BaseExercise):
    muscles = (ms.Triceps,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.0

class TricepExtensionPulse(OverheadTricepExtension):
    rep_time = None


class InnerThighRaise(BaseExercise):
    muscles = (ms.Adductors,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.0

class PlankJack(Plank):
    muscles = (ms.Abdominals, ms.Quadriceps, ms.Shoulders)
    etype = 'cardio'
    rep_time = 1.0

class UprightRow(BaseExercise):
    muscles = (ms.Traps, ms.Shoulders)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.25


class SingleArmUprightRow(UprightRow):
    pass

class BentOverRow(BaseExercise):
    muscles = (ms.MiddleBack,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 1.8


class BentOverY(BackFly):
    muscles = (ms.MiddleBack, ms.Traps)


class DumbbellPullover(BaseExercise):
    muscles = (ms.Lats, ms.Shoulders)
    etype = 'strength'
    equipment = ('dumbbell', 'kettlebell')
    rep_time = 2.25


class RussianTwist(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.75

class KettleBellSwing(BaseExercise):
    muscles = (ms.LowerBack, ms.Hamstrings, ms.Shoulders)
    etype = 'cardio'
    equipment = ('dumbbell', 'kettlebell')
    rep_time = 1.8

class TeaPot(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 1.75

class DeclinePushUp(PushUp):
    pass

class SumoDeadLift(DeadLift):
    pass

class Windmill(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = ('dumbbell', 'kettlebell')
    rep_time = 3.0
class GoodMorning(BaseExercise):
    muscles = (ms.LowerBack, ms.Hamstrings)
    etype = 'strength'
    equipment = ('dumbbell', 'kettlebell')
    rep_time = 2.25

class Wiggle(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.65

class ArnoldPress(BaseExercise):
    muscles = (ms.Shoulders,)
    etype = 'strength'
    equipment = ('kettlebell', 'dumbbell')
    rep_time = 3.0

class SvendPress(BaseExercise):
    muscles = (ms.Shoulders,)
    etype = 'strength'
    equipment = ('kettlebell', 'dumbbell')
    rep_time = 2.25

class JudoRoll(BaseExercise):
    muscles = (ms.Abdominals, ms.Quadriceps)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 3.25


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
del ALL_EXERCISES['bcolors']