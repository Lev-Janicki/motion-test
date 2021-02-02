while True:
    if input.acceleration(Dimension.X + Dimension.Y + Dimension.Z) > 10:
        light.set_all(color.rgb(255,255,0))
    else:
        light.clear()
