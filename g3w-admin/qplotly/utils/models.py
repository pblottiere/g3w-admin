# coding=utf-8
"""" Model tuils function

.. note:: This program is free software; you can redistribute it and/or modify
    it under the terms of the Mozilla Public License 2.0.

"""

__author__ = 'lorenzetti@gis3w.it'
__date__ = '2020-09-22'
__copyright__ = 'Copyright 2015 - 2020, Gis3w'


from django.db.models import Q
from qdjango.utils.structure import datasource2dict
from qplotly.models import QplotlyWidget


def get_qplotlywidgets4layer(layer):
    """
    Return qplotly widgets list for qdjango layer instance
    :param layer: Qdjango Layer model instance
    :return: List or Querydict of Widget models
    """

    # different by layer type
    # for postgis layer
    if layer.layer_type == 'postgres':
        ds = datasource2dict(layer.datasource)
        to_contain = Q(datasource__contains=u'dbname=\'{}\''.format(ds['dbname'])) & \
                     Q(datasource__contains=u'host={}'.format(ds['host'])) & \
                     Q(datasource__contains=u'table={}'.format(ds['table']))
        return QplotlyWidget.objects.filter(to_contain)
    else:
        return QplotlyWidget.objects.filter(datasource=layer.datasource)
