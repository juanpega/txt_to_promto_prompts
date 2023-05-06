from cx_Freeze import setup, Executable

# Configuración de las dependencias
build_exe_options = {
    "packages": ["os", "openai", "requests", "json", "shutil"],
    "excludes": []
}

# Configuración del ejecutable
exe = Executable(
    script="txt_to_prompto_prompts.py",  # Reemplace esto con el nombre de su script
    base=None,
    target_name="txt_to_promto_files",  # Cambie esto al nombre que desee para el archivo ejecutable
)

setup(
    name="txt_to_promto_files",
    version="1.0",
    description="Descripción de su aplicación",
    options={"build_exe": build_exe_options},
    executables=[exe]
)