from random import choice

data = [
        {"correct": "гн&#1123;здо", "false": "гнездо"},
        {"correct": "гн&#1123;та", "false": "гнета"},
        {"correct": "грести", "false": "гр&#1123;сти"},
        {"correct": "гречиха", "false": "гр&#1123;чиха"},
        {"correct": "кл&#1123;тка", "false": "клетка"},
        {"correct": "клешня", "false": "кл&#1123;шня"},
        {"correct": "кр&#1123;пкий", "false": "крепкий"},
        {"correct": "обр&#1123;зать", "false": "обрезать"},
        {"correct": "обремененiе", "false": "обр&#1123;мененiе"},
        {"correct": "щепка", "false": "щ&#1123;пка"},
        {"correct": "т&#1123;сто", "false": "тесто"}
    ]

def generate_q():
    return choice(data)
