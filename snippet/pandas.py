# title, content 컬럼을 합쳐서 새로운 컬럼만들기
def make_contents(x):
    if type(x['title']) == str:
        t = x['title'].strip()
    else:
        t = ' '

    if type(x['content']) == str:
        a = x['content'].strip()
    else:
        a = ' '
    return (t + ' ' + a).strip()

df['contents'] = df.apply(make_contents, axis=1)



# 공백제거, http 태그제거
def clean_text(x):
    s = x['article']

    if len(str(s)) >= 2:
        try:
            x = re.sub(r"\s+", " ", s)
            x = re.sub(r"http\S+", "", x)
            x = re.sub(r"<.*?>", "", x)
        except:
            return ''
    else:
        return ''

    return x

df['contents'] = df['contents'].apply(clean_text, axis=1)



# pandas print options
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
