import sys


script = open('add_id.py').read()
sys.argv = ["add_id.py", 'VIP']
exec(script)
