# __author__ = 'HankZhao'
# __date__ = '2017/12/25 20:21'
# Description:

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc', ]
    list_fields = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_num', 'fav_num', 'image', 'address', 'city']
    search_fields = ['name', 'desc', 'click_num', 'fav_num', 'image', 'address', 'city']
    list_fields = ['name', 'desc', 'click_num', 'fav_num', 'image', 'address', 'city__name']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_num',
                    'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_num']
    list_fields = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_num',
                   'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
