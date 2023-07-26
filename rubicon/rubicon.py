import csv, json, ldif
import os, re, pandas as pd

# inputs
wd = os.getcwd()
data_folder = 'dane'
file_extensions = ['csv', 'json', 'ldif'] # must define read_$EXTENSION function for each
entry_columns = ['Customer', 'Country', 'Order', 'Status', 'Group']

# 1
def read_csv(file_path):
    csv_data = []
    with open(file_path, 'r') as csv_file_handle:
        csv_file = csv.reader(csv_file_handle, delimiter='|')
        for i in csv_file:
            csv_data.append(i)
    return csv_data[1:]
def read_json(file_path):
    json_data = []
    with open(file_path, 'r') as json_file_handle:
        json_file = json.load(json_file_handle)
        for row in json_file['data']:
            json_data.append(row)
    return json_data
def read_ldif(file_path):
    with open(file_path, 'r') as ldif_file_handle:
        ldif_data = ''
        for i in ldif_file_handle:
            ldif_data += i
        entries = re.split(r'\n\s*\n', ldif_data.strip())

        parsed_data = []
        for entry in entries:
            elements = re.findall(r'(\w+):(.+)', entry)
            parsed_entry = [value.strip() for _, value in elements]
            parsed_data.append(parsed_entry)
    return parsed_data
def x_read_all(entry_coulmns=entry_columns, data_folder=data_folder):
    dataframes = []
    all_df = pd.DataFrame()
    for file in os.listdir(os.path.join(wd, data_folder)):
        for extension in file_extensions:
            if file.endswith(extension):
                array = globals()['read_' + extension](os.path.join(wd, data_folder, file))
                df = pd.DataFrame(array, columns=entry_columns)
                # print(file)
                # print(df[df['Status'] == '8'], '\n')
                dataframes.append({'filename': file, 'df' : df})
                all_df = pd.concat([all_df, df], ignore_index=True)
    return all_df, dataframes

# 2
def count_top_orders(all_df, top_count):
    order_counts = all_df['Order'].value_counts()[:top_count]
    return order_counts

# 3
def top_countries_in_groups(all_orders):
    groups = all_orders.Group.unique()
    top_countries = []
    for group in groups:
        if group == None:
            break
        df1 = all_orders[all_orders['Group'] == group]
        all_counts = df1['Country'].value_counts()
        max_counts = all_counts.max()
        most_frequent_countries = all_counts[all_counts == max_counts]
        countries = []
        for j in most_frequent_countries.index:
            countries.append(j)
        top_countries.append([group, max_counts, countries])
    return sorted(top_countries, key=lambda x: x[0])

# 4
def find_status_max(df, key=None):
    status_count = df['Status'].value_counts()
    return status_count
def top_status_files(dataframes):
        statuses_df = pd.DataFrame()
        for chunk in dataframes:
            extension = chunk['filename'].split('.')[1]
            statuses_df = pd.concat([statuses_df, find_status_max(chunk['df']).to_frame(name=extension)], axis=1)
        statuses = all_df.Status.unique()
        dfa = statuses_df.transpose()
        vals = statuses_df.transpose().max()
        top_status = []
        for status in statuses:
            dfb = dfa[dfa == vals[status]]
            file_types = dfb[dfb[status] == vals[status]].index.tolist()
            top_status.append([status, vals[status], file_types])
        return top_status

# 5
def count_consonants(all_df):
        count = 0
        letters = 'qwrtpsdfghjklzxcvbnm'
        for i in all_df.Customer:
            for j in i.lower():
                if j in letters:
                    count += 1
        return count


if __name__ == '__main__':

    # 1
    all_df, dataframes = x_read_all()

    # 2
    most_ordered = count_top_orders(all_df, 30)
    
    # 3
    cntry_grps = top_countries_in_groups(all_df)

    #4 
    top_files = top_status_files(dataframes)
    # print(top_files)

    # 5 
    consonants_count = count_consonants(all_df)
    # print(consonants_count)

    
    with open('html_preamble', 'r') as html_preamble:
        with open('index.html', 'w+') as file:
            file.write(html_preamble.read())


            html_chunk = '\n<div id=\"mst\"><table><tr class=\"head\">'
            for i in ['NAZWA LEKU', 'LICZBA ZAMÓWIEŃ']:
                html_chunk = html_chunk + '<td>'+i+'</td>'
            html_chunk = html_chunk+'</tr>'
            for i in most_ordered.index:
                html_chunk = html_chunk+'\n<tr><td>'+str(i)+'</td><td>'+str(most_ordered[i])+'</td></tr>'
            html_chunk = html_chunk+'\n</table></div>'
            file.write(html_chunk)

            html_chunk = '\n<div id=\"mst\"><table><tr class=\"head\">'
            for i in ['GRUPA', 'LICZBA', 'PAŃSTWA']:
                html_chunk = html_chunk + '<td>'+i+'</td>'
            html_chunk = html_chunk+'</tr>'
            for i in cntry_grps:
                html_chunk = html_chunk+'\n<tr><td>'+str(i[0])+'</td><td>'+str(i[1])+'</td><td>'
                for j in i[2]:
                    html_chunk = html_chunk+j+', '
                html_chunk = html_chunk+'</td></tr>'
            html_chunk = html_chunk+'\n</table></div>'
            file.write(html_chunk)
            # print(top_files)

            html_chunk = '\n<div id=\"mst\"><table><tr class=\"head\">'
            for i in ['STATUS', 'PLIK', 'LICZBA']:
                html_chunk = html_chunk + '<td>'+i+'</td>'
            html_chunk = html_chunk+'</tr>'
            for i in top_files:
                html_chunk = html_chunk+'\n<tr><td>'+str(i[0])+'</td><td>'+str(i[2])+'</td><td>'+str(i[1])+'</td></tr>'
            html_chunk = html_chunk+'\n</table></div>'
            file.write(html_chunk)


            html_chunk = '\n<div id=\"cns\"><table><tr class=\"head\"><td>LICZBA SPÓŁGŁOSEK</td></tr><tr><td>'+str(consonants_count)+'</td></tr></table></div>'
            file.write(html_chunk)

            html_chunk = '</body></html>'
            file.write(html_chunk)