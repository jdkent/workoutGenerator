Blockly.Python['chest'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '"Chest"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['exox'] = function(block) {
  var text_wout_name = block.getFieldValue('wout_name');
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
  return [code, Blockly.Python.ORDER_ATOMIC];;
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
  var value_workouts_clean = value_workouts.substring(1, value_workouts.length - 1).replace(/\.init\(/g, ".init(exclude_exercises=exclude, ").replace(/\n, /g, "\nwout += wout\nexclude=list(set([ex.__class__ for ex in wout]))\n");
  var code = 'wout = []\n' + 'exclude = []\n' + value_workouts_clean + last_line;
  return code;
};