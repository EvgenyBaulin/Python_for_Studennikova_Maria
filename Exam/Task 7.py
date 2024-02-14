def check_state(states):
	matching_states = []

	for state_info in states:
		state, capital, biggest_city = state_info

		if capital == biggest_city:
			matching_states.append(state)

	matching_states.sort()

	return matching_states
