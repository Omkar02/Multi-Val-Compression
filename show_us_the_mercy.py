import csv
import start as s
import helper as h


def line_finder(file_name, all_lines=[]):
    with open(file_name, "r") as f:
        for x in f:
            if len(x.split()) >= 2 and '---' not in x:
                all_lines.append((x.replace('\n', ''),
                                  x.replace('\n', '').split()[0],
                                  x.replace('\n', '').split()[1]))
            else:
                all_lines.append((x.replace('\n', ''),
                                  None,
                                  None))

    return all_lines, file_name


def when_keys_meet_ddl(pass_line_finder, pass_com_val_d, please_wrk=[]):
    for line_i, master, d_flag in pass_line_finder:
        # print(line_i, master, d_flag)
        try:
            all_value = pass_com_val_d[master]
            cha_val = h.get_chanded(all_value, d_flag)
            if '))' not in line_i:
                please_wrk.append(line_i.replace(',', '') + f' COMPRESS {cha_val},')
            else:
                thats_do_something = line_i[0:len(line_i) - 1]
                please_wrk.append(thats_do_something + f' COMPRESS {cha_val}),')
        except Exception as e:
            please_wrk.append(line_i.replace('\n', ''))
    return please_wrk


def txt_writer(pass_arr, name, pass_the_lis_of_all_dict):
    name = name.split('.')
    with open(f'{name[0]}_{name[1]}.sql', 'w') as writer:
        writer.writelines('-' * 10 + f'| {name[0]}_{name[1]} |' + '-' * 10 + '\n')
        for cnt_N, ww in enumerate(pass_arr):
            if cnt_N == 0:
                continue
            if ';' not in ww:
                writer.writelines(ww + '\n')
            else:
                writer.writelines(ww + '\n')
                break


lf, name = line_finder('EDW_SCVER.POR_DLY_AGG.ddl_1')
compress_val_d = s.processing(s.Lets_dig_in('EDW_SCVER.POR_DLY_AGG.MVC'))
lis_key = list(compress_val_d.keys())
txt_writer(when_keys_meet_ddl(lf, compress_val_d), name, lis_key)
