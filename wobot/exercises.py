from dataclasses import dataclass
import sys
import inspect
import re

import wobot.muscles as ms

@dataclass
class BaseExercise:
    on_time: int = 0
    reps: int = 0

    PATTERN = re.compile(r'(?<!^)(?=[A-Z])')

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        if self.reps:
            quantity = self.reps
            unit = "reps"
        else:
            quantity = self.on_time
            unit = "seconds"
        return f"{quantity} {unit} of {self.PATTERN.sub(' ', self.__class__.__name__)}"


class PushUps(BaseExercise):
    muscles = (ms.Chest, ms.Triceps, ms.Shoulders)
    etype = 'strength'
    equipment = (None,)
    rep_time = 2.25

class TPushUps(PushUps):
    rep_time = 3.0

class ChaturangaPushUps(PushUps):
    pass

class DiveBombPushUps(PushUps):
    rep_time = 5.0


class Crunches(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.0

class SitUps(Crunches):
    rep_time = 1.75

class StraightLegSitUps(SitUps):
    pass

class BicycleCrunches(Crunches):
    etype = 'cardio'

class HighKnees(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 0.5

class ShoulderTaps(BaseExercise):
    muscles = (ms.Shoulders, ms.Abdominals)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 0.75

class Planks(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = None


class PlankWithHipRotations(Planks):
    rep_time = 1.0
class Supermans(BaseExercise):
    muscles = (ms.LowerBack,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.75

class DeadLifts(BaseExercise):
    muscles = (ms.LowerBack, ms.Hamstrings)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.8

class Lunges(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'strength'
    equipment = (None, 'kettlebell', 'dumbbell')
    rep_time = 2.0

class SingleLegDeadLifts(DeadLifts):
    pass
    
class JumpingJacks(BaseExercise):
    muscles = (ms.Shoulders, ms.Calves)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 1.0

class FireHydrants(BaseExercise):
    muscles = (ms.Abductors,)
    etype = 'strength'
    equipment = (None, 'dumbbell')
    rep_time = 1.25

class SidePlanks(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None, 'dumbbell')
    rep_time = None

class SidePlankDips(SidePlanks):
    rep_time = 1.1


class SidePlankRotations(SidePlanks):
    rep_time = 2.25

class SquatJumps(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 1.75

class SquatJump180s(SquatJumps):
    pass

class Dips(BaseExercise):
    muscles = (ms.Triceps, ms.Chest)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.8

class AnkleTaps(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.5

class Bridges(BaseExercise):
    muscles = (ms.LowerBack, ms.Glutes, ms.Hamstrings)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.25

class Squats(BaseExercise):
    muscles = (ms.Quadriceps, ms.Glutes)
    etype = 'strength'
    equipment = (None, 'band', 'kettlebell', 'dumbbell')
    rep_time = 1.5

class BridgePulses(Bridges):
    rep_time = None

class SquatPulses(Squats):
    rep_time = None

class CurtsyLunges(Lunges):
    rep_time = 3.25

class FrogPressBridges(BaseExercise):
    muscles = (ms.LowerBack, ms.Abductors)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.25

class SingleLegBridges(Bridges):
    rep_time = 1.5


class CalfRaises(BaseExercise):
    muscles = (ms.Calves,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.5

class DownDogPushUps(PushUps):
    muscles = (ms.Shoulders,)
    rep_time = 2.5

class LegLifts(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 2.0

class FigureEightLegLifts(LegLifts):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 6.0

class ShoulderPresses(BaseExercise):
    muscles = (ms.Shoulders,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.25

class SpiderPlanks(Planks):
    rep_time = 1.75

class StarPlanks(Planks):
    pass


class ReverseCrunches(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 3.0

class DeadBugs(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.25

class BirdDogs(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.85

class HollowBodyRocks(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = None

class LSits(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = None

class BeastPoseHolds(BaseExercise):
    muscles = (ms.Abdominals, ms.Quadriceps, ms.Shoulders)
    etype = 'strength'
    equipment = (None,)
    rep_time = None

class ReversePlanks(BaseExercise):
    muscles = (ms.Shoulders, ms.LowerBack)
    etype = 'strength'
    equipment = (None,)
    rep_time = None

class MountainClimbers(BaseExercise):
    muscles = (ms.Abdominals, ms.Quadriceps, ms.Shoulders)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 0.5

class MountainClimberTwists(BaseExercise):
    muscles = (ms.Abdominals, ms.Quadriceps, ms.Shoulders)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 0.5

class AlternateJacks(BaseExercise):
    muscles = (ms.LowerBack, ms.Quadriceps, ms.Calves)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 1.8

class UpDownPlanks(Planks):
    muscles = (ms.Abdominals, ms.Shoulders, ms.Triceps,)
    rep_time = 2.5

class InchWorms(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 5.0

class TuckJumps(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 2.0

class RenegadePushUps(BaseExercise):
    muscles = (ms.Chest, ms.Triceps, ms.Shoulders, ms.MiddleBack)
    etype = 'strength'
    equipment = ('dumbbell', 'kettlebell')
    rep_time = 4.0

class SpiderManPushUps(PushUps):
    muscles = (ms.Chest, ms.Triceps, ms.Shoulders, ms.Abdominals)
    rep_time = 3.00

class StarCrunches(Crunches):
    rep_time = 1.25
class VUps(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.75

class StarJumps(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 2.50

class ProneLegLifts(BaseExercise):
    muscles = (ms.LowerBack,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 2.25

class SkaterHops(BaseExercise):
    muscles = (ms.Quadriceps, ms.Abductors)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 1.75

class ToeTouches(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.0

class BusDrivers(BaseExercise):
    muscles = (ms.Shoulders,)
    etype = 'strength'
    equipment = ('dumbbell',)
    rep_time = None

class Burpees(BaseExercise):
    muscles = (ms.Quadriceps, ms.Chest, ms.Shoulders, ms.Abdominals)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 3.0


class LungeBurpees(Burpees):
    rep_time = 3.75

class YTWLs(BaseExercise):
    muscles = (ms.MiddleBack, ms.Shoulders)
    etype = 'strength'
    equipment = (None,)
    rep_time = 4.0


class SurferBurpees(Burpees):
    rep_time = 3.5

class DoubleJumpBurpees(Burpees):
    rep_time = 4.0

class Curls(BaseExercise):
    muscles = (ms.Biceps,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.0

class OutwardCurls(Curls):
    pass

class HighCurls(Curls):
    muscles = (ms.Biceps, ms.Shoulders)

class OutAndInCurls(Curls):
    rep_time = None


class HammerCurls(Curls):
    pass


class ForearmCurls(Curls):
    pass


class CurlPulses(Curls):
    rep_time = None

class WoodChoppers(BaseExercise):
    muscles = (ms.Abdominals, ms.Shoulders)
    etype = 'strength'
    equipment = ('kettlebell', 'dumbbell')
    rep_time = 2.25

class PistolSquats(BaseExercise):
    muscles = (ms.Quadriceps,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 4.0

class SumoSquats(BaseExercise):
    muscles = (ms.Quadriceps, ms.Adductors)
    etype = 'strength'
    equipment = (None, 'kettlebell', 'dumbbell')
    rep_time = 1.8

class WindshieldWipers(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 2.75

class ChestFlies(BaseExercise):
    muscles = (ms.Chest,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.25

class BackFlies(BaseExercise):
    muscles = (ms.MiddleBack,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.25

class FlutterKicks(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.30

class AccordianCrunches(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.25

class ClappingPushUps(PushUps):
    rep_time = 3.0

class NarrowPushUps(PushUps):
    pass

class SquatHold(Squats):
    rep_time = None

class WallSit(Squats):
    rep_time = None

class SquatPresses(Squats):
    muscles = (ms.Quadriceps, ms.Shoulders)
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.5

class HalfBurpees(Burpees):
    rep_time = 2.5

class GobletSquats(Squats):
    equipment = ('kettlebell', 'dumbbell')
    rep_time = 2.25

class LateralRaises(BaseExercise):
    muscles = (ms.Shoulders,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 3.0

class FrontRaises(LateralRaises):
    pass

class LatPullDowns(BaseExercise):
    muscles = (ms.Lats,)
    etype = 'strength'
    equipment = ('band',)
    rep_time = 1.5

class ButterflyCrunches(Crunches):
    pass

class PushUpJackTaps(PushUps):
    muscles = (ms.Chest, ms.Triceps, ms.Shoulders, ms.Quadriceps)
    etype = 'cardio'
    rep_time = 2.75

class ObliqueCrunches(BaseExercise):
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


class SwitchLunges(Lunges):
    etype = 'cardio'
    rep_time = 1.5


class SideLunges(Lunges):
    rep_time = 2.5

class BandPullAparts(BaseExercise):
    muscles = (ms.MiddleBack,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.75

class MuleKicks(BaseExercise):
    muscles = (ms.Quadriceps, ms.Shoulders, ms.Abdominals)
    etype = 'cardio'
    equipment = (None,)
    rep_time = 2.75


class DonkeyKicks(BaseExercise):
    muscles = (ms.Glutes,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.75

class DonkeyPulses(DonkeyKicks):
    rep_time = None


class DonkeyKneeToElbows(DonkeyKicks):
    rep_time = 2.5

class DonkeyRainbows(DonkeyKicks):
    rep_time = 2.5


class OverheadTricepExtensions(BaseExercise):
    muscles = (ms.Triceps,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.0


class SkullCrushers(BaseExercise):
    muscles = (ms.Triceps,)
    etype = 'strength'
    equipment = ('kettlebell', 'dumbbell')
    rep_time = 2.25

class BentOverTricepExtensions(BaseExercise):
    muscles = (ms.Triceps,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.0

class TricepExtensionPulses(OverheadTricepExtensions):
    rep_time = None


class InnerThighRaises(BaseExercise):
    muscles = (ms.Adductors,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 1.0

class PlankJacks(Planks):
    muscles = (ms.Abdominals, ms.Quadriceps, ms.Shoulders)
    etype = 'cardio'
    rep_time = 1.0

class UprightRows(BaseExercise):
    muscles = (ms.Traps, ms.Shoulders)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 2.25


class SingleArmUprightRows(UprightRows):
    pass

class BentOverRows(BaseExercise):
    muscles = (ms.MiddleBack,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 1.8


class BentOverYs(BackFlies):
    muscles = (ms.MiddleBack, ms.Traps)


class DumbbellPullovers(BaseExercise):
    muscles = (ms.Lats, ms.Shoulders)
    etype = 'strength'
    equipment = ('dumbbell', 'kettlebell')
    rep_time = 2.25


class RussianTwists(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.75

class KettleBellSwings(BaseExercise):
    muscles = (ms.LowerBack, ms.Hamstrings, ms.Shoulders)
    etype = 'cardio'
    equipment = ('dumbbell', 'kettlebell')
    rep_time = 1.8

class TeaPots(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = ('band', 'kettlebell', 'dumbbell')
    rep_time = 1.75

class DeclinePushUps(PushUps):
    pass

class SumoDeadLifts(DeadLifts):
    pass

class Windmills(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = ('dumbbell', 'kettlebell')
    rep_time = 3.0
class GoodMornings(BaseExercise):
    muscles = (ms.LowerBack, ms.Hamstrings)
    etype = 'strength'
    equipment = ('dumbbell', 'kettlebell')
    rep_time = 2.25

class Wiggles(BaseExercise):
    muscles = (ms.Abdominals,)
    etype = 'strength'
    equipment = (None,)
    rep_time = 0.65

class ArnoldPresses(BaseExercise):
    muscles = (ms.Shoulders,)
    etype = 'strength'
    equipment = ('kettlebell', 'dumbbell')
    rep_time = 3.0

class SvendPresses(BaseExercise):
    muscles = (ms.Shoulders,)
    etype = 'strength'
    equipment = ('kettlebell', 'dumbbell')
    rep_time = 2.25

class JudoRolls(BaseExercise):
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