#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from distutils.core import setup

IS_IN_DEBBUILDER = os.environ.get("IS_IN_DEBBUILDER", "false") == "true"
VERSION = "1.0"


install_requires = ['easyevent', 'PyGObject']

if IS_IN_DEBBUILDER:
    install_requires = [
        'easyevent',
        'gir1.2-gstreamer-1.0',
        'gstreamer1.0-tools',
        'libgstreamer1.0-0',
        'gstreamer1.0-plugins-base',
        'gir1.2-gst-plugins-base-1.0',
        'gstreamer1.0-plugins-good',
        'libgstreamer-plugins-bad1.0-0',
        'gstreamer1.0-plugins-bad',
        'gstreamer1.0-plugins-ugly',
        'gstreamer1.0-vaapi',
        'gi',
        'python3-gi'
        'python3-gst-1.0',
        'libgstreamer1.0'
    ]

setup(
    name="gstmanager1",
    version=VERSION,
    description="gstmanager is a helper for building gstreamer applications",
    author="Florent Thiery",
    author_email="florent.thiery@ubicast.eu",
    url="https://github.com/UbiCastTeam/gstmanager",
    license="GNU/LGPLv3",
    packages=[
        'gstmanager1',
        'gstmanager1/detectors',
        'gstmanager1/sbins',
        'gstmanager1/sbins/encoders',
        'gstmanager1/sbins/analysis',
        'gstmanager1/sbins/sinks',
        'gstmanager1/sbins/sources',
        'gstmanager1/profiles'
    ],
    install_requires=install_requires
)
