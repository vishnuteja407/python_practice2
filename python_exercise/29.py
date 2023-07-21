# import ephem

# mars = ephem.Mars()

# mars.compute("2023/1/1")

# print(mars.dec)

# jupiter = ephem.Jupiter()
# jupiter.compute('1230/1/1')
# distance_au_units = jupiter.sun_distance
# distance_km = distance_au_units * 149597870.691
# print(distance_km)


from screeninfo import get_monitors
for m in get_monitors():
    print(f"width: {m.width}, Height: {m.height}")


from screeninfo import get_monitors
    
width=get_monitors()[0].width
height=get_monitors()[0].height
    
print("Width: %s,  Height: %s" % (width, height))