import os
import sys

def main():
	for n in os.listdir():
		if n!=sys.argv[0]:
			if os.path.isdir(n):
				os.rmdir(n)
			else:
				os.remove(n)

if __name__=="__main__":
	main()