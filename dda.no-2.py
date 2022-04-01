def DDA(x0, y0, x1, y1):

	dx = abs(x0 - x1)
	dy = abs(y0 - y1)

	steps = max(dx, dy)

	xinc = dx/steps
	yinc = dy/steps

	x = float(x0)
	y = float(y0)

	x_coordinates = []
	y_coordinates = []

	for i in range(steps):
		x_coordinates.append(x)
		y_coordinates.append(y)

		x = x + xinc
		y = y + yinc

	plt.plot(x_coordinates, y_coordinates)
	plt.show()


if __name__ == "__main__":

	x0, y0 = 50, 50
	x1, y1 = 150, 150
	DDA(x0, y0, x1, y1)
