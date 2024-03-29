from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    describe = models.TextField(verbose_name=_('description'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('price'))
    active = models.BooleanField(default=True, verbose_name=_('product status'))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('created time'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('modified time'))

    class Meta:
        verbose_name_plural = _('Products')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _('very bad')),
        ('2', _('bad')),
        ('3', _('normal')),
        ('4', _('good')),
        ('5', _('perfect')),
    ]

    product = models.ForeignKey(Product,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name=_('product'))
    author = models.ForeignKey(get_user_model(),
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name=_('comment author'))
    body = models.TextField(verbose_name=_('comment text'))
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_('rate us'))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('comment submited time'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('comment modified time'))

    active = models.BooleanField(default=True, verbose_name=_('comment status'))

    # Manager
    objects = models.Manager()    
    active_comments_manager = ActiveCommentsManager()

    class Meta:
        verbose_name_plural = _('Comments')

    def get_absolute_url(self):
        return reverse("product_detail", args = [self.product.id])
    
    
    
