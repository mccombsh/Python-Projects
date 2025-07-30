import PIL.Image

width = 1000
height = 1000

image = PIL.Image.new("HSV", (width, height))

max_iteration = 360

for i in range(height):
    for j in range(width):
        x = (j / width) * 3.0 - 1.5
        y = (i / height) * 3.0 - 1.5

        c_real = -0.7
        c_imag = 0.26015
        iteration = 0
        while x*x + y*y < 4 and iteration < max_iteration:
            tempx = x*x - y*y + c_real
            y = 2*x*y + c_imag
            x = tempx
            iteration += 1

        if iteration == max_iteration:
            #print(f"Set pixel at ({j}, {i}) to black")
            image.putpixel((j, i), (0, 0, 0))
        else:
            #print(f"Set pixel at ({j}, {i}) to not black")
            image.putpixel((j, i), (iteration, 255, 255))

rgb_image = image.convert("RGB")
rgb_image.save("julia.png")
