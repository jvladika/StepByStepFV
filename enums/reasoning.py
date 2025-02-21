from enum import Enum


class ReasoningEnum(str, Enum):
    GPT_4 = "gpt-4"
    GPT_3_5 = "gpt-4o-mini"
    MIXTRAL = "mixtral-8x7b-instruct"
    LLAMA = "llama3.1-70b"

