from lxml import etree

with open('./books.xml', 'r') as fh:
    txt = fh.read()

exp = u'//book/title/text()'
sel = etree.HTML(txt)
print(sel.xpath(exp))
