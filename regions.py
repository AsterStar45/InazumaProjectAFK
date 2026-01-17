REGIONES = [
    {
        "nombre": "Empezar Partido",
        "region": (790, 950, 350, 80),
        "palabras": ["EMP", "PART", "PULSA", "BOTON"],
        "min_match": 1,        
        "tecla": "enter",
        "cooldown": 0.1
        ,
        "psm": 7,
        "lang": "eng"
    },

    {
        "nombre": "Confirmar Si",
        "region": (480, 600, 300, 80),
        "palabras": ["SI"],
        "tecla": "enter",
        "cooldown": 0.1,
        "psm": 7,
        "lang": "eng"
    },
    
    {
        "nombre": "Comenzar 2da Parte",
        "region": (1568, 960, 200, 70),
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
        "region": (1570, 900, 320, 80),
        "palabras": ["SIGUIENTE", "FINALIZAR", "PARTIDO"],
        "min_match": 1,         
        "repetir_texto": True,
        "tecla": "enter",
        "cooldown": 0.1,
        "psm": 7,
        "lang": "eng"
    },

    {
        "nombre": "Terminar edicion",
        "region": (230, 960, 400, 90),
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
        "region": (980, 890, 140, 90),
        "palabras": ["CENT"],
        "min_match": 1,
        "click": True,
        "click_pos": "center",
        "click_tipo": "left",
        "click_delay": 0.1,
        "cooldown": 0.1,
        "psm": 7,
        "lang": "eng"
    },


    {
        "nombre": "Equipo rival",
        "region": (880, 340, 180, 40),
        "palabras": ["LUZ", "ETE"],
        "min_match": 1,          
        "repetir_texto": False,
        "click": True,
        "click_pos": (950, 515),
        "click_tipo": "left",
        "click_delay": 0.1,
        "cooldown": 0.1,
        "psm": 7,
        "lang": "eng"
    },    

    {
        "nombre": "Batalla heroica",
        "region": (250, 480, 120, 60),
        "palabras": ["PLAN"],     
        "min_match": 1,             
        "repetir_texto": True,
        "click": True,
        "click_pos": (415, 780),
        "click_tipo": "left",
        "click_delay": 0.5,
        "cooldown": 0.5,
        "psm": 7,
        "lang": "eng"
    },        
]
