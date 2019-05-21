import pytest
from com.stondo.solution_class import Solution, Best


# Constants
LINK_STATIONS = [[0, 0, 10],
        [20, 20, 5],
        [10, 0, 12]]

P1, P2, P3, P4 = (0, 0), (100, 100), (15, 10), (18, 18)

POINTS = [P1, P2, P3, P4]

BEST_EXPECTED_1 = Best(0, 0, 100.0, 0, 0)
BEST_EXPECTED_2 = Best(None, None, 0, 100, 100)
BEST_EXPECTED_3 = Best(10, 0, 0.6718427000252355, 15, 10)
BEST_EXPECTED_4 = Best(20, 20, 4.715728752538098, 18, 18)


# Fxtures
@pytest.fixture
def solution():
  return Solution(LINK_STATIONS, POINTS)


# Helpers
def verify_solution(expected, found):
  assert expected == found


# Test Cases
def test_find_best_station_for_device_at(solution):
  result_1 = solution.find_best_station_for_device_at(P1)
  result_2 = solution.find_best_station_for_device_at(P2)
  result_3 = solution.find_best_station_for_device_at(P3)
  result_4 = solution.find_best_station_for_device_at(P4)

  verify_solution(BEST_EXPECTED_1, result_1)
  verify_solution(BEST_EXPECTED_2, result_2)
  verify_solution(BEST_EXPECTED_3, result_3)
  verify_solution(BEST_EXPECTED_4, result_4)
