##############################################################################
#
# Copyright (c) 1996-1998, Digital Creations, Fredericksburg, VA, USA.
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
#   o Redistributions of source code must retain the above copyright
#     notice, this list of conditions, and the disclaimer that follows.
# 
#   o Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions, and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
# 
#   o All advertising materials mentioning features or use of this
#     software must display the following acknowledgement:
# 
#       This product includes software developed by Digital Creations
#       and its contributors.
# 
#   o Neither the name of Digital Creations nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
# 
# 
# THIS SOFTWARE IS PROVIDED BY DIGITAL CREATIONS AND CONTRIBUTORS *AS IS*
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL DIGITAL
# CREATIONS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
# OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
# TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
# DAMAGE.
#
# 
# If you have questions regarding this software, contact:
#
#   Digital Creations, L.C.
#   910 Princess Ann Street
#   Fredericksburge, Virginia  22401
#
#   info@digicool.com
#
#   (540) 371-6909
#
##############################################################################
from DocumentTemplate import HTML, HTMLFile, String, File

def d(**kw): return kw

class D:
    def __init__(self, **kw):
        for k, v in kw.items(): self.__dict__[k]=v

    def __repr__(self): return "D(%s)" % `self.__dict__`

xxx=(D(name=1), D(name=2), D(name=3))
data=(
    d(name='jim', age=39),
    d(name='kak', age=29),
    d(name='will', age=8),
    d(name='andrew', age=5),
    d(name='chessie',age=2),
    )

html="""
<!--#in data mapping-->
  <!--#var name-->, <!--#var age-->
<!--#else-->
  <!--#in xxx    -->
    <!--#var name-->
  <!--#/in-->
  Sorry, no data
<!--#/in-->
"""

print '='*74
print HTML(html)(data=data, xxx=xxx)
print '='*74
print HTML(html)(xxx=xxx)
print '='*74

s="""
%(in data mapping)[
  %(name)s, %(age)s
%(else)[
  %(in xxx)[
    %(name)s
  %(in)]
  Sorry, no data
%(in)]
"""

print '='*74
print String(s)(data=data, xxx=xxx)
print '='*74
print String(s)(xxx=xxx)
print '='*74
