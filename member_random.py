import random

member = ['성우', '재서', '희제', '호찬']
today = ['React', 'PS', 'OS/NET', 'JS']

random_q = []

while True:
	random_q = [i for i in range(4)]
	random.shuffle(random_q)
	is_dup = False
	for i in range(4):
		if random_q[i] == i:
			is_dup = True
	if not is_dup:
		break

for idx, ran_num in enumerate(random_q):
	print(f"{member[idx]}은(는) {today[ran_num]} 질문을 받는다!")
