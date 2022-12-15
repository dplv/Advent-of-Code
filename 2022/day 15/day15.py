import os
import re


def read_input():
    dir = os.path.dirname(__file__)
    lines = open(dir + '\input.txt', 'r').read().split('\n')
    lines = [list(map(int, re.findall('[xy]=(-*\d+)', line))) for line in lines]
    return lines


def manhattan_distance(x1, y1, x2, y2) -> int:
    return abs(x1 - x2) + abs(y1 - y2)

if __name__ == '__main__':
    sensors = read_input()

    TARGET_ROW = 2000000
    COVERED_POSITIONS = set()

    for sensor in sensors:
        distance_to_beacon = manhattan_distance(*sensor)
        sensor_x, sensor_y, beacon_x, beacon_y = [*sensor]

        if TARGET_ROW in range(sensor_y - distance_to_beacon, sensor_y + distance_to_beacon):
            distance_to_row = abs(sensor_y - TARGET_ROW)
            target_row_coverage = distance_to_row * 2 + 1 - abs(2 * distance_to_beacon)
            x_coverage_start = sensor_x - (target_row_coverage - 1) // 2
            x_coverage_end = sensor_x + (target_row_coverage - 1) // 2
            COVERED_POSITIONS.add(x_coverage_start)
            COVERED_POSITIONS.add(x_coverage_end)

    print(max(COVERED_POSITIONS) - min(COVERED_POSITIONS)) #part 1