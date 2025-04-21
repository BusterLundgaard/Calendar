weekdays = ['Mon', 'Tue', 'Wen', 'Thur', 'Fri', 'Sat', 'Sun']    
    
def main():
    res = ""
    lines = open("cal.org", "r").readlines()
    l = [line.strip() for line in lines]
    weekday = 2 
    week = 2
    
    for line in l:
        if line.startswith("** "):
            res += line + ": Week " + str(week) + " -- " + str(week+4) + "\n"
        elif line.startswith("*** "):
            if weekday == 0:
                res += line + " " + weekdays[weekday] + " - Week " + str(week) + "\n"
                week += 1
            else:
                res += line + " " + weekdays[weekday] + "\n"
            weekday = (weekday + 1) % 7
        else:
            res += line + "\n"

    open("fixed.org", "w").write(res)

if __name__ == "__main__":
    main()
