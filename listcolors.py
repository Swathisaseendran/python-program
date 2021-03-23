#create a list of colors from comma-separated color names entered by user.Display first and last colors.

color=input("Enter the colors seperated by commas")
print("The first color is",color.split(",")[0])
print("The last color is",color.split(",")[-1])
