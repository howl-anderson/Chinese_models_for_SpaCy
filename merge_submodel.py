#!/usr/bin/python3

import shutil
import json
from pathlib import Path


def read_pipeline(meta_file):
    with open(meta_file) as fd:
        data = json.load(fd)
        return data["pipeline"]


def update_pipeline(meta_file, pipeline):
    with open(meta_file) as fd:
        data = json.load(fd)

    data["pipeline"] = pipeline

    with open(meta_file, "w") as fd:
        json.dump(data, fd)


def copy_tree(src: Path, dst: Path, folder: str):
    shutil.copytree(src / folder, dst / folder)


def main():
    target_dir = Path("./spacy_models/final_model")
    target_dir.mkdir(exist_ok=True)

    pipeline = []

    source_dir = Path("./spacy_models/dependency_model/model-best")
    copy_tree(source_dir, target_dir, "parser")
    copy_tree(source_dir, target_dir, "tagger")
    copy_tree(source_dir, target_dir, "vocab")

    pipeline.extend(read_pipeline(source_dir / "meta.json"))

    source_dir = Path("./spacy_models/ner_model/model-best")
    copy_tree(source_dir, target_dir, "ner")
    shutil.copy(source_dir / "meta.json", target_dir / "meta.json")

    pipeline.extend(read_pipeline(source_dir / "meta.json"))

    update_pipeline(target_dir / "meta.json", pipeline)


if __name__ == "__main__":
    main()
