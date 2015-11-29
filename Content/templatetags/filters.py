# -*- coding: utf-8 -*-
from Content import jalali as convertor 
from django import template

register = template.Library()
MONTHS = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']

@register.filter(name='jalali')
def jalali(value):
        value = convertor.Gregorian(value.encode('utf-8')).persian_string()
        month = MONTHS[int(value.split('-')[1])]
        return value.split('-')[0] + ',' + month.decode('utf-8') + ' ' + value.split('-')[2]
