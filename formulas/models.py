import uuid



class Formula:

	def __init__(self, nombre, mat1, mat2, mat3, mat4, uid=None):
		self.nombre = nombre
		self.mat1 = mat1
		self.mat2 = mat2
		self.mat3 = mat3
		self.mat4 = mat4
		self.uid = uid or uuid.uuid4()

	def to_dict(self):
		return vars(self)

	@staticmethod
	def schema():
		return ['nombre', 'mat1', 'mat2', 'mat3', 'mat4', 'uid']


