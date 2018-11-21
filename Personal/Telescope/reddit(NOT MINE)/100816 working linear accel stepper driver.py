import time
import RPi.GPIO as GPIO

dis = 0
dir_r = 0
time_1 = 0
time_2 = 0
acc = 500 ##step/s/s
vel_max = 1000 ##step/s
error = 0
step_time = []
tel_steps = 0
target_steps = 16000

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

step_pin = 38
dir_pin = 40
enable_pin = 36

GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(enable_pin, GPIO.OUT)

#Ensure stepper driver is enabled
GPIO.output(enable_pin, GPIO.LOW)

while tel_steps != target_steps:

    print(tel_steps)
    error = target_steps - tel_steps

    if error > 0:

        dir_r = 1 ##CW
        GPIO.output(dir_pin, GPIO.HIGH)
    else:

        dir_r = -1 ##CCW
        error = -error ##make error positive
        GPIO.output(dir_pin, GPIO.LOW)

    if error <= 10:  ##small corrections less than 10 steps

        while tel_steps != target_steps:

#           stpmtr.dir(dir_r)
            GPIO.output(step_pin, GPIO.HIGH)
            GPIO.output(step_pin, GPIO.LOW)
            time.sleep(0.1)
            tel_steps += dir_r

## If error is less that 2 * vel_max the motor will not reach full speed
## the while loop will create a step_time list of half the move length.
## the motor will accelerate for half of the move then decelerate to target.
## if error is odd the move will lose 1 step. the step will be regained the next
## pass through the loop

    elif error <= 2 * vel_max:

        dis = 0
        step_time = []
        time_1 = 0
        time_2 = 0

## create a list (step_time) of delta_t values which equal the time
## between step pulses to create a linear acceleration of the stepper motor.

        while dis < int(error / 2):

            dis += 1
            time_1 = ((2 * dis) / acc) ** 0.5
            step_time.append(time_1-time_2)
            time_2 = time_1

## send pulses to stepper motor with length of time between pulses delta_t

        for delta_t in step_time:

#                       stpmtr.dir(dir_r)
                        GPIO.output(step_pin, GPIO.HIGH)
                        GPIO.output(step_pin, GPIO.LOW)
                        time.sleep(delta_t)
                        tel_steps += dir_r

        step_time.reverse() ## reverse step_time for next loop to decelerate

        for delta_t in step_time:

#           stpmtr.dir(dir_r)
                        GPIO.output(step_pin, GPIO.HIGH)
                        GPIO.output(step_pin, GPIO.LOW)
                        time.sleep(delta_t)
                        tel_steps += dir_r


## if error > 2 * vel_max then the motor will be able to reach full speed (vel_max) and coast
## before decelerating

    elif error > 2 * vel_max:

        dis = 0
        step_time = []
        time_1 = 0
        time_2 = 0

## create list of delta_t values to accelerate to full speed

        while time_1 < vel_max / acc:

            dis += 1
            time_1 = ((2 * dis) / acc) ** 0.5
            step_time.append(time_1-time_2)
            time_2 = time_1

        for delta_t in step_time: ##accelerate motor to vel_max using step_time list

#           stpmtr.dir(dir_r)
                        GPIO.output(step_pin, GPIO.HIGH)
                        GPIO.output(step_pin, GPIO.LOW)
                        time.sleep(delta_t)
                        tel_steps += dir_r

        for _ in range(error - (2 * vel_max)):  ##coast at vel_max

#           stpmtr.dir(dir_r)
                        GPIO.output(step_pin, GPIO.HIGH)
                        GPIO.output(step_pin, GPIO.LOW)
                        time.sleep(1 / vel_max)
                        tel_steps += dir_r

        step_time.reverse()

        for delta_t in step_time:  ##decelerate using reversed list of step_time

#           stpmtr.dir(dir_r)
                        GPIO.output(step_pin, GPIO.HIGH)
                        GPIO.output(step_pin, GPIO.LOW)
                        time.sleep(delta_t)
                        tel_steps += dir_r
