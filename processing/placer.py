from shapely import Polygon, LineString

from preparation.checks import check
from preparation.detector import find_contours_polygon_sheet

import shapely.ops as so
import matplotlib.pyplot as plt

from processing.place import place


def plot_placed_objects(placed_objects, polygon):
    print(placed_objects)
    objs = [obj for obj in placed_objects]
    new_shape = so.unary_union(objs)
    fig, axs = plt.subplots()
    axs.set_aspect('equal', 'datalim')
    if type(new_shape) == Polygon:
        xs, ys = new_shape.exterior.xy
        axs.fill(xs, ys, alpha=1, fc='g', ec='none')
    else:
        for geom in new_shape.geoms:
            if type(geom) == LineString:
                xs, ys = geom.xy
                axs.fill(xs, ys, alpha=1, fc='g', ec='none')
            else:
                xs, ys = geom.exterior.xy
                axs.fill(xs, ys, alpha=1, fc='b', ec='none')
    plt.rcParams["figure.figsize"] = [10.00, 10.00]
    plt.rcParams["figure.autolayout"] = True
    x, y = Polygon(polygon[:, 0, :]).exterior.xy
    plt.plot(x, y, c="black")
    plt.show()


def main():
    file_path = '../test_inputs/pic12.jpg'
    contours, polygon, sheet, path = find_contours_polygon_sheet(file_path)
    # placing(polygon, contours, path)
    if not check(polygon, contours):
        print("Решение не найдено")
        return

    placed_objects = place(polygon, contours)
    plot_placed_objects(placed_objects, polygon)

    if placed_objects == 0:
        print("Решение не найдено")
        return -1
    if (type(placed_objects) == int):
        print("Решение не найдено")
    else:
        return

    return

if __name__ == '__main__':
    main()
