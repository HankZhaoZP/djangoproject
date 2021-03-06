from django.utils import timezone
from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(max_length=2, choices=(("cj","初级"),("zj","中级"),("gj","高级")), verbose_name='课程难度')
    learn_times = models.IntegerField(default=0, verbose_name='学习时长（小时）')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面')
    click_nums = models.ImageField(default=0, verbose_name='点击数')
    add_time = models.DateField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='章节名')
    add_time = models.DateField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节名')
    name = models.CharField(max_length=100, verbose_name='视频名')
    add_time = models.DateField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='视频名')
    download_url = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='课程资料')
    add_time = models.DateField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course
