from shapely.geometry import Point, Polygon
import csv

def generate_points_within_area(vertices, step=0.0001):
    # Create a Shapely Polygon object for the specified area
    area_polygon = Polygon(vertices)

    # Find the bounding box for the area
    min_lat, min_lon = min(vertices, key=lambda x: x[0])[0], min(vertices, key=lambda x: x[1])[1]
    max_lat, max_lon = max(vertices, key=lambda x: x[0])[0], max(vertices, key=lambda x: x[1])[1]

    # Generate points within the bounding box with the specified step
    all_points = []
    current_lat = min_lat
    while current_lat <= max_lat:
        current_lon = min_lon
        while current_lon <= max_lon:
            point = Point(current_lat, current_lon)
            if point.within(area_polygon):
                all_points.append((current_lat, current_lon))
            current_lon += step
        current_lat += step

    return all_points

area_vertices = [
    (-123.2949529, 48.4586182),
    (-123.2940088, 48.4578498),
    (-123.2925497, 48.4586751),
    (-123.2935796, 48.4593582),
    (-123.2949529, 48.4586182),
]

# Adjust the step size based on your needs
step_size = 0.0001

# Generate points within the specified area
all_points_within_area = generate_points_within_area(area_vertices, step=step_size)

with open('eggs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(all_points_within_area)