import re

title_regex = r'(?<=<title>).+(?=<\/title>)'
body_regex = r'<body>.+<\/body>'
inside_body_regex = r'>([^<>]*)<'

text = input()
title = ' '.join(re.findall(title_regex, text))
print(f"Title: {title}")
body = ' '.join(re.findall(body_regex, text))
content = re.findall(inside_body_regex, body)
content = [i.replace('\\n', ' ').strip() for i in content if len(i) != 0]
content = ' '.join(content)
print(f"Content: {content}")
