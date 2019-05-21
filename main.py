from com.stondo.solution_class import Solution

def main():
  link_stations = [[0, 0, 10],
          [20, 20, 5],
          [10, 0, 12]]

  points = [(0, 0), (100, 100), (15, 10), (18, 18)]

  solution = Solution(link_stations, points)
  solution.find_all()

main()
