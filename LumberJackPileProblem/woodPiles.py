#First real effort at committing code every day :)

#Read datafile - read() brings in all file contents as a string - 
#split() delimits data items by space by default
data = [int(n) for n in open("data.txt").read().split()]

n, to_place = data[0], data[1] 
piles = data[2:]
smallest = min(piles)

while to_place > 0:
	for index, pile in enumerate(piles):
		#pile is a copy of the enumerated item at piles[index]		
		print(smallest)
		if pile == smallest:
			
			#Why does pile += 1 result in infinite loop?
			# - results in infinite loop because 
			# -- smallest gets incremented after
			# --- piles has been iterated through
			# ---- but changing a pile doesn't actually do anything
			# ----- to the piles list

			#pile += 1
			piles[index] += 1
			to_place -= 1
			if to_place == 0:
				break
	smallest += 1

for i in range(0, n*n, n):
	print(*piles[i:i+n])
