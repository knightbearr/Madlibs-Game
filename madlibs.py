# Madblibs Games

def main():
	adj = input("Adjevtive : ")
	verb1 = input("Verb : ")
	verb2 = input("Verb : ")
	famous_person = input("Famous person : ")

	print("=" * 20)

	madlib = f"Computer programming is so {adj}."
	madlib2 = f"! It makes me feel so excited all the time because I love to {verb1}." 
	madlib3 = f"Stay hydrated and {verb2} like you are {famous_person}!"

	print(madlib, madlib2, madlib3)

if __name__ == '__main__':
	main()