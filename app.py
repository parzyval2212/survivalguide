import streamlit as st

st.set_page_config(
    page_title="Survival Guide",
    layout="centered"
)

st.title("Survival Guide: El Reto Móvil")
st.write("Bienvenido estudiante. Tu misión es sobrevivir a Programación Móvil.")


# Variables de estado

if "fase" not in st.session_state:
    st.session_state.fase = 1

if "reglas_aprobado" not in st.session_state:
    st.session_state.reglas_aprobado = False

if "notas_aprobado" not in st.session_state:
    st.session_state.notas_aprobado = False

if "skills_aprobado" not in st.session_state:
    st.session_state.skills_aprobado = False

if "timeline_aprobado" not in st.session_state:
    st.session_state.timeline_aprobado = False


# Seccion 1 - Reglas

if st.session_state.fase == 1:

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

    if st.button("Ya leí las reglas"):
        st.session_state.fase = 2
        st.rerun()


# Quiz reglas

elif st.session_state.fase == 2:

    st.header("Mini reto")

    with st.form("quiz_reglas"):

        p1 = st.radio(
            "¿Qué porcentaje mínimo de asistencia se requiere?",
            ["50%", "70%", "80%"]
        )

        p2 = st.radio(
            "¿Dónde deben subirse las tareas?",
            ["WhatsApp", "Google Classroom", "Facebook"]
        )

        enviar1 = st.form_submit_button("Responder")

    if enviar1:

        correctas = 0

        if p1 == "80%":
            correctas += 1

        if p2 == "Google Classroom":
            correctas += 1

        if correctas == 2:

            st.success("Cámara de las Reglas desbloqueada")
            st.session_state.reglas_aprobado = True
            st.session_state.fase = 3
            st.rerun()

        else:

            st.error("Respuestas incorrectas. Debes volver a leer.")
            st.session_state.fase = 1
            st.rerun()


# Seccion 2 - Notas

elif st.session_state.fase == 3:

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

    if st.button("Ya entendí el sistema de evaluación"):
        st.session_state.fase = 4
        st.rerun()


# Quiz notas

elif st.session_state.fase == 4:

    st.header("Mini reto")

    with st.form("quiz_notas"):

        p3 = st.radio(
            "¿Qué porcentaje vale el proyecto integrador en el 3er parcial?",
            ["10%", "30%", "50%"]
        )

        p4 = st.radio(
            "¿Cuánto vale la evidencia de conocimiento en el 1er parcial?",
            ["20%", "40%", "50%"]
        )

        enviar2 = st.form_submit_button("Responder")

    if enviar2:

        correctas2 = 0

        if p3 == "50%":
            correctas2 += 1

        if p4 == "40%":
            correctas2 += 1

        if correctas2 == 2:

            st.success("Oráculo desbloqueado")
            st.session_state.notas_aprobado = True
            st.session_state.fase = 5
            st.rerun()

        else:

            st.error("Respuestas incorrectas. Debes volver a estudiar.")
            st.session_state.fase = 3
            st.rerun()


# Seccion 3 - Skills

elif st.session_state.fase == 5:

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

    if st.button("Continuar"):
        st.session_state.fase = 6
        st.rerun()


# Quiz skills

elif st.session_state.fase == 6:

    st.header("Mini reto")

    with st.form("quiz_skills"):

        p5 = st.radio(
            "¿Qué desarrollará el estudiante?",
            ["Páginas web", "Aplicaciones móviles", "Videojuegos retro"]
        )

        p6 = st.radio(
            "¿Qué se utilizará para crear las aplicaciones?",
            ["Herramientas de programación móvil", "Motores industriales", "Robótica"]
        )

        enviar3 = st.form_submit_button("Responder")

    if enviar3:

        correctas3 = 0

        if p5 == "Aplicaciones móviles":
            correctas3 += 1

        if p6 == "Herramientas de programación móvil":
            correctas3 += 1

        if correctas3 == 2:

            st.success("Skills desbloqueadas")
            st.session_state.skills_aprobado = True
            st.session_state.fase = 7
            st.rerun()

        else:

            st.error("Fallaste el reto. Intenta nuevamente.")
            st.session_state.fase = 5
            st.rerun()


# Seccion 4 - Timeline

elif st.session_state.fase == 7:

    st.header("La Línea del Tiempo")

    st.write("""
    ### Fechas importantes

    - 1er Parcial: 01-06-26
    - 2do Parcial: 06-07-26
    - 3er Parcial: 10-08-26
    - Final: 17-08-26
    """)

    if st.button("Memorizar fechas"):
        st.session_state.fase = 8
        st.rerun()


# Quiz timeline

elif st.session_state.fase == 8:

    st.header("Mini reto")

    with st.form("quiz_timeline"):

        p7 = st.radio(
            "¿Cuándo es el examen final?",
            ["17-08-26", "01-06-26", "25-12-26"]
        )

        p8 = st.radio(
            "¿Cuál es la fecha del segundo parcial?",
            ["10-08-26", "06-07-26", "17-08-26"]
        )

        enviar4 = st.form_submit_button("Responder")

    if enviar4:

        correctas4 = 0

        if p7 == "17-08-26":
            correctas4 += 1

        if p8 == "06-07-26":
            correctas4 += 1

        if correctas4 == 2:

            st.success("FELICIDADES, HAS COMPLETADO EL SURVIVAL GUIDE")
            st.balloons()
            st.session_state.timeline_aprobado = True

        else:

            st.error("Respuestas incorrectas. Vuelve a revisar las fechas.")
            st.session_state.fase = 7
            st.rerun()