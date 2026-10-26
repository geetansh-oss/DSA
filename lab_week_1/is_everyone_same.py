import sys


def main():
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	n, q = data[0], data[1]
	values = data[2:2 + n]

	# Prefix count of adjacent positions where the value changes.
	changes = [0] * n
	for i in range(1, n):
		changes[i] = changes[i - 1] + (values[i] != values[i - 1])

	answers = []
	query_start = 2 + n
	for i in range(q):
		left, right = data[query_start + 2 * i:query_start + 2 * i + 2]
		answers.append("YES" if changes[right - 1] == changes[left - 1] else "NO")

	sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
	main()
