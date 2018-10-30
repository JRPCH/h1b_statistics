
import sys
import csv

columns_selected1 = ['SOC_NAME','CASE_STATUS','WORKSITE_STATE']              # New header for H1B file    
columns_selected2 = ['LCA_CASE_SOC_NAME','STATUS','LCA_CASE_WORKLOC1_STATE'] # Old headers for H1B file

## Parse data, return column names, data, and column index.
##
def read_data(h1b_input):
    columns_selected_index = []
    columns_selected = []
    with open(h1b_input, encoding = 'UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ';')
        try:
            column_names = next(csv_reader)

            if 'CASE_STATUS' in column_names:                      ## check with version of H1B file is.
                columns_selected = columns_selected1
            else:
                columns_selected = columns_selected2               ## Old Version.  
            for names in columns_selected:
                columns_selected_index.append(column_names.index(names))

            data_list = list(csv_reader)
            assert len(data_list[0]) == len(column_names), 'Columns names not matching data'
            return column_names, data_list, columns_selected_index
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(h1b_input, cvs_reader.line_num, e))

## Count certified applications that correspont to job title and state
## Return total_certified_apps, total_occupation, total_state.
##
def total_columns(columns_names, data, index):
    total_occupation = dict()
    total_state = dict()

    ## Assign index varaible.
    soc_name_idx = index[0]
    status_idx = index[1]
    state_idx = index[2]
    
    total_certified_apps = 0
    for row in data:
        if row[status_idx] == 'CERTIFIED':
            occupation = row[soc_name_idx].strip('"')       # Remove quotes in job titles.

            total_occupation[occupation] = total_occupation.get(occupation, 0) + 1
            state = row[state_idx]
            total_state[state] = total_state.get(state, 0) + 1
            total_certified_apps += 1
    return total_certified_apps, total_occupation, total_state

## Rank total occupation taking the certification application count
## similarly for total state with the certication application count
## sorted in descendin order and return the top 10.
def rank_data(group_data, total):   

    ranked_data = [[key, value, '{:.1%}'.format(value/total)] \
    for (key, value) in group_data.items()]
    ranked_data.sort(key = lambda x: (-x[1], x[0]), reverse=False)
    return ranked_data[:10]

## Write the top 10 occupations and percentage.
def write_top10_ocupations(rank_occupation, occupation_output):
 
    with open(occupation_output, 'w', encoding = 'UTF-8') as occup_file:
        writer = csv.writer(occup_file, delimiter = ';')
        writer.writerow(['TOP_OCCUPATIONS','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE'])
        writer.writerows(rank_occupation)

## Write the top states and percentage.
def write_top10_states(rank_state, state_output):

    with open(state_output, 'w', encoding = 'UTF-8') as state_file:
        writer = csv.writer(state_file, delimiter = ';')
        writer.writerow(['TOP_STATES','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE'])
        writer.writerows(rank_state)


def main(argv):

    ## Assign arguments from the command line.
    h1b_input = sys.argv[1]
    occupation_output = sys.argv[2]
    state_output = sys.argv[3]

    columns_names, data, index = read_data(h1b_input)
    total_certified_apps, total_occupation, total_state = total_columns(columns_names, data, index)
    rank_occupation = rank_data(total_occupation, total_certified_apps)
    rank_state = rank_data(total_state, total_certified_apps)
    write_top10_ocupations(rank_occupation, occupation_output)
    write_top10_states(rank_state, state_output)

if __name__ == '__main__': main(sys.argv[1:])

