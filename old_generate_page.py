# =================================================
#       PAGE GENERATION
#
#       HTML PAGE LAYOUT
#
#       +-----------+
#       | head.html |       snippets[0]
#       +-----------+
#       | menu.html |       snippets[1]
#       +-----------+
#       |  CONTENT  |
#       +-----------+
#       | foot.html |       snippets[2]
#       +-----------+


import random
import os
os.chdir(os.path.dirname(__file__))

subpages = {
    'index'     : 'Strona główna',
    'offer'     : 'Oferta',
    'galery'    : 'Galeria',
    'contact'   : 'Kontakt'
}


def make_website(subpages):
    for page in subpages:
        pass

def create_page():
    snippets = ['snippets/begin.html',
                'snippets/menu.html',
                'snippets/end.html'
    ]
    filename = 'index.html'
    
    # snippet buffering
    for idx, snippet_path in enumerate(snippets):
        with open(snippet_path, 'r') as f:
            snippets[idx] = f.read()

    # writing to file
    output_file_handle = open(filename, 'w')
    output_file_handle.write(snippets[0])               # head
    output_file_handle.write(create_index_content())
    output_file_handle.write(snippets[2])               # foot
    output_file_handle.close()

    # report
    print('written:\t' + filename)

def create_index_content():
    index_content_file = 'snippets/index_content.html'
    index_content = '\n'
    index_content += open(index_content_file, 'r').read() + '\n\n'
    # index_content += generate_blinds(columns=7, length=30, width=3, size_in_px=568)
    return index_content

def create_picture_with_description_portfolio():
    # in portfolio_directory, there should be pairs of pict
    portfolio_directory = 'pictures-content'
    
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
        portfolio_content += '<div id=\'pictures-container\'><div id=\'floated\'>' + \
            '<img src=\'' + portfolio_directory + '\\' + element + '.jpg\' loading=\'lazy\'' + \
            '></div>' + element[0:4] + '<br>' + element_txt + '</div>'

    # print(content_list) 
    return portfolio_content

def create_menu():
    menu = '' 
    # mdfiles tree
    return menu

def create_bio():
    html_code = ''
    with open('portfolio/art-bio-en.md', 'r') as file_handle:
        bio_file = file_handle.readlines()
        for idx ,line in enumerate(bio_file):
            if '##' in line:
                html_code += '<h2>' + line.replace('## ', '').strip() + '</h2>\n'
                print(idx)
                for jdx ,element in enumerate(bio_file[idx+1:]):
                    if line.startswith('!'):
                        pass
                    elif element.startswith('-'):
                        splitline = element.replace('- ', '').replace('\n', '').split(' / ')
                        html_code += '<div class="grid-container"><div class="grid-text">'
                        for i in splitline:
                            if i.startswith('http'):
                                html_code += '<a href="' + i + '">' + i + '</a><br>\n'
                            elif i.startswith('img'):
                                html_code += f'</div>\
                            <div class="grid-img">\
                            <img src="{splitline[-1].split(" : ")[1]}">\
                            </div>\n<br>'
                            else:
                                html_code += i + '<br>\n'
                    elif element.startswith('#'):
                        break
                html_code += '</div><br>\n'
        print(html_code)
        output_file = open('portfolio/en/index.html', 'w+')
        output_file.writelines(html_code)
        output_file.close()

def create_visual():
    html_code = ''
    files = []
    with open('snippets/head.html', 'r') as file_handle:
        html_code += file_handle.read()
    for filename in os.listdir('visual'):
        files.append(filename)
    random.shuffle(files)
    for filename in files:
        if filename.endswith('mp4'):
            html_code += '<video autoplay loop muted><source src="' + filename + '" type="video/mp4"></video>\n'
        elif filename.endswith('jpg'):
            html_code += '<img src="' + filename + '">\n'    
    output_file = open('visual/index.html', 'w+')
    output_file.writelines(html_code)
    output_file.close()

def generate_blinds(columns, length, width, size_in_px):
    symbols_list = '!@#$^&*()_+|}{\'\':?>,./;[]\\=-'
    txt = ''
    w, l, c = width, length, columns
    while(c):
        txt += '<div class=\'blinds\' style=\'position: absolute; top: 0px; left: '
        txt += str((c-1)*size_in_px/(columns)) + 'px;\'>'
        l = length
        while(l):
            w = width
            while(w):
                txt += symbols_list[int(random.random()*len(symbols_list))]
                w -= 1
            txt += '<br>'
            l -= 1
        c -= 1
        txt += '</div>\n'
    return txt


create_bio()