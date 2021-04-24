from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser,User
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField

""" модели для Статей """
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


class News(models.Model):
    class Genres(models.TextChoices):
        action = ('action', 'action')
        adventure = ('adventure', 'adventure')
        simulator = ('simulator', 'simulator')
        strategy = ('strategy', 'strategy')
        rpg = ('RPG', 'RPG')
        puzzle = ('puzzle', 'puzzle')

    class Platforms(models.TextChoices):
        pc = ('PC', 'PC')
        mac = ('Mac', 'Mac')
        linux = ('linux', 'linux')
        nintendo_sw = ('Nintendo switch', 'Nintendo switch')
        psp = ('PSP', 'PSP')
        playstation = ('Playstation', 'Playstation')
        xbox = ('XBOX', 'XBOX')
        vr = ('VR', 'VR')
        android = ('Android', 'Android')
        iphone = ('ios', 'ios')

    title = models.CharField('Название статьи', max_length=50)
    platform = MultiSelectField('Платформа', max_length=50, choices=Platforms.choices, max_choices=6)
    genre1 = MultiSelectField('Жанр', max_length=20, choices=Genres.choices, max_choices=2)
    creators = models.CharField('Разработчик', max_length=50)
    publisher = models.CharField('Издатель', max_length=100, blank=True)
    gm_photo = models.ImageField('Лого игры', upload_to='photos/%y/%m/%d/')
    release_date = models.DateField('Дата релиза')
    text = models.TextField('Обзор на игру',default='')
    steam_url = models.CharField('Ссылка на игру в стиме',max_length=100,default='')
    metascore_url = models.CharField('Ссылка на оценку в метакритике',max_length=100,default='')
    trailer_youtube_url = models.CharField('Ссылка на трейлер в ютубе',max_length=200,default='')
    pub_date = models.DateTimeField('Дата статьи', auto_now_add=True)
    oform = models.PositiveSmallIntegerField('Оформление', validators=[MinValueValidator(0), MaxValueValidator(10)])
    mech = models.PositiveSmallIntegerField('Механика', validators=[MinValueValidator(0), MaxValueValidator(10)])
    plot = models.PositiveSmallIntegerField('Сюжет', validators=[MinValueValidator(0), MaxValueValidator(10)])
    likes = models.ManyToManyField(User,related_name='Лайки',blank=True)


    def total_likes(self):
        return self.likes.count()

    def score(self):
        return toFixed(sum([self.oform,self.plot,self.mech])/3,1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Cтатьи'
        ordering = ['-pub_date']




class Comment(models.Model):
    com_news = models.ForeignKey(News, on_delete=models.CASCADE)
    com_author = models.CharField('Автор', max_length=50)
    com_text = models.CharField('Комментарий', max_length=300)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'

# Create your models here.
