'''----------Alphabet_Array----------'''

import numpy as np
import lst_cretr as ls
import csv

#creating alphabet lists.
# a==97 , z==122

l1 = ls.lst_cretr(97) #start from a
l2 = ls.lst_cretr(98)
l3 = ls.lst_cretr(99)
l4 = ls.lst_cretr(100)
l5 = ls.lst_cretr(101)
l6 = ls.lst_cretr(102)
l7 = ls.lst_cretr(103)
l8 = ls.lst_cretr(104)
l9 = ls.lst_cretr(105)
l10 = ls.lst_cretr(106)
l11 = ls.lst_cretr(107)
l12 = ls.lst_cretr(108)
l13 = ls.lst_cretr(109)
l14 = ls.lst_cretr(110)
l15 = ls.lst_cretr(111)
l16 = ls.lst_cretr(112)
l17 = ls.lst_cretr(113)
l18 = ls.lst_cretr(114)
l19 = ls.lst_cretr(115)
l20 = ls.lst_cretr(116)
l21 = ls.lst_cretr(117)
l22 = ls.lst_cretr(118)
l23 = ls.lst_cretr(119)
l24 = ls.lst_cretr(120)
l25 = ls.lst_cretr(121)
l26 = ls.lst_cretr(122) #start from z

#making 2D array of 26 alphalist.

alpha_arr= np.array([l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26])

#print(alpha_arr)
#print(np.ndim(alpha_arr))
#print(np.shape(alpha_arr))
#print(np.size(alpha_arr))



#ENCODER

key = input("Enter the encoding key   -->  ")
test_lst = ['hello','bell','asdfgg'] #test
#function to add seperated alphas.
def jnr(lst):
	for s in range(len(lst)):
		snt_var  = lst[s]
		word_var = ''
		for d in range(len(snt_var)):
			temp_alpha = snt_var[d]
			word_var +=temp_alpha
		lst[s] = word_var


#function to convert list element to alphalist the 

def encoder(snt_lst,key):
	for i in range(len(snt_lst)):
		active_snt = snt_lst[i]
		active_snt = str(active_snt)

		#function to make key of same size as sentance list
		active_key = key
		pointer = 0
		while True:
			if len(active_key) < len(active_snt):
				active_key+=key[pointer]
			if len(active_key) == len(active_snt):
				break
			pointer +=1
			if pointer == len(key):
				pointer =0
		active_key = list(active_key)
		active_key_arr = np.array(active_key)
		print(active_key_arr) #test

		active_snt = list(active_snt)
		active_snt_arr = np.array(active_snt)

		#vertical_stacking sentance array and key array.
		stkd_arr = np.vstack((active_snt_arr,active_key_arr))
		print('stcked arr ',stkd_arr) #test
		#encrypted list
		encpt_lst = []

		#using stacked array to pick alpha from alpha_arr.
		for h in range(len(active_snt_arr)):
			x = stkd_arr[0,h]	#select alpha from sentace array
			y = stkd_arr[1,h]	#select alpha from key array
			#for loop to find x-coordinate from alpha_arr.
			x_pointer = 0		#keep track of coordinate of x axis
			for g in range(len(alpha_arr[0])):
				if alpha_arr[0,g]==x:
					print('x-coordinate set') #test
					break
				else:
					x_pointer += 1
			#for loop to find y-coordinate from alpha_arr.
			y_pointer = 0		#keep track of coordinate of y-axis
			for t in range(len(alpha_arr[0])):
				if alpha_arr[t,0]==y:
					break
				else:
					y_pointer += 1

			print(x_pointer,y_pointer) #test
			#picking alphabet from alpha_arr using x and y coordinates
			enc_alpha = alpha_arr[x_pointer,y_pointer]
			encpt_lst.append(enc_alpha)	#appending the picked alpha from alpha_arr to ecnpt list.

		#changing the list sentence to encrypted sentence.
		snt_lst[i] = encpt_lst

	#adding back the seprated alpha to form encrypted sentance.
	jnr(snt_lst)


encoder(test_lst,key) #test
print(test_lst)  #test



#function to take a sentence and break it into list of words
#making csv file contaning indexes of ,.!;:'"[{()}]?@

sent = 'inni mini m.ino, ()(({{}}}:;''"""".....,,,,,,,,,,@@@@@!!11??????mo' #test

comma = 0
period = 0
excl_mark = 0
semi_col = 0
col = 0
appost = 0
doub_appost = 0
sq_o = 0
cur_o = 0
sml_o = 0
sml_c = 0
cur_c = 0
sq_c = 0
q_mark = 0
at_rt = 0


#making data csv from file to encrypt containing indexes of symbol.

main_file = 'file.txt' #test
def csv_mkr(main_file):
	with open('symbol.csv','w') as csv_file:
		csv_file.write('line-num~index~comma~period~excl_mark~semi_col~col~appost~doub_appost~sq_o~cur_o~sml_o~sml_c~cur_c~sq_c~q_mark~at_rt\n')

	with open(main_file,'r') as file:
		snt_ori = file.readlines()
		for b in range(len(snt_ori)):
			snt = str(snt_ori[b])
			print(snt) #test

			global comma
			global period
			global excl_mark
			global semi_col
			global col
			global appost
			global doub_appost
			global sq_o
			global cur_o
			global sml_o
			global sml_c
			global cur_c
			global sq_c
			global q_mark
			global at_rt

			comma = 0
			period = 0
			excl_mark = 0
			semi_col = 0
			col = 0
			appost = 0
			doub_appost = 0
			sq_o = 0
			cur_o = 0
			sml_o = 0
			sml_c = 0
			cur_c = 0
			sq_c = 0
			q_mark = 0
			at_rt = 0

			for y in range(len(snt)):

				if snt[y]==',':
					comma = 1
				if snt[y]!=',':
					comma = 0
				if snt[y]=='.':
					period = 1
				if snt[y]!='.':
					period = 0
				if snt[y]=='!':
					excl_mark = 1
				if snt[y]!='!':
					excl_mark = 0
				if snt[y]==';':
					semi_col = 1
				if snt[y]!=';':
					semi_col = 0
				if snt[y]==':':
					col = 1
				if snt[y]!=':':
					col = 0
				if snt[y]=="'":
					appost = 1
				if snt[y]!="'":
					appost = 0
				if snt[y]=='"':
					 doub_appost= 1
				if snt[y]!='"':
					 doub_appost= 0
				if snt[y]=='[':
					sq_o = 1
				if snt[y]!='[':
					sq_o = 0
				if snt[y]=='{':
					cur_o = 1
				if snt[y]!='{':
					cur_o = 0
				if snt[y]=='(':
					sml_o = 1
				if snt[y]!='(':
					sml_o = 0
				if snt[y]==')':
					sml_c = 1
				if snt[y]!=')':
					sml_c = 0
				if snt[y]!='}':
					cur_c = 1
				if snt[y]!='}':
					cur_c = 0
				if snt[y]==']':
					sq_c = 1
				if snt[y]!=']':
					sq_c = 0
				if snt[y]=='?':
					q_mark = 1
				if snt[y]!='?':
					q_mark = 0
				if snt[y]=='@':
					at_rt = 1
				if snt[y]!='@':
					at_rt = 0

				with open('symbol.csv','a') as csv_file:

					name_field = ['line-num','index','comma','period','excl_mark','semi_col','col,appost','doub_appost','sq_o','cur_o','sml_o','sml_c','cur_c','sq_c','q_mark','at_rt']
					val_field = [b,y,comma,period,excl_mark,semi_col,col,appost,doub_appost,sq_o,cur_o,sml_o,sml_c,cur_c,sq_c,q_mark,at_rt]
					for q in range(len(name_field)):
						if name_field[q] == 'at_rt':
							csv_file.write(str(val_field[q])+'\n')
						else:
							csv_file.write(str(val_field[q])+'~')



''' To Add ->
	#making dictCSV for easy reading and extracting data.
	with open('symbol.csv','r') as file113:
		csv_reader = csv.DictReader(file113)
		with open('sample.csv','w') as file12:
#			fields = ['line-num~index~comma~period~excl_mark~semi_col~col~appost~doub_appost~sq_o~cur_o~sml_o~sml_c~cur_c~sq_c~q_mark~at_rt']

			fields = ['line-num','index','comma','period','excl_mark','semi_col','col,appost','doub_appost','sq_o','cur_o','sml_o','sml_c','cur_c','sq_c','q_mark','at_rt']
			csv_writer = csv.DictWriter(file12,fieldnames=fields,delimiter='~')
			for l112 in csv_reader:
				csv_writer.writerow(l112)
'''


csv_mkr('file.txt') #test








#def w_seperator(snt):
##	snt.split(
