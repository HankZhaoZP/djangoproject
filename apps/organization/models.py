from django.utils import timezone
from django.db import models

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=50, verbose_name='城市名')
    desc = models.TextField(verbose_name='描述')
    add_time = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}:{1}'.format(self.name, self.desc)


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name='机构名')
    desc = models.TextField(verbose_name='机构描述')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name='封面图')
    address = models.CharField(max_length=150, verbose_name='机构地址')
    city = models.ForeignKey(CityDict, verbose_name='所在城市')

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构')
    name = models.CharField(max_length=50, verbose_name='教师名')
    work_years = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(max_length=50, verbose_name='就职公司')
    work_position = models.CharField(max_length=50, verbose_name='公司职位')
    points = models.CharField(max_length=50, verbose_name='教学特点')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    add_time = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = '课程教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
