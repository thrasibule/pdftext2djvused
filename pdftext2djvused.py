import sys
from xml.etree import ElementTree as ET

document = ET.parse(sys.argv[1])
ns = 'http://www.w3.org/1999/xhtml'
dpi = 300
#djvu coordinates are in pixels and computed from the bottom left corner
for page in document.findall('.//{{{0}}}page'.format(ns)):
    djvuheight = float(page.attrib['height']) * dpi / 72
    djvuwidth = float(page.attrib['width']) * dpi / 72
    print '( page 0 0 {0} {1}'.format(int(djvuwidth), int(djvuheight))
    for word in page.getchildren():
        djvuxmin = float(word.attrib['xMin']) * dpi /72
        djvuxmax = float(word.attrib['xMax']) * dpi /72
        djvuymin = (float(page.attrib['height']) - float(word.attrib['yMax'])) * dpi /72
        djvuymax = (float(page.attrib['height']) - float(word.attrib['yMin'])) * dpi /72
        print '( word {0} {1} {2} {3} \"{4}\")'.format(int(djvuxmin), int(djvuymin), int(djvuxmax), int(djvuymax), word.text)
