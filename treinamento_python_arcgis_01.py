# Importação da biblioteca
import arcpy

# Variaveis com o diretório dos arquivos
affected_area_app = 'C:\\Dados\\CursoArcgisPython\\Treinamento_Arcgis\\EsriTraining\\PYTS\\Data\\AffectedAreaApp.shp'
affected_area_copy = 'C:\\Dados\\CursoArcgisPython\\Treinamento_Arcgis\\EsriTraining\\PYTS\\Default.gdb\\affected_area_copy'

# Substitui arquivo antigo pelo novo após cada execução
arcpy.env.overwriteOutput = True

# Copiar o arquivo para o Geodatabase
arcpy.management.CopyFeatures(affected_area_app, affected_area_copy, '', None, None, None)

# Variáveis obrigatórias KernelDensity
in_features = "C:\\Dados\\CursoArcgisPython\\Treinamento_Arcgis\\EsriTraining\\PYTS\\Default.gdb\\affected_area_copy"
population_field = "NONE"

# Executar KernelDensity e salvar um arquivo raster
out_dens = arcpy.sa.KernelDensity(in_features, population_field)
out_dens.save(r"C:\Dados\CursoArcgisPython\Treinamento_Arcgis\EsriTraining\PYTS\Default.gdb\out_raster_density")