# Filter-CSV-into-New-CSV-by-State
This is a simple program where you put inside the code the URL to the CSV you want to filter and what USA state you want to filter by. It will then generate a new csv file keeping the rows that are only in the state specfied

How to use:
Remember to install Python 3. 
Go to this line in the code: input_file = 'PATH HERE'   # Replace with your file name
if you use windows 11 copy as path then remove one set of the quotations as the duplicate will cause an issue.
Now for row five, `state_column_name = 'state'  # Replace with your column name if different, like if is "States" OR whatever.` Do as the comment says.
In the CSV I was programming this for it was called "state" so I just used that.
Go to line 17. `if row[state_column_name].strip().upper() == "ST":` replace the ST with your state name like the comment says. The two digit code thing (example CA, NY, NJ, FL, etc.) 
