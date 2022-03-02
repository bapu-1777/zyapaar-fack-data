# BY MAYANK
import string
import random
import numpy as np

pan=''.join(np.random.choice(list(string.ascii_uppercase), size=3, replace=False))+random.choice("CPHFATBLJG")+random.choice(list(string.ascii_uppercase))+(str(random.randint(1,9999))).zfill(4)+random.choice(list(string.ascii_uppercase))

gst=(str(random.randint(1,35))).zfill(2)+pan+str(random.randint(0,9))+random.choice(list(string.ascii_uppercase))+random.choice("CPHFATBLJG")

aathar1=''.join(np.random.choice(list(string.ascii_uppercase), size=2, replace=False))+(str(random.randint(1,999999999))).zfill(10)
aathar2="UDYAM-"+''.join(np.random.choice(list(string.ascii_uppercase), size=2, replace=False))+"-"+(str(random.randint(1,35))).zfill(2)+"-"+(str(random.randint(1,9999999))).zfill(7)

print("PAN NUMBER : "+pan+"\nGST NUMBER : "+gst+"\nOLD UDYAM AATHAR : "+aathar1+
"\nNEW UDYAM AATHAR : "+aathar2)
