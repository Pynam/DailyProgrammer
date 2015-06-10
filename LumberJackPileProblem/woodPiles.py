data = [int(n) for n in open("data.txt").read().split()]

n, to_place = data[0], data[1] 
piles = data[2:]

# print(n)
# print(to_place)
# print(piles)
smallest = min(piles)

while to_place > 0:
	for index, pile in enumerate(piles):
		if pile == smallest:
			piles[index] += 1
			to_place -= 1
			if to_place == 0:
				break

	smallest += 1

for i in range(0, n*n, n):
	print(*piles[i:i+n])
