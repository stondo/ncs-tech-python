from com.stondo.solution_func import distance, get_ls_power_at, is_better, build_message
from com.stondo.solution_namedtuples import Best

# Constants
LINK_STATION_1 = [0, 0, 10]

POINT_1 = (0, 0)
POINT_2 = (3, 4)

POWER_1 = 99.0
POWER_2 = 74.35

BEST_EXPECTED_1 = Best(0, 0, 100.0, 0, 0)
BEST_EXPECTED_2 = Best(None, None, 0, 100, 100)


# Tests
def test_distance():
  dist = distance(POINT_1, POINT_2)
  assert dist == 5.0

def test_get_ls_power_at():
  ls_pnt = (LINK_STATION_1[0], LINK_STATION_1[1])
  reach = LINK_STATION_1[2]
  dist = distance(POINT_1, ls_pnt)
  power = get_ls_power_at(reach, dist)
  assert power == 100.0

def test_is_better():
  result_1 = is_better(POWER_1, POWER_2)
  result_2 = is_better(POWER_2, POWER_1)
  assert not result_1
  assert result_2

def test_build_message():
  success_msg = build_message(BEST_EXPECTED_1) 
  failure_msg = build_message(BEST_EXPECTED_2)
  assert success_msg == 'Best link station for point 0,0 is 0,0 with power 100.0'
  assert failure_msg == 'No link station within reach for point 100,100'
