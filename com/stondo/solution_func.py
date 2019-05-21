"""
solution_func.py contains functions with no side effects.
"""

from math import sqrt

SUCCESS_MSG = 'Best link station for point {},{} is {},{} with power {}'
FAILURE_MSG = 'No link station within reach for point {},{}'

def distance(device, ls):
  return sqrt(pow(ls[0] - device[0], 2) + pow(ls[1] - device[1], 2))

def get_ls_power_at(reach, device_distance):
  return pow(reach - device_distance, 2)

def is_better(best_power, power):
  return power > best_power

def build_message(best):
  if best.power > 0:
    return SUCCESS_MSG.format(best.pointx, best.pointy, best.lsx, best.lsy, best.power)

  return FAILURE_MSG.format(best.pointx, best.pointy)
