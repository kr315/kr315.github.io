import os
os.chdir('/Users/kr315/Desktop/_dev/kr315.github.io/lumistone')
newline = '\n'

subpages = {
    # 'index'     : 'o mnie',
    'galeria/index'    : 'galeria',
    'catalogue/index'    : 'katalog',
    # 'contact'   : 'kontakt'
}

# _??? variables are replace-values for snippets 
_page_title = 'Lumi Stone'
_description = 'illuminated stones'
_canonical_address = 'https://lumistone.pl'

_menu = '| '
for item_page, item_name in subpages.items():
    _menu += f'<span><a href="{item_page}.html">{item_name}</a></span> | '

# read 'begin.html' snippet
with open('snippets/begin.html', 'r') as file:
    begin_html = f"{file.read().replace(newline, '')}".format(**locals())

# generate menu from subpages list
with open('snippets/menu.html', 'r') as file:
    menu_html = f"{file.read().replace(newline, '')}".format(**locals())

# read 'end.html' snippet
with open('snippets/end.html', 'r') as file:
    end_html = f"{file.read().replace(newline, '')}".format(**locals())

# create content for each page
pass

def create_galeria():
    # generate image list, paths, description
    images_list = []
    for filename in os.listdir('galeria'):
        if filename.endswith('jpeg'):
            images_list.append(filename)
    images_list.sort()
    galeria_html = ''
    for img in images_list:
        print(img)
        current_index = images_list.index(img)
        if current_index + 1 == len(images_list):
            next = images_list[0]
        else:
            next = images_list[current_index+1]
        prev = images_list[current_index-1]
        img_html_code = begin_html
        img_html_code += f'<table class="viewer"><tbody>\
            <tr><td><a href="{prev}.html">&lt;&lt;</a></td><td><a href="index.html">powrót</a></td><td><a href="{next}.html">&gt;&gt;</a></td></tr>\
            <tr><td colspan="3"><img src="{img}" class="preview"></td></tr>\
            </tbody></table>'
        img_html_code += end_html
        with open(f'galeria/{img}.html', 'w') as img_html_page:
            img_html_page.write(img_html_code)
        galeria_html += f'<a href="{img}.html"><img src="{img}" class="thumbnail"></a>\n'
    return galeria_html


def create_catalogue():
    # in portfolio_directory, there should be pairs of pict
    portfolio_directory = 'catalogue'
    
    portfolio_content = ''
    jpg_list = []
    txt_list = []
    for filename in os.listdir(portfolio_directory):
        if filename.endswith('.jpg'): jpg_list.append(filename[:-4])
        if filename.endswith('.txt'): txt_list.append(filename[:-4])
    for jpg in jpg_list:
        if jpg in txt_list:
            continue
        else:
            # raise exception
            print('\nerror: txt for jpg not found for ' + jpg + '\n\n')
            exit()

    txt_list.sort(reverse=True)
    for element in txt_list:
        element_txt = open(portfolio_directory + '/' + element + '.txt', 'r').read()
        portfolio_content += '<div id="pictures-container"><div id="floated">' + \
            '<img src="' + portfolio_directory + "\\" + element + '.jpg" loading="lazy"' + \
            '></div>' + element[0:4] + '<br>' + element_txt + '</div>'

    # print(content_list) 
    return portfolio_content


catalogue_html = create_catalogue()
galeria_html = create_galeria()

# write all pages
for item_page, item_name in subpages.items():
    with open(item_page+'.html', 'w') as page:
        page.write(begin_html)
        page.write(menu_html)
        if item_page == 'galeria/index':
            page.write(galeria_html)
        if item_page == 'catalogue/index':
            page.write(catalogue_html)
        page.write(end_html)
