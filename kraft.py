from numpy import array, zeros, count_nonzero, double

class Kraft(object):
    """Generell klasse for konsentrerte/fordelte laster og momenter"""

    def __init__(self, navn="", type=(0, 0), f=[0,0,0],
                 q=[0,0,0], b=0, e=[0,0,0]):
        """
        Initierer kraft/moment-objekt.
        :param navn: Identifikasjonstag for kraftens opphav
        :param type: (Rad, etasje) for plassering i R-matrise
        :param f: Kraftkomponenter [x, y, z]  [N]
        :param q: Kraftkomponenter for fordelt last [x, y, z]  [N/m]
        :param b: Utstrekning av fordelt last [m]
        :param e: Eksentrisitet fra origo [x, y, z]  [m]
        """

        self.navn = navn
        self.type = type
        self.f = array(f)
        self.q = array(q)
        self.b = b
        self.e = array(e)


    def __repr__(self):
        return self.rep()

    def rep(self):
        rep = "{}   type={}\n".format(self.navn, self.type)
        if not count_nonzero(self.q) == 0:
            rep += "q*b = {}\n".format(self.q * self.b)
        else:
            rep += "f = {}\n".format(self.f)
        rep += "e = {}\n".format(self.e)
        return rep

    def snu_lastretning(self):
        self.f = -self.f
        self.q = -self.q

    def nullstill(self):
        self.f = zeros(3,dtype=double)
        self.q = zeros(3,dtype=double)






