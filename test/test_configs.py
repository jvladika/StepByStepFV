from enums.datasets import DatasetEnum
from enums.method import MethodEnum
from enums.reasoning import ReasoningEnum
from enums.source import EvidenceSourceEnum

TEST_CONFIGS = {
    "QACHECK_GPT3.5_GPT3.5_HOVER_2HOP": {
        "method": MethodEnum.QACHECK,
        "reasoning": ReasoningEnum.GPT_3_5,
        "evidence_source": EvidenceSourceEnum.GPT_3_5,
        "dataset": DatasetEnum.HOVER,
        "num_hops": 2
    },
    "QACHECK_GPT3.5_GPT3.5_HOVER_3HOP": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.GPT_3_5,
            "evidence_source": EvidenceSourceEnum.GPT_3_5,
            "dataset": DatasetEnum.HOVER,
            "num_hops": 3
        },
    "QACHECK_GPT3.5_GPT3.5_HOVER_4HOP": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.GPT_3_5,
            "evidence_source": EvidenceSourceEnum.GPT_3_5,
            "dataset": DatasetEnum.HOVER,
            "num_hops": 4
        },
    "QACHECK_GPT3.5_HUGGINGCHAT_HOVER_2HOP": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.GPT_3_5,
            "evidence_source": EvidenceSourceEnum.HUGGING_CHAT,
            "dataset": DatasetEnum.HOVER,
            "num_hops": 2
        },
    "QACHECK_GPT3.5_HUGGINGCHAT_HOVER_3HOP": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.GPT_3_5,
            "evidence_source": EvidenceSourceEnum.HUGGING_CHAT,
            "dataset": DatasetEnum.HOVER,
            "num_hops": 3
        },
    "QACHECK_GPT3.5_HUGGINGCHAT_HOVER_4HOP": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.GPT_3_5,
            "evidence_source": EvidenceSourceEnum.HUGGING_CHAT,
            "dataset": DatasetEnum.HOVER,
            "num_hops": 4
        },
    "QACHECK_GPT3.5_GOOGLE_HOVER_2HOP": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.GPT_3_5,
            "evidence_source": EvidenceSourceEnum.GOOGLE,
            "dataset": DatasetEnum.HOVER,
            "num_hops": 2
        },
    "QACHECK_GPT3.5_GOOGLE_HOVER_3HOP": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.GPT_3_5,
            "evidence_source": EvidenceSourceEnum.GOOGLE,
            "dataset": DatasetEnum.HOVER,
            "num_hops": 3
        },
    "QACHECK_GPT3.5_DUCK_HEALTHFC": {
        "method": MethodEnum.QACHECK,
        "reasoning": ReasoningEnum.GPT_3_5,
        "evidence_source": EvidenceSourceEnum.DUCK,
        "dataset": DatasetEnum.HEALTH_FC,
        "num_hops": 3
    },
    "QACHECK_GPT3.5_DUCK_COVERT": {
        "method": MethodEnum.QACHECK,
        "reasoning": ReasoningEnum.GPT_3_5,
        "evidence_source": EvidenceSourceEnum.DUCK,
        "dataset": DatasetEnum.COVERT,
        "num_hops": 3
    },
    "QACHECK_GPT3.5_DUCK_SCIFACT": {
        "method": MethodEnum.QACHECK,
        "reasoning": ReasoningEnum.GPT_3_5,
        "evidence_source": EvidenceSourceEnum.DUCK,
        "dataset": DatasetEnum.SCIFACT,
        "num_hops": 3
    },
    "FOLK_GPT3.5_DUCK_HEALTHFC": {
        "method": MethodEnum.FOLK,
        "reasoning": ReasoningEnum.GPT_3_5,
        "evidence_source": EvidenceSourceEnum.DUCK,
        "dataset": DatasetEnum.HEALTH_FC,
        "num_hops": 3
    },
     "FOLK_GPT3.5_DUCK_COVERT": {
        "method": MethodEnum.FOLK,
        "reasoning": ReasoningEnum.GPT_3_5,
        "evidence_source": EvidenceSourceEnum.DUCK,
        "dataset": DatasetEnum.COVERT,
        "num_hops": 3
    },
    "FOLK_GPT3.5_DUCK_SCIFACT": {
        "method": MethodEnum.FOLK,
        "reasoning": ReasoningEnum.GPT_3_5,
        "evidence_source": EvidenceSourceEnum.DUCK,
        "dataset": DatasetEnum.SCIFACT,
        "num_hops": 3
    },
     "QACHECK_INTERNAL_HEALTHFC": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.GPT_3_5,
            "evidence_source": EvidenceSourceEnum.GPT_3_5,
            "dataset": DatasetEnum.HEALTH_FC,
            "num_hops": 4
        },
    "QACHECK_INTERNAL_COVERT": {
        "method": MethodEnum.QACHECK,
        "reasoning": ReasoningEnum.GPT_3_5,
        "evidence_source": EvidenceSourceEnum.GPT_3_5,
        "dataset": DatasetEnum.COVERT,
        "num_hops": 4
    },

     "QACHECK_INTERNAL_SCIFACT": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.GPT_3_5,
            "evidence_source": EvidenceSourceEnum.GPT_3_5,
            "dataset": DatasetEnum.SCIFACT,
            "num_hops": 4
        },

    "FOLK_INTERNAL_HEALTHFC": {
            "method": MethodEnum.FOLK,
            "reasoning": ReasoningEnum.GPT_3_5,
            "evidence_source": EvidenceSourceEnum.GPT_3_5,
            "dataset": DatasetEnum.HEALTH_FC,
            "num_hops": 4
        },

    "FOLK_INTERNAL_COVERT": {
            "method": MethodEnum.FOLK,
            "reasoning": ReasoningEnum.GPT_3_5,
            "evidence_source": EvidenceSourceEnum.GPT_3_5,
            "dataset": DatasetEnum.COVERT,
            "num_hops": 4
        },

    "FOLK_INTERNAL_SCIFACT": {
            "method": MethodEnum.FOLK,
            "reasoning": ReasoningEnum.GPT_3_5,
            "evidence_source": EvidenceSourceEnum.GPT_3_5,
            "dataset": DatasetEnum.SCIFACT,
            "num_hops": 4
        },
    "QACHECK_MIXTRAL_INTERNAL_HEALTHFC": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.MIXTRAL,
            "evidence_source": EvidenceSourceEnum.MIXTRAL,
            "dataset": DatasetEnum.HEALTH_FC,
            "num_hops": 4
        },

        "QACHECK_MIXTRAL_INTERNAL_SCIFACT": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.MIXTRAL,
            "evidence_source": EvidenceSourceEnum.MIXTRAL,
            "dataset": DatasetEnum.SCIFACT,
            "num_hops": 4
        },

        "QACHECK_MIXTRAL_INTERNAL_COVERT": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.MIXTRAL,
            "evidence_source": EvidenceSourceEnum.MIXTRAL,
            "dataset": DatasetEnum.COVERT,
            "num_hops": 4
        },


        "QACHECK_MIXTRAL_DUCK_HEALTHFC": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.MIXTRAL,
            "evidence_source": EvidenceSourceEnum.DUCK,
            "dataset": DatasetEnum.HEALTH_FC,
            "num_hops": 4,
            "range_from":200
        },

       "QACHECK_MIXTRAL_DUCK_COVERT": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.MIXTRAL,
            "evidence_source": EvidenceSourceEnum.DUCK,
            "dataset": DatasetEnum.COVERT,
            "num_hops": 4
        },

             "QACHECK_MIXTRAL_DUCK_SCIFACT": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.MIXTRAL,
            "evidence_source": EvidenceSourceEnum.DUCK,
            "dataset": DatasetEnum.SCIFACT,
            "num_hops": 4
        },

    
    "QACHECK_LLAMA_INTERNAL_HEALTHFC": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.MIXTRAL,
            "evidence_source": EvidenceSourceEnum.MIXTRAL,
            "dataset": DatasetEnum.HEALTH_FC,
            "num_hops": 4
        },

        "QACHECK_LLAMA_INTERNAL_SCIFACT": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.MIXTRAL,
            "evidence_source": EvidenceSourceEnum.MIXTRAL,
            "dataset": DatasetEnum.SCIFACT,
            "num_hops": 4
        },

        "QACHECK_LLAMA_INTERNAL_COVERT": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.MIXTRAL,
            "evidence_source": EvidenceSourceEnum.MIXTRAL,
            "dataset": DatasetEnum.COVERT,
            "num_hops": 4
        },

         "QACHECK_LLAMA_DUCK_HEALTHFC": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.MIXTRAL,
            "evidence_source": EvidenceSourceEnum.DUCK,
            "dataset": DatasetEnum.HEALTH_FC,
            "num_hops": 4,
            "range_from":200
        },

       "QACHECK_LLAMA_DUCK_COVERT": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.MIXTRAL,
            "evidence_source": EvidenceSourceEnum.DUCK,
            "dataset": DatasetEnum.COVERT,
            "num_hops": 4
        },

             "QACHECK_LLAMA_DUCK_SCIFACT": {
            "method": MethodEnum.QACHECK,
            "reasoning": ReasoningEnum.MIXTRAL,
            "evidence_source": EvidenceSourceEnum.DUCK,
            "dataset": DatasetEnum.SCIFACT,
            "num_hops": 4,
            "range_from":366
        },



}