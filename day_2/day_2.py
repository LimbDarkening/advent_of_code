
# Problem 1
readings = []
with open ("input.txt") as file:
        for line in file:
                reading = line.split()
                readings.append(reading)

def valid(reading:list[int])->bool:
	monitonic_flag = 0
	for i, r in enumerate(reading[:-1]):
		dif = int(reading[i+1]) - int(reading[i])
		if dif == 0:
			return False
		if monitonic_flag == 0:
			monitonic_flag = 1 if dif > 0 else 0
		else:
			implied_flag = 1 if dif > 0 else 0
			if implied_flag != monitonic_flag:
				return False
			if dif >3:
				return False
	return True

print(sum([valid(r) for r in readings]))
