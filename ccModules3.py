import pandas as pd







def read_spread(file, sheet=0, index_col=None, header=None):
    if 'ods' in file:
        engine = 'odf'
    else:
        engine = 'openpyxl'
    
    return pd.read_excel(file, sheet_name=sheet, engine=engine,index_col=index_col, header=header)

def write_spread(frame, file, index=False):
    if 'ods' in file:
        engine = 'odf'
    else:
        engine = 'openpyxl'
    
    return frame.to_excel(file, engine=engine, index=index)