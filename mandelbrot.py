import PIL.Image

width = 4000
height = 4000

image = PIL.Image.new("HSV", (width, height))

x0 = 0
y0 = 0

max_iteration = 360

# iteration based load balancing, each node gets a few thousand iterations and handles a few pixels

for i in range(height):
    for j in range(width):
        x0 = (j / width) * 3.0 - 2.5
        y0 = (i / height) * 2 - 1

        x = 0
        y = 0
        iteration = 0
        while x*x + y*y < 4 and iteration < max_iteration:
            tempx = x*x - y*y + x0
            y = 2*x*y + y0
            x = tempx
            iteration += 1

        if iteration == max_iteration:
            #print(f"Set pixel at ({j}, {i}) to black")
            image.putpixel((j, i), (0, 0, 0))
        else:
            #print(f"Set pixel at ({j}, {i}) to not black")
            image.putpixel((j, i), (iteration, 255, 255))

rgb_image = image.convert("RGB")
rgb_image.save("mandelbrot.png")
