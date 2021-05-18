import random

list1=['1','2','3','4','5','6','7','8','9','K','Q','J']*4
list2=['diamond','heart','spade','clubs']
list3=[]
dealer=[]
player=[]
player_nos=[]
dealer_nos=[]

def draw_card():
  found =0
  while found == 0:
	   ch=random.choice(list1) + " of " + random.choice(list2)
	   if ch in list3:
	     continue
	   else:
	     list3.append(ch)
	     found=1
	     return ch 	

def dealer_draw():
	dealer.append(draw_card())

def player_draw():
	player.append(draw_card())

def initialize():
	dealer_draw()
	dealer_draw()
	d_card1=dealer[0]
	d_card2=dealer[1]
	player_draw()
	player_draw()
	p_card1=player[0]
	p_card2=player[1]
	print("\nDEALER CARD : " )
	print(d_card1)
	for x in player:
		player_nos.append(x[0].lower())
	for x in dealer:
		dealer_nos.append(x[0].lower())	

def player_calc():
	print("\nYOUR CARDS : ")
	for x in player:
		print(x)
	total_player=0
	for x in player_nos:
		if x == 'j'or x == 'k' or x == 'q':
			total_player=total_player+10
		elif x == '1':
		    ip=input("\ndo you want to treat Ace as 1 or 11 ? :")
		    if ip == '1':
		       total_player=total_player+1
		    else:
		    	total_player=total_player+11
		else:
		    total_player=total_player+int(x) 	
		         	
	return total_player	         		

def dealer_calc():
	total_dealer=0
	for x in dealer_nos:
		if x == 'j'or x == 'k' or x == 'q':
			 total_dealer=total_dealer+10
		elif x == '1':
		    if total_dealer+11 < 21:
		         total_dealer=total_dealer+11
		    else:
		    	 total_dealer=total_dealer+1
		else:
		     total_dealer=total_dealer+int(x) 	
		         	
	return total_dealer

def check(total_player):
	if total_player > 21 :
		print("\nsorry you lose !!")
		return True
	elif total_player == 21:
	    print("\nyay you won !!!")
	    return True	
	else :
	    return False     

def check1(total_player,total_dealer):
	if total_dealer > 21:
		dealer.pop()
		dealer_nos.pop()
		total_dealer=dealer_calc()
		check1(total_player,total_dealer)
	elif total_dealer > total_player :
		print("\nDEALER'S CARDS : ")
		for x in dealer :
			print(x)
		print("\ndealer's total :" +str(total_dealer))
		print("\nyou lose the bet dealer beat you!!!")
		return True
	elif total_dealer < total_player :
		print("\n DEALER'S CARDS : ")
		for x in dealer :
			print(x)
		print("\ndealer's total :" +str(total_dealer))
		print("\nyou win the bet you beat dealer!!!")
		return True	

def play():
	win =False
	choice='hit'
	while choice== 'hit' and win == False:    
	        initialize()
	        total_player=player_calc()
	        print("\nyour total :" +str(total_player))
	        win=check(total_player)
	        if win == True :
	        	continue
	        choice= input("\nhit/bust? :")
	        while choice == 'hit' and win == False:
		        player_draw()
		        player_nos.append(player[-1][0].lower())
		        total_player=player_calc()
		        print("\nyour total :" +str(total_player))
		        win=check(total_player)
		        if win == True:
		            continue 
		        choice= input("\nhit/bust? :")
	win = False
	while win == False and choice == 'bust':
		dealer_draw()
		dealer_nos.append(dealer[-1][0].lower())
		total_dealer=dealer_calc()
		win=check1(total_player,total_dealer)
		if win == True :
			continue

	        
ch='yes'
while ch == 'yes':
	list3.clear()
	player.clear()
	dealer.clear()
	player_nos.clear()
	dealer_nos.clear()
	play()
	ch=input("\ndo you want to play again ? (yes/no) :")
if ch == 'no':
    print("\nsee ya later :) ")	
