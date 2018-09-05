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
Subject: födelsedagsfest med fullmåne 26.11

hejsan %s,

jag firar min födelsedag på fredag den 26.11,
som dessutom råkar vara en fullmåne.

jag bjöd in micke treis, som ju inte bor så långt bort,
och han frågade mig om jag bjudit in några andra från
klassen. det hade jag faktiskt inte, men eftersom det 
låter som en bra idee gör jag det nu.

jag skulle alltså tycka det vore jättekul att se dig här 
i lörrach nära basel in sydvästra hörnet av tyskland
den 26.11, om du har lust och tid.

annars ser jag fram emot någon annan träff någon 
annanstans i stället.

jag önskar dig en underbar höst!

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
