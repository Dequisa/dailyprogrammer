baserow = ['  a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] 
board = ['','','','','','','','',baserow]
pieces_dict = {'p': u"\u265F", 'n':u"\u265E", 'r':u"\u265C", 'b':u"\u265D", 'q':u"\u265B", 'k':u"\u265A", 'P':u"\u2659", 'N':u"\u2658",'R':u"\u2656",'B':u"\u2657",'Q':u"\u2655",'K':u"\u2654"}
#empty squares
light = u"\u2610"
dark  = u"\u2612"

def fen_convert(input_list, row_num):
    return_list = []
    count = 0
    for element in input_list:
        if str(element).isalpha():
            count = count + 1
            return_list.append(pieces_dict[element])
        if str(element).isdigit():
            return_list = return_list + add_some_blanks(int(element), row_num, count)
            count = count + len(add_some_blanks(int(element), row_num, count))
    return return_list

def add_some_blanks(blank_num, row_num, start_num):
    light_dark = [light, dark]
    start_on_light = False
    give_back_list = []
    if row_num%2 == 0:
        if start_num%2 == 0:
            start_on_light = True
        elif start_num%2 == 1:
            start_on_light = False
    if row_num%2 == 1:
        if start_num%2 == 0:
            start_on_light = False
        if start_num%2 == 1:
            start_on_light = True

    if start_on_light:
        for x in range(0, blank_num):
            give_back_list.append(light_dark[x%2])
    
    if not start_on_light:
        for x in range(1, blank_num + 1):
            give_back_list.append(light_dark[x%2])
    return give_back_list

def print_board(fen_list_in):
    row_number = 8
    for x in range (0,8):
        board[x] = fen_convert(list(fen_list_in[x]), x)
    for row in board:
        if row_number >0:
            print row_number,
        row_number = row_number - 1
        for square in row:
            print square,
        print "\n"
    print "\n"

def user_input():
    valid_conditions = False
    while valid_conditions == False:
        count = 0
        valid_conditions = True
        fen_input = raw_input("Please enter a board state using FEN (e.g. 'rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR': ")
        fen_list = fen_input.split('/')
        if len(fen_list) != 8:
            print "You must have 8 entries, each separated by a '/'"
            valid_conditions = False
        if '/' not in fen_input:
            print "You need to use '/' to separate each entry"
            valid_conditions = False
        if '0' in fen_input:
            print "0 is not a valid character in FEN"
        for element in fen_list:
            for char in element:
                if not (char.isdigit() or char.isalpha()):
                    print "Only enter numbers, letters or '/' to show the next row"
                    valid_conditions = False
                    break
                if str(char).isalpha():
                    count = count + 1
                if str(char).isdigit():
                    count = count + int(char)
        if count != 64:
            print "Each row must describe exactly 8 squares"
            valid_conditions = False

        if valid_conditions == True:
            print_board(fen_list)

user_input()
