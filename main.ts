while (true) {
    console.log(input.acceleration(Dimension.X))
    if (input.acceleration(Dimension.X) > 50) {
        light.setAll(color.rgb(255, 0, 255))
    } else {
        light.clear()
    }
    
}
