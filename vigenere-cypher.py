'''----------Alphabet_Array----------'''

import numpy as np
import lst_cretr as ls

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
test_lst = ['hello','bell'] #test
#function to add seperated alphas.
def jnr(lst):
	for s in range(len(lst)):
		snt_var  = lst[s]
		word_var = ''
		for d in range(len(snt_var)):
			temp_alpha = snt_var[d]
			word_var +=temp_alpha
		lst[s] = word_var


'''#function to remove \n and substitute , . ! [{()}]
def subs(word):
	lst = list(word)
	for z in range(len(lst)):
		if lst[z] == '\n':
			del lst[z]
	return jnr(lst)'''

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

'''test'''
##f_path = input('Enter file path   -->  ')

'''with open('file.txt','r') as file :
	data = file.readlines()
	encoder(data,key)
	with open('/home/awert/Desktop/crypter/file2.txt','w') as bub:
		bub.writeline(data)
'''
