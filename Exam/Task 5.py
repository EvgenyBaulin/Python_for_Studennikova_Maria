alice_states = set(input().split())
laura_states = set(input().split())

new_states = set(input().split())

selected_states = sorted(alice_states - new_states - laura_states)

if selected_states:
	print(", ".join(selected_states))
