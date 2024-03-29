Blockly.Blocks['exox'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("EXOX");
    this.appendDummyInput()
        .appendField("n_exercises:")
        .appendField(new Blockly.FieldNumber(4, 0), "n_exercises");
    this.appendDummyInput()
        .appendField("rounds:")
        .appendField(new Blockly.FieldNumber(3, 0), "rounds");
    this.appendDummyInput()
        .appendField("difficulty:")
        .appendField(new Blockly.FieldNumber(75, 0, 100), "difficulty");
    this.appendDummyInput()
        .appendField("interval:")
        .appendField(new Blockly.FieldNumber(60, 0), "interval");
    this.appendValueInput("etypes")
        .setCheck("Array")
        .appendField("etypes");
    this.appendValueInput("equipment")
        .setCheck("Array")
        .appendField("equipment");
    this.appendValueInput("muscles")
        .setCheck("Array")
        .appendField("muscles");
    this.setOutput(true, "workout");
    this.setColour(30);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['tabata'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Tabata");
    this.appendDummyInput()
        .appendField("n_exercises:")
        .appendField(new Blockly.FieldNumber(4, 0), "n_exercises");
    this.appendDummyInput()
        .appendField("rounds:")
        .appendField(new Blockly.FieldNumber(3, 0), "rounds");
    this.appendDummyInput()
        .appendField("on_time:")
        .appendField(new Blockly.FieldNumber(20, 0), "on_time");
    this.appendDummyInput()
        .appendField("off_time:")
        .appendField(new Blockly.FieldNumber(10, 0), "off_time");
    this.appendDummyInput()
        .appendField("round_rest:")
        .appendField(new Blockly.FieldNumber(10, 0), "round_rest"); 
    this.appendDummyInput()
        .appendField("alternate:")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "alternate");   
    this.appendValueInput("etypes")
        .setCheck("Array")
        .appendField("etypes");
    this.appendValueInput("equipment")
        .setCheck("Array")
        .appendField("equipment");
    this.appendValueInput("muscles")
        .setCheck("Array")
        .appendField("muscles");
    this.setOutput(true, "workout");
    this.setColour(30);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['drop_set'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Drop Set");
    this.appendDummyInput()
        .appendField("n_exercises:")
        .appendField(new Blockly.FieldNumber(4, 0), "n_exercises");
    this.appendDummyInput()
        .appendField("on_time:")
        .appendField(new Blockly.FieldNumber(30, 0), "on_time");
    this.appendDummyInput()
        .appendField("off_time:")
        .appendField(new Blockly.FieldNumber(0, 0), "off_time");
    this.appendDummyInput()
        .appendField("round_rest:")
        .appendField(new Blockly.FieldNumber(10, 0), "round_rest");    
    this.appendValueInput("etypes")
        .setCheck("Array")
        .appendField("etypes");
    this.appendValueInput("equipment")
        .setCheck("Array")
        .appendField("equipment");
    this.appendValueInput("muscles")
        .setCheck("Array")
        .appendField("muscles");
    this.setOutput(true, "workout");
    this.setColour(30);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['timed_workout'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Timed Workout");
    this.appendDummyInput()
        .appendField("n_exercises:")
        .appendField(new Blockly.FieldNumber(4, 0), "n_exercises");
    this.appendDummyInput()
        .appendField("rounds:")
        .appendField(new Blockly.FieldNumber(3, 0), "rounds");
    this.appendDummyInput()
        .appendField("on_time:")
        .appendField(new Blockly.FieldNumber(20, 0), "on_time");
    this.appendDummyInput()
        .appendField("off_time:")
        .appendField(new Blockly.FieldNumber(10, 0), "off_time");
    this.appendDummyInput()
        .appendField("round_rest:")
        .appendField(new Blockly.FieldNumber(10, 0), "round_rest");
    this.appendDummyInput()
        .appendField("alternate:")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "alternate");    
    this.appendValueInput("etypes")
        .setCheck("Array")
        .appendField("etypes");
    this.appendValueInput("equipment")
        .setCheck("Array")
        .appendField("equipment");
    this.appendValueInput("muscles")
        .setCheck("Array")
        .appendField("muscles");
    this.setOutput(true, "workout");
    this.setColour(30);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['time_pyramid'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Time Pyramid");
    this.appendDummyInput()
        .appendField("bottom:")
        .appendField(new Blockly.FieldNumber(20, 0), "bottom");
    this.appendDummyInput()
        .appendField("top:")
        .appendField(new Blockly.FieldNumber(60, 0), "top");
    this.appendDummyInput()
        .appendField("off_time:")
        .appendField(new Blockly.FieldNumber(10, 0), "off_time");
    this.appendDummyInput()
        .appendField("n_exercises:")
        .appendField(new Blockly.FieldNumber(5, 0), "n_exercises"); 
    this.appendDummyInput()
        .appendField("single_top:")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "single_top");     
    this.appendValueInput("etypes")
        .setCheck("Array")
        .appendField("etypes");
    this.appendValueInput("equipment")
        .setCheck("Array")
        .appendField("equipment");
    this.appendValueInput("muscles")
        .setCheck("Array")
        .appendField("muscles");
    this.setOutput(true, "workout");
    this.setColour(30);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['total_random'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Total Random");
    this.appendDummyInput()
        .appendField("on_time - low:")
        .appendField(new Blockly.FieldNumber(20, 0), "on_low")
        .appendField("high:")
        .appendField(new Blockly.FieldNumber(60, 0), "on_high");
    this.appendDummyInput()
        .appendField("off_time - low:")
        .appendField(new Blockly.FieldNumber(5, 0), "off_low")
        .appendField("high:")
        .appendField(new Blockly.FieldNumber(20, 0), "off_high");
    this.appendDummyInput()
        .appendField("on_probability:")
        .appendField(new Blockly.FieldNumber(75, 0, 100), "on_probability");
    this.appendDummyInput()
        .appendField("n_exercises:")
        .appendField(new Blockly.FieldNumber(35, 0), "n_exercises");
    this.appendValueInput("etypes")
        .setCheck("Array")
        .appendField("etypes");
    this.appendValueInput("equipment")
        .setCheck("Array")
        .appendField("equipment");
    this.appendValueInput("muscles")
        .setCheck("Array")
        .appendField("muscles");
    this.setOutput(true, "workout");
    this.setColour(30);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['rest'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Rest");
    this.appendDummyInput()
        .appendField("on_time")
        .appendField(new Blockly.FieldNumber(10, 0), "on_time");
    this.setOutput(true, "workout");
    this.setColour(30);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['chest'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("chest");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['middle_back'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("middle back");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['forearms'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("forearms");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['lats'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("lats");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['lower_back'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("lower back");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['neck'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("neck");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['quadriceps'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("quadriceps");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['hamstrings'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("hamstrings");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['calves'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("calves");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['triceps'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("triceps");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['traps'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("traps");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['shoulders'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("shoulders");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['abdominals'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("abdominals");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['glutes'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("glutes");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['biceps'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("biceps");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['adductors'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("adductors");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['abductors'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("abductors");
    this.setOutput(true, "muscle");
    this.setColour(90);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['body_weight'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("body_weight");
    this.setOutput(true, "equipment");
    this.setColour(10);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['dumbbell'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("dumbbell");
    this.setOutput(true, "equipment");
    this.setColour(10);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['band'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("band");
    this.setOutput(true, "equipment");
    this.setColour(10);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['kettlebell'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("kettlebell");
    this.setOutput(true, "equipment");
    this.setColour(10);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['strength'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("strength");
    this.setOutput(true, "etype");
    this.setColour(270);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['cardio'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("cardio");
    this.setOutput(true, "etype");
    this.setColour(270);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['connect_workouts'] = {
  init: function() {
    this.appendValueInput("workouts")
        .setCheck("Array")
        .appendField("workouts");
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};