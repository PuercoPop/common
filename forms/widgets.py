# -*- coding: utf-8 -*-

from django.forms.widgets import Select
from django.forms.widgets import RadioSelect
from django.forms.extras.widgets import SelectDateWidget
from django.utils.safestring import mark_safe
from django.utils.dates import MONTHS
import datetime
import re

class SelectWithEmptyLabel(Select):

    def __init__(self, attrs=None, choices=(), empty_label='-------'):
        choices = list(choices)
        choices.insert(0, (u'',empty_label,))
        super(SelectWithEmptyLabel, self).__init__(attrs, choices)

class BirthDateWidget(SelectDateWidget):

     def __init__(self, attrs=None, years=None, required=True):                  
        this_year = datetime.date.today().year                              
        years = range(this_year, this_year - 101, -1) 
        super(BirthDateWidget, self).__init__(attrs, years, required)

class HorizRadioRenderer(RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class HorizRadioSelect(RadioSelect):
    renderer = HorizRadioRenderer
