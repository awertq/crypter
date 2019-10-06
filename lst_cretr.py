'''function to create aphabet list '''

def lst_cretr(str_val):
	lst_n = []
	srt_v = str_val-1

	for k in range(26):
		k = srt_v

		if k == 122:
			srt_v = 97
		else:
			srt_v +=1

		lst_n.append(chr(srt_v))

	return(lst_n)

