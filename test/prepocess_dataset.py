from datasets import load_dataset, Dataset

from enums.datasets import DatasetEnum
import pickle

import pandas as pd 

class DatasetLoader:
    @staticmethod
    def load(config, preprocess=True):
        if config["dataset"] == DatasetEnum.HOVER:
            dataset = load_dataset("hover", split="validation")
        elif config["dataset"] == DatasetEnum.CLIMATE_FEVER:
            dataset = load_dataset("climate_fever", split="test")
        elif config["dataset"] == DatasetEnum.HEALTH_FC:
            dataset = load_dataset("csv", data_files="datasets_local/healthFC_annotated.csv")["train"]
        elif config["dataset"] == DatasetEnum.COVERT:
            #with open("datasets_local/covert.pkl", 'rb') as file:
            #    data_dict = pickle.load(file)
            #data_dict.pop("evidence")
            covert_df = pd.read_json("datasets_local/CoVERT_FC_annotations.jsonl", lines=True)
            covert_claims = covert_df.claim.tolist()
            covert_claims = [c.replace("@username", "").replace("\n", " ") for c in covert_claims]

            covert_labels = covert_df.label.tolist()
            mapper = {'REFUTES':0, 'SUPPORTS':1, 'NOT ENOUGH INFO':2}
            covert_labels = [mapper[l] for l in covert_labels]

            covert_df["label"] = covert_labels

            covert_dict = {"claim":covert_claims, "label":covert_labels}
            dataset = Dataset.from_dict(covert_dict)

        elif config["dataset"] == DatasetEnum.FACTKG:
            with open("datasets_local/factkg_test.pickle", 'rb') as file:
                d = pickle.load(file)

            claims = []
            for claim, data in d.items():
                data["claim"] = claim
                claims.append(data)
            dataset = Dataset.from_list(claims)

        elif config["dataset"] == DatasetEnum.SCIFACT:
            scifact_df = pd.read_csv("datasets_local/scifact_no-nei_dataset.csv", index_col=[0])
            scifact_claims = scifact_df.claim.tolist()
            scifact_labels = scifact_df.label.tolist()

            scifact_dict = {"claim":scifact_claims, "label":scifact_labels}
            dataset = Dataset.from_dict(scifact_dict)

        else:
            raise Exception(f"Loader for dataset {config['dataset']} not available.")

        if preprocess:
            return DatasetLoader.preprocess(config, dataset)

        return dataset

    @staticmethod
    def preprocess(config, dataset):
        if config["dataset"] == DatasetEnum.HOVER:
            return DatasetLoader.hover(config, dataset)
        elif config["dataset"] == DatasetEnum.CLIMATE_FEVER:
            return DatasetLoader.climate_fever(dataset)
        elif config["dataset"] == DatasetEnum.HEALTH_FC:
            return DatasetLoader.health_fc(dataset)
        elif config["dataset"] == DatasetEnum.COVERT:
            return DatasetLoader.covert(dataset)
        elif config["dataset"] == DatasetEnum.FACTKG:
            return DatasetLoader.factkg(dataset)
        elif config["dataset"] == DatasetEnum.SCIFACT:
            return DatasetLoader.covert(dataset)

        raise Exception(f"Dataset {config['dataset']} could not be processed")

    @staticmethod
    def hover(config, dataset):

        return dataset.remove_columns(["id", 'supporting_facts', 'hpqa_id']). \
            rename_column("uid", "id"). \
            filter(lambda row: row["num_hops"] == config["num_hops"])

    @staticmethod
    def climate_fever(dataset):
        def extract_veracity(row):
            if row["label"] == 0:
                row["label"] = 1
            elif row["label"] == 1:
                row["label"] = 0

            return row

        return dataset.remove_columns(["evidences"]). \
            rename_column("claim_id", "id"). \
            rename_column("claim_label", "label"). \
            map(extract_veracity)

    @staticmethod
    def health_fc(dataset):
        
        def extract_veracity(row):
            if row["label"] == 0:
                row["label"] = 1
            elif row["label"] == 2:
                row["label"] = 0
            else:
                row["label"] = 2

            return row

        #with open("datasets_local/healthfc_claims_new.pkl", "rb") as g:
        #    claims = pickle.load(g)
        df = pd.read_csv("datasets_local/healthFC_annotated.csv")
        claims = df.en_claim.tolist()
        labels = df.label.tolist()
        yesno_claims = df[df.label != 1].en_claim.tolist() #include only positive/negative claims
        yesno_labels = df[df.label != 1].label.tolist()

        scifact_dict = {"claim":yesno_claims, "label":yesno_labels}
        dataset = Dataset.from_dict(scifact_dict)
        
        """ 
        return dataset.remove_columns(['en_explanation', 'en_text', 'en_studies', 'en_sentences', 'en_ids',
                                       'de_verdict', 'de_claim', 'de_explanation', 'de_text', 'de_studies',
                                       'de_sentences', 'de_ids', 'de_title', 'authors', 'url']). \
            map(extract_veracity). \
            add_column("claim", yesno_claims)
        """

        return dataset

    @staticmethod
    def covert(dataset):
        def extract_veracity(row):
            if row["label"] == "SUPPORTS":
                row["label"] = 1
            elif row["label"] == "REFUTES":
                row["label"] = 0
            else:
                row["label"] = 2

            return row

        return dataset
        #return dataset.map(extract_veracity)

    @staticmethod
    def factkg(dataset):
        def extract_veracity(row):
            if row["Label"][0] == True:
                row["label"] = 1
            elif row["Label"][0] == False:
                row["label"] = 0
            return row

        return dataset.map(extract_veracity)
