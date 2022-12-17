import os
import re


def read_input():
    dir = os.path.dirname(__file__)
    lines = open(dir + '\input.txt', 'r').read().split('\n')
    lines = [tuple(map(int, re.findall('[xy]=(-*\d+)', line))) for line in lines]
    return lines


def manhattan_distance(x1, y1, x2, y2) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def sensor_perimiter(sensor, distance, coord) -> set:
    sensor_x, sensor_y, _, _ = [*sensor]
    x = list(range(sensor_x - distance - 1, sensor_x + distance + 2)) + \
            list(range(sensor_x + distance, sensor_x - distance - 1, -1))

    y = list(range(sensor_y, sensor_y - (distance + 2), -1)) + \
            list(range(sensor_y - distance, sensor_y + distance + 1)) + \
                list(range(sensor_y + distance + 1, sensor_y, -1))

    # perimiter = set(zip(x, y))
    return set([point for point in zip(x, y) if point_in_range(point, coord)])


def point_in_range(point: set, max_coord: int) -> bool:
    x, y = [*point]
    return all([x >= 0, x < max_coord, y >= 0, y < max_coord])


if __name__ == '__main__':
    SENSORS = read_input()
    SENSORS = {sensor: manhattan_distance(*sensor) for sensor in SENSORS}

    TARGET_ROW = 2000000
    COVERED_POSITIONS = set()

    
    for sensor in SENSORS:
        distance_to_beacon = SENSORS[sensor]
        sensor_x, sensor_y, beacon_x, beacon_y = [*sensor]

        if TARGET_ROW in range(sensor_y - distance_to_beacon, sensor_y + distance_to_beacon):
            distance_to_row = abs(sensor_y - TARGET_ROW)
            target_row_coverage = distance_to_row * 2 + 1 - abs(2 * distance_to_beacon)
            x_coverage_start = sensor_x - (target_row_coverage - 1) // 2
            x_coverage_end = sensor_x + (target_row_coverage - 1) // 2
            COVERED_POSITIONS.add(x_coverage_start)
            COVERED_POSITIONS.add(x_coverage_end)

    distress_beacon = None
    for sensor in SENSORS:
        perimiter = sensor_perimiter(sensor, distance_to_beacon, 2 * TARGET_ROW)

        for point in perimiter:
            for s in SENSORS:
                d = manhattan_distance(*point, *s[:2]) 
                if d <= SENSORS[s]:    
                    beacon = None
                    break
                beacon = point

            if beacon is not None:
                distress_beacon = beacon
                break

    print(max(COVERED_POSITIONS) - min(COVERED_POSITIONS)) #part 1
    print(distress_beacon[0] * 4000000 + distress_beacon[1]) #part 2
