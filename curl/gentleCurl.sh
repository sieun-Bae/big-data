#download one website page
curl https://www.wikipedia.org

#download one Website page and save output to a file “wiki.html”
curl https://www.wikipedia.org -o wiki.html

# download several Website pages and save to the appropriate files
curl https://www.wikipedia.org -o wiki.html https://www.coursera.org/ -o coursera.html

#print headers
curl -i http://www.google.com

#follow redirects manually:
curl http://www.google.ru/?gfe_rd=cr&dcr=0&ei=q0-zWe-zL8bG7gSt5aLQAw

#or follow redirects automatically
curl -L http://www.google.com
