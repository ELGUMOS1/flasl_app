# Check the PYTHONPATH environment variable before beginning to ensure that the
# top-level directory is included.  If not, append the top-level.  This allows
# the modules within the .../project/ directory to be discovered.
import sys
import os

print('Creating database tables ...')

if os.path.abspath(os.curdir) not in sys.path:
    print('...missing directory in PYTHONPATH... added!')
    sys.path.append(os.path.abspath(os.curdir))


# Create the database tables, add some initial data, and commit to the database
from project import db
from project.models import Solutions

def solveNQueens(n):
	sols = []
	def dfs(state, pd, nd):
		r = len(state)
		if r < n:
			for c in range(n):
				if c not in state and c-r not in pd and c+r not in nd:
					dfs(state+[c], pd|{c-r}, nd|{c+r})
		else: 
			sols.append(state)
	
	dfs([], set(), set())
	return sols
	
# Drop all of the existing database tables
db.drop_all()

# Create the database and the database table
db.create_all()

# Insert  data
for i in range(1,15):
	    temp = str(solveNQueens(i))
	    sol = Solutions(n = i, sol = temp)
	    db.session.add(sol)
	    db.session.commit()
	    
#
print('...done!')
