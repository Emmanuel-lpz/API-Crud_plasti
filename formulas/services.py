import csv
import os

from formulas.models  import Formula


class ServicioClient:

	def __init__(self, table_name):
		self.table_name = table_name

	def crear_formula(self, formula):
		with open(self.table_name, mode='a') as f:
			writer = csv.DictWriter(f, fieldnames=Formula.schema())
			writer.writerow(formula.to_dict())

	def lista_formulas(self):
		with open(self.table_name, mode='r') as f:
			reader = csv.DictReader(f, fieldnames=Formula.schema())

			return list(reader)

	def actualizar_formulas(self, actualiza_formula):
		formulas = self.lista_formulas()

		actualiza_formulas = []
		for formula in formulas:
			if formula['uid'] == actualiza_formula.uid:
				actualiza_formulas.append(actualiza_formula.to_dict())
			else:
				actualiza_formulas.append(formula)

		self._save_to_disk(actualiza_formulas)

	def elimina_formula(self, formula_uid):
		formulas = self.lista_formulas()
		actualiza_formulas = [formula for formula in formulas if formula['uid'] != formula_uid]

		self._save_to_disk(actualiza_formulas)

	def _save_to_disk(self, formulas):
		tmp_table_name = self.table_name + '.tmp'
		with open(tmp_table_name, mode='w') as f:
			writer = csv.DictWriter(f, fieldnames=Formula.schema())
			writer.writerows(formulas)

		os.remove(self.table_name)
		os.rename(tmp_table_name, self.table_name)

		