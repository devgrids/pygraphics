from pygraphics.core.object import Object

class Object3D(Object):
    def load_data_from_file(self, file):
        # Aquí deberías implementar la lógica de carga específica para Object3D
        # Por ejemplo, cargar los datos del archivo y procesarlos
        # La siguiente línea es solo un placeholder
        super().load_data_from_file(file)

    def compute_model_matrix(self):
        mat = self.mesh.get_material() if self.mesh else None
        if not mat:
            return
        mat.get_program().use()
        mat.get_program().set_matrix("mMat", self.model)
