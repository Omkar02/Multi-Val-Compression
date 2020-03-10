import csv
import helper as H
def Lets_dig_in(text_file_name):
    with open(text_file_name) as f:
        a = csv.reader(f, delimiter=',')

        temp_val = []
        for cnt, stuff in enumerate(a):
            temp_val.append(stuff)
    return temp_val
# print(Lets_dig_in('EDW_SCVER.POR_DLY_AGG.MVC')[0:10])


def processing(pass_th_arr):
	length = len(pass_th_arr)
	d_val = {}
	new_key = ''
	len_a = 0
	nc = 0
	for i in range(0,length):
		header = pass_th_arr[i][0].split()
		
		if header[1] == 'CN' and header[2] == 'PER':
			d_val.setdefault(header[0], [])
			new_key = header[0]
			nc = 0

		if '---' in pass_th_arr[i][0].split()[0]:
			len_a = len(pass_th_arr[i][0].split()[0])
		
		if '---' not in pass_th_arr[i][0][0:len_a]:
			if nc != 0:
				d_val[new_key].append(H.whitespace(pass_th_arr[i][0][0:len_a]))
		nc+=1


	# for ke, va in d_val.items():
	# 	print(ke,' ---> ',va)
	return d_val

# print(processing(Lets_dig_in('EDW_SCVER.POR_DLY_AGG.MVC')))
