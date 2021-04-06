Blockly.Python['exox'] = function(block) {
  var number_n_exercises = block.getFieldValue('n_exercises');
  var number_rounds = block.getFieldValue('rounds');
  var number_difficulty = block.getFieldValue('difficulty');
  var number_interval = block.getFieldValue('interval');
  var value_etypes = Blockly.Python.valueToCode(block, 'etypes', Blockly.Python.ORDER_ATOMIC);
  var value_equipment = Blockly.Python.valueToCode(block, 'equipment', Blockly.Python.ORDER_ATOMIC);
  var value_muscles = Blockly.Python.valueToCode(block, 'muscles', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var difficulty = number_difficulty / 100
  var code = (
    'exox = EXOX(n_exercises='
    + number_n_exercises
    + ', rounds='
    + number_rounds
    + ', difficulty='
    + difficulty
    + ', interval='
    + number_interval
    + ')\n'
    + 'wout += exox.init(etypes='
    + value_etypes
    + ', equipment='
    + value_equipment
    + ', muscles='
    + value_muscles
    + ')\n'
  )
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['tabata'] = function(block) {
  var number_n_exercises = block.getFieldValue('n_exercises');
  var number_rounds = block.getFieldValue('rounds');
  var number_on_time = block.getFieldValue('on_time');
  var number_off_time = block.getFieldValue('off_time');
  var number_round_rest = block.getFieldValue('round_rest');
  var checkbox_alternate = block.getFieldValue('alternate') == 'TRUE';
  var value_etypes = Blockly.Python.valueToCode(block, 'etypes', Blockly.Python.ORDER_ATOMIC);
  var value_equipment = Blockly.Python.valueToCode(block, 'equipment', Blockly.Python.ORDER_ATOMIC);
  var value_muscles = Blockly.Python.valueToCode(block, 'muscles', Blockly.Python.ORDER_ATOMIC);
  if (checkbox_alternate) {
    checkbox_alternate = 'True'
  } else {
    checkbox_alternate = 'False'
  }
  var code = (
    'tabata = Tabata(n_exercises='
    + number_n_exercises
    + ', rounds='
    + number_rounds
    + ', on_time='
    + number_on_time
    + ', off_time='
    + number_off_time
    + ', round_rest='
    + number_round_rest
    + ')\n'
    + 'wout += tabata.init(etypes='
    + value_etypes
    + ', equipment='
    + value_equipment
    + ', muscles='
    + value_muscles
    + ', alt='
    + checkbox_alternate
    + ')\n'
  )
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['drop_set'] = function(block) {
  var number_n_exercises = block.getFieldValue('n_exercises');
  var number_on_time = block.getFieldValue('on_time');
  var number_off_time = block.getFieldValue('off_time');
  var number_round_rest = block.getFieldValue('round_rest');
  var value_etypes = Blockly.Python.valueToCode(block, 'etypes', Blockly.Python.ORDER_ATOMIC);
  var value_equipment = Blockly.Python.valueToCode(block, 'equipment', Blockly.Python.ORDER_ATOMIC);
  var value_muscles = Blockly.Python.valueToCode(block, 'muscles', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = (
    'drop = DropSet(n_exercises='
    + number_n_exercises
    + ', on_time='
    + number_on_time
    + ', off_time='
    + number_off_time
    + ', round_rest='
    + number_round_rest
    + ')\n'
    + 'wout += drop.init(etypes='
    + value_etypes
    + ', equipment='
    + value_equipment
    + ', muscles='
    + value_muscles
    + ')\n'
  )
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['timed_workout'] = function(block) {
  var number_n_exercises = block.getFieldValue('n_exercises');
  var number_rounds = block.getFieldValue('rounds');
  var number_on_time = block.getFieldValue('on_time');
  var number_off_time = block.getFieldValue('off_time');
  var number_round_rest = block.getFieldValue('round_rest');
  var checkbox_alternate = block.getFieldValue('alternate') == 'TRUE';
  var value_etypes = Blockly.Python.valueToCode(block, 'etypes', Blockly.Python.ORDER_ATOMIC);
  var value_equipment = Blockly.Python.valueToCode(block, 'equipment', Blockly.Python.ORDER_ATOMIC);
  var value_muscles = Blockly.Python.valueToCode(block, 'muscles', Blockly.Python.ORDER_ATOMIC);
  if (checkbox_alternate) {
    checkbox_alternate = 'True'
  } else {
    checkbox_alternate = 'False'
  }
  var code = (
    'timed_wout = TimedWorkout(n_exercises='
    + number_n_exercises
    + ', rounds='
    + number_rounds
    + ', on_time='
    + number_on_time
    + ', off_time='
    + number_off_time
    + ', round_rest='
    + number_round_rest
    + ')\n'
    + 'wout += timed_wout.init(etypes='
    + value_etypes
    + ', equipment='
    + value_equipment
    + ', muscles='
    + value_muscles
    + ', alt='
    + checkbox_alternate
    + ')\n'
  )
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['time_pyramid'] = function(block) {
  var number_n_exercises = block.getFieldValue('n_exercises');
  var number_bottom = block.getFieldValue('bottom');
  var number_top = block.getFieldValue('top');
  var number_off_time = block.getFieldValue('off_time');
  var checkbox_single_top = block.getFieldValue('single_top') == 'TRUE';
  var value_etypes = Blockly.Python.valueToCode(block, 'etypes', Blockly.Python.ORDER_ATOMIC);
  var value_equipment = Blockly.Python.valueToCode(block, 'equipment', Blockly.Python.ORDER_ATOMIC);
  var value_muscles = Blockly.Python.valueToCode(block, 'muscles', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  if (checkbox_single_top) {
    checkbox_single_top = 'True'
  } else {
    checkbox_single_top = 'False'
  }
  var code = (
    'pyramid = TimePyramid(n_exercises='
    + number_n_exercises
    + ', bottom='
    + number_bottom
    + ', top='
    + number_top
    + ', off_time='
    + number_off_time
    + ', single_top='
    + checkbox_single_top
    + ')\n'
    + 'wout += pyramid.init(etypes='
    + value_etypes
    + ', equipment='
    + value_equipment
    + ', muscles='
    + value_muscles
    + ')\n'
  )
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['total_random'] = function(block) {
  var number_n_exercises = block.getFieldValue('n_exercises');
  var number_on_low = block.getFieldValue('on_low');
  var number_on_high = block.getFieldValue('on_high');
  var number_off_low = block.getFieldValue('off_low');
  var number_off_high = block.getFieldValue('off_high');
  var number_on_probability = block.getFieldValue('on_probability');
  var value_etypes = Blockly.Python.valueToCode(block, 'etypes', Blockly.Python.ORDER_ATOMIC);
  var value_equipment = Blockly.Python.valueToCode(block, 'equipment', Blockly.Python.ORDER_ATOMIC);
  var value_muscles = Blockly.Python.valueToCode(block, 'muscles', Blockly.Python.ORDER_ATOMIC);
  var on_probability = number_on_probability / 100
  var code = (
    'tot_rand = TotalRandom(n_exercises='
    + number_n_exercises
    + ', on_range='
    + '(' + number_on_low + ',' + number_on_high + ')'
    + ', off_range='
    + '(' + number_off_low + ',' + number_off_high + ')'
    + ', on_prob='
    + on_probability
    + ')\n'
    + 'wout += tot_rand.init(etypes='
    + value_etypes
    + ', equipment='
    + value_equipment
    + ', muscles='
    + value_muscles
    + ')\n'
  )
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['rest'] = function(block) {
  var number_on_time = block.getFieldValue('on_time');
  var code = 'wout += ([' + 'Rest(' + number_on_time + ')])';
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['chest'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Chest"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['middle_back'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"MiddleBack"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['forearms'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Forearms"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['lats'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Lats"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['lower_back'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"LowerBack"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['neck'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Neck"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['quadriceps'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Quadriceps"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['hamstrings'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Hamstrings"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['calves'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Calves"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['triceps'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Triceps"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['traps'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Traps"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['shoulders'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Shoulders"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['abdominals'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Abdominals"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['glutes'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Glutes"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['biceps'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Biceps"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['adductors'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Adductors"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['abductors'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Abductors"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['body_weight'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = 'None';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['dumbbell'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"dumbbell"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['band'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"band"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['kettlebell'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"kettlebell"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['strength'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"strength"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['cardio'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"cardio"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['connect_workouts'] = function(block) {
  var value_workouts = Blockly.Python.valueToCode(block, 'workouts', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var last_line = 'wout'
  var value_workouts_clean = value_workouts.substring(1, value_workouts.length - 1).replace(/\.init\(/g, ".init(exclude_exercises=exclude, ").replace(/\n, /g, "\nexclude=list(set([ex.__class__ for ex in wout]))\n").replace(/\)\]\), /g, ")])\n");
  var code = 'wout = []\n' + 'exclude = []\n' + value_workouts_clean + last_line;
  return code;
};