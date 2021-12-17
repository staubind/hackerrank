import re

def detect_html(str):
    # return format: link,text_name
    link_regex = re.compile(r'href="(.*?)"') # collect
    text_regex = re.compile(r'(?<=>)([\w\t \..]+?)(?=<)') # sometimes collects too much
    #link = re.findall(link_regex, str)
    text = re.findall(text_regex, str)
    #print('link is: ', link)
    print('text is: ', text)
    #print(','.join([link[0].strip(),text[0].strip()]))

detect_html('<li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z">Main page</a></li>')
detect_html('<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>')
detect_html('<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>')
detect_html('<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>')

detect_html('''<div class="portal" role="navigation" id="p-navigation">
<h3>Navigation</h3>
<div class="body">
<ul>
 <li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z">Main page</a></li>
 <li id="n-contents"><a href="/wiki/Portal:Contents" title="Guides to browsing Wikipedia">Contents</a></li>
 <li id="n-featuredcontent"><a href="/wiki/Portal:Featured_content" title="Featured content  the best of Wikipedia">Featured content</a></li>
<li id="n-currentevents"><a href="/wiki/Portal:Current_events" title="Find background information on current events">Current events</a></li>
<li id="n-randompage"><a href="/wiki/Special:Random" title="Load a random article [x]" accesskey="x">Random article</a></li>
<li id="n-sitesupport"><a href="//donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en" title="Support us">Donate to Wikipedia</a></li>
</ul>
</div>
</div> ''')

