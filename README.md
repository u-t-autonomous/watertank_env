# watertank_env

## Important Information
This is a simple GUI that displays a water tank and allows you to fill or drain it by inputting values between -3 and 3
## Dependencies

* Python 3.5
* Pygame

## Documentation

### Instantiating

```python
watertank(sx, sy)
```

##### Parameters:

sx = int

sy = int

##### Returns:

An instance of watertank()

##### Usage:
```python
tank = watertank(800, 800)
```

### Move Command

```python
tank.move(num)
```

##### Parameters:

-3 <= num <= 3
##### Returns:

Int: Amount Filled

String: Gives Status - Either Full or Empty
##### Usage:
```python
P3.move(1)
```
1-3: Fill up the tank
0: Nothing happens
-3 - -1: Empty the tank


## Usage Example

```python
from Watertank import watertank
import pygame
pygame.init()
tank = watertank(800, 800)
done = False
while not done:

    x = int(input("enter a number between -3 and 3: "))
    if x > 3 or x < -3:
        done = True
    else:
        tank.fill(x)
        print (tank.water_l)
```

## Developers

* [@batman13524](https://github.com/batman13524)
* [@sahabi](https://github.com/sahabi)

