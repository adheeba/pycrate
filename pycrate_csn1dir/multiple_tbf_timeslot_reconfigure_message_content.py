# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.3
# *
# * Copyright 2018. Benoit Michau. ANSSI.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/multiple_tbf_timeslot_reconfigure_message_content.py
# * Created : 2018-07-30
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.31a Multiple TBF Timeslot Reconfigure
# top-level object: Multiple TBF Timeslot Reconfigure message content

# external references
from pycrate_csn1dir.pulse_format_ie import pulse_format_ie
from pycrate_csn1dir.egprs_window_size_ie import egprs_window_size_ie
from pycrate_csn1dir.global_tfi_ie import global_tfi_ie
from pycrate_csn1dir.starting_frame_number_description_ie import starting_frame_number_description_ie
from pycrate_csn1dir.dual_carrier_frequency_parameters_ie import dual_carrier_frequency_parameters_ie
from pycrate_csn1dir.egprs_level_ie import egprs_level_ie
from pycrate_csn1dir.egprs_modulation_and_coding_scheme_ie import egprs_modulation_and_coding_scheme_ie
from pycrate_csn1dir.global_packet_timing_advance_ie import global_packet_timing_advance_ie
from pycrate_csn1dir.padding_bits import padding_bits
from pycrate_csn1dir.frequency_parameters_ie import frequency_parameters_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

uplink_tbf_assignment_2_struct = CSN1List(name='uplink_tbf_assignment_2_struct', list=[
  CSN1Bit(name='pfi', bit=7),
  CSN1Bit(name='rlc_mode'),
  CSN1Bit(name='tfi_assignment', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='egprs_channel_coding_command', obj=egprs_modulation_and_coding_scheme_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='egprs_window_size', obj=egprs_window_size_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='npm_transfer_time', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='reported_timeslots_c1', bit=8),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='reported_timeslots_c2', bit=8)])})])}),
  CSN1Bit(name='usf_granularity'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='tbf_timeslot_allocation', bit=('# unprocessed: (N)', lambda: 0))])}),
  CSN1List(list=[
    CSN1Val(name='', val='0'),
    CSN1Bit(name='usf_allocation_c1', bit=3),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='usf_allocation_c2', bit=3)])}),
    CSN1Bit(name='usf_allocation', bit=3),
    CSN1Alt(num=('# unprocessed: (M-1)', lambda: 0), alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='usf_allocation', bit=3)])})])])

timeslot_description_struct = CSN1Alt(name='timeslot_description_struct', alt={
  '0': ('', [
  CSN1Bit(name='ms_timeslot_allocation', bit=8)]),
  '1': ('', [
  CSN1Bit(name='alpha', bit=4),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn0', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn3', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn4', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn5', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn6', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn7', bit=5)])})])})

assignment_info_struct = CSN1List(name='assignment_info_struct', list=[
  CSN1Bit(name='assignment_type', bit=2),
  CSN1Bit(name='carrier_id')])

downlink_tbf_assignment_2_struct = CSN1List(name='downlink_tbf_assignment_2_struct', list=[
  CSN1Bit(name='pfi', bit=7),
  CSN1Bit(name='rlc_mode'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='uplink_control_timeslot_c1', bit=3)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='uplink_control_timeslot_c2', bit=3)])}),
  CSN1Bit(name='tfi_assignment', bit=5),
  CSN1Bit(name='control_ack'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='npm_transfer_time', bit=5)])}),
  CSN1Bit(name='event_based_fanr'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='downlink_egprs_window_size', obj=egprs_window_size_ie)])})])

downlink_tbf_assignment_struct = CSN1List(name='downlink_tbf_assignment_struct', list=[
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='rb_id', bit=5)]),
    '1': ('', [
    CSN1Bit(name='pfi', bit=7),
    CSN1Bit(name='rlc_mode')])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='uplink_control_timeslot', bit=3)])}),
  CSN1Bit(name='tfi_assignment', bit=5),
  CSN1Bit(name='control_ack'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='downlink_egprs_window_size', obj=egprs_window_size_ie)])})])

uplink_tbf_assignment_struct = CSN1List(name='uplink_tbf_assignment_struct', list=[
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='rb_id', bit=5)]),
    '1': ('', [
    CSN1Bit(name='pfi', bit=7),
    CSN1Bit(name='rlc_mode')])}),
  CSN1Bit(name='tfi_assignment', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='channel_coding_command', bit=2)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='egprs_channel_coding_command', obj=egprs_modulation_and_coding_scheme_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='uplink_egprs_window_size', obj=egprs_window_size_ie)])}),
  CSN1Bit(name='usf_granularity'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='tbf_timeslot_allocation', bit=('# unprocessed: (N)', lambda: 0))])}),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='usf_allocation', bit=3)]),
    '1': ('', [
    CSN1Bit(name='usf_allocation', bit=3),
    CSN1Alt(num=('# unprocessed: (M-1)', lambda: 0), alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='usf_allocation', bit=3)])})])})])

timeslot_description_2_struct = CSN1Alt(name='timeslot_description_2_struct', alt={
  '0': ('', [
  CSN1Bit(name='ms_timeslot_allocation_c1', bit=8),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='ms_timeslot_allocation_c2', bit=8)])})]),
  '1': ('', [
  CSN1Bit(name='alpha_c1', bit=4),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn0_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn1_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn2_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn3_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn4_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn5_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn6_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn7_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='alpha_c2', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn0_c2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn1_c2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn2_c2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn3_c2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn4_c2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn5_c2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn6_c2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn7_c2', bit=5)])})])})

rtti_multiple_downlink_assignment_dc_struct = CSN1List(name='rtti_multiple_downlink_assignment_dc_struct', list=[
  CSN1Bit(name='rtti_downlink_pdch_pair_assignment_dc', bit=8),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='uplink_control_timeslot_c1', bit=3)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='uplink_control_timeslot_c2', bit=3)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='downlink_tbf_assignment', obj=downlink_tbf_assignment_2_struct)]),
  CSN1Val(name='', val='0')])

multiple_uplink_assignment_2_struct = CSN1List(name='multiple_uplink_assignment_2_struct', list=[
  CSN1Bit(name='extended_dynamic_allocation'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='p0_c1', bit=4),
    CSN1Bit(name='pr_mode_c1'),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='p0_c2', bit=4),
      CSN1Bit(name='pr_mode_c2')])})])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='tsh', bit=2)])})])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='global_timeslot_description', obj=timeslot_description_2_struct),
      CSN1List(num=-1, list=[
        CSN1Val(name='', val='1'),
        CSN1Ref(name='uplink_tbf_assignment', obj=uplink_tbf_assignment_2_struct)]),
      CSN1Val(name='', val='0')])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='alpha_c1', bit=4),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='alpha_c2', bit=4)])}),
        CSN1Bit(name='n_pairs', bit=3),
        CSN1Alt(num=([3], lambda x: x + 1), alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='gamma', bit=5)])}),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Alt(num=([-1, 3], lambda x: x + 1), alt={
            '0': ('', []),
            '1': ('', [
            CSN1Bit(name='gamma', bit=5)])})])})])}),
      CSN1List(num=-1, list=[
        CSN1Val(name='', val='1'),
        CSN1Ref(name='uplink_tbf_assignment', obj=uplink_tbf_assignment_2_struct),
        CSN1Bit(name='rtti_usf_mode')]),
      CSN1Val(name='', val='0')])})])})])

btti_multiple_downlink_assignment_struct = CSN1List(name='btti_multiple_downlink_assignment_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='timeslot_allocation_c1', bit=8)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='timeslot_allocation_c2', bit=8)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='uplink_control_timeslot_c1', bit=3)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='uplink_control_timeslot_c2', bit=3)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='downlink_tbf_assignment', obj=downlink_tbf_assignment_2_struct)]),
  CSN1Val(name='', val='0')])

multiple_downlink_assignment_struct = CSN1List(name='multiple_downlink_assignment_struct', list=[
  CSN1Bit(name='timeslot_allocation', bit=8),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='uplink_control_timeslot', bit=3)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='downlink_tbf_assignment', obj=downlink_tbf_assignment_struct)]),
  CSN1Val(name='', val='0')])

rtti_multiple_downlink_assignment_sc_struct = CSN1List(name='rtti_multiple_downlink_assignment_sc_struct', list=[
  CSN1Bit(name='rtti_downlink_pdch_pair_assignment_sc', bit=4),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='uplink_control_timeslot_c1', bit=3)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='downlink_tbf_assignment', obj=downlink_tbf_assignment_2_struct)]),
  CSN1Val(name='', val='0')])

multiple_uplink_assignment_struct = CSN1List(name='multiple_uplink_assignment_struct', list=[
  CSN1Bit(name='extended_dynamic_allocation'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='p0', bit=4),
    CSN1Bit(name='pr_mode')])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='tbf_starting_time', obj=starting_frame_number_description_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='global_timeslot_description', obj=timeslot_description_struct),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Ref(name='uplink_tbf_assignment', obj=uplink_tbf_assignment_struct)]),
    CSN1Val(name='', val='0')])})])

multiple_tbf_timeslot_reconfigure_message_content = CSN1List(name='multiple_tbf_timeslot_reconfigure_message_content', list=[
  CSN1Bit(name='page_mode', bit=2),
  CSN1List(list=[
    CSN1Val(name='', val='0'),
    CSN1Ref(name='global_tfi', obj=global_tfi_ie),
    CSN1Alt(alt={
      '0': ('', [
      CSN1List(list=[
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='channel_coding_command', bit=2)])}),
        CSN1Ref(name='global_packet_timing_advance', obj=global_packet_timing_advance_ie),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Ref(name='frequency_parameters', obj=frequency_parameters_ie)])}),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='packet_extended_timing_advance', bit=2)])}),
        CSN1List(num=-1, list=[
          CSN1Val(name='', val='1'),
          CSN1Ref(name='multiple_downlink_assignment', obj=multiple_downlink_assignment_struct)]),
        CSN1Val(name='', val='0'),
        CSN1Ref(name='multiple_uplink_assignment', obj=multiple_uplink_assignment_struct),
        CSN1Ref(obj=padding_bits)])]),
      '1': ('', [
      CSN1Alt(alt={
        '00': ('', [
        CSN1List(list=[
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='egprs_channel_coding_command', obj=egprs_modulation_and_coding_scheme_ie)])}),
          CSN1Bit(name='resegment'),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='downlink_egprs_window_size', obj=egprs_window_size_ie)])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Ref(name='uplink_egprs_window_size', obj=egprs_window_size_ie)])}),
            CSN1Bit(name='link_quality_measurement_mode', bit=2),
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Bit(name='bep_period2', bit=4)])})])}),
          CSN1Ref(name='global_packet_timing_advance', obj=global_packet_timing_advance_ie),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Bit(name='packet_extended_timing_advance', bit=2)])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='frequency_parameters', obj=frequency_parameters_ie)])}),
          CSN1List(num=-1, list=[
            CSN1Val(name='', val='1'),
            CSN1Ref(name='multiple_downlink_assignment', obj=multiple_downlink_assignment_struct)]),
          CSN1Val(name='', val='0'),
          CSN1Ref(name='multiple_uplink_assignment', obj=multiple_uplink_assignment_struct),
          CSN1Alt(alt={
            '0': ('', [
            CSN1Bit(bit=-1)]),
            '1': ('', [
            CSN1Alt(num=-1, alt={
              '0': ('', []),
              '1': ('', [
              CSN1Bit(name='npm_transfer_time', bit=5)])}),
            CSN1Val(name='', val='0'),
            CSN1Alt(alt={
              '0': ('', [
              CSN1Bit(bit=-1)]),
              '1': ('', [
              CSN1Bit(name='indication_of_upper_layer_pdu_start_for_rlc_um', num=-1),
              CSN1Val(name='', val='0'),
              CSN1Bit(name='enhanced_flexible_timeslot_assignment'),
              CSN1Ref(obj=padding_bits)]),
              None: ('', [])})]),
            None: ('', [])})])]),
        '01': ('', [
        CSN1List(list=[
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='egprs_channel_coding_command', obj=egprs_modulation_and_coding_scheme_ie)])}),
          CSN1Bit(name='resegment'),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='downlink_egprs_window_size', obj=egprs_window_size_ie)])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Ref(name='uplink_egprs_window_size', obj=egprs_window_size_ie)])}),
            CSN1Bit(name='link_quality_measurement_mode', bit=2),
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Bit(name='bep_period2', bit=4)])})])}),
          CSN1Ref(name='global_packet_timing_advance', obj=global_packet_timing_advance_ie),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Bit(name='packet_extended_timing_advance', bit=2)])}),
          CSN1Alt(alt={
            '00': ('', []),
            '01': ('', [
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Ref(name='frequency_parameters_c1', obj=frequency_parameters_ie)])}),
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Ref(name='frequency_parameters_c2', obj=frequency_parameters_ie)])})]),
            '10': ('', [
            CSN1Ref(name='dual_carrier_frequency_parameters', obj=dual_carrier_frequency_parameters_ie)])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Bit(name='fanr'),
            CSN1List(num=-1, list=[
              CSN1Val(name='', val='1'),
              CSN1Ref(name='btti_multiple_downlink_assignment', obj=btti_multiple_downlink_assignment_struct)]),
            CSN1Val(name='', val='0')])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Alt(alt={
              '0': ('', [
              CSN1Alt(alt={
                '00': ('', []),
                '01': ('', []),
                '10': ('', [
                CSN1Bit(name='downlink_pdch_pairs_c1', bit=8),
                CSN1Bit(name='uplink_pdch_pairs_c1', bit=8)])}),
              CSN1List(num=-1, list=[
                CSN1Val(name='', val='1'),
                CSN1Ref(name='rtti_multiple_downlink_assignment_sc', obj=rtti_multiple_downlink_assignment_sc_struct)]),
              CSN1Val(name='', val='0')]),
              '1': ('', [
              CSN1Alt(alt={
                '00': ('', []),
                '01': ('', []),
                '10': ('', [
                CSN1Bit(name='downlink_pdch_pairs_c1', bit=8),
                CSN1Bit(name='downlink_pdch_pairs_c2', bit=8),
                CSN1Bit(name='uplink_pdch_pairs_c1', bit=8),
                CSN1Bit(name='uplink_pdch_pairs_c2', bit=8)])}),
              CSN1List(num=-1, list=[
                CSN1Val(name='', val='1'),
                CSN1Ref(name='rtti_multiple_downlink_assignment_dc', obj=rtti_multiple_downlink_assignment_dc_struct)]),
              CSN1Val(name='', val='0')])})])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='multiple_uplink_assignment', obj=multiple_uplink_assignment_2_struct)])}),
          CSN1Ref(name='uplink_egprs_level', obj=egprs_level_ie),
          CSN1Ref(name='downlink_egprs_level', obj=egprs_level_ie),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='pulse_format', obj=pulse_format_ie)])}),
          CSN1Alt(alt={
            '0': ('', [
            CSN1Bit(bit=-1)]),
            '1': ('', [
            CSN1Bit(name='indication_of_upper_layer_pdu_start_for_rlc_um', num=-1),
            CSN1Val(name='', val='0'),
            CSN1Bit(name='enhanced_flexible_timeslot_assignment'),
            CSN1Ref(obj=padding_bits)]),
            None: ('', [])})])])})])})])])
