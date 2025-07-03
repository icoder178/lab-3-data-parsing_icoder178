import pandas as pd 
df = {}
df['raw'] = pd.read_csv("messy_strings.csv")

# baseline Python approach
def clean_strings(strings):
    strings = df['raw'].values.tolist()
    ret = []
    for _ in strings:
        for s in _:
            curr = []
            for x in s:
                if (ord(x) >= ord('a') and ord(x) <= ord('z')) or (ord(x) >= ord('0') and ord(x) <= ord('9')):
                    curr.append(x)
                elif ord(x) >= ord('A') and ord(x) <= ord('Z'):
                    curr.append(chr(ord(x)-ord('A')+ord('a')))
            if len(curr) > 0:
                ret.append(''.join(curr))
    return pd.DataFrame({'clean': ret})
# TODO: pandas method

df['clean'] = clean_strings(df['raw'])

print(f"Cleaned data has {df['clean'].size} rows.")
stats = df['clean'].value_counts()
print(f"Cleaned data has {stats.count()} unique names.")
print(f"Most common name in cleaned data is \"{stats.index[0][0]}\".")

#hacky mess (I think I broke something previously)
pd.DataFrame({'raw': df['raw'].values.tolist(), 'clean': df['clean'].values.tolist()},index=range(50)).to_csv('messy_strings_clean.csv', index=False)

stats.head(5).plot.bar()