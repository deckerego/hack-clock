goog.provide('Blockly.Python.display');

goog.require('Blockly.Python');

Blockly.Python['led_display'] = function(block) {
  Blockly.Python.definitions_['import_display'] = 'from Libs.SevenSegment import Display';
  Blockly.Python.definitions_['init_display'] = 'display = Display()';
  return ['display', Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['set_display_minutes'] = function(block) {
  var number_minutes = block.getFieldValue('minutes');
  var value_display = Blockly.Python.valueToCode(block, 'display', Blockly.Python.ORDER_ATOMIC);
  return ''+value_display+'.setMinutes('+number_minutes+');\n';
};

Blockly.Python['set_display_hours'] = function(block) {
  var number_hours = block.getFieldValue('hours');
  var value_display = Blockly.Python.valueToCode(block, 'display', Blockly.Python.ORDER_ATOMIC);
  return ''+value_display+'.setHours('+number_hours+');\n';
};

Blockly.Python['set_colon'] = function(block) {
  var checkbox_enabled = block.getFieldValue('enabled') == 'TRUE';
  var value_display = Blockly.Python.valueToCode(block, 'display', Blockly.Python.ORDER_ATOMIC);
  return ''+value_display+'.setColon('+checkbox_enabled+');\n';
};

Blockly.Python['is_evening'] = function(block) {
  var checkbox_enabled = block.getFieldValue('enabled') == 'TRUE';
  var value_display = Blockly.Python.valueToCode(block, 'display', Blockly.Python.ORDER_ATOMIC);
  return ''+value_display+'.setEvening('+checkbox_enabled+');\n';
};

Blockly.Python['set_display_brightness'] = function(block) {
  var option_brightness = block.getFieldValue('brightness');
  var value_display = Blockly.Python.valueToCode(block, 'display', Blockly.Python.ORDER_ATOMIC);
  return ''+value_display+'.setBrightness('+option_brightness+');\n';
};
