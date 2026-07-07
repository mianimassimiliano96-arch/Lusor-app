from dataclasses import dataclass, field
from typing import List


@dataclass
class Apparecchio:
    tipologia: str = ""
    potenza: str = ""
    installazione: str = ""
    altezza_installazione: str = ""
    accensione: str = ""
    quantita: int = 1

    def to_dict(self):
        return {
            "tipologia": self.tipologia,
            "potenza": self.potenza,
            "installazione": self.installazione,
            "altezza_installazione": self.altezza_installazione,
            "accensione": self.accensione,
            "quantita": self.quantita,
        }

    @staticmethod
    def from_dict(d):
        return Apparecchio(
            tipologia=d.get("tipologia", ""),
            potenza=d.get("potenza", ""),
            installazione=d.get("installazione", ""),
            altezza_installazione=d.get("altezza_installazione", ""),
            accensione=d.get("accensione", ""),
            quantita=d.get("quantita", 1),
        )


@dataclass
class Stanza:
    id_locale: str = ""
    piano: str = ""
    altezza: str = ""
    destinazione: str = ""
    controsoffitto: str = ""
    apparecchi: List[Apparecchio] = field(default_factory=list)
    foto_paths: List[str] = field(default_factory=list)

    def to_dict(self):
        return {
            "id_locale": self.id_locale,
            "piano": self.piano,
            "altezza": self.altezza,
            "destinazione": self.destinazione,
            "controsoffitto": self.controsoffitto,
            "foto_paths": self.foto_paths,
            "apparecchi": [a.to_dict() for a in self.apparecchi],
        }

    @staticmethod
    def from_dict(d):
        foto_paths = d.get("foto_paths", [])
        if not foto_paths and d.get("foto_path"):
            foto_paths = [d["foto_path"]]
        return Stanza(
            id_locale=d.get("id_locale", ""),
            piano=d.get("piano", ""),
            altezza=d.get("altezza", ""),
            destinazione=d.get("destinazione", ""),
            controsoffitto=d.get("controsoffitto", ""),
            foto_paths=foto_paths,
            apparecchi=[Apparecchio.from_dict(a) for a in d.get("apparecchi", [])],
        )


@dataclass
class Edificio:
    nome: str = ""
    indirizzo: str = ""
    data_rilievo: str = ""
    stanze: List[Stanza] = field(default_factory=list)

    def to_dict(self):
        return {
            "edificio": {"nome": self.nome, "indirizzo": self.indirizzo, "data_rilievo": self.data_rilievo},
            "stanze": [s.to_dict() for s in self.stanze],
        }

    @staticmethod
    def from_dict(d):
        ed = d.get("edificio", {})
        e = Edificio(nome=ed.get("nome", ""), indirizzo=ed.get("indirizzo", ""), data_rilievo=ed.get("data_rilievo", ""))
        e.stanze = [Stanza.from_dict(s) for s in d.get("stanze", [])]
        return e
