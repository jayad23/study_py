'''
  El método set() convierte elementos como tuplas y strings a conjuntos/sets.
  Tenemos otros métodos:
  add()
  update() // la diferencia entre el método app y el update, es que el método update permite agrega
  varios elementos al conjunto. Su sintaxis es en forma de otro conjunto. El método add solo permite 
  agregar un único elemento.
  remove()
  discard() // la diferencia entre remove y discard es que remove arroja un error que
  rompe la ejecución, mientras que discard permite el manejo de error.
  clear()

'''
set_countries = {
  'Col', 'Mex', 'Bol'
}
set_numbers = { 1, 2, 3 }
set_name = set("jaider");
data = [];
'''
  Detectar valores repetidos.
'''
'''
numbers = [1,2,3,3, 3, 4, 4, 5, 2, 5, 9, 10, 23]
removed = set(numbers)
unique = list(removed);
set_countries.add('Spa')
set_countries.update({'Eng', 'Fra', 'Ger'})
'''

#UNION
#Unir dos conjuntos.
countries_a = {'Col', 'Per', 'Arg'}
countries_b = {'Per', 'Bol'}
animals_a = {'Perro', 'Gato', 'Hamster'}
animals_b = {'Vaca', 'Gallina', 'Cerdo'}
#option a: Método .union()
countries = countries_a.union(countries_b);
#print(countries)
#option b: Operador |
animals = animals_a | animals_b
#print(animals)
'''
  Diferencia:
  Método: .diference()
  Operador: -

  Intersección:
  Método: .intersection()
  Operador: &

  Diferencia simétrica:
  Método: .symetric_difference()
  operador: ^

  No está muy claro la diferencia entre una unión simple y una diferencia simétrica.
'''

#LISTAS / Comprehensions
numbers = [];
for number in range(1, 11):
  numbers.append(number / 2);

#print(numbers);

numbers_2 = [element for element in range(1, 20)];
#print(numbers_2)

even_numbers = [element for element in range(1, 21) if element % 2 == 0];
#print(even_numbers);
dictionary = {}
for i in range(1, 11):
  dictionary[i] = i * i;

print(dictionary);
import random;
dictionary_2 = { i : i * i for i in range(1, 6)}
print(dictionary_2);

con = ["Col", "Mex", "Per", "Bol"];
pop = {};

for c in con:
  pop[c] = random.randint(1, 100);

print(pop);

pop_2 = { c: random.randint(1000, 5000) for c in con };
print(pop_2)

names = ["Max", "Antonia", "Kike", "Laura", "Mine"];
ages = [8, 5, 36, 29]
#la función zip() crea una unión entre listas en forma de tuplas.
union_info = list(zip(names, ages));
names_ages = { name: age for (name, age) in zip(names, ages) };
print(names_ages);

print(int(43 / 7));