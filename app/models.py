class Source:
    """Source class to define Source objects"""

    def __init__(self,id,name,description,language):
        self.id = id
        self.name = name
        self.description = description
        self.language = language


class Article:
    """Class Article to define article objects """

    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

    # def save_article(self):
    # Article.append(self)