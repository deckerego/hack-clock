goog.provide('Blockly.Python.weather');

goog.require('Blockly.Python');

Blockly.Python['weather_station'] = function(block) {
  Blockly.Python.definitions_['import_weather'] = 'from hackclock.runapp.Libs.Weather import Weather';
  Blockly.Python.definitions_['import_configuration'] = 'from hackclock.config import configuration';
  Blockly.Python.definitions_['init_weather'] = 'weather_station = Weather(configuration.get(\'weather_station\'))';
  return ['weather_station', Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['current_temp'] = function(block) {
  var value_weather_station = Blockly.Python.valueToCode(block, 'weather_station', Blockly.Python.ORDER_ATOMIC);
  return [value_weather_station + '.getCurrentTemp()', Blockly.Python.ORDER_ATOMIC];
};
