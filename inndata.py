import configparser

class Inndata(object):
    """Klasse som holder inngangsparametre fra .ini-fil"""

    def __init__(self, ini):
        cfg = configparser.ConfigParser()
        cfg.read("input.ini")

        # Oppretter variabler for data fra .ini-fil

        # Info
        self.banestrekning = cfg.getint("Info", "banestrekning")
        self.km = cfg.getfloat("Info", "km")
        self.prosjektnr = cfg.getint("Info", "prosjektnr")
        self.mastenr = cfg.getint("Info", "mastenr")
        self.signatur = cfg.get("Info", "signatur")
        self.dato = cfg.get("Info", "dato")
        self.kontroll = cfg.get("Info", "kontroll")
        self.kontrolldato = cfg.get("Info", "kontrolldato")

        # Mastealternativer
        self.siste_for_avspenning = cfg.getboolean("Mastealternativer", "siste_for_avspenning")
        self.linjemast_utliggere = cfg.getint("Mastealternativer", "linjemast_utliggere")
        self.avstand_fixpunkt = cfg.getint("Mastealternativer", "avstand_fixpunkt")
        self.fixpunktmast = cfg.getboolean("Mastealternativer", "fixpunktmast")
        self.fixavspenningsmast = cfg.getboolean("Mastealternativer", "fixavspenningsmast")
        self.avspenningsmast = cfg.getboolean("Mastealternativer", "avspenningsmast")
        self.strekkutligger = cfg.getboolean("Mastealternativer", "strekkutligger")
        self.master_bytter_side = cfg.getboolean("Mastealternativer", "master_bytter_side")
        self.avspenningsbardun = cfg.getboolean("Mastealternativer", "avspenningsbardun")

        # Fastavspente ledninger
        self.matefjern_ledn = cfg.getboolean("Fastavspent", "matefjern_ledn")
        self.matefjern_antall = cfg.getint("Fastavspent", "matefjern_antall")
        self.at_ledn = cfg.getboolean("Fastavspent", "at_ledn")
        self.at_type = cfg.getint("Fastavspent", "at_type")
        self.forbigang_ledn = cfg.getboolean("Fastavspent", "forbigang_ledn")
        self.jord_ledn = cfg.getboolean("Fastavspent", "jord_ledn")
        self.jord_type = cfg.getint("Fastavspent", "jord_type")
        self.fiberoptisk_ledn = cfg.getboolean("Fastavspent", "fiberoptisk_ledn")
        self.retur_ledn = cfg.getboolean("Fastavspent", "retur_ledn")
        self.differansestrekk = cfg.getfloat("Fastavspent", "differansestrekk")

        # System
        self.systemnavn = cfg.get("System", "systemnavn")
        self.radius = cfg.getint("System", "radius")
        self.hogfjellsgrense = cfg.getboolean("System", "hogfjellsgrense")
        self.masteavstand = cfg.getfloat("System", "masteavstand")
        self.vindkasthastighetstrykk = cfg.getfloat("System", "vindkasthastighetstrykk")

        # Geometri
        self.h = cfg.getfloat("Geometri", "h")
        self.hfj = cfg.getfloat("Geometri", "hfj")
        self.hf = cfg.getfloat("Geometri", "hf")
        self.hj = cfg.getfloat("Geometri", "hj")
        self.hr = cfg.getfloat("Geometri", "hr")
        self.fh = cfg.getfloat("Geometri", "fh")
        self.sh = cfg.getfloat("Geometri", "sh")
        self.e = cfg.getfloat("Geometri", "e")
        self.sms = cfg.getfloat("Geometri", "sms")

        # Diverse
        self.s235 = cfg.getboolean("Div", "s235")
        self.materialkoeff = cfg.getfloat("Div", "materialkoeff")
        self.traverslengde = cfg.getfloat("Div", "traverslengde")
        self.ec3 = cfg.getboolean("Div", "ec3")

