import re

# match - looks for a regular expression at the beginning of the string

email_pattern = r"[a-zA-Z\.]+@[a-zA-Z]{3,}\.[a-zA-Z]{2,3}"
assert re.match(email_pattern, 'joe.johnson@gmail.com'), 'is a valid email'
assert not re.match(email_pattern, 'joe.johnson8@gmail.com'), 'is not a valid email'

# match - might be a problem for these kind of strings
assert re.match(email_pattern, 'joe@gmail.com#_yolo'), 'pattern still matches with the wrong email'

# solution is to define start- and endpoints in your regex
email_pattern = r"^[a-zA-Z\.]+@[a-zA-Z]{3,}\.[a-zA-Z]{2,3}$"
assert not re.match(email_pattern, 'joe@gmail.com#_yolo'), 'pattern does not match'

postalcode_pattern = r"[1-9][0-9]{3}"
assert re.match(postalcode_pattern, "3013"), 'is a valid postalcode'
assert not re.match(postalcode_pattern, "256"), 'is not a valid postalcode'

# search - looks for a regular expression anywhere in the string

word_pattern = r"cat"
assert re.search(word_pattern, 'cat'), 'pattern will be found'
assert re.search(word_pattern, 'catdog'), 'pattern will be found'
assert re.search(word_pattern, 'housecat'), 'pattern will be found'
assert not re.search(word_pattern, 'hotdog'), 'pattern will not be found'
