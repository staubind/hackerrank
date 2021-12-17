import re

def detect_html(str):
    # return format: link,text_name
    # grab the link
    link_regex = re.compile(r'href="([\w\W]+)"') # collect
    text_regex = re.compile(r'>([\w\W]*)<')
    