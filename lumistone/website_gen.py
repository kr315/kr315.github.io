import os
os.chdir('/Users/kr315/Desktop/_dev/kr315.github.io/lumistone')
newline = '\n'

subpages = {
    # 'index'     : 'o mnie',
    'gallery'    : 'gallery',
    'catalogue'    : 'catalogue',
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

def create_contact_form():
    pass

# content for each subpage
def create_landing():
    pass

def create_gallery():
    # generate image list, paths, description
    print('generating "gallery", pictures:')
    images_list = []
    for filename in os.listdir('gallery'):
        if filename.endswith('jpeg') or filename.endswith('jpg'):
            images_list.append(filename)
    images_list.sort()
    site_content_html = ''
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
            <tr><td><a href="{prev}.html">&lt;&lt;</a></td><td><a href="gallery.html">powrót</a></td><td><a href="{next}.html">&gt;&gt;</a></td></tr>\
            <tr><td colspan="3"><img src="gallery/{img}" class="preview"></td></tr>\
            </tbody></table>'
        img_html_code += end_html
        with open(f'{img}.html', 'w') as img_html_page:
            img_html_page.write(img_html_code)
        site_content_html += f'<a href="{img}.html"><img src="gallery/{img}" class="thumbnail" loading="lazy"></a>\n'
    return site_content_html

def create_catalogue():
    print('generating "catalogue", items:')
    site_content_html = ''
    with open('catalogue/catalogue.md') as input_file:
        lines = input_file.readlines()
        items = []
        for line in lines:
            if line.startswith('- '):
                items.append(line.strip()[2:].split(' / '))
        if 'no' in lines[2]:
            items.pop(0)
        for item in items:
            print(item)
            site_content_html +=    f'<div class="c-item">\
                                    <div class="c-item-image"><img src="catalogue/{item[2]}.jpg" class="c-item-img"></div>\
                                    <div class="c-item-name">{item[0]}</div>\
                                    <div class="c-item-price">{item[1]}</div>\
                                    </div>'

    return site_content_html


# create html for each
catalogue_html = create_catalogue()

gallery_html = create_gallery()

# write all pages
for item_page, item_name in subpages.items():
    with open(item_page+'.html', 'w') as page:
        page.write(begin_html)
        page.write(menu_html)
        if item_page == 'gallery':
            page.write(gallery_html)
        if item_page == 'catalogue':
            page.write(catalogue_html)
        page.write(end_html)
