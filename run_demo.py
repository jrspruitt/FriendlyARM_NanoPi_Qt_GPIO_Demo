#!/usr/bin/env python
#############################################################################
# The MIT License (MIT)
# 
# Copyright (c) 2015 Jason Pruitt
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#############################################################################

import sys
import threading
from time import sleep

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from demo_ui import Ui_MainWindow

from fgpio import GPIO
from fgpio.boards.nanopi import Config


class Demo(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(QApplication.desktop().availableGeometry())
        self.setFixedSize(320, 240)
        self.setupUi(self)
        self._init_events()
        self._g = GPIO(Config())
        self._init_buttons()
        self._init_leds()
        self._pin_servo = 26
        self._servo_dc = 50
        self._pin_dimmer = 22
        self._dimmer_dc = 50
        self._g.pwm_init(self._pin_servo, 20000000, 1500000)
        self._g.pwm_init(self._pin_dimmer, 1000000, 500000)

    def _exit(self):
        self._close_servo()
        self._close_dimmer()
        self._close_leds()
        self._close_buttons()
        exit()

    def _init_events(self):
        self.tab_demo.currentChanged.connect(self._tab_changer)
        self.btn_exit.clicked.connect(self._exit)
        self.dial_servo.valueChanged.connect(self._servo_dial)
        self.dial_dimmer.valueChanged.connect(self._dimmer_dial)
        self.rbox_1.clicked.connect(self._rbox1_handler)
        self.rbox_2.clicked.connect(self._rbox2_handler)
        self.rbox_3.clicked.connect(self._rbox3_handler)

    def _tab_changer(self, index):
        if index == 0:
            pass
        elif index == 1:
            self._g.pwm_stop(self._pin_servo)
            self._init_dimmer()
            self.dial_dimmer.setValue(self._dimmer_dc)

        elif index == 2:
            self._g.pwm_stop(self._pin_dimmer)
            # See above comment about setting period in ns.
            self._init_servo()
            self.dial_servo.setValue(self._servo_dc)

    def _init_leds(self):
        self._toggling = False
        self._l1 = 11
        self._l2 = 13
        self._g.gpio_init(self._l1, 'out')
        self._g.gpio_init(self._l2, 'out')
        self._g.gpio_write(self._l1, 1)

    def _rbox1_handler(self):
        self._toggling = False
        self._g.gpio_write(self._l2, 0)
        self._g.gpio_write(self._l1, 1)

    def _rbox2_handler(self):
        self._toggling = False
        self._g.gpio_write(self._l1, 0)
        self._g.gpio_write(self._l2, 1)

    def _rbox3_handler(self):
        self._toggling = True
        r3 = threading.Thread(target=self._led_toggler)
        r3.daemon = True
        r3.start()

    def _led_toggler(self):
        led = False
        while self._toggling:
            led = not led
            if led :
                self._g.gpio_write(self._l1, 0)
                self._g.gpio_write(self._l2, 1)
            else:
                self._g.gpio_write(self._l2, 0)
                self._g.gpio_write(self._l1, 1)
            sleep(1)

    def _close_leds(self):
        self._toggling = False
        sleep(.2)
        self._g.gpio_close(self._l1)
        self._g.gpio_close(self._l2)

    def _init_buttons(self):
        self._button_running = True
        b1 = threading.Thread(target=self._button_press, args=(29, self.lbl_btn_1))
        b1.daemon = True
        b1.start()
        b2 = threading.Thread(target=self._button_press, args=(15, self.lbl_btn_2))
        b2.daemon = True
        b2.start()

    def _button_press(self, pin, btn):
        self._g.eint_init(pin, 'high')
        btn_on = False

        while self._button_running:
            if self._g.eint_event(pin):
                self._g.eint_clear(pin)
                if not btn_on:
                    btn.setText('ON')
                    btn_on = True
            else:
                if btn_on:
                    btn.setText('OFF')
                    btn_on = False
            sleep(.05)

        self._g.eint_close(pin)

    def _close_buttons(self):
        self._button_running = False
        sleep(.2)

    def _init_dimmer(self):
        self.dial_dimmer.setEnabled(True)
        self._g.pwm_period(self._pin_dimmer, 1000000)
        self._g.pwm_start(self._pin_dimmer)

    def _close_dimmer(self):
        self.dial_dimmer.setEnabled(False)
        try:
            self._g.pwm_close(self._pin_dimmer)
        except:
            pass

    def _dimmer_dial(self, value):
        base_dc = 0
        max_dc  = 1000000
        new_dc = base_dc + (value*10000)

        if new_dc > max_dc:
            new_dc = max_dc

        self._dimmer_dc = value
        self._g.pwm_duty_cycle(self._pin_dimmer, new_dc)

    def _init_servo(self):
        self.dial_servo.setEnabled(True)
        self._g.pwm_period(self._pin_servo, 20000000)
        self._g.pwm_start(self._pin_servo)

    def _close_servo(self):
        self.dial_servo.setEnabled(False)
        try:
            self._g.pwm_close(self._pin_servo)
        except:
            pass

    def _servo_dial(self, value):
        base_dc = 1000000
        max_dc  = 2000000
        new_dc = base_dc + (value*(base_dc/100))

        if new_dc > max_dc:
            new_dc = max_dc

        self._servo_dc = value
        self._g.pwm_duty_cycle(self._pin_servo, new_dc)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    d = Demo()
    d.show()
    sys.exit(app.exec_())

