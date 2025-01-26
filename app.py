import streamlit as st
from polymer_builder import load_monomer, construct_polymer, save_polymer

# Título de la app
st.title("Constructor de Polímeros")
st.write("Genera cadenas poliméricas en formato XYZ a partir de un monómero.")

# Entrada: archivo monómero
uploaded_file = st.file_uploader("Carga tu archivo de monómero (formato .xyz)", type=["xyz"])

# Entrada: número de repeticiones
n_units = st.number_input("Número de unidades en la cadena polimérica", min_value=1, max_value=100, value=10, step=1)

if uploaded_file:
    # Leer contenido del archivo subido
    content = uploaded_file.read().decode("utf-8")
    atom_count, structure = load_monomer(content)
    st.success(f"Monómero cargado correctamente con {atom_count} átomos.")

    # Botón para construir el polímero
    if st.button("Construir polímero"):
        polymer = construct_polymer(atom_count, structure, n_units)
        polymer_output = save_polymer(polymer)

        # Mostrar el resultado
        st.download_button(
            label="Descargar cadena polimérica",
            data=polymer_output,
            file_name="polymer_chain.xyz",
            mime="text/plain"
        )
        st.text_area("Vista previa del polímero generado:", value=polymer_output, height=300)
