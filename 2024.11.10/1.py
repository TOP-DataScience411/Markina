def strong_password(password):   
    if len(password) < 8:
        return False
        
    u_alpha = 0
    l_alpha = 0
    num = 0
    other = 0
    
    for i in password:
        if i.isupper():
            u_alpha += 1
        elif i.islower():
            l_alpha += 1
        elif i.isdigit():
            num += 1
        else:
            other += 1
         
    if u_alpha > 0 and l_alpha > 0 and num >= 2 and other > 0:
        return True
    else:
        return False

        
# >>> strong_password('aP3:kD_l3')
# True
# >>> strong_password('password')
# False