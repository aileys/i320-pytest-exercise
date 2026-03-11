import pytest

def fix_phone_num(phone_num_to_fix):
    if len(phone_num_to_fix) != 10:
        raise ValueError("Input must be exactly 10 digits")
    if not phone_num_to_fix.isdigit():
        raise ValueError("Input must contain only numeric digits")
    
    area_code = phone_num_to_fix[0:3]
    three_part = phone_num_to_fix[3:6]
    four_part = phone_num_to_fix[6:]
    
    fixed_num = "(" + area_code + ")" + " " + three_part + "-" + four_part
    
    return fixed_num
  
