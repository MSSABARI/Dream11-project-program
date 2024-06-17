#Dream 11 contest 
Kohli  = 8 #initial points
Hardik = 6 #initial points
Rohit  = 4 #initial points
Bumrah = 4 #initial points
chahal = 4 #initial points

playing_11 =['Kohli', 'Hardik', 'Rohit', 'Bumrah',"Chahal"]
captain='runs'*3
vice_captain='runs'*2
normal_player='runs'*1
bowler='wicket'*25
catcher= 'catch'*8

selected_player=input()

if selected_player in playing_11:
    print(f"yes {selected_player} is available in this match")

    if selected_player=="Kohli" :
        runs=int(input("Runs scored by kohli is:"))
        catch=int(input("How many catches he catched:"))
        captain=runs*2
        catch=catch*16
        print(f'{selected_player} points in this match is {captain+catch}')
    elif selected_player == 'Hardik':
        runs=float(input("Runs scored by Hardik is:"))
        catch=int(input("How many catches he catched:"))
        vice_captain=runs*1.5
        catch=catch*12
        print(f"{selected_player} points in this match is {vice_captain+catch}")
    elif selected_player =="Rohit":
        runs=int(input("Runs scored by Rohit is:"))
        catch=int(input("How many catches he catched:"))
        normal_player=runs*1
        catch=catch*8
        print(f"{selected_player} points in this match is {normal_player+catch}")
    elif selected_player== "Bumrah":
        wicket=int(input("wickets taken by Bumrah is:"))
        catch=int(input("How many catches he catched:"))
        bowler=wicket*25
        catch=catch*8
        print(f"{selected_player} points in this match is {bowler+catch}")
    elif selected_player== "Chahal":
        wicket=int(input("wickets taken by Chahal is:"))
        catch=int(input("How many catches he catched:"))
        bowler=wicket*25
        catch=catch*8
        print(f"{selected_player} points in this match is {bowler+catch}")
    
    else:
         print(f"{selected_player} is not available in this match")
            











