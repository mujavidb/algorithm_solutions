type position = int * int
type spreadsheet
 
val create    : unit -> spreadsheet
val set_const : spreadsheet -> position -> float -> unit
val set_sum   : spreadsheet -> position -> position -> position -> unit
                                 target      cell1      cell2
val get_value : spreadsheet -> position -> float option

set_const sheet (0,0) 7;
set_const sheet (0,1) 4;
set_sum sheet (1,0) (0,1) (0,0);

get_value sheet (1,0)    (* returns 11 *)
set_const sheet (0,1) 5
get_value sheet (1,0)    (* returns 12 *)



class Cell:
    def __init__(self, constant_value=None, x1=None, y1=None, x2=None, y2=None):
        self.constant_value = constant_value
        self.first = [x1,y1]
        self.second = [x2,y2]

# Cell(constant_value=5)
# Cell(x1=0,x2=5,y1=1,y2=5)

#       if x1:
#           self.value = self.spreadsheet.cells[x1][y1] + self.spreadsheet.cells[x2][y2]

class Spreadsheet:
    def __init__(self, rows, columns):
        self.cells = []
        #table created of size x by y, all init to 0
            # = Cell(0)
        self.rows = rows
        self.columns = columns
    
    def getValue(self,x,y):
        if x <= self.rows and x >=0 and y <= self.columns and y >=0:
            if self.cells[x][y].constant_value != None:
                return self.cells[x][y].constant_value
            else:
                first = self.cells[x][y].first
                second = self.cells[x][y].second
                if first == second:
                    return self.getValue(first[0],first[1]) * 2
                else:
                    return self.getValue(first[0],first[1]) + self.getValue(second[0],second[1])

(0,0) is 1
(0,1) is (0,0) + (0,0)
(0,2) is (0,1) + (0,1)
(0,3) is (0,2) + (0,2)
...
(0,n) is (0,n-1) + (0,n-1)

How many times do we visit (0,0) if I call getValue(0,n)


(0,0) is 1
(1,0) is 1

(0,1) is (0,0) + (1,0)
(1,1) is (0,0) + (1,0)

(0,2) is (0,1) + (1,1)
(1,2) is (0,1) + (1,1)

(0,3) is (0,2) + (1,2)
(1,3) is (0,2) + (1,2)

...

(0,n) is (0,n-1) + (1,n-1)
(1,n) is (0,n-1) + (1,n-1)

How many times do we visit (0,0) if I call getValue(0,n)







Cell(0, spredsheet)
Cell(0, spredsheet, x1, y1, x2, y2)
            
            
            
            
            
            