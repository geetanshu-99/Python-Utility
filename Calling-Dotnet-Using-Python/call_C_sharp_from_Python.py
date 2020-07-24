import sys

assembly_path = r"/Users/mayankkhanna/Work/Dotnet/CallCSFromPy"
sys.path.append(assembly_path)

import clr
clr.AddReference("Calculate")
from CallCSFromPy import Calculate
ct = Calculate()

print(ct.Add(1,4))
print(ct.Subtract(7,11))

# We can also execute the function like this
# params = [1,2]
# print(ct.Add(*params))
# print(ct.Subtract(*params))