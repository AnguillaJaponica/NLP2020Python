def remove_markup(text):
    # 強調マークアップの除去
    pattern = r'\'{2,5}'
    text = re.sub(pattern, '', text)

    # 内部リンクマークアップの除去
    pattern = r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]'
    text = re.sub(pattern, r'\1', text)

    # 外部リンクマークアップの除去
    pattern = r'https?://[\w!?/\+\-_~=;\.,*&@#$%\(\)\'\[\]]+'
    text = re.sub(pattern, '', text)

    # htmlタグの除去
    pattern = r'<.+?>'
    text = re.sub(pattern, '', text)

    # テンプレートの除去
    pattern = r'\{\{(?:lang|仮リンク)(?:[^|]*?\|)*?([^|]*?)\}\}'
    text = re.sub(pattern, r'\1', text)

    return text


result_rm = {k: remove_markup(v) for k, v in result.items()}
for k, v in result_rm.items():
    print(k + ': ' + v)
