# Implementing two of the pillars of OOP: Encapsulation and Polymorphism

class Eevee:
    def __init__(self, name = "Eevee"):
        self._name = name
        self._evolution_type = "Normal Type Pokemon"
        
    def move(self):
        return "Normal Attack"


class Vaporeon(Eevee):
    def __init__(self, name = "Vaporeon"):
        super().__init__(name)
        self._evolution_type = "Water Type Pokemon"
        
    def move(self):
        return "Hydro Pump"


class Jolteon(Eevee):
    def __init__(self, name = "Jolteon"):
        super().__init__(name)
        self._evolution_type = "Electric Type Pokemon"
        
    def move(self):
        return "Volt Switch"
    

class Flareon(Eevee):
    def __init__(self, name = "Flareon"):
        super().__init__(name)
        self._evolution_type = "Fire Type Pokemon"
        
    def move(self):
        return "Flare Blitz"
    

class Espeon(Eevee):
    def __init__(self, name = "Espeon"):
        super().__init__(name)
        self._evolution_type = "Psychic Type Pokemon"
        
    def move(self):
        return "Future Sight"
    

class Umbreon(Eevee):
    def __init__(self, name = "Umbreon"):
        super().__init__(name)
        self._evolution_type = "Dark Type Pokemon"
    
    def move(self):
        return "Dark Pulse"
    

class Leafeon(Eevee):
    def __init__(self, name = "Leafeon"):
        super().__init__(name)
        self._evolution_type = "Grass Type Pokemon"
        
    def move(self):
        return "Leaf Blade"
    

class Glaceon(Eevee):
    def __init__(self, name = "Glaceon"):
        super().__init__(name)
        self._evolution_type = "Ice Type Pokemon"
        
    def move(self):
        return "Ice Beam"
    

class Sylveon(Eevee):
    def __init__(self, name = "Sylveon"):
        super().__init__(name)
        self._evolution_type = "Fairy Type Pokemon"
        
    def move(self):
        return "Dazzling Gleam"
    

def eevee_evolution():
    evolution_path = [Eevee(), Vaporeon(), Jolteon(), Flareon(), Espeon(), Umbreon(), Leafeon(), Glaceon(), Sylveon()]
    
    for evolution in evolution_path:
        print(f"{evolution._name} is a {evolution._evolution_type} and it uses {evolution.move()}.")

eevee_evolution()