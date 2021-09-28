







[체험기](https://jetsonaicar.tistory.com/26)

[출처](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#obstacle-detection)

​    

## [Obstacle Detection](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#obstacle-detection)

The TurtleBot3 can be moved or stopped by LDS data. When the TurtleBot3 moves, it stops when it detects an obstacle ahead.

**[Remote PC]** Launch the obstacle file.

```
$ roslaunch turtlebot3_example turtlebot3_obstacle.launch
```

구동중에 장애물 탐지

​    

## [Position Control](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#position-control)

**NOTE**: This feature is available for Dashing.

## [Point Operation](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#point-operation)

The TurtleBot3 can be moved by 2D `point (x, y)` and `z-angular`. For example, if you insert (0.5, 0.3, 60), TurtleBot3 moves to point (x = 0.5m, y = 0.3m) and then rotates 60 deg.

**[Remote PC]** launch the pointop file.

```
$ roslaunch turtlebot3_example turtlebot3_pointop_key.launch
```

(x, y) 좌표로 이동시키는 방법 (외 1자율주행, 2다중키 원격제어 방식 등이 있다.)

​    

## [Patrol](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#patrol)

The TurtleBot3 can be moved by custom routes. There are three routes(rectangle, triangle and circle). This example uses action topic. Action client translates patrol data(mode, area, count) to action server. And then action server translates `cmd_vel` to TurtleBot3. Please refer to the above [tutorial video](https://youtu.be/Xg1pKFQY5p4) for more detailed usage.

**[Remote PC]** Launch the patrol server file.

```
$ rosrun turtlebot3_example turtlebot3_server
```

**[Remote PC]** Launch the patrol client file.

```
$ roslaunch turtlebot3_example turtlebot3_client.launch
```