#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example file to import the csv files.

:copyright:
    The PDART Development Team & Ceri Nunn
:license:
    GNU Lesser General Public License, Version 3
    (https://www.gnu.org/copyleft/lesser.html)
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA
from pdart.binary_import_work_tapes import import_csv_work_tapes

if __name__ == "__main__":

    base_dir='/Users/cnunn/lunar_data/PDART_TAPES/work_tapes/'
    out_base_dir='/Users/cnunn/lunar_data/PDART_CSV_WORK_TAPES'
    out_base_dir_full='/Users/cnunn/lunar_data/PDART_CSV_WORK_TAPES_FULL'

    filenames_all = ['wtn.1.1.gz',
    'wtn.1.10.gz',
    'wtn.1.11.gz',
    'wtn.1.12.gz',
    'wtn.1.13.gz',
    'wtn.1.14.gz',
    'wtn.1.15.gz',
    'wtn.1.16.gz',
    'wtn.1.17.gz',
    'wtn.1.18.gz',
    'wtn.1.19.gz',
    'wtn.1.2.gz',
    'wtn.1.20.gz',
    'wtn.1.21.gz',
    'wtn.1.22.gz',
    'wtn.1.23.gz',
    'wtn.1.24.gz',
    'wtn.1.25.gz',
    'wtn.1.26.gz',
    'wtn.1.27.gz',
    'wtn.1.28.gz',
    'wtn.1.29.gz',
    'wtn.1.3.gz',
    'wtn.1.30.gz',
    'wtn.1.31.gz',
    'wtn.1.32.gz',
    'wtn.1.33.gz',
    'wtn.1.34.gz',
    'wtn.1.35.gz',
    'wtn.1.36.gz',
    'wtn.1.37.gz',
    'wtn.1.38.gz',
    'wtn.1.39.gz',
    'wtn.1.4.gz',
    'wtn.1.40.gz',
    'wtn.1.41.gz',
    'wtn.1.42.gz',
    'wtn.1.43.gz',
    'wtn.1.44.gz',
    'wtn.1.45.gz',
    'wtn.1.46.gz',
    'wtn.1.47.gz',
    'wtn.1.48.gz',
    'wtn.1.49.gz',
    'wtn.1.5.gz',
    'wtn.1.50.gz',
    'wtn.1.51.gz',
    'wtn.1.52.gz',
    'wtn.1.53.gz',
    'wtn.1.54.gz',
    'wtn.1.55.gz',
    'wtn.1.6.gz',
    'wtn.1.7.gz',
    'wtn.1.8.gz',
    'wtn.1.9.gz',
    'wtn.10.1.gz',
    'wtn.10.10.gz',
    'wtn.10.11.gz',
    'wtn.10.12.gz',
    'wtn.10.13.gz',
    'wtn.10.14.gz',
    'wtn.10.15.gz',
    'wtn.10.16.gz',
    'wtn.10.17.gz',
    'wtn.10.18.gz',
    'wtn.10.19.gz',
    'wtn.10.2.gz',
    'wtn.10.20.gz',
    'wtn.10.21.gz',
    'wtn.10.22.gz',
    'wtn.10.23.gz',
    'wtn.10.24.gz',
    'wtn.10.25.gz',
    'wtn.10.26.gz',
    'wtn.10.27.gz',
    'wtn.10.28.gz',
    'wtn.10.29.gz',
    'wtn.10.3.gz',
    'wtn.10.30.gz',
    'wtn.10.31.gz',
    'wtn.10.32.gz',
    'wtn.10.33.gz',
    'wtn.10.34.gz',
    'wtn.10.35.gz',
    'wtn.10.36.gz',
    'wtn.10.37.gz',
    'wtn.10.38.gz',
    'wtn.10.39.gz',
    'wtn.10.4.gz',
    'wtn.10.40.gz',
    'wtn.10.41.gz',
    'wtn.10.42.gz',
    'wtn.10.43.gz',
    'wtn.10.44.gz',
    'wtn.10.45.gz',
    'wtn.10.46.gz',
    'wtn.10.47.gz',
    'wtn.10.48.gz',
    'wtn.10.49.gz',
    'wtn.10.5.gz',
    'wtn.10.50.gz',
    'wtn.10.51.gz',
    'wtn.10.52.gz',
    'wtn.10.53.gz',
    'wtn.10.54.gz',
    'wtn.10.55.gz',
    'wtn.10.6.gz',
    'wtn.10.7.gz',
    'wtn.10.8.gz',
    'wtn.10.9.gz',
    'wtn.11.1.gz',
    'wtn.11.10.gz',
    'wtn.11.11.gz',
    'wtn.11.12.gz',
    'wtn.11.13.gz',
    'wtn.11.14.gz',
    'wtn.11.15.gz',
    'wtn.11.16.gz',
    'wtn.11.17.gz',
    'wtn.11.18.gz',
    'wtn.11.19.gz',
    'wtn.11.2.gz',
    'wtn.11.20.gz',
    'wtn.11.21.gz',
    'wtn.11.22.gz',
    'wtn.11.23.gz',
    'wtn.11.24.gz',
    'wtn.11.25.gz',
    'wtn.11.26.gz',
    'wtn.11.27.gz',
    'wtn.11.28.gz',
    'wtn.11.29.gz',
    'wtn.11.3.gz',
    'wtn.11.30.gz',
    'wtn.11.31.gz',
    'wtn.11.32.gz',
    'wtn.11.33.gz',
    'wtn.11.34.gz',
    'wtn.11.35.gz',
    'wtn.11.36.gz',
    'wtn.11.37.gz',
    'wtn.11.38.gz',
    'wtn.11.39.gz',
    'wtn.11.4.gz',
    'wtn.11.40.gz',
    'wtn.11.41.gz',
    'wtn.11.42.gz',
    'wtn.11.43.gz',
    'wtn.11.44.gz',
    'wtn.11.45.gz',
    'wtn.11.46.gz',
    'wtn.11.47.gz',
    'wtn.11.48.gz',
    'wtn.11.49.gz',
    'wtn.11.5.gz',
    'wtn.11.50.gz',
    'wtn.11.51.gz',
    'wtn.11.52.gz',
    'wtn.11.53.gz',
    'wtn.11.54.gz',
    'wtn.11.55.gz',
    'wtn.11.6.gz',
    'wtn.11.7.gz',
    'wtn.11.8.gz',
    'wtn.11.9.gz',
    'wtn.12.1.gz',
    'wtn.12.10.gz',
    'wtn.12.11.gz',
    'wtn.12.12.gz',
    'wtn.12.13.gz',
    'wtn.12.14.gz',
    'wtn.12.15.gz',
    'wtn.12.16.gz',
    'wtn.12.17.gz',
    'wtn.12.18.gz',
    'wtn.12.19.gz',
    'wtn.12.2.gz',
    'wtn.12.20.gz',
    'wtn.12.21.gz',
    'wtn.12.22.gz',
    'wtn.12.23.gz',
    'wtn.12.24.gz',
    'wtn.12.25.gz',
    'wtn.12.26.gz',
    'wtn.12.27.gz',
    'wtn.12.28.gz',
    'wtn.12.29.gz',
    'wtn.12.3.gz',
    'wtn.12.30.gz',
    'wtn.12.31.gz',
    'wtn.12.32.gz',
    'wtn.12.33.gz',
    'wtn.12.34.gz',
    'wtn.12.35.gz',
    'wtn.12.36.gz',
    'wtn.12.37.gz',
    'wtn.12.38.gz',
    'wtn.12.39.gz',
    'wtn.12.4.gz',
    'wtn.12.40.gz',
    'wtn.12.41.gz',
    'wtn.12.42.gz',
    'wtn.12.43.gz',
    'wtn.12.44.gz',
    'wtn.12.45.gz',
    'wtn.12.46.gz',
    'wtn.12.47.gz',
    'wtn.12.48.gz',
    'wtn.12.49.gz',
    'wtn.12.5.gz',
    'wtn.12.50.gz',
    'wtn.12.51.gz',
    'wtn.12.52.gz',
    'wtn.12.53.gz',
    'wtn.12.54.gz',
    'wtn.12.55.gz',
    'wtn.12.6.gz',
    'wtn.12.7.gz',
    'wtn.12.8.gz',
    'wtn.12.9.gz',
    'wtn.13.1.gz',
    'wtn.13.10.gz',
    'wtn.13.11.gz',
    'wtn.13.12.gz',
    'wtn.13.13.gz',
    'wtn.13.14.gz',
    'wtn.13.15.gz',
    'wtn.13.16.gz',
    'wtn.13.17.gz',
    'wtn.13.18.gz',
    'wtn.13.19.gz',
    'wtn.13.2.gz',
    'wtn.13.20.gz',
    'wtn.13.21.gz',
    'wtn.13.22.gz',
    'wtn.13.23.gz',
    'wtn.13.24.gz',
    'wtn.13.25.gz',
    'wtn.13.26.gz',
    'wtn.13.27.gz',
    'wtn.13.28.gz',
    'wtn.13.29.gz',
    'wtn.13.3.gz',
    'wtn.13.30.gz',
    'wtn.13.31.gz',
    'wtn.13.32.gz',
    'wtn.13.33.gz',
    'wtn.13.34.gz',
    'wtn.13.35.gz',
    'wtn.13.36.gz',
    'wtn.13.37.gz',
    'wtn.13.38.gz',
    'wtn.13.39.gz',
    'wtn.13.4.gz',
    'wtn.13.40.gz',
    'wtn.13.41.gz',
    'wtn.13.42.gz',
    'wtn.13.43.gz',
    'wtn.13.44.gz',
    'wtn.13.45.gz',
    'wtn.13.46.gz',
    'wtn.13.47.gz',
    'wtn.13.48.gz',
    'wtn.13.49.gz',
    'wtn.13.5.gz',
    'wtn.13.50.gz',
    'wtn.13.51.gz',
    'wtn.13.52.gz',
    'wtn.13.53.gz',
    'wtn.13.54.gz',
    'wtn.13.55.gz',
    'wtn.13.56.gz',
    'wtn.13.57.gz',
    'wtn.13.6.gz',
    'wtn.13.7.gz',
    'wtn.13.8.gz',
    'wtn.13.9.gz',
    'wtn.14.1.gz',
    'wtn.14.10.gz',
    'wtn.14.11.gz',
    'wtn.14.12.gz',
    'wtn.14.13.gz',
    'wtn.14.14.gz',
    'wtn.14.15.gz',
    'wtn.14.16.gz',
    'wtn.14.17.gz',
    'wtn.14.18.gz',
    'wtn.14.19.gz',
    'wtn.14.2.gz',
    'wtn.14.20.gz',
    'wtn.14.21.gz',
    'wtn.14.22.gz',
    'wtn.14.23.gz',
    'wtn.14.24.gz',
    'wtn.14.25.gz',
    'wtn.14.26.gz',
    'wtn.14.27.gz',
    'wtn.14.28.gz',
    'wtn.14.29.gz',
    'wtn.14.3.gz',
    'wtn.14.30.gz',
    'wtn.14.31.gz',
    'wtn.14.32.gz',
    'wtn.14.33.gz',
    'wtn.14.34.gz',
    'wtn.14.35.gz',
    'wtn.14.36.gz',
    'wtn.14.37.gz',
    'wtn.14.38.gz',
    'wtn.14.39.gz',
    'wtn.14.4.gz',
    'wtn.14.40.gz',
    'wtn.14.41.gz',
    'wtn.14.42.gz',
    'wtn.14.43.gz',
    'wtn.14.44.gz',
    'wtn.14.45.gz',
    'wtn.14.46.gz',
    'wtn.14.47.gz',
    'wtn.14.48.gz',
    'wtn.14.49.gz',
    'wtn.14.5.gz',
    'wtn.14.50.gz',
    'wtn.14.51.gz',
    'wtn.14.52.gz',
    'wtn.14.53.gz',
    'wtn.14.54.gz',
    'wtn.14.55.gz',
    'wtn.14.6.gz',
    'wtn.14.7.gz',
    'wtn.14.8.gz',
    'wtn.14.9.gz',
    'wtn.15.1.gz',
    'wtn.15.10.gz',
    'wtn.15.11.gz',
    'wtn.15.12.gz',
    'wtn.15.13.gz',
    'wtn.15.14.gz',
    'wtn.15.15.gz',
    'wtn.15.16.gz',
    'wtn.15.17.gz',
    'wtn.15.18.gz',
    'wtn.15.19.gz',
    'wtn.15.2.gz',
    'wtn.15.20.gz',
    'wtn.15.21.gz',
    'wtn.15.22.gz',
    'wtn.15.23.gz',
    'wtn.15.24.gz',
    'wtn.15.25.gz',
    'wtn.15.26.gz',
    'wtn.15.27.gz',
    'wtn.15.28.gz',
    'wtn.15.29.gz',
    'wtn.15.3.gz',
    'wtn.15.30.gz',
    'wtn.15.31.gz',
    'wtn.15.32.gz',
    'wtn.15.33.gz',
    'wtn.15.34.gz',
    'wtn.15.35.gz',
    'wtn.15.36.gz',
    'wtn.15.37.gz',
    'wtn.15.38.gz',
    'wtn.15.39.gz',
    'wtn.15.4.gz',
    'wtn.15.40.gz',
    'wtn.15.41.gz',
    'wtn.15.42.gz',
    'wtn.15.43.gz',
    'wtn.15.44.gz',
    'wtn.15.45.gz',
    'wtn.15.46.gz',
    'wtn.15.47.gz',
    'wtn.15.48.gz',
    'wtn.15.49.gz',
    'wtn.15.5.gz',
    'wtn.15.50.gz',
    'wtn.15.51.gz',
    'wtn.15.52.gz',
    'wtn.15.53.gz',
    'wtn.15.54.gz',
    'wtn.15.55.gz',
    'wtn.15.6.gz',
    'wtn.15.7.gz',
    'wtn.15.8.gz',
    'wtn.15.9.gz',
    'wtn.16.1.gz',
    'wtn.16.10.gz',
    'wtn.16.11.gz',
    'wtn.16.12.gz',
    'wtn.16.13.gz',
    'wtn.16.14.gz',
    'wtn.16.15.gz',
    'wtn.16.16.gz',
    'wtn.16.17.gz',
    'wtn.16.18.gz',
    'wtn.16.19.gz',
    'wtn.16.2.gz',
    'wtn.16.20.gz',
    'wtn.16.21.gz',
    'wtn.16.22.gz',
    'wtn.16.23.gz',
    'wtn.16.24.gz',
    'wtn.16.25.gz',
    'wtn.16.26.gz',
    'wtn.16.27.gz',
    'wtn.16.28.gz',
    'wtn.16.29.gz',
    'wtn.16.3.gz',
    'wtn.16.30.gz',
    'wtn.16.31.gz',
    'wtn.16.32.gz',
    'wtn.16.33.gz',
    'wtn.16.34.gz',
    'wtn.16.35.gz',
    'wtn.16.36.gz',
    'wtn.16.37.gz',
    'wtn.16.38.gz',
    'wtn.16.39.gz',
    'wtn.16.4.gz',
    'wtn.16.40.gz',
    'wtn.16.41.gz',
    'wtn.16.42.gz',
    'wtn.16.43.gz',
    'wtn.16.44.gz',
    'wtn.16.45.gz',
    'wtn.16.46.gz',
    'wtn.16.47.gz',
    'wtn.16.48.gz',
    'wtn.16.49.gz',
    'wtn.16.5.gz',
    'wtn.16.50.gz',
    'wtn.16.51.gz',
    'wtn.16.52.gz',
    'wtn.16.53.gz',
    'wtn.16.54.gz',
    'wtn.16.55.gz',
    'wtn.16.6.gz',
    'wtn.16.7.gz',
    'wtn.16.8.gz',
    'wtn.16.9.gz',
    'wtn.17.1.gz',
    'wtn.17.10.gz',
    'wtn.17.11.gz',
    'wtn.17.12.gz',
    'wtn.17.13.gz',
    'wtn.17.14.gz',
    'wtn.17.15.gz',
    'wtn.17.16.gz',
    'wtn.17.17.gz',
    'wtn.17.18.gz',
    'wtn.17.19.gz',
    'wtn.17.2.gz',
    'wtn.17.20.gz',
    'wtn.17.21.gz',
    'wtn.17.22.gz',
    'wtn.17.23.gz',
    'wtn.17.24.gz',
    'wtn.17.25.gz',
    'wtn.17.26.gz',
    'wtn.17.27.gz',
    'wtn.17.28.gz',
    'wtn.17.29.gz',
    'wtn.17.3.gz',
    'wtn.17.30.gz',
    'wtn.17.31.gz',
    'wtn.17.32.gz',
    'wtn.17.33.gz',
    'wtn.17.34.gz',
    'wtn.17.35.gz',
    'wtn.17.36.gz',
    'wtn.17.37.gz',
    'wtn.17.38.gz',
    'wtn.17.39.gz',
    'wtn.17.4.gz',
    'wtn.17.40.gz',
    'wtn.17.41.gz',
    'wtn.17.42.gz',
    'wtn.17.43.gz',
    'wtn.17.44.gz',
    'wtn.17.45.gz',
    'wtn.17.46.gz',
    'wtn.17.47.gz',
    'wtn.17.48.gz',
    'wtn.17.49.gz',
    'wtn.17.5.gz',
    'wtn.17.50.gz',
    'wtn.17.51.gz',
    'wtn.17.52.gz',
    'wtn.17.53.gz',
    'wtn.17.54.gz',
    'wtn.17.55.gz',
    'wtn.17.6.gz',
    'wtn.17.7.gz',
    'wtn.17.8.gz',
    'wtn.17.9.gz',
    'wtn.18.1.gz',
    'wtn.18.10.gz',
    'wtn.18.11.gz',
    'wtn.18.12.gz',
    'wtn.18.13.gz',
    'wtn.18.14.gz',
    'wtn.18.15.gz',
    'wtn.18.16.gz',
    'wtn.18.17.gz',
    'wtn.18.18.gz',
    'wtn.18.19.gz',
    'wtn.18.2.gz',
    'wtn.18.20.gz',
    'wtn.18.21.gz',
    'wtn.18.22.gz',
    'wtn.18.23.gz',
    'wtn.18.24.gz',
    'wtn.18.25.gz',
    'wtn.18.26.gz',
    'wtn.18.27.gz',
    'wtn.18.28.gz',
    'wtn.18.29.gz',
    'wtn.18.3.gz',
    'wtn.18.30.gz',
    'wtn.18.31.gz',
    'wtn.18.32.gz',
    'wtn.18.33.gz',
    'wtn.18.34.gz',
    'wtn.18.35.gz',
    'wtn.18.36.gz',
    'wtn.18.37.gz',
    'wtn.18.38.gz',
    'wtn.18.39.gz',
    'wtn.18.4.gz',
    'wtn.18.40.gz',
    'wtn.18.41.gz',
    'wtn.18.42.gz',
    'wtn.18.43.gz',
    'wtn.18.44.gz',
    'wtn.18.45.gz',
    'wtn.18.46.gz',
    'wtn.18.47.gz',
    'wtn.18.48.gz',
    'wtn.18.49.gz',
    'wtn.18.5.gz',
    'wtn.18.50.gz',
    'wtn.18.51.gz',
    'wtn.18.52.gz',
    'wtn.18.53.gz',
    'wtn.18.54.gz',
    'wtn.18.55.gz',
    'wtn.18.6.gz',
    'wtn.18.7.gz',
    'wtn.18.8.gz',
    'wtn.18.9.gz',
    'wtn.19.1.gz',
    'wtn.19.10.gz',
    'wtn.19.11.gz',
    'wtn.19.12.gz',
    'wtn.19.13.gz',
    'wtn.19.14.gz',
    'wtn.19.15.gz',
    'wtn.19.16.gz',
    'wtn.19.17.gz',
    'wtn.19.18.gz',
    'wtn.19.19.gz',
    'wtn.19.2.gz',
    'wtn.19.20.gz',
    'wtn.19.21.gz',
    'wtn.19.22.gz',
    'wtn.19.23.gz',
    'wtn.19.24.gz',
    'wtn.19.25.gz',
    'wtn.19.26.gz',
    'wtn.19.27.gz',
    'wtn.19.28.gz',
    'wtn.19.29.gz',
    'wtn.19.3.gz',
    'wtn.19.30.gz',
    'wtn.19.31.gz',
    'wtn.19.32.gz',
    'wtn.19.33.gz',
    'wtn.19.34.gz',
    'wtn.19.35.gz',
    'wtn.19.36.gz',
    'wtn.19.37.gz',
    'wtn.19.38.gz',
    'wtn.19.39.gz',
    'wtn.19.4.gz',
    'wtn.19.40.gz',
    'wtn.19.41.gz',
    'wtn.19.42.gz',
    'wtn.19.43.gz',
    'wtn.19.44.gz',
    'wtn.19.45.gz',
    'wtn.19.46.gz',
    'wtn.19.47.gz',
    'wtn.19.48.gz',
    'wtn.19.49.gz',
    'wtn.19.5.gz',
    'wtn.19.50.gz',
    'wtn.19.51.gz',
    'wtn.19.52.gz',
    'wtn.19.53.gz',
    'wtn.19.54.gz',
    'wtn.19.55.gz',
    'wtn.19.6.gz',
    'wtn.19.7.gz',
    'wtn.19.8.gz',
    'wtn.19.9.gz',
    'wtn.2.1.gz',
    'wtn.2.10.gz',
    'wtn.2.11.gz',
    'wtn.2.12.gz',
    'wtn.2.13.gz',
    'wtn.2.14.gz',
    'wtn.2.15.gz',
    'wtn.2.16.gz',
    'wtn.2.17.gz',
    'wtn.2.18.gz',
    'wtn.2.19.gz',
    'wtn.2.2.gz',
    'wtn.2.20.gz',
    'wtn.2.21.gz',
    'wtn.2.22.gz',
    'wtn.2.23.gz',
    'wtn.2.24.gz',
    'wtn.2.25.gz',
    'wtn.2.26.gz',
    'wtn.2.27.gz',
    'wtn.2.28.gz',
    'wtn.2.29.gz',
    'wtn.2.3.gz',
    'wtn.2.30.gz',
    'wtn.2.31.gz',
    'wtn.2.32.gz',
    'wtn.2.33.gz',
    'wtn.2.34.gz',
    'wtn.2.35.gz',
    'wtn.2.36.gz',
    'wtn.2.37.gz',
    'wtn.2.38.gz',
    'wtn.2.39.gz',
    'wtn.2.4.gz',
    'wtn.2.40.gz',
    'wtn.2.41.gz',
    'wtn.2.42.gz',
    'wtn.2.43.gz',
    'wtn.2.44.gz',
    'wtn.2.45.gz',
    'wtn.2.46.gz',
    'wtn.2.47.gz',
    'wtn.2.48.gz',
    'wtn.2.49.gz',
    'wtn.2.5.gz',
    'wtn.2.50.gz',
    'wtn.2.51.gz',
    'wtn.2.52.gz',
    'wtn.2.53.gz',
    'wtn.2.54.gz',
    'wtn.2.55.gz',
    'wtn.2.6.gz',
    'wtn.2.7.gz',
    'wtn.2.8.gz',
    'wtn.2.9.gz',
    'wtn.20.1.gz',
    'wtn.20.10.gz',
    'wtn.20.11.gz',
    'wtn.20.12.gz',
    'wtn.20.13.gz',
    'wtn.20.14.gz',
    'wtn.20.15.gz',
    'wtn.20.16.gz',
    'wtn.20.17.gz',
    'wtn.20.18.gz',
    'wtn.20.19.gz',
    'wtn.20.2.gz',
    'wtn.20.20.gz',
    'wtn.20.21.gz',
    'wtn.20.22.gz',
    'wtn.20.23.gz',
    'wtn.20.24.gz',
    'wtn.20.25.gz',
    'wtn.20.26.gz',
    'wtn.20.27.gz',
    'wtn.20.28.gz',
    'wtn.20.29.gz',
    'wtn.20.3.gz',
    'wtn.20.30.gz',
    'wtn.20.31.gz',
    'wtn.20.32.gz',
    'wtn.20.33.gz',
    'wtn.20.34.gz',
    'wtn.20.35.gz',
    'wtn.20.36.gz',
    'wtn.20.37.gz',
    'wtn.20.38.gz',
    'wtn.20.39.gz',
    'wtn.20.4.gz',
    'wtn.20.40.gz',
    'wtn.20.41.gz',
    'wtn.20.42.gz',
    'wtn.20.43.gz',
    'wtn.20.44.gz',
    'wtn.20.45.gz',
    'wtn.20.46.gz',
    'wtn.20.47.gz',
    'wtn.20.48.gz',
    'wtn.20.49.gz',
    'wtn.20.5.gz',
    'wtn.20.50.gz',
    'wtn.20.51.gz',
    'wtn.20.52.gz',
    'wtn.20.53.gz',
    'wtn.20.54.gz',
    'wtn.20.6.gz',
    'wtn.20.7.gz',
    'wtn.20.8.gz',
    'wtn.20.9.gz',
    'wtn.21.1.gz',
    'wtn.21.10.gz',
    'wtn.21.11.gz',
    'wtn.21.12.gz',
    'wtn.21.13.gz',
    'wtn.21.14.gz',
    'wtn.21.15.gz',
    'wtn.21.16.gz',
    'wtn.21.17.gz',
    'wtn.21.18.gz',
    'wtn.21.19.gz',
    'wtn.21.2.gz',
    'wtn.21.20.gz',
    'wtn.21.21.gz',
    'wtn.21.22.gz',
    'wtn.21.23.gz',
    'wtn.21.24.gz',
    'wtn.21.25.gz',
    'wtn.21.26.gz',
    'wtn.21.27.gz',
    'wtn.21.28.gz',
    'wtn.21.29.gz',
    'wtn.21.3.gz',
    'wtn.21.30.gz',
    'wtn.21.31.gz',
    'wtn.21.32.gz',
    'wtn.21.33.gz',
    'wtn.21.34.gz',
    'wtn.21.35.gz',
    'wtn.21.36.gz',
    'wtn.21.37.gz',
    'wtn.21.38.gz',
    'wtn.21.39.gz',
    'wtn.21.4.gz',
    'wtn.21.40.gz',
    'wtn.21.41.gz',
    'wtn.21.42.gz',
    'wtn.21.43.gz',
    'wtn.21.44.gz',
    'wtn.21.45.gz',
    'wtn.21.46.gz',
    'wtn.21.47.gz',
    'wtn.21.48.gz',
    'wtn.21.5.gz',
    'wtn.21.6.gz',
    'wtn.21.7.gz',
    'wtn.21.8.gz',
    'wtn.21.9.gz',
    'wtn.3.1.gz',
    'wtn.3.10.gz',
    'wtn.3.11.gz',
    'wtn.3.12.gz',
    'wtn.3.13.gz',
    'wtn.3.14.gz',
    'wtn.3.15.gz',
    'wtn.3.16.gz',
    'wtn.3.17.gz',
    'wtn.3.18.gz',
    'wtn.3.19.gz',
    'wtn.3.2.gz',
    'wtn.3.20.gz',
    'wtn.3.21.gz',
    'wtn.3.22.gz',
    'wtn.3.23.gz',
    'wtn.3.24.gz',
    'wtn.3.25.gz',
    'wtn.3.26.gz',
    'wtn.3.27.gz',
    'wtn.3.28.gz',
    'wtn.3.29.gz',
    'wtn.3.3.gz',
    'wtn.3.30.gz',
    'wtn.3.31.gz',
    'wtn.3.32.gz',
    'wtn.3.33.gz',
    'wtn.3.34.gz',
    'wtn.3.35.gz',
    'wtn.3.36.gz',
    'wtn.3.37.gz',
    'wtn.3.38.gz',
    'wtn.3.39.gz',
    'wtn.3.4.gz',
    'wtn.3.40.gz',
    'wtn.3.41.gz',
    'wtn.3.42.gz',
    'wtn.3.43.gz',
    'wtn.3.44.gz',
    'wtn.3.45.gz',
    'wtn.3.46.gz',
    'wtn.3.47.gz',
    'wtn.3.48.gz',
    'wtn.3.49.gz',
    'wtn.3.5.gz',
    'wtn.3.50.gz',
    'wtn.3.51.gz',
    'wtn.3.52.gz',
    'wtn.3.53.gz',
    'wtn.3.54.gz',
    'wtn.3.55.gz',
    'wtn.3.6.gz',
    'wtn.3.7.gz',
    'wtn.3.8.gz',
    'wtn.3.9.gz',
    'wtn.4.1.gz',
    'wtn.4.10.gz',
    'wtn.4.11.gz',
    'wtn.4.12.gz',
    'wtn.4.13.gz',
    'wtn.4.14.gz',
    'wtn.4.15.gz',
    'wtn.4.16.gz',
    'wtn.4.17.gz',
    'wtn.4.18.gz',
    'wtn.4.19.gz',
    'wtn.4.2.gz',
    'wtn.4.20.gz',
    'wtn.4.21.gz',
    'wtn.4.22.gz',
    'wtn.4.23.gz',
    'wtn.4.24.gz',
    'wtn.4.25.gz',
    'wtn.4.26.gz',
    'wtn.4.27.gz',
    'wtn.4.28.gz',
    'wtn.4.29.gz',
    'wtn.4.3.gz',
    'wtn.4.30.gz',
    'wtn.4.31.gz',
    'wtn.4.32.gz',
    'wtn.4.33.gz',
    'wtn.4.34.gz',
    'wtn.4.35.gz',
    'wtn.4.36.gz',
    'wtn.4.37.gz',
    'wtn.4.38.gz',
    'wtn.4.39.gz',
    'wtn.4.4.gz',
    'wtn.4.40.gz',
    'wtn.4.41.gz',
    'wtn.4.42.gz',
    'wtn.4.43.gz',
    'wtn.4.44.gz',
    'wtn.4.45.gz',
    'wtn.4.46.gz',
    'wtn.4.47.gz',
    'wtn.4.48.gz',
    'wtn.4.49.gz',
    'wtn.4.5.gz',
    'wtn.4.50.gz',
    'wtn.4.51.gz',
    'wtn.4.52.gz',
    'wtn.4.53.gz',
    'wtn.4.54.gz',
    'wtn.4.55.gz',
    'wtn.4.6.gz',
    'wtn.4.7.gz',
    'wtn.4.8.gz',
    'wtn.4.9.gz',
    'wtn.5.1.gz',
    'wtn.5.10.gz',
    'wtn.5.11.gz',
    'wtn.5.12.gz',
    'wtn.5.13.gz',
    'wtn.5.14.gz',
    'wtn.5.15.gz',
    'wtn.5.16.gz',
    'wtn.5.17.gz',
    'wtn.5.18.gz',
    'wtn.5.19.gz',
    'wtn.5.2.gz',
    'wtn.5.20.gz',
    'wtn.5.21.gz',
    'wtn.5.22.gz',
    'wtn.5.23.gz',
    'wtn.5.24.gz',
    'wtn.5.25.gz',
    'wtn.5.26.gz',
    'wtn.5.27.gz',
    'wtn.5.28.gz',
    'wtn.5.29.gz',
    'wtn.5.3.gz',
    'wtn.5.30.gz',
    'wtn.5.31.gz',
    'wtn.5.32.gz',
    'wtn.5.33.gz',
    'wtn.5.34.gz',
    'wtn.5.35.gz',
    'wtn.5.36.gz',
    'wtn.5.37.gz',
    'wtn.5.38.gz',
    'wtn.5.39.gz',
    'wtn.5.4.gz',
    'wtn.5.40.gz',
    'wtn.5.41.gz',
    'wtn.5.42.gz',
    'wtn.5.43.gz',
    'wtn.5.44.gz',
    'wtn.5.45.gz',
    'wtn.5.46.gz',
    'wtn.5.47.gz',
    'wtn.5.48.gz',
    'wtn.5.49.gz',
    'wtn.5.5.gz',
    'wtn.5.50.gz',
    'wtn.5.51.gz',
    'wtn.5.52.gz',
    'wtn.5.53.gz',
    'wtn.5.54.gz',
    'wtn.5.55.gz',
    'wtn.5.6.gz',
    'wtn.5.7.gz',
    'wtn.5.8.gz',
    'wtn.5.9.gz',
    'wtn.6.1.gz',
    'wtn.6.10.gz',
    'wtn.6.11.gz',
    'wtn.6.12.gz',
    'wtn.6.13.gz',
    'wtn.6.14.gz',
    'wtn.6.15.gz',
    'wtn.6.16.gz',
    'wtn.6.17.gz',
    'wtn.6.18.gz',
    'wtn.6.19.gz',
    'wtn.6.2.gz',
    'wtn.6.20.gz',
    'wtn.6.21.gz',
    'wtn.6.22.gz',
    'wtn.6.23.gz',
    'wtn.6.24.gz',
    'wtn.6.25.gz',
    'wtn.6.26.gz',
    'wtn.6.27.gz',
    'wtn.6.28.gz',
    'wtn.6.29.gz',
    'wtn.6.3.gz',
    'wtn.6.30.gz',
    'wtn.6.31.gz',
    'wtn.6.32.gz',
    'wtn.6.33.gz',
    'wtn.6.34.gz',
    'wtn.6.35.gz',
    'wtn.6.36.gz',
    'wtn.6.37.gz',
    'wtn.6.38.gz',
    'wtn.6.39.gz',
    'wtn.6.4.gz',
    'wtn.6.40.gz',
    'wtn.6.41.gz',
    'wtn.6.42.gz',
    'wtn.6.43.gz',
    'wtn.6.44.gz',
    'wtn.6.45.gz',
    'wtn.6.46.gz',
    'wtn.6.47.gz',
    'wtn.6.48.gz',
    'wtn.6.49.gz',
    'wtn.6.5.gz',
    'wtn.6.50.gz',
    'wtn.6.51.gz',
    'wtn.6.52.gz',
    'wtn.6.53.gz',
    'wtn.6.54.gz',
    'wtn.6.55.gz',
    'wtn.6.6.gz',
    'wtn.6.7.gz',
    'wtn.6.8.gz',
    'wtn.6.9.gz',
    'wtn.7.1.gz',
    'wtn.7.10.gz',
    'wtn.7.11.gz',
    'wtn.7.12.gz',
    'wtn.7.13.gz',
    'wtn.7.14.gz',
    'wtn.7.15.gz',
    'wtn.7.16.gz',
    'wtn.7.17.gz',
    'wtn.7.18.gz',
    'wtn.7.19.gz',
    'wtn.7.2.gz',
    'wtn.7.20.gz',
    'wtn.7.21.gz',
    'wtn.7.22.gz',
    'wtn.7.23.gz',
    'wtn.7.24.gz',
    'wtn.7.25.gz',
    'wtn.7.26.gz',
    'wtn.7.27.gz',
    'wtn.7.28.gz',
    'wtn.7.29.gz',
    'wtn.7.3.gz',
    'wtn.7.30.gz',
    'wtn.7.31.gz',
    'wtn.7.32.gz',
    'wtn.7.33.gz',
    'wtn.7.34.gz',
    'wtn.7.35.gz',
    'wtn.7.36.gz',
    'wtn.7.37.gz',
    'wtn.7.38.gz',
    'wtn.7.39.gz',
    'wtn.7.4.gz',
    'wtn.7.40.gz',
    'wtn.7.41.gz',
    'wtn.7.42.gz',
    'wtn.7.43.gz',
    'wtn.7.44.gz',
    'wtn.7.45.gz',
    'wtn.7.46.gz',
    'wtn.7.47.gz',
    'wtn.7.48.gz',
    'wtn.7.49.gz',
    'wtn.7.5.gz',
    'wtn.7.50.gz',
    'wtn.7.51.gz',
    'wtn.7.52.gz',
    'wtn.7.53.gz',
    'wtn.7.54.gz',
    'wtn.7.55.gz',
    'wtn.7.56.gz',
    'wtn.7.6.gz',
    'wtn.7.7.gz',
    'wtn.7.8.gz',
    'wtn.7.9.gz',
    'wtn.8.1.gz',
    'wtn.8.10.gz',
    'wtn.8.11.gz',
    'wtn.8.12.gz',
    'wtn.8.13.gz',
    'wtn.8.14.gz',
    'wtn.8.15.gz',
    'wtn.8.16.gz',
    'wtn.8.17.gz',
    'wtn.8.18.gz',
    'wtn.8.19.gz',
    'wtn.8.2.gz',
    'wtn.8.20.gz',
    'wtn.8.21.gz',
    'wtn.8.22.gz',
    'wtn.8.23.gz',
    'wtn.8.24.gz',
    'wtn.8.25.gz',
    'wtn.8.26.gz',
    'wtn.8.27.gz',
    'wtn.8.28.gz',
    'wtn.8.29.gz',
    'wtn.8.3.gz',
    'wtn.8.30.gz',
    'wtn.8.31.gz',
    'wtn.8.32.gz',
    'wtn.8.33.gz',
    'wtn.8.34.gz',
    'wtn.8.35.gz',
    'wtn.8.36.gz',
    'wtn.8.37.gz',
    'wtn.8.38.gz',
    'wtn.8.39.gz',
    'wtn.8.4.gz',
    'wtn.8.40.gz',
    'wtn.8.41.gz',
    'wtn.8.42.gz',
    'wtn.8.43.gz',
    'wtn.8.44.gz',
    'wtn.8.45.gz',
    'wtn.8.46.gz',
    'wtn.8.47.gz',
    'wtn.8.48.gz',
    'wtn.8.49.gz',
    'wtn.8.5.gz',
    'wtn.8.50.gz',
    'wtn.8.51.gz',
    'wtn.8.52.gz',
    'wtn.8.53.gz',
    'wtn.8.54.gz',
    'wtn.8.55.gz',
    'wtn.8.6.gz',
    'wtn.8.7.gz',
    'wtn.8.8.gz',
    'wtn.8.9.gz',
    'wtn.9.1.gz',
    'wtn.9.10.gz',
    'wtn.9.11.gz',
    'wtn.9.12.gz',
    'wtn.9.13.gz',
    'wtn.9.14.gz',
    'wtn.9.15.gz',
    'wtn.9.16.gz',
    'wtn.9.17.gz',
    'wtn.9.18.gz',
    'wtn.9.19.gz',
    'wtn.9.2.gz',
    'wtn.9.20.gz',
    'wtn.9.21.gz',
    'wtn.9.22.gz',
    'wtn.9.23.gz',
    'wtn.9.24.gz',
    'wtn.9.25.gz',
    'wtn.9.26.gz',
    'wtn.9.27.gz',
    'wtn.9.28.gz',
    'wtn.9.29.gz',
    'wtn.9.3.gz',
    'wtn.9.30.gz',
    'wtn.9.31.gz',
    'wtn.9.32.gz',
    'wtn.9.33.gz',
    'wtn.9.34.gz',
    'wtn.9.35.gz',
    'wtn.9.36.gz',
    'wtn.9.37.gz',
    'wtn.9.38.gz',
    'wtn.9.39.gz',
    'wtn.9.4.gz',
    'wtn.9.40.gz',
    'wtn.9.41.gz',
    'wtn.9.42.gz',
    'wtn.9.43.gz',
    'wtn.9.44.gz',
    'wtn.9.45.gz',
    'wtn.9.46.gz',
    'wtn.9.47.gz',
    'wtn.9.48.gz',
    'wtn.9.49.gz',
    'wtn.9.5.gz',
    'wtn.9.50.gz',
    'wtn.9.51.gz',
    'wtn.9.52.gz',
    'wtn.9.53.gz',
    'wtn.9.54.gz',
    'wtn.9.55.gz',
    'wtn.9.6.gz',
    'wtn.9.7.gz',
    'wtn.9.8.gz',
    'wtn.9.9.gz']



    # import_csv_work_tapes(base_dir=base_dir, out_base_dir=out_base_dir_full,filenames=['wtn.9.9.gz'])
    import_csv_work_tapes(base_dir=base_dir, out_base_dir=out_base_dir_full,filenames=['wtn.19.45.gz'])


