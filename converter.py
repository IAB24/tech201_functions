def cm_to_m_converter(cm: int):
     formula = int(cm) / 100
     return formula
custom_input = int(input("Please enter a value in cm"))

functioncall = cm_to_m_converter(custom_input)


print(functioncall, "m")

def m_to_feet_converter(m: int):
     formula = int(m) * 3.28084
     return formula
custom_input = int(input("Please enter a value in m"))

functioncall = m_to_feet_converter(custom_input)

print(functioncall, "feet")


