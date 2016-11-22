#!/usr/bin/env python
#coding:utf-8
# license removed for brevity
import threading
import time

class Timer(threading.Thread):
    """
    very simple but useless timer.
    """
    def __init__(self, seconds):
        threading.Thread.__init__(self)
        self.runTime = seconds


    def run(self):
        time.sleep(self.runTime)
        print "Buzzzz!! Time's up!"



class CountDownTimer(Timer):
    """
    a timer that can counts down the seconds.
    """
    def run(self):
        counter = self.runTime
        for sec in range(self.runTime):
            print counter
            time.sleep(1.0)
            counter -= 1
        print "Done"
        Timer.run(self)


class CountDownExec(CountDownTimer):
    """
    a timer that execute an action at the end of the timer run.
    """
    def __init__(self, seconds, action, args=[]):
        self.args = args
        self.action = action
        CountDownTimer.__init__(self, seconds)
    def run(self):
        CountDownTimer.run(self)
        self.action(self.args)


def myAction(args=[]):
    print "Performing my action with args:"
    print args


if __name__ == "__main__":
    t = CountDownExec(3, myAction, ["hello", "world"])
    t.start()
