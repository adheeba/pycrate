# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2018. Benoit Michau. ANSSI. P1sec.
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
# * File Name : pycrate_csn1dir/p3_rest_octets.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.25 P3 Rest Octets
# top-level object: P3 Rest Octets



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

priority = CSN1Bit(name='priority', bit=3)

p3_rest_octets = CSN1List(name='p3_rest_octets', list=[
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='cn3', bit=2),
    CSN1Bit(name='cn4', bit=2)]),
    'L': ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='nln_pch', bit=2),
    CSN1Bit(name='nln_status_pch')]),
    'L': ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Ref(name='priority1', obj=priority)]),
    'L': ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Ref(name='priority2', obj=priority)]),
    'L': ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Ref(name='priority3', obj=priority)]),
    'L': ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Ref(name='priority4', obj=priority)]),
    'L': ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='implicit_reject_cs'),
    CSN1Bit(name='implicit_reject_ps')]),
    'L': ('', []),
    None: ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='ipa_support')]),
    'L': ('', []),
    None: ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='peo_bcch_change_mark', bit=2),
    CSN1Bit(name='rcc', bit=3)]),
    'L': ('', []),
    None: ('', [])}),
  CSN1Ref(obj=spare_padding)])

