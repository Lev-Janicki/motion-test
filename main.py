while True:
    print(input.acceleration(Dimension.X))
    if input.acceleration(Dimension.X) > 50:
        light.set_all(color.rgb(255,0,255))
    else:
        light.clear()
