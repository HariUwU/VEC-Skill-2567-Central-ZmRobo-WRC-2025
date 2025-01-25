import rcu
import math

var_flag = 0

def white():
  global var_flag
  rcu.SetMotorPower(100,78,80,100)
  if (rcu.GetTraceV2I2C(5,22) > 91):
    rcu.SetMotor(2,-20)
    rcu.SetMotor(3,100)
  else:
    if (rcu.GetTraceV2I2C(5,23) > 121):
      rcu.SetMotor(2,-60)
      rcu.SetMotor(3,100)
    else:
      if (rcu.GetTraceV2I2C(5,25) > 124):
        rcu.SetMotor(2,-100)
        rcu.SetMotor(3,60)
      else:
        if (rcu.GetTraceV2I2C(5,26) > 118):
          rcu.SetMotor(2,-100)
          rcu.SetMotor(3,20)
        else:
          if (rcu.GetTraceV2I2C(5,24) > 148):
            rcu.SetMotor(2,-100)
            rcu.SetMotor(3,100)

def black():
  global var_flag
  rcu.SetMotorPower(100,78,80,100)
  if (rcu.GetTraceV2I2C(5,22) < 63):
    rcu.SetMotor(2,-20)
    rcu.SetMotor(3,100)
  else:
    if (rcu.GetTraceV2I2C(5,23) < 47):
      rcu.SetMotor(2,-60)
      rcu.SetMotor(3,100)
    else:
      if (rcu.GetTraceV2I2C(5,25) < 46):
        rcu.SetMotor(2,-100)
        rcu.SetMotor(3,60)
      else:
        if (rcu.GetTraceV2I2C(5,26) < 56):
          rcu.SetMotor(2,-100)
          rcu.SetMotor(3,20)
        else:
          if (rcu.GetTraceV2I2C(5,24) < 66):
            rcu.SetMotor(2,-100)
            rcu.SetMotor(3,100)

def lw():
  global var_flag
  rcu.SetMotorPower(100,100,100,100)
  if ((rcu.GetTraceV2I2C(5,21) > 101) and (rcu.GetTraceV2I2C(5,22) > 104)):
    rcu.SetMotor(2,-50)
    rcu.SetMotor(3,50)
    rcu.SetWaitForTime(0.2)
    rcu.SetMotor(2,50)
    rcu.SetMotor(3,50)

def task1():
  global var_flag
  go(300)
  gowhite(8500)
  r(350)
  gowhite(3960)
  go(110)
  l(100)
  goblack(1650)
  go(250)
  mt(14500)
  back(100)
  r(100)
  goblack(7000)
  fn()

def rw():
  global var_flag
  rcu.SetMotorPower(100,100,100,100)
  if ((rcu.GetTraceV2I2C(5,26) > 115) and (rcu.GetTraceV2I2C(5,27) > 95)):
    rcu.SetMotor(2,-50)
    rcu.SetMotor(3,50)
    rcu.SetWaitForTime(0.2)
    rcu.SetMotor(2,-50)
    rcu.SetMotor(3,-50)

def lb():
  global var_flag
  rcu.SetMotorPower(100,100,100,100)
  if ((rcu.GetTraceV2I2C(5,21) < 92) and (rcu.GetTraceV2I2C(5,22) < 63)):
    rcu.SetMotor(2,-50)
    rcu.SetMotor(3,50)
    rcu.SetWaitForTime(0.2)
    rcu.SetMotor(2,30)
    rcu.SetMotor(3,50)

def fn():
  global var_flag
  gowhite(100)
  rcu.SetMotor(4,100)
  rcu.SetWaitForTime(0.3)
  rcu.SetMotor(4,0)
  rcu.SetWaitForTime(2)
  go(250)

def mt(code):
  global var_flag
  rcu.SetMotorPower(100,100,100,100)
  rcu.SetMotorCode(1)
  rcu.SetMotor(1,-100)
  var_flag = 0
  while not((var_flag > 0)):
    if ((math.fabs(rcu.GetMotorCode(1))) > code):
      var_flag = 1
  rcu.SetMotor(1,100)
  rcu.SetWaitForTime(0.02)
  rcu.SetMotor(1,0)

def gowhite(code):
  global var_flag
  rcu.SetMotorPower(100,100,100,100)
  rcu.SetMotorCode(2)
  rcu.SetMotor(2,-100)
  rcu.SetMotor(3,100)
  var_flag = 0
  while not((var_flag > 0)):
    if ((math.fabs(rcu.GetMotorCode(2))) > code):
      var_flag = 1
    lw()
    rw()
    white()
  rcu.SetMotor(2,100)
  rcu.SetMotor(3,-100)
  rcu.SetWaitForTime(0.02)
  rcu.SetMotor(2,0)
  rcu.SetMotor(3,0)

def goblack(code):
  global var_flag
  rcu.SetMotorPower(100,100,100,100)
  rcu.SetMotorCode(2)
  rcu.SetMotor(2,-100)
  rcu.SetMotor(3,100)
  var_flag = 0
  while not((var_flag > 0)):
    if ((math.fabs(rcu.GetMotorCode(2))) > code):
      var_flag = 1
    lb()
    rb()
    black()
  rcu.SetMotor(2,100)
  rcu.SetMotor(3,-100)
  rcu.SetWaitForTime(0.02)
  rcu.SetMotor(2,0)
  rcu.SetMotor(3,0)

def l(code):
  global var_flag
  rcu.SetMotorPower(100,100,100,100)
  rcu.SetMotorCode(2)
  rcu.SetMotor(2,50)
  rcu.SetMotor(3,50)
  var_flag = 0
  while not((var_flag > 0)):
    if ((math.fabs(rcu.GetMotorCode(2))) > code):
      var_flag = 1
  rcu.SetMotor(2,-50)
  rcu.SetMotor(3,-50)
  rcu.SetWaitForTime(0.02)
  rcu.SetMotor(2,0)
  rcu.SetMotor(3,0)

def rb():
  global var_flag
  rcu.SetMotorPower(100,100,100,100)
  if ((rcu.GetTraceV2I2C(5,26) < 56) and (rcu.GetTraceV2I2C(5,27) < 72)):
    rcu.SetMotor(2,-50)
    rcu.SetMotor(3,50)
    rcu.SetWaitForTime(0.2)
    rcu.SetMotor(2,-50)
    rcu.SetMotor(3,-30)

def r(code):
  global var_flag
  rcu.SetMotorPower(100,100,100,100)
  rcu.SetMotorCode(2)
  rcu.SetMotor(2,-50)
  rcu.SetMotor(3,-50)
  var_flag = 0
  while not((var_flag > 0)):
    if ((math.fabs(rcu.GetMotorCode(2))) > code):
      var_flag = 1
  rcu.SetMotor(2,50)
  rcu.SetMotor(3,50)
  rcu.SetWaitForTime(0.02)
  rcu.SetMotor(2,0)
  rcu.SetMotor(3,0)

def go(code):
  global var_flag
  rcu.SetMotorPower(100,100,100,100)
  rcu.SetMotorCode(2)
  rcu.SetMotor(2,-100)
  rcu.SetMotor(3,100)
  var_flag = 0
  while not((var_flag > 0)):
    if ((math.fabs(rcu.GetMotorCode(2))) > code):
      var_flag = 1
  rcu.SetMotor(2,100)
  rcu.SetMotor(3,-100)
  rcu.SetWaitForTime(0.02)
  rcu.SetMotor(2,0)
  rcu.SetMotor(3,0)

def back(code):
  global var_flag
  rcu.SetMotorPower(100,100,100,100)
  rcu.SetMotorCode(2)
  rcu.SetMotor(2,100)
  rcu.SetMotor(3,-100)
  var_flag = 0
  while not((var_flag > 0)):
    if ((math.fabs(rcu.GetMotorCode(2))) > code):
      var_flag = 1
  rcu.SetMotor(2,-100)
  rcu.SetMotor(3,100)
  rcu.SetWaitForTime(0.02)
  rcu.SetMotor(2,0)
  rcu.SetMotor(3,0)

task1()