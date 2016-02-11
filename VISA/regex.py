import re 
import sys

data ="""
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
sys.stdout.write(pat.sub("\g<1>;", data))