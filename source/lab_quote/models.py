from django.db import models

QUOTE_NEW = 'new'
QUOTE_APPROVED = 'approved'
QUOTE_STATUS_CHOICES = (
    (QUOTE_NEW, 'New'),
    (QUOTE_APPROVED, 'Approved')
)


class Quote(models.Model):
    text = models.TextField(max_length=2000, verbose_name='Quotes')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    author_name = models.CharField(max_length=50, verbose_name='Who added?')
    author_email = models.EmailField(verbose_name='Email')
    rating = models.IntegerField(default=0, verbose_name='Rating')
    status = models.CharField(max_length=20, choices=QUOTE_STATUS_CHOICES, default=QUOTE_NEW, verbose_name='Status')

    def __str__(self):
        return self.text[:20] + '...'

    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'