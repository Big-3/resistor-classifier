# resistor-classifier
Xarxa Neuronal per classificar i reconnexier resistències a partir del seu propi codi de colors.

## Setup

Abans d'iniciar res, necessitem instal·lar el packet manager `pip`:

```
conda install pip
```

Després, instal·lem els requeriments amb la comanda:
```
pip install -r requeriments.txt
```

Finalment, fem el setup per a que python pugui saber quins paquets estem modificant:
```
python setup.py
```

## Testing

Fem servir la llibreria [unittest](https://docs.python.org/3/library/unittest.html). Per crear els tests:
```
#imports necessaris

class NomDelTestGlobal(unittest.TestCase):
	def nom_del_test_local(self):
		# codi que necessitis probar
		self.assertEqual(valor_que_esperem, quelcom_que_volguem_validar)

	## PODEM POSAR TANTS TESTS COM VOLGUEM
	def nom_del_test_local2(self):
		#yadayadayada
		self.assertEqual('test', 'test')

if __name__=='__main__':
	unittest.main()
```

Podem corre només un test en especific:
```
python test.py
```
O podem corre tots els tests:
```
./runall.sh
```

Si no va el `./runall` fes la següent comanda:
```
`chmod +x runall.sh
```
