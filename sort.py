import numpy as np
data_type=[("name","S18"),("class",int),("height",float)]
student_details=[("John",9,5.2),("Alex",8,5.0),("Jason",10,5.6)]
structured_arr=np.array(student_details,dtype=data_type)
print("original arr",student_details)
print("atructured arr",structured_arr)
print("Sorting by height:",np.sort(structured_arr,order="height"))