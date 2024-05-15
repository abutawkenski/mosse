from django.db import models

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=200)


    def __str__(self):
        return self.title



class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='blog/')
    body = models.TextField()
    tag = models.ManyToManyField(Tag, )
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class About(models.Model):
    name = models.CharField(max_length=202)
    image = models.FileField(upload_to='about/')
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    body = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    message = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.last_name


class Subscription(models.Model):
    email = models.EmailField()


    def __str__(self):
        return self.email

class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    message = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name