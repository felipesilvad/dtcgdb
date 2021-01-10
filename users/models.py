from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from cards.models import Card, Set

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # usercards = models.ManyToManyField(Card, through=UserCard)

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
# class UserCard(models.Model):
#     card = models.ForeignKey(Card, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     quantity = models.IntegerField(blank=True, null=True)