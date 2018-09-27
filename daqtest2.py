# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 03:06:37 2017

@author: Ben
"""

# Copyright (c) 2005-2006, California Institute of Technology
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:

#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.

#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.

#     * Neither the name of the California Institute of Technology nor
#       the names of its contributors may be used to endorse or promote
#       products derived from this software without specific prior
#       written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Author: Andrew Straw

import UniversalLibrary as UL
import numpy

BoardNum = 0
UDStat = 0
Gain = UL.BIP5VOLTS

LowChan = 0
HighChan = 0

Count = 20
Rate = 3125

Options = UL.CONVERTDATA + UL.BACKGROUND + UL.SINGLEIO
ADData = numpy.zeros((Count,), dtype=numpy.int16)
Rate = UL.cbAInScan(BoardNum, LowChan, HighChan, Count,
                    Rate, Gain, ADData, Options)

Status = UL.RUNNING
CurCount = 0
CurIndex =0
while Status==UL.RUNNING:
    Status, CurCount, CurIndex = UL.cbGetStatus(BoardNum, Status, CurCount, CurIndex, UL.AIFUNCTION)