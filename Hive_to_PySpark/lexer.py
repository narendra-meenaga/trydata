import re

# def lex(characters,token_defs):
#     pos = 0
#     tokens_list = []
#     while pos < len(characters):
#         match = None
#         for token_def in token_defs:
#             pattern, tag = token_def
#             regex = re.compile(pattern)
#             match = regex.match(characters, pos)
#             if match:
#                 text = match.group(0)
#                 if tag:
#                     token = (text, tag)
#                     tokens_list.append(token)
#                 break
#         if not match:
#             sys.stderr.write('Illegal character: %s\\n' % characters[pos])
#             sys.exit(1)
#         else:
#             pos = match.end(0)
#     return tokens_list
         
def lex(characters,token_defs):
    pos = 0
    tokens_list = []
    while pos < len(characters):
        match = None
        for token_def in token_defs:
            pattern, tag = token_def
            print(pattern)
            