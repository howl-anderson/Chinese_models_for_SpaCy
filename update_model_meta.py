import json


def main():
    with open("./spacy_models/base_model/meta.json") as fd:
        data = json.load(infd)

    data["name"] = "core_web_sm"

    with open("./spacy_models/base_model/meta.json", "wt") as fd:
        json.dump(data, fd)


if __name__ == "__main__":
    main()
