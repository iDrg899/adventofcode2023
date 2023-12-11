time = 49979494
record = 263153213781851

# The following numbers were attained in Desmos
parth = 5980000
jain = 44000000
# These are approximately the roots of the parabola
# y = (49979494 - x)x - 263153213781851

while (time - parth) * parth <= record:
    parth += 1

while (time - jain) * jain <= record:
    jain -= 1

print(jain - parth + 1)



# Also, note that 2|√(b² - 4ac) / 2a| would be the answer
# y = -x² + 49979494x - 263153213781851
# 2|√(b² - 4ac) / 2a| = √(b² + 4c)
#                     = √(time² + 4·record)