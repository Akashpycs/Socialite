from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "Post")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' '+ str(self.date.date())


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userImage = models.ImageField(upload_to = "Profiles", default = "default/default.png")
    bio = models.CharField(max_length=100, blank = True)
    connection = models.CharField(max_length = 100, blank=True)
    follower = models.IntegerField(default=0)
    following = models.IntegerField(default=0)


    def __str__(self):
        return str(self.user)

class Like(models.Model):
    user = models.ManyToManyField(User, related_name="linkingUser")
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    # for liking post
    @classmethod
    def like(cls, post, liking_user):
        obj, create  = cls.objects.get_or_create(post = post)
        obj.user.add(liking_user)

    # for disliking post
    @classmethod
    def dislike(cls, post, disliking_user):
        obj, create  = cls.objects.get_or_create(post = post)
        obj.user.remove(disliking_user)

    def __str__(self):
        return str(self.post)

class Following(models.Model):
    """ Following of the user """
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    followed = models.ManyToManyField(User, related_name="followed")
    follower = models.ManyToManyField(User, related_name="follower")

    @classmethod
    def follow(cls, user, another_account):
        obj = cls.objects.get(user = user)
        obj.followed.add(another_account)

    @classmethod
    def unfollow(cls, user, another_account):
        obj = cls.objects.get(user = user)
        obj.followed.remove(another_account)

    def __str__(self):
        return str(self.user)

class Share(Post, models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.user)

# P p ; { * " : _
