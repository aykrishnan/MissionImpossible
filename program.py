# MissionImpossible

def main():
	game_header()
	game_loop()
	game_over()


def game_header():
	print("..........Mission Impossible..........")

def game_loop():
	print("'After the kidnapping took place last night...the only objective is to rescue your son'")

	action = input("Do you chooose to walk[w] or Hijack[h] a car: ")
	if action == 'w':
		print("you've choosen to walk..")

	if action == 'h':
		print("You chose to hijack an innocent pedestrian")



def game_over():
	print("Game over")


if __name__ == '__main__':
	main()

