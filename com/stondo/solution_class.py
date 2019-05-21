"""
solution_class.py contains the Solution class.
It uses the functions from solution_func to solve the problem.
It uses the function from solution_side_eff to print the result.
"""

from com.stondo.solution_func import distance, get_ls_power_at, is_better
from com.stondo.solution_namedtuples import Best
from com.stondo.solution_side_eff import print_result


class Solution():
  def __init__(self, link_stations, points):
    self._link_stations = link_stations
    self._points = points

  def find_best_station_for_device_at(self, pnt):
    best = Best(None, None, 0, pnt[0], pnt[1])

    for ls in self._link_stations:
      ls_reach = ls[2]

      distance_from_ls = distance((ls[0], ls[1]), pnt)

      power = 0 if (distance_from_ls > ls_reach) else get_ls_power_at(ls_reach, distance_from_ls)

      best = Best(ls[0], ls[1], power, pnt[0], pnt[1]) if (is_better(best.power, power)) else best

    return best

  def find_all(self):
    for point in self._points:
      print_result(self.find_best_station_for_device_at(point))
