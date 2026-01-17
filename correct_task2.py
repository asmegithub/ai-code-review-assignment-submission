"""Count valid email addresses with simple structural checks."""


def count_valid_emails(emails):
	count = 0

	for email in emails:
		if not isinstance(email, str):
			continue
		if " " in email:
			continue
		if email.count("@") != 1:
			continue

		local, domain = email.split("@")
		if not local or not domain:
			continue
		if "." not in domain:
			continue
		if domain.startswith(".") or domain.endswith("."):
			continue
		if ".." in domain:
			continue

		count += 1

	return count
