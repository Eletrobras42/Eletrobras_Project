class NormalizationService:
    @staticmethod
    def normalize_indicator_name(raw_text: str) -> str:
        return raw_text.strip().lower()

    @staticmethod
    def parse_numeric_value(value_text: str):
        try:
            return float(value_text.replace(".", "").replace(",", "."))
        except Exception:
            return None
