def remove_markup(text):
    # 強調マークアップの除去
    pattern = r'\'{2,5}'
    text = re.sub(pattern, '', text)

    return text


result_rm = {k: remove_markup(v) for k, v in result.items()}
for k, v in result_rm.items():
    print(k + ': ' + v)
