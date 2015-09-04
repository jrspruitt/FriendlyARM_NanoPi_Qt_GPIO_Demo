##PyQt Demo app for [pyfa_gpio](https://github.com/jrspruitt/pyfa_gpio)

Built for Qt 4.8

###Install###
 * Copy run_demo.py and demo_ui.py to target device.
 * Install [pyfa_gpio](https://github.com/jrspruitt/pyfa_gpio)
     * Will need to change imports if not installed to system.

###Run###

    ./run_demo.py -qws

Tabs for LEDs/Buttons, Dimmer and Servo.

###Hardware Hook Up###

**Caution:** Don't hook LEDs up directly, use a transistor. Take proper care on all pin connections.

The PWM outputs share the prescaler value, when switching tabs between Dimmer and Servo, the deselected one will stop.

Buttons should pull the line high.

LEDs should trigger on line high.

**Pin out:**

 * led1: 11
 * led2: 13
 * button1: 29
 * button2: 15
 * dimmer: 22
 * servo: 26


**TODO**

Schematic
