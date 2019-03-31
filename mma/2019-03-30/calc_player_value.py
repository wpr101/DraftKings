class Player():
    def __init__(self, name, odds, salary):
        self.name = name
        self.odds = int(odds)
        self.salary = int(salary)

    def __repr__(self):
        return 'Player(name=%s, odds=%s, salary=%s)' % \
    (self.name, self.odds, self.salary)



def convert_to_percent(odds):
    percent = 1
    if odds < 0:
        percent *= float(odds) / float((odds - 100))
    else:
        percent *= float(100) / float((odds + 100))
    return (percent)

print(convert_to_percent(-369))

#(9600, .80)
#(9500, .78)
#(9400, .76)
#(9300, .74)
#(9200, .72)
#(9100, .70)
#(9000, .68)
#(8900, .66)
#(8800, .64)
#(8700, .62)
#(8600, .60)
#(8500, .58)
#(8400, .56)
#(8300, .54)
#(8200, .52)
#(8100, .50)
#(8000, .48)
#(7900, .46)
#(7800, .44)
#(7700, .42)
#(7600, .40)
#(7500, .38)
#(7400, .36)
#(7300, .34)
#(7200, .32)
#(7100, .30)
#(7000, .28)
#(6900, .26)
#(6800, .24)
#(6700, .22)
#(6600, .20)
