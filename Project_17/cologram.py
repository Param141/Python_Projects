import colorgram

colors = colorgram.extract('image.jpg', 6)  # Extract 6 colors from the image in the form of a list of Color objects

rgb_colors = []
for color in colors:
    rgb = color.rgb # it gives an object of type Rgb with attributes r, g, b e.g., Rgb(r=245, g=245, b=220) 
    rgb_colors.append((rgb.r, rgb.g, rgb.b))

    # or can have used rgb_colors.append(color.rgb) directly but this would print the  output as : Rgb(r=245, g=245, b=220) form
    # so we are using the above method to get the output in the form of a tuple (r, g, b)

    # or write as r=color.rgb.r, g=color.rgb.g, b=color.rgb.b then new_color = (r, g, b) to form tuple and then rgb_colors.append(new_color)

print(rgb_colors)