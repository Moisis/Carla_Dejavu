import carla
import time
client = carla.Client('172.17.0.1', 2000)
client.set_timeout(2.0)


def draw_waypoints(waypoints, road_id=None, life_time=50.0):

  for waypoint in waypoints:

    if(waypoint.road_id == road_id):
      client.get_world().debug.draw_string(waypoint.transform.location, 'O00000', draw_shadow=False,
                                   color=carla.Color(r=255, g=0, b=0), life_time=life_time,
                                   persistent_lines=True)
      time.sleep(0.5)
                                   
waypoints = client.get_world().get_map().generate_waypoints(distance=1.0)
# waypoints = client.get_world().get_map().get_spawn_points()
# for i in range (30):
#     print(i)
#     draw_waypoints(waypoints, road_id=i, life_time=1)
#     time.sleep(1.0)

draw_waypoints(waypoints, road_id=13, life_time=0.5)

  