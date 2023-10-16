from django.db import models


class Category(models.Model):
    """
    Model for representing article categories.

    Attributes:
        name (str): Name of the category.
        parent (Category, optional): A reference to the parent category.
    """

    name = models.CharField(max_length=100, default='Top-News')
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        """
        Return the category's name as a string.

        Returns:
            str: The name of the category.
        """
        return self.name


class Article(models.Model):
    """
    Model for representing articles.

    Attributes:
        title (str): Title of the article.
        slug (str): Slug for generating SEO-friendly URLs.
        body (str): Main content of the article.
        date (datetime): Date and time when the article was created.
        thumb (Image, optional): Thumbnail image for the article.
        category (Category): Category to which the article belongs.
    """

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return the article's title as a string.

        Returns:
            str: The title of the article.
        """
        return self.title

    def snippet(self):
        """
        Return a snippet of the article's body.

        Returns:
            str: A snippet of the article's body.
        """
        return self.body[:150] + '...'


class Images(models.Model):
    """
    Model for representing images associated with articles.

    Attributes:
        article (Article): Article to which the image is related.
        description (str): Description of the image.
        image (Image): Image file.
    """

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        """
        Return the image's description as a string.

        Returns:
            str: The description of the image.
        """
        return self.description
