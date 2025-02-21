from enum import Enum


class EvidenceSourceEnum(str, Enum):
    GPT_3_5 = "gpt-4o-mini"  # "Base model"
    MIXTRAL = "llama"  # "Base model"
    GOOGLE = "google"  # "Google search"
    HUGGING_CHAT = "huggingchat"  # "HuggingChat"
    DUCK = "duckduckgo"
