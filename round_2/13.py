# HTML Tag Validator: Write a function that validates a string of HTML, ensuring all tags are properly opened and closed in the correct order.

def html_tag_validator(html):
    if not html or '<' not in html:
        return False

    stack = []
    i = 0
    while i < len(html):
        if html[i] == '<' and html[i + 1] != '/':
            j = i + 1
            while j < len(html) and html[j] != '>':
                j += 1
            if j < len(html):
                tag = html[i:j + 1] # slicing the opening tag and adding it to the stack
                if tag[-2] != '/':
                    stack.append(tag)
                i = j
        elif html[i] == '<' and html[i + 1] == '/':
            j = i + 2
            while j < len(html) and html[j] != '>':
                j += 1
            if j < len(html):
                end = html[i:j + 1]
                if not stack or stack[-1][1:] != end[2:]:
                    return False
                stack.pop()
                i = j
        i += 1
    
    return len(stack) == 0

html = '''
<html>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
'''

print(html_tag_validator(html))

