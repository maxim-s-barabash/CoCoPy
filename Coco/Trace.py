#-------------------------------------------------------------------------
#Trace.py -- Trace file generation routines
#Compiler Generator Coco/R,
#Copyright (c) 1990, 2004 Hanspeter Moessenboeck, University of Linz
#extended by M. Loeberbauer & A. Woess, Univ. of Linz
#ported from Java to Python by Ronald Longo
#
#This program is free software; you can redistribute it and/or modify it
#under the terms of the GNU General Public License as published by the
#Free Software Foundation; either version 2, or (at your option) any
#later version.
#
#This program is distributed in the hope that it will be useful, but
#WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
#for more details.
#
#You should have received a copy of the GNU General Public License along
#with this program; if not, write to the Free Software Foundation, Inc.,
#59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
#As an exception, it is allowed to write an extension of Coco/R that is
#used as a plugin in non-free software.
#
#If not otherwise stated, any source code generated by Coco/R (other than
#Coco/R itself) does not fall under the GNU General Public License.
#-------------------------------------------------------------------------*/

import os.path

class Trace( object ):
   fileName = ''
   trace    = None

   @staticmethod
   def Init( dir ):
      assert isinstance( dir, str )
      Trace.fileName = os.path.join( dir, 'trace.txt' )
      try:
         Trace.trace = open(Trace.fileName, 'wt', encoding="utf-8")
      except IOError:
         raise RuntimeError( '-- Compiler Error: could not open ' + Trace.fileName )

   @staticmethod
   def formatString( s:str, w:int ):
      ''' Returns a string with a minimum length of |w| characters
      the string is left-adjusted if w < 0 and right-adjusted otherwise'''
      assert isinstance( s, str )
      assert isinstance( w, int )

      size = len(s)
      b = ''
      if w >= 0:
         b += ' ' * (w - size)
         return b + s
      else:
         for i in range( w, -size ):
            b += ' '
         return s + b

   @staticmethod
   def Write( s:str, w:int=None ):
      '''writes a string with a maximum length of |w| characters'''
      assert isinstance( s, str )
      assert isinstance( w, int ) or (w is None)
      if w is None:
         Trace.trace.write( s )
      else:
         Trace.trace.write( Trace.formatString( s, w ) )

   @staticmethod
   def WriteLine( s:str=None, w:int=None ):
      assert isinstance( s, str ) or (s is None)
      assert isinstance( w, int ) or (w is None)
      if s is not None:
         if w is not None:
            Trace.trace.write( Trace.formatString( s, w ) )
         else:
            Trace.trace.write( s )

      Trace.trace.write( '\n' )

   @staticmethod
   def Close( ):
      Trace.trace.close( )
      stat = os.stat( Trace.fileName )
      if stat.st_size == 0:
         os.remove( Trace.fileName )
      else:
         print()
         print('trace output is in', os.path.basename(Trace.fileName))
