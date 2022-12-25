from django.db import models
from datetime import datetime

# Create your models here.


class Category(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='published',
    )
    name = models.CharField(
        max_length=64,
        verbose_name='category'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='published',
    )
    name = models.CharField(
        max_length=64,
        verbose_name='product'
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='picture'
    )
    descr = models.CharField(
        max_length=3000,
        verbose_name='description'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='category'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_products'
        verbose_name = 'product'
        verbose_name_plural = 'products'



WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)



class WorkSchedule(models.Model):
    week_day = models.CharField(
        max_length=20,
        verbose_name='week day',
        choices=WEEK,
        unique=True,
    )
    is_published = models.BooleanField(
        verbose_name='published',
        default=True,
    )
    opening_time = models.TimeField(
        verbose_name='opening time',
        blank=True,
        null=True,
    )
    closing_time = models.TimeField(
        verbose_name='closing time',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.week_day

    def weekday_is_now(self):
        return self.week_day == datetime.now().strftime('%A')

    class Meta:
        db_table = 'main_work_schedule'
        verbose_name = 'work schedule'
        verbose_name_plural = 'work schedules'
        # ordering = ['week_day']


