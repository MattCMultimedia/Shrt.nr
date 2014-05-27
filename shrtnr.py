import sys
import mappings


if (len(sys.argv) < 2):
    print("Requires input string as first argument.")
    exit(1)


inString = unicode(sys.argv[1])
print 'IN ', inString, len(inString)

for normalText, specialText in mappings.unicodeHashMap.iteritems():
    if normalText in inString:
        inString = inString.replace(normalText, specialText)

print "OUT", inString, len(inString)