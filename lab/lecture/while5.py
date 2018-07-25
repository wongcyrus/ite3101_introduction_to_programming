tolerance = 1.0e-15
uncertainty = 2.0

while uncertainty > tolerance:
    uncertainty /= 2.0
    print(uncertainty)

print('Final uncertainty: ', uncertainty)
