import re

class MooreMachine:
    def __init__(self):
        # Patrones regex para identificar los diferentes tipos
        self.patterns = {
            "NAME": re.compile(r"^([A-Z][a-z]+( [A-Z][a-z]+)*)$"),
            "COMMENT": re.compile(r"^[A-Za-z ,.;]*$"),
            "PHONE": re.compile(r"^\d{8}$"),
            "NIT": re.compile(r"^\d{4,8}-(\d{1}|k)$"),
            "EMAIL": re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"),
            "DATE": re.compile(r"^([0-2][0-9]|3[0-1])/([0][1-9]|1[0-2])/[0-9]{2}$"),
            "TIME": re.compile(r"^([0-1][0-9]|2[0-3]):[0-5][0-9](AM|PM)$")
        }
        self.state = "START"

    def process(self, input_data):
        # Separa la entrada usando '&' como delimitador
        parts = input_data.split('&')
        result = []

        # Procesa cada parte para identificar su tipo
        for part in parts:
            dtype = self.identify_type(part)
            result.append(f"{part}: {dtype}")

        return result

    def identify_type(self, input_data):
        # Identifica el tipo de dato según el patrón
        for dtype, pattern in self.patterns.items():
            if pattern.match(input_data):
                return dtype
        return "ERROR"