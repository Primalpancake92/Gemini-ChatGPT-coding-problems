def active_borrower(borrow_log):
    active = 0
    
    for detail in borrow_log:
        return_date = detail[3]
        
        if return_date == "None":
            active += 1
    
    return active    
    

def main():
    with open("borrowers.txt") as f:
        borrow_log = [line.strip().split(",") for line in f]
        print(active_borrower(borrow_log))


main()