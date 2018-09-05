#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# sendmail.py -- send personally addressed emails to a list of people
#
# jeremy tammik, autodesk consulting, 2005-10-24
#
import string, smtplib

##server = smtplib.SMTP('localhost')
#server = smtplib.SMTP( 'webmail.cadiware.ch' )
server = smtplib.SMTP( 'pop.aemmenet.ch' )
##server.set_debuglevel( 1 )

#body = """From: jeremy@redcor.ch
#Reply-To: %s

body = """From: %s
To: %s
Subject: birthday party 26.11

dear %s,

jag firar min födelsedag på lördag den 26.11.

i'm celebrating my birthday saturday 26.11.

ich feiere am samstag den 26.11 geburtstag.

i would love to see you then!

i am celebrating with food, wine, song, men and women, and anything else that comes along.

food and drink is provided, as well as a nice big warm fire.

musical inspiration and contributions to the buffet are welcome.

i'll be around all day, so you can come and go when you like. 

i do expect most people to be there in the evening, though.

whether i see you or not, i wish you a wonderful autumn!

best regards,

jeremy
--
Huenerbergweg 30 -- 79539 Loerrach -- +49-7621-44175
"""

#fromaddr = 'jeremy.tammik@eur.autodesk.com'
fromaddr = 'jeremy@redcor.ch'

f = open( 'invite1.txt' )
lines = f.readlines()
f.close()

#f = open( 'addr_klassentreffen_2002.txt' )
#lines = f.readlines()
#f.close()

#f = open( 'invite.txt' )
#lines.extend( f.readlines() )
#f.close()

for line in map( string.strip, lines ):
  if '#' == line[0]: continue
  name, toaddr = map( string.strip, line.split( ':' ) )
  first = name.split()[0].strip()
  assert ',' not in toaddr, toaddr
  assert ';' not in toaddr, toaddr
  toaddr = toaddr.split()
  print "send message to '%s' at '%s'" % (first, toaddr)
  for to in toaddr:
    msg = body % (fromaddr, to, first)
    print msg
    server.sendmail( fromaddr, (to,), msg )
  
server.quit()
