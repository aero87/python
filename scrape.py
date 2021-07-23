# Import required module
import newspaper

# Assign URL
url = input('Type in the link/URL: ')

# Extract web data
url_i = newspaper.Article(url="%s" % (url), language='en')
url_i.download()
url_i.parse()

# Display scrapped data
print(url_i.text)