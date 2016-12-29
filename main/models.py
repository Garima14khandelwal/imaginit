from __future__ import unicode_literals
from django.contrib.auth.admin import User
from django.db import models
import hashlib
import os
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from django.dispatch import receiver
from imaginit.settings import BASE_DIR
from imagekit.models import ProcessedImageField


class UploadFile(models.Model):
    """Uploadfile and save."""

    file = ProcessedImageField(upload_to='profile/%Y/%m/%d',
                               processors=[ResizeToFit(800,600,False)],
                               format='JPEG',
                               options={'quality': 100})
    owner = models.ForeignKey(User)
    edited = models.SmallIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    thumbnail = ImageSpecField(source='file',
                                      processors=[ResizeToFit(200,150,False)],
                                      format='JPEG',
                                      options={'quality': 100})

    class Meta:
        ordering = ('-modified_on',)

    def get_url(self):
        """
            Handle IOERR : This function checks if file exists,
            if it doesnt it deletes the record plus any thumbnail 
            that might exist
        """
        try:
            # get url if exists

            if os.path.isfile(BASE_DIR + self.file.url):
                return self.thumbnail.url
            # if the path is not a file do house cleaning
            self.delete()
            return None
        except IOError:
            return None


class UserProfile(models.Model):

    """Add a picture to users"""

    user = models.OneToOneField(User, related_name='profile')
    def __unicode__(self):
        return "{}'s profile".format(self.user.username) 

    class Meta:
        db_table = 'user_profile'

			
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


def _delete_file(path):
    """Deletes file from filesystem."""
    if os.path.isfile(path):
        os.remove(path)


@receiver(models.signals.post_delete, sender=UploadFile)
def delete_file(sender, instance, *args, **kwargs):
    """Delete image files on `post_delete`."""
    if instance.file:
        _delete_file(instance.file.path)


@receiver(models.signals.post_delete, sender=UploadFile)
def delete_thumbnail(sender, instance, *args, **kwargs):
    """Delete thumbnail files on `post_delete`."""
    if instance.thumbnail:
        _delete_file(instance.thumbnail.path)
