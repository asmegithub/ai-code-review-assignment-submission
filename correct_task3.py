"""Compute average of numeric, non-missing measurements."""


def average_valid_measurements(values):
	total = 0.0
	count = 0

	for value in values:
		if value is None:
			continue
		try:
			number = float(value)
		except (TypeError, ValueError):
			continue

		total += number
		count += 1

	return total / count if count else 0.0
