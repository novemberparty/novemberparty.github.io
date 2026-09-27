emails = []
f = open( 'emil.txt' )
lines = f.readlines()
f.close()
for line in lines:
  emil = line.split( ':' )[1].strip()
  #emil = emil.replace( ' ', '\n' )
  #print emil
  for emil2 in emil.split():
    emails.append( emil2 )
emails.sort()
print '\nemil:'
for emil in emails:
  print emil

emails2 = []
f = open( 'emilg.txt' )
lines = f.readlines()
f.close()
for line in lines:
  emil = line.strip()
  emails2.append( emil )
emails2.sort()
print '\nemilg:'
for emil in emails2:
  print emil

print '\nmissing:'
for emil in emails2:
  if emil.lower() not in emails:
    print emil

