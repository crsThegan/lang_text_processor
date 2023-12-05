def process(text: str):
    res = ""
    cmb = ""
    last_correct = ""
    last_correct_unproc_len = 0
    
    i = 0
    while i < len(text):
        cmb += text[i]
        for j in range(4):
            try:
                last_correct = transl[cmb]
                last_correct_unproc_len = len(cmb)
            except KeyError:
                pass
            if j + i + 1 < len(text):
                cmb += text[i + j + 1]
            else:
                break
            
        res += last_correct if len(last_correct) > 0 else text[i]
        i += last_correct_unproc_len if last_correct_unproc_len > 0 else 1
        
        cmb = last_correct = ""
        last_correct_unproc_len = 0
    return res
