
string = "PAYPALISHIRING"
nrows = 3
#def acrosticker(string, nrows):
    # #ans_array = []
    # col1=string[:nrows]
    # # how many rows are single letters zagging
    # zagrows = nrows//2
    # col2 =
    # col3 =
    # have to move row wise
    
def acrosticker(string, nrows):
    if nrows == 1:
        return string

    rows = [""] * nrows
    current_row = 0
    going_down = False

    for char in string:
        rows[current_row] += char
        if current_row == 0 or current_row == nrows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1

    return "".join(rows)