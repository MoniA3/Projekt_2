# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Informatyka_projekt2
                                 A QGIS plugin
 Wtyczka informatyka projekt 2
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-07
        copyright            : (C) 2024 by 325781, 325780
        email                : Maja Kurek, Monika Kulińska
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Informatyka_projekt2 class from file Informatyka_projekt2.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Inf2 import Informatyka_projekt2
    return Informatyka_projekt2(iface)
