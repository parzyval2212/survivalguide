import streamlit as st

st.set_page_config(
    page_title="Survival Guide",
    layout="centered"
)

st.title("📱 Survival Guide: El Reto Móvil")
st.write("Bienvenido estudiante. Tu misión es sobrevivir a Programación Móvil.")



if "reglas" not in st.session_state:
    st.session_state.reglas = False

if "notas" not in st.session_state:
    st.session_state.notas = False

if "skills" not in st.session_state:
    st.session_state.skills = False

if "timeline" not in st.session_state:
    st.session_state.timeline = False


st.header("La Cámara de las Reglas")

st.write("""
1. Se requiere 80% de asistencia y 80% de trabajos para evaluación parcial.

2. Hay 10 minutos de tolerancia únicamente en horarios de inicio.

3. Las faltas deben justificarse mediante correo institucional.

4. Las tareas deben subirse a Google Classroom.

5. No se aceptan trabajos fuera de tiempo sin justificante.

6. El plagio o copia puede causar reprobación.

7. Cualquier deshonestidad académica será sancionada.

8. El uso de dispositivos móviles será únicamente académico.

9. Prohibido usar audífonos durante la clase.

10. Prohibido comer o tomar líquidos en el salón.
""")

st.subheader("Mini reto")

p1 = st.radio(
    "¿Qué porcentaje mínimo de asistencia se requiere?",
    ["50%", "70%", "80%"],
    key="p1"
)

p2 = st.radio(
    "¿Dónde deben subirse las tareas?",
    ["WhatsApp", "Google Classroom", "Facebook"],
    key="p2"
)

correctas = 0

if p1 == "80%":
    correctas += 1

if p2 == "Google Classroom":
    correctas += 1

if correctas >= 2:

    compromiso1 = st.checkbox("Acepto respetar el reglamento")

    if compromiso1:
        st.success("Cámara de las Reglas desbloqueada")
        st.session_state.reglas = True


if st.session_state.reglas:

    st.header("El Oráculo de las Notas")

    st.write("""
    ### Primer Parcial
    - Evidencia de conocimiento: 40%
    - Evidencia de desempeño: 20%
    - Evidencia de producto: 30%
    - Proyecto integrador: 10%

    ### Segundo Parcial
    - Evidencia de conocimiento: 40%
    - Evidencia de desempeño: 20%
    - Evidencia de producto: 30%
    - Proyecto integrador: 10%

    ### Tercer Parcial
    - Evidencia de conocimiento: 10%
    - Evidencia de desempeño: 10%
    - Evidencia de producto: 30%
    - Proyecto integrador: 50%
    """)

    st.subheader("Mini reto")

    p3 = st.radio(
        "¿Qué porcentaje vale el proyecto integrador en el 3er parcial?",
        ["10%", "30%", "50%"],
        key="p3"
    )

    p4 = st.radio(
        "¿Cuánto vale la evidencia de conocimiento en el 1er parcial?",
        ["20%", "40%", "50%"],
        key="p4"
    )

    correctas2 = 0

    if p3 == "50%":
        correctas2 += 1

    if p4 == "40%":
        correctas2 += 1

    if correctas2 >= 2:

        compromiso2 = st.checkbox("Acepto el sistema de evaluación")

        if compromiso2:
            st.success("Oráculo desbloqueado")
            st.session_state.notas = True



if st.session_state.notas:

    st.header("Skills a Desbloquear")

    st.write("""
    Objetivo de la materia:

    Desarrollará aplicaciones móviles mediante:

    - Lenguajes de programación
    - Entornos de desarrollo
    - Diseño de interfaces
    - Arquitecturas
    - Patrones de diseño
    - Herramientas de programación móvil
    """)

    st.subheader(" Mini reto")

    p5 = st.radio(
        "¿Qué desarrollará el estudiante?",
        ["Páginas web", "Aplicaciones móviles", "Videojuegos retro"],
        key="p5"
    )

    p6 = st.radio(
        "¿Qué se utilizará para crear las aplicaciones?",
        ["Herramientas de programación móvil", "Motores industriales", "Robótica"],
        key="p6"
    )

    correctas3 = 0

    if p5 == "Aplicaciones móviles":
        correctas3 += 1

    if p6 == "Herramientas de programación móvil":
        correctas3 += 1

    if correctas3 >= 2:

        compromiso3 = st.checkbox("Acepto desbloquear mis skills")

        if compromiso3:
            st.success("Skills desbloqueadas")
            st.session_state.skills = True


if st.session_state.skills:

    st.header("La Línea del Tiempo")

    st.write("""
    ### Fechas importantes

    - 1er Parcial: 01-06-26
    - 2do Parcial: 06-07-26
    - 3er Parcial: 10-08-26
    - Final: 17-08-26
    """)

    st.subheader("Mini reto")

    p7 = st.radio(
        "¿Cuándo es el examen final?",
        ["17-08-26", "01-06-26", "25-12-26"],
        key="p7"
    )

    p8 = st.radio(
        "¿Cuál es la fecha del segundo parcial?",
        ["10-08-26", "06-07-26", "17-08-26"],
        key="p8"
    )

    correctas4 = 0

    if p7 == "17-08-26":
        correctas4 += 1

    if p8 == "06-07-26":
        correctas4 += 1

    if correctas4 >= 2:

        compromiso4 = st.checkbox("Acepto sobrevivir el semestre")

        if compromiso4:
            st.success("FELICIDADES, HAS COMPLETADO EL SURVIVAL GUIDE")
            st.balloons()