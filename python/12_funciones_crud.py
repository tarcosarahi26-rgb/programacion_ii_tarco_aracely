flota = [
    {"N1-001": {
        "nombre": "Caza N-1",
        "combustible": 80
        }
    },
    
    {
        "N1-002": {
            "nombre": "Nave Real",
            "combustible": 35
        }
    }

]


def create_nave(nave):
    flota.append(nave)


def update_nave(nave_update, index):
    flota[index].update(nave_update)      

def read_nave(index):
    return flota[index]

def delete_nave(index):
    return flota.pop(index)

print(flota)

new_nave = {
        "N1-003": {
        "nombre": "Nave Real 2",
        "combustible": 80
            }
}  
create_nave(new_nave)  
print(flota)
nave_update = {
        "N1-003": {
        "nombre": "Nave Real NR6",
        "combustible": 85
        }    
    }

update_nave(nave_update, 2)
print(flota)
print(read_nave(2))
print(delete_nave(2))
print(flota)