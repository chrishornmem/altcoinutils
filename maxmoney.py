start_block_reward = 15000
reward_interval=1051200
def max_money():
	current_reward = 15000 * 10**8
	total = 0
	while current_reward > 0:
		total += reward_interval * current_reward
		current_reward /= 2
	return total

print "Total BTC to ever be created:", max_money(), "Satoshis"
