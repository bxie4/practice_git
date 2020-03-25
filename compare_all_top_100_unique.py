import numpy as np
import os
import pandas as pd 
def _read_txt(file_txt):
  f = open(file_txt,'r')
  lines=f.read().split('\n')
  f.close()
  data=[]
  for line in lines:
    if line!='':
      #data.append(line)
      data.append(int(line.split('"')[1]))##count_gene_id
  return data

def convert_gene_id_to_seq(gene_ids, excel_file):
  d = pd.read_excel(excel_file)
  indexes = []
  for i in range(len(d)):
    for g in gene_ids:
      if g ==d['count_gene_id'][i]:
        indexes.append(i)
  sequences = []
  for index in indexes:
    sequences.append(d['tail'][index])
  return sequences

def compare_diff(P12_data,P13_data):
  common_part = list(set(P12_data).intersection(set(P13_data))) #common colored part
  diff_gene_id_P12 =[] 
  diff_gene_id_P13 =[]
  for p in P12_data:
    if not p in common_part:
      diff_gene_id_P12.append(p)
  for p in P13_data:
    if not p in common_part:
      diff_gene_id_P13.append(p)
  return diff_gene_id_P12, diff_gene_id_P13, common_part

home_dir = '/home/bxie/PycharmProjects/benchmark/building_new_model/199_training_database/'
#----tested sequences ----#
#top_P12 =os.path.join(home_dir,'rnn_modular_package', '199data_training_batch1_prediction_P12_human_proteins','Done_experimental_already_all_top_100.txt') 
top_P12 = '/home/bxie/PycharmProjects/benchmark/using_old_model/199_training_database/rnn_modular_package/Done_experimental_already_all_top_100.txt'#It's not P12, it is the results generated through old models
top_P13 =os.path.join(home_dir,'rnn_modular_package', '199data_training_batch1_prediction_P13_human_proteins','Done_experimental_already_all_top_100.txt')
#bottom_P12=os.path.join(home_dir,'rnn_modular_package','199data_training_batch1_prediction_P12_human_proteins', 'Done_experimental_already_all_bottom_100.txt')
bottom_P12 = '/home/bxie/PycharmProjects/benchmark/using_old_model/199_training_database/rnn_modular_package/Done_experimental_already_all_bottom_100.txt' ##It's not P12, it is the results generated through old models
bottom_P13=os.path.join(home_dir,'rnn_modular_package','199data_training_batch1_prediction_P13_human_proteins', 'Done_experimental_already_all_bottom_100.txt')

top_P12_data = _read_txt(top_P12)
top_P13_data = _read_txt(top_P13)
bottom_P12_data = _read_txt(bottom_P12)
bottom_P13_data = _read_txt(bottom_P13)

colored_top_P12_sequences = convert_gene_id_to_seq(top_P12_data, '/home/bxie/PycharmProjects/benchmark/using_old_model/199_training_database/rnn_modular_package/all_top_100.xlsx') ##### use old models for P13 prediction, not exactly P12
#top_P12_sequences = convert_gene_id_to_seq(top_P12_data, os.path.join(home_dir,'rnn_modular_package','199data_training_batch1_prediction_P12_human_proteins','all_top_100.xlsx'))
colored_top_P13_sequences = convert_gene_id_to_seq(top_P12_data, os.path.join(home_dir,'rnn_modular_package','199data_training_batch1_prediction_P13_human_proteins','all_top_100.xlsx'))
colored_bottom_P12_sequences = convert_gene_id_to_seq(bottom_P12_data, '/home/bxie/PycharmProjects/benchmark/using_old_model/199_training_database/rnn_modular_package/all_bottom_100.xlsx') #### use old models for P13 prediction, not exactly P12
#bottom_P12_sequences = convert_gene_id_to_seq(bottom_P12_data, os.path.join(home_dir,'rnn_modular_package','199data_training_batch1_prediction_P12_human_proteins','all_bottom_100.xlsx'))
colored_bottom_P13_sequences = convert_gene_id_to_seq(bottom_P13_data, os.path.join(home_dir,'rnn_modular_package','199data_training_batch1_prediction_P13_human_proteins','all_bottom_100.xlsx'))

f = open('colored_sequences_top_P12.txt','w')
for c in list(set(colored_top_P12_sequences)):
  f.write(c+'\n')
f.close()
f = open('colored_sequences_top_P13.txt','w')
for c in list(set(colored_top_P13_sequences)):
  f.write(c+'\n')
f.close()
f = open('colored_sequences_bottom_P12.txt','w')
for c in list(set(colored_bottom_P12_sequences)):
  f.write(c+'\n')
f.close()
f = open('colored_sequences_bottom_P13.txt','w')
for c in list(set(colored_bottom_P13_sequences)):
  f.write(c+'\n')
f.close()



diff_top_P12, diff_top_P13, common_top =compare_diff(colored_top_P12_sequences,colored_top_P13_sequences)
diff_bottom_P12, diff_bottom_P13, common_bottom =compare_diff(colored_bottom_P12_sequences,colored_bottom_P13_sequences)

f = open('different_models_on_P13_human_database_top_bottom_record.txt','w')
f.write('****** TOTAL TOP SEQUENCES P12 number is '+"%4d"%(len(list(set(diff_top_P12)))+len(common_top))+'\n')
f.write('****** TOTAL TOP SEQUENCES P13 number is '+"%4d"%(len(list(set(diff_top_P13)))+len(common_top))+'\n')
f.write('****** COMMON TOP SEQUENCES number is '+"%4d"%(len(common_top))+'\n')
f.write('****** DIFFERENT TOP SEQUENCE P12 number is '+"%4d"%(len(list(set(diff_top_P12))))+'\n')
f.write('****** DIFFERENT TOP SEQUENCE P13 number is '+"%4d"%(len(list(set(diff_top_P13))))+'\n')
f.write('\n****** TOTAL BOTTOM SEQUENCE P12 number is '+"%4d"%(len(list(set(diff_bottom_P12)))+len(common_bottom))+'\n')
f.write('****** TOTAL BOTTOM SEQUENCE P13 number if '+"%4d"%(len(list(set(diff_bottom_P13)))+len(common_bottom))+'\n')
f.write('****** COMMON BOTTOM SEQUENCE number is '+"%4d"%(len(common_bottom))+'\n')
f.write('****** DIFFERENT BOTTOM SEQUENCE P12 number is '+"%4d"%(len(list(set(diff_bottom_P12))))+'\n')
f.write('****** DIFFERENT BOTTOM SEQUENCE P13 number is '+"%4d"%(len(list(set(diff_bottom_P13))))+'\n\n')

f.write('#------------------ TOP COMMON SEQUENCES -------------#\n')
for c in list(set(common_top)):
  f.write(c+'\n')
f.write('#------------------ TOP Unique P12 SEQUE -------------#\n')
for d in list(set(diff_top_P12)):
  f.write(d+'\n')
f.write('#------------------ TOP Unique P13 SEQUE -------------#\n')
for d in list(set(diff_top_P13)):
  f.write(d+'\n')
f.write('#------------------ BOTTOM COMMON SEQUNE -------------#\n')
for d in list(set(common_bottom)):
  f.write(d+'\n')
f.close()

def get_all_sequences_from_excel(excel_file):
  d = pd.read_excel(excel_file)
  dictionary={}
  for x in range(len(d)):
    if str(d['tail'][x])!='nan':
      dictionary[str(d['tail'][x])] = str(d['av_RNN_score'][x])
  return dictionary
all_P12_top_dic = get_all_sequences_from_excel('/home/bxie/PycharmProjects/benchmark/using_old_model/199_training_database/rnn_modular_package/all_top_100.xlsx')
#all_P12_top_dic = get_all_sequences_from_excel(os.path.join(home_dir,'rnn_modular_package','199data_training_batch1_prediction_P12_human_proteins','all_top_100.xlsx'))
all_P13_top_dic = get_all_sequences_from_excel(os.path.join(home_dir,'rnn_modular_package','199data_training_batch1_prediction_P13_human_proteins','all_top_100.xlsx'))
print ('P12 TOP sequences total number is ', len(all_P12_top_dic))
print ('P13 TOP sequences total number is ', len(all_P13_top_dic))

f = open('untest_top_sequences_P13_old_model.txt','w')
for key in all_P12_top_dic.keys():
  if not key in diff_top_P12 and not key in common_top:
    f.write(key+' '+all_P12_top_dic[key]+'\n')
f.close()
f = open('untest_top_sequences_P13_new_model.txt','w') 
for key in all_P13_top_dic.keys():
  if not key in diff_top_P13 and not key in common_top:
    f.write(key+' '+all_P13_top_dic[key]+'\n')
f.close()
f = open('untest_top_sequences_P13_both_models.txt','w')
total_sequences =list(list(all_P12_top_dic.keys())+list(all_P13_top_dic.keys()))
tested_sequences = list(set(diff_top_P12+diff_top_P13+common_top))
for t in total_sequences:
  if not t in tested_sequences:
    if t in all_P12_top_dic.keys():
      print (t, 'in P12 TOP')
      f.write(t+' '+all_P12_top_dic[t]+'\n')
    elif t in all_P13_top_dic.keys():
      print (t, 'in P13 TOP')
      f.write(t+' '+all_P13_top_dic[t]+'\n')
    else:
     print (t, 'NOT IN ANY TOP SEQUENCES DATABASE, NEED CHECK WHERE IT IS FROM')
f.close()


