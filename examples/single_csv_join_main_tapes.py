#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Run csv_join_work_tapes and view the results (usually for a single day
and station). Works for work tapes or main tapes. 

:copyright:
    The PDART Development Team & Ceri Nunn
:license:
    GNU Lesser General Public License, Version 3
    (https://www.gnu.org/copyleft/lesser.html)
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA
from pdart.csv_join_work_tapes import call_csv_join_work_tapes
# from pdart.view import plot_from_stream
from obspy.core.stream import read
import pdart.config as config
from pdart.extra_plots.plot_timing_divergence import plot_timing_from_dir
from obspy.core.utcdatetime import UTCDateTime 


import logging
# logging.handlers

import pandas as pd
import numpy as np

def run_csv_join_work_tapes():
    processed_dir='/Users/cnunn/lunar_data/PDART_PROCESSED'
    join_dir='/Users/cnunn/lunar_data/tmp_PDART'
    log_dir='/Users/cnunn/lunar_data/tmp_PDART_LOG'

    config.combine_ground_stations=True
    config.clean_spikes=True
    print('MAKE SURE THAT THESE ARE RERUN PROPERLY ')
    config.fix_jump_error = True
    config.fix_clock_error = True 

    print('log dir: ', log_dir)

    # if true, run call_csv_join_work_tapes
    # set run_single=False and plot_timing=True to see the current version
    run_single=True

    # if true, plot the timing
    plot_timing=True

    year=1974
    day=103
    stations=['S12','S14','S15','S16']

    if run_single:
        config.view_corrected_traces = False
        call_csv_join_work_tapes(
        processed_dir=processed_dir,
        join_dir=join_dir,
        log_dir=log_dir,
        year_start=year,
        year_end=year,
        day_start=day,
        day_end=day,
        stations=stations,
        manual_clock_correction='../manual_fix_files/manual_clock_fix.csv',
        manual_jump_correction='../manual_fix_files/manual_jump_fix.csv',
        manual_exclude='../manual_fix_files/manual_exclude.csv',
        manual_grab_before='../manual_fix_files/manual_grab_before.csv',
        manual_grab_after='../manual_fix_files/manual_grab_after.csv',
        logging_level=logging.DEBUG)

    if plot_timing:
        plot_timing_from_dir(top_level_dir=join_dir, start_time=UTCDateTime(year=year,julday=day), stations=stations, include_line=True, out_dir='../extra_plots_output', save_fig=False, plot_fig=True)


if __name__ == "__main__":    
    run_csv_join_work_tapes()
