from os import listdir



heading_html_file = "snippets/head.html"
menu_html_file = "snippets/menu.html"
footer_html_file = "snippets/foot.html"

index_content_file = "snippets/index_content.html"

portfolio_directory = "content" 

def create_page(page_type, snippets):                    # defines layout
        if page_type == "index":
            content = create_index_content()
            filename = "index.html"
        if page_type == "portfolio":
            content = create_portfolio_content()
            filename = "portfolio.html"

        output_file_handle = open(filename, 'w')
        output_file_handle.write(snippets[0])               # head
        output_file_handle.write(snippets[1])               # menu
        output_file_handle.write(content)               # content
        
        output_file_handle.write(snippets[2])               # foot
        output_file_handle.close()

def buffer_main_snippets():
    head = open(heading_html_file).read()
    menu = open(menu_html_file).read()
    foot = open(footer_html_file).read()
    return [head, menu, foot] 

def create_index_content():
    index_content = open("snippets/index_content.html", "r").read()
    return index_content

def create_portfolio_content():
    portfolio_content = ""
    content_list = create_portfolio_list(portfolio_directory)
    content_list.sort(reverse=True)
    for element in content_list:
        element_txt = open(portfolio_directory + "/" + element + ".txt", 'r').read()

        portfolio_content += "<div id=\"container\"><div id=\"floated\">" + \
            "<img src=\"" + portfolio_directory + "\\" + element + ".png\" loading=\"lazy\"" + "></div>" + \
            element[0:4] + "<br>" + element_txt + "</div>"

    # print(content_list) 
    return portfolio_content

def create_portfolio_list(content_directory):
    png_list = []
    txt_list = []

    for file in listdir(content_directory):
        create_png_list(file, png_list)
        create_txt_list(file, txt_list)

    for png in png_list:
        if png in txt_list:
            continue
        else:
            print("\nerror: txt for png not found for " + png + "\n\n")
            exit()
            
    return txt_list

def create_png_list(filename, list):
    if filename.endswith(".png"):
        list.append(filename[:-4])

def create_txt_list(filename, list):
    if filename.endswith(".txt"):
        list.append(filename[:-4])


def main():

    page_snippets = buffer_main_snippets()  # head, menu, foot
    create_page("index", page_snippets)
    # create_page("portfolio", page_snippets)

    # create_page("portfolio")



    print("end")

main()