import sys
import mappings

try:
    if not sys.argv[1]:
        print("Requires input string.")
        exit(1)
except Exception, e:
    print(e)
    exit(1)


inString = unicode(sys.argv[1])
print inString, len(inString)

for normalText, specialText in mappings.unicodeHashMap.iteritems():
    if normalText in inString:
        inString = inString.replace(normalText, specialText)

print "->", inString, len(inString)