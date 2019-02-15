import re

email_pattern = r"[a-zA-Z\.]+@[a-zA-Z]{3,}\.[a-zA-Z]{2,3}"
postalcode_pattern = r"[1-9][0-9]{3}"

assert re.match(email_pattern, 'joe.johnson@gmail.com'), 'is a valid email'
assert not re.match(email_pattern, 'joe.johnson8@gmail.com'), 'is not a valid email'

assert re.match(postalcode_pattern, "3013"), 'is a valid postalcode'
assert not re.match(postalcode_pattern, "256"), 'is not a valid postalcode'