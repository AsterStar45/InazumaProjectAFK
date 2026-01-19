REGIONES = [
    {
        "nombre": "Empezar Partido",
        "region": (0.411, 0.880, 0.182, 0.074),
        "palabras": ["EMP", "PART", "PULSA", "BOTON"],
        "min_match": 1,        
        "tecla": "enter",
        "cooldown": 0.1,
        "psm": 7,
        "lang": "eng"
    },

    {
        "nombre": "Confirmar Si",
        "region": (0.250, 0.556, 0.156, 0.074),
        "palabras": ["SI"],
        "tecla": "enter",
        "cooldown": 0.1,
        "psm": 7,
        "lang": "eng"
    },

    {
        "nombre": "Todo listo",
        "region": (0.7333, 0.8343, 0.0781, 0.0741),
        "palabras": ["LISTO"],
        "repetir_texto": False,
        "tecla": "e",
        "cooldown": 0.1,
        "psm": 7,
        "lang": "eng"
    },    
    
    {
        "nombre": "Comenzar 2da Parte",
        "region": (0.817, 0.889, 0.104, 0.065),
        "palabras": ["COM", "SIG", "FIN"],
        "repetir_texto": True,
        "min_match": 1,            
        "tecla": "enter",
        "cooldown": 0.1,
        "psm": 6,
        "lang": "eng"
    },

    {
        "nombre": "Siguiente / Finalizar",
        "region": (0.818, 0.833, 0.167, 0.074),
        "palabras": ["SIGUIENTE", "FINALIZAR", "PARTIDO"],
        "min_match": 1,         
        "repetir_texto": True,
        "tecla": "enter",
        "cooldown": 0.1,
        "psm": 6,
        "lang": "eng"
    },

    {
        "nombre": "Terminar edicion",
        "region": (0.120, 0.889, 0.208, 0.083),
        "palabras": ["TERMINAR", "EDICION"],
        "repetir_texto": True,
        "click": True,
        "click_pos": "center",
        "click_tipo": "left",
        "click_delay": 0.1,
        "cooldown": 0.1,
        "psm": 7,
        "lang": "eng"
    },

    {
        "nombre": "Saque de Centro",
        "region": (0.510, 0.824, 0.073, 0.083),
        "palabras": ["CENTRO"],
        "repetir_texto": False,
        "click": True,
        "click_pos": "center",
        "click_tipo": "left",
        "click_delay": 0.1,
        "cooldown": 0.1,
        "psm": 7,
        "lang": "eng"
    },

    {
        "nombre": "Reanudar",
        "region": (0.510, 0.824, 0.073, 0.083),
        "palabras": ["IDAR"],
        "repetir_texto": True,
        "click": True,
        "click_pos": "center",
        "click_tipo": "left",
        "click_delay": 0.1,
        "cooldown": 0.1,
        "psm": 6,
        "lang": "eng"
    },    

    {
        "nombre": "Equipo rival",
        "region": (0.458, 0.315, 0.094, 0.037),
        "palabras": ["LUZ", "ETE"],
        "min_match": 1,          
        "repetir_texto": False,
        "click": True,
        "click_pos": (0.495, 0.477),
        "click_tipo": "left",
        "click_delay": 0.1,
        "cooldown": 0.1,
        "psm": 7,
        "lang": "eng"
    },    

    {
        "nombre": "Batalla heroica",
        "region": (0.130, 0.444, 0.063, 0.056),
        "palabras": ["PLAN"],     
        "min_match": 1,             
        "repetir_texto": True,
        "click": True,
        "click_pos": (0.216, 0.722),
        "click_tipo": "left",
        "click_delay": 0.5,
        "cooldown": 0.5,
        "psm": 7,
        "lang": "eng"
    },        
]
