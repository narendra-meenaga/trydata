

token_defs = [
              (r'[ \n\t]+',None),       
              (r'--[^\n]*',None),
              (r'[0-9]+','INTEG'),
              (r'[A-Za-z][A-Za-z0-9_]*','VAR'),
              (r';','RESERVED'),
              (r'*','RESERVED'),
              (r'>','RESERVED'),
              (r'SELECT','RESERVED'),
              (r'FROM','RESERVED'),
              (r'WHERE','RESERVED'),
              (r'LOAD','RESERVED'),
              (r'DATA','RESERVED'),
              (r'LOCAL','RESERVED'),
              (r'INPATH','RESERVED'),
              (r'OVERWRITE','RESERVED'),
              (r'INTO','RESERVED'),
              (r'TABLE','RESERVED')
             ]