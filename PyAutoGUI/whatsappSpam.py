import pyautogui

for i in range(1000):
	pyautogui.click(492, 992)  # position of chatbox
	pyautogui.typewrite('lol', interval=0.001)
	pyautogui.click(924, 9860)  # position of end button
