FILE = r'bilingual'

# title for the columns of the source/target language
SOURCE_COL = 'zh'
TARGET_COL = 'ja'

FONT_COLOR = 'd9d5d6'
BACKGROUND_COLOR = '322b28'
# characters that marks the in-text scripts
DELIMITER = ('[', ']', '-')
PLACEHOLDER = ('{', '}')
SP_CHAR = ['$', '_', '|']
BACKSLASH = '\\'

ROW_OFFSET = 2

# escape sequences
ESCAPE_CHAR = {'n': '\n', 'r': '\r', 't': '\t', 'b': '\b', 'f': '\f'}

# html stuffs
TAG_P = '<p class="textbox" style="color:#' + FONT_COLOR + ';">'
TAG_CLOSE = {'h': '</h>', 'p': '</p>', 'html': '</html>'}
NEWLINE = '<br>'
LINK = '<!DOCTYPE html><html><head>' \
       '<link rel= "stylesheet" type= "text/css" href= "{{ url_for(\'static\',filename=\'styles/main.css\') }}">' \
       '</head>'
div = ['<div class="parent">', '<div class="child0">', '<div class="child1">', '</div>']

# test strings
test0 = str('\n')
test1 = r'$$[57ea57]意地っ張りな少年{0}[-]と農場のことを尋ねる'
test2 = '[de2524][デビアス]を開放{開放した}した後に\n受注可能[-]$$$町にいる[57ea57]{0}[-]を探そう{abcdefg}'
test3 = '[57ea57][57ea57]part0[-] part1 [57ea57]part2[de2524]part3[-][-]'
test4 = '[57ea57]part0[-]'
test5 = '[57ea57][de2524]part0[-][-]'
test6 = '[57ea57]part0[-][de2524]part1[-]'
test7 = '[57ea57]part0[de2524]part1[-]part2[abc123]part3[-]part4[-]npart5'
test8 = '[57ea57]part0[de2524]part1[-][-][de2524]part2[-]'
test9 = '[aaa111]p0[bbb222]p1[ccc333]p2[ddd444]p3[-]p4[-]p5[-][-]'
