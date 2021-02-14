from dataclasses import dataclass
import re
import sys
import inspect

# match camelCase
PATTERN = re.compile(r'(?<!^)(?=[A-Z])')


@dataclass
class Chest:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class Forearms:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class Lats:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class MiddleBack:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class LowerBack:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class Neck:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class Quadriceps:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class Hamstrings:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class Calves:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class Triceps:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class Traps:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class Shoulders:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class Abdominals:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class Glutes:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class Biceps:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class Adductors:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

@dataclass
class Abductors:
    def __str__(self):
        return PATTERN.sub('_', self.__doc__.rstrip('()')).lower()

Chest.opposite = (MiddleBack,)
MiddleBack.opposite = (Chest,)

Forearms.opposite = None

Lats.opposite = (Traps,)
Traps.opposite = (Lats,)

LowerBack.opposite = (Abdominals,)
Abdominals.opposite = (LowerBack, Glutes)
Glutes.opposite = (Abdominals, Quadriceps)

Neck.opposite = None

Quadriceps.opposite = (Hamstrings, Glutes)
Hamstrings.opposite = (Quadriceps,)

Calves.opposite = None

Triceps.opposite = (Biceps,)
Biceps.opposite = (Triceps,)

Shoulders.opposite = None

Adductors.opposite = (Abductors,)
Abductors.opposite = (Adductors,)

ALL_MUSCLES = {
    name: obj for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass) if obj.__module__ is __name__
    }