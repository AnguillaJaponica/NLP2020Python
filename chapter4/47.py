with open('./ans47.txt', 'w') as f:
    for sentence in sentences:
        for chunk in sentence.chunks:
            for morph in chunk.morphs:
                if morph.pos == '動詞':  # chunkの左から順番に動詞を探す
                    for i, src in enumerate(
                            chunk.srcs):  # 見つけた動詞の係り元chunkが「サ変接続名詞+を」で構成されるか確認
                        if len(sentence.chunks[src].morphs) == 2 and sentence.chunks[src].morphs[
                                0].pos1 == 'サ変接続' and sentence.chunks[src].morphs[1].surface == 'を':
                            predicate = ''.join(
                                [sentence.chunks[src].morphs[0].surface, sentence.chunks[src].morphs[1].surface, morph.base])
                            cases = []
                            modi_chunks = []
                            for src_r in chunk.srcs[:i] + \
                                    chunk.srcs[i + 1:]:  # 残りの係り元chunkから助詞を探す
                                case = [
                                    morph.surface for morph in sentence.chunks[src_r].morphs if morph.pos == '助詞']
                                if len(case) > 0:  # 助詞を含むchunkの場合は助詞と項を取得
                                    cases = cases + case
                                    modi_chunks.append(
                                        ''.join(
                                            morph.surface for morph in sentence.chunks[src_r].morphs if morph.pos != '記号'))
                            if len(
                                    cases) > 0:  # 助詞が1つ以上見つかった場合は重複除去後辞書順にソートし、項と合わせて出力
                                cases = sorted(list(set(cases)))
                                line = '{}\t{}\t{}'.format(
                                    predicate, ' '.join(cases), ' '.join(modi_chunks))
                                print(line, file=f)
                            break
