#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# sendmail.py
#
import string, smtplib

#server = smtplib.SMTP('localhost')
server = smtplib.SMTP( 'webmail.cadiware.ch' )
#server.set_debuglevel( 1 )

body = """From: %s
To: %s
Subject: f�delsedagsfest med fullm�ne 26.11

hejsan %s,

jag firar min f�delsedag p� fredag den 26.11,
som dessutom r�kar vara en fullm�ne.

jag bj�d in micke treis, som ju inte bor s� l�ngt bort,
och han fr�gade mig om jag bjudit in n�gra andra fr�n
klassen. det hade jag faktiskt inte, men eftersom det 
l�ter som en bra idee g�r jag det nu.

jag skulle allts� tycka det vore j�ttekul att se dig h�r 
i l�rrach n�ra basel in sydv�stra h�rnet av tyskland
den 26.11, om du har lust och tid.

annars ser jag fram emot n�gon annan tr�ff n�gon 
annanstans i st�llet.

jag �nskar dig en underbar h�st!

jerre
"""

fromaddr = 'jeremy@redcor.ch'

f = open( 'addr_klassentreffen_2002.txt' )
lines = f.readlines()
for line in map( string.strip, lines ):
  if '#' == line[0]: continue
  name, toaddr = map( string.strip, line.split( ':' ) )
  print "send message to '%s' at '%s'" % (name, toaddr)
  msg = body % (fromaddr, toaddr, name)
  server.sendmail( fromaddr, (toaddr,), msg )
  
server.quit()
