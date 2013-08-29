import os
import datetime
import hashlib
import unicodedata

from django.conf import settings
from django.db import models
from django.utils.timezone import utc
from django.dispatch import receiver

from sorl.thumbnail import ImageField


def now():
    return datetime.datetime.utcnow().replace(tzinfo=utc)


def _upload_path(tag):
    def _upload_path_tagged(instance, filename):
        if isinstance(filename, unicode):
            filename = (
                unicodedata
                .normalize('NFD', filename)
                .encode('ascii', 'ignore')
            )
        now = datetime.datetime.now()
        path = os.path.join(now.strftime('%Y'), now.strftime('%m'),
                            now.strftime('%d'))
        hashed_filename = (hashlib.md5(filename +
                           str(now.microsecond)).hexdigest())
        __, extension = os.path.splitext(filename)
        #root = settings.MEDIA_ROOT
        #return os.path.join(root, tag, path, hashed_filename + extension)
        return os.path.join(tag, path, hashed_filename + extension)
    return _upload_path_tagged


class Category(models.Model):
    name = models.CharField(max_length=100)
    modified = models.DateTimeField(default=now)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class CentimeterSizeField(models.CharField):
    __metaclass__ = models.SubfieldBase
    description = 'width and height in centimeters'

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 100)
        super(CentimeterSizeField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, (list, tuple)):
            return value
        if value is None:
            return None
        #raise Exception(value)
        value = value.replace('cm', '')
        return [int(x) for x in value.split('x') if x.strip()]

    def get_prep_value(self, value):
        return 'x'.join(str(x) for x in value)


from south.modelsinspector import add_introspection_rules
# For South migrations to understand what this field is
add_introspection_rules([], ["^stephanie\.main\.models\.CentimeterSizeField"])

class ArtGroup(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=65, unique=True, db_index=True, default='')
    #slug = models.SlugField(max_length=65, null=True, blank=True, db_index=True)
    modified = models.DateTimeField(default=now)

    def __unicode__(self):
        return self.name


class Artwork(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=65, unique=True, db_index=True)
    group = models.ForeignKey(ArtGroup)
    description = models.TextField(null=True, blank=True)
    created = models.DateField(null=True, blank=True)
    material = models.CharField(max_length=200, null=True, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    commission = models.BooleanField(default=False)
    commission_notes = models.TextField(null=True, blank=True)
    size = CentimeterSizeField(null=True, blank=True)

    picture = ImageField(upload_to=_upload_path('artwork'))

    added = models.DateTimeField(default=now)
    modified = models.DateTimeField(default=now)

    class Meta:
        verbose_name_plural = 'Artwork'

    def __unicode__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    sent = models.BooleanField(default=False)
    modified = models.DateTimeField(default=now)

@receiver(models.signals.pre_save, sender=Category)
@receiver(models.signals.pre_save, sender=Artwork)
@receiver(models.signals.pre_save, sender=ArtGroup)
@receiver(models.signals.pre_save, sender=Contact)
def update_modified(sender, instance, raw, *args, **kwargs):
    if raw:
        return
    instance.modified = now()
