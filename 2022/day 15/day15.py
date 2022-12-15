import os
import re


def read_input():
    dir = os.path.dirname(__file__)
    lines = open(dir + '\input_test.txt', 'r').read().split('\n')
    lines = [list(map(int, re.findall('[xy]=(-*\d+)', line))) for line in lines]
    return lines


def manhattan_distance(x1, y1, x2, y2) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def sensor_perimiter(sensor, distance) -> set:
    sensor_x, sensor_y, _, _ = [*sensor]
    x = list(range(sensor_x - distance - 1, sensor_x + distance + 2)) + \
            list(range(sensor_x + distance, sensor_x - distance - 1, -1))

    y = list(range(sensor_y, sensor_y - (distance + 2), -1)) + \
            list(range(sensor_y - distance, sensor_y + distance + 1)) + \
                list(range(sensor_y + distance + 1, sensor_y, -1))

    return list(zip(x, y))


if __name__ == '__main__':
    sensors = read_input()

    TARGET_ROW = 10
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

        print(sensor_x, sensor_y, distance_to_beacon, sensor_perimiter(sensor, distance_to_beacon))

    print(max(COVERED_POSITIONS) - min(COVERED_POSITIONS)) #part 1