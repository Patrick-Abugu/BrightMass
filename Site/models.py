from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length= 100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='bmt.jpg', blank= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default='None' )

    class Meta:
        ordering = [ '-date']

    def __str__(self):
        return self.title

    def snippet(self):
         return self.body[:300]+'...'


class Feedback(models.Model):
    subject = models.CharField(max_length = 100)
    email: models.EmailField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

#adding comments model
#class Comment(models.Model):
    #post = models.ForeignKey(Post, on_delete =models.CASCADE, related_name = comments)
    #name = models.CharField(max_length = 100)
    #email = models.EmailField(max_length=100)
   # comments = models.TextField()
    #created = models.DateTimeField(auto_now_add=True)
    #author = models.ForeignKey('self', on_delete=models.CASCADE, null= True, blank=True)

    #class Meta:
        #ordering = ('-created')

     #def __str__(self):
         #return 'Comment By {}'.format(self.name)
