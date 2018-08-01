#!/usr/bin/env python

from spacy import displacy

import zh_core_web_sm

nlp = zh_core_web_sm.load()


def main():
    doc = nlp("王小明在北京的清华大学读书")
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop, token.has_vector,
              token.ent_iob_, token.ent_type_,
              token.vector_norm, token.is_oov)

    # displacy.serve(doc)


if __name__ == "__main__":
    main()
