from django.db import models

class Post(models.Model):
    '''Post data'''
    title = models.CharField('Post name', max_length=100)
    description = models.TextField('Post content')
    author = models.CharField('Author name', max_length=100)
    date = models.DateField('Published date')
    img = models.ImageField('Post image', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comments(models.Model):
    '''Comments'''
    email = models.EmailField()
    name = models.CharField('Name', max_length=50)
    text_comments = models.TextField('Comment text', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Post ID', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'