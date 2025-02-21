from enum import Enum


class DatasetEnum(str, Enum):
    HOVER = "hover"
    CLIMATE_FEVER = "climate-fever"
    HEALTH_FC = "health-fc"
    COVERT = "covert"
    FACTKG = "factkg"
    SCIFACT = "scifact"

