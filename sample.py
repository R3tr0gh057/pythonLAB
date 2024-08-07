import pyautogui
import time

def main():
	print(f"What should I write?\n")
	data = input()
	time.sleep(2)
	pyautogui.typewrite(data)

	print(f"data: {data}, has been written")

if __name__ == "__main__":
	main()