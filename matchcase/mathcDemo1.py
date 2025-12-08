'''
    match(choice):
        case 1:
            block
        case 2:
            block    

'''

choice = int(input(f" enter 1 for Add \n enter 2 for sub \n enter 3 for mul"))

match choice:
    case 1:
        print("add block called..")
    case 2:
        print("sub block called..")
    case _:
        print("invalid choice..")        
