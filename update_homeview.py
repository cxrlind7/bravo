import os

file_path = r'c:\Users\CarlosOmarAldabaEstr\Documents\proy\Bravo\bravo\src\views\HomeView.vue'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

def to_lines(s):
    # splitlines() splits by \n, \r, \r\n etc and discards them. We add \n back.
    return [line + '\n' for line in s.splitlines()]

# New Mobile CSS content
new_mobile_css = """    /* Ajustes del contenedor en móvil */
    .services-snap-container {
        gap: 1rem; /* Menos espacio entre tarjetas */
        padding: 1rem 0.5rem;
        /* En móvil, queremos que el scroll empiece desde el borde izquierdo */
        justify-content: flex-start; 
    }

    /* Ajustes de la tarjeta en móvil */
    .service-card {
        /* Hacemos que el ancho sea relativo a la pantalla del móvil */
        width: 85vw; 
        max-width: 320px; /* Pero que no se pase de cierto tamaño */
        padding: 2rem 1.5rem;
    }

    .service-icon {
        width: 70px;
        height: 70px;
        font-size: 1.5rem;
        margin-bottom: 1.5rem;
        background: #6a6a6a;
        /* Color simple */
    }

    .service-card h3 {
        font-size: 1.3rem;
        margin-bottom: 1rem;
        color: #1a1a1a;
    }

    .service-card p {
        font-size: 0.95rem;
        color: #4a4a4a;
    }"""

# New CSS content
new_css = """/* Contenedor con CSS Scroll Snap */
.services-snap-container {
    display: flex; /* Cambiado de grid a flex para el carrusel */
    gap: 2rem;     /* Espacio entre tarjetas */
    overflow-x: auto; /* Habilita el scroll horizontal */
    scroll-snap-type: x mandatory; /* Fuerza que el scroll se detenga en los puntos de anclaje */
    padding: 2rem 1rem; /* Padding para que se vean las sombras */
    max-width: 1200px;
    margin: 0 auto;
    
    /* Ocultar la barra de scroll de forma moderna y limpia */
    scrollbar-width: none; /* Firefox */
    -ms-overflow-style: none; /* IE/Edge */
}
.services-snap-container::-webkit-scrollbar {
    display: none; /* Chrome/Safari/Opera */
}

.service-card {
    /* Configuración para que funcione dentro del flex container */
    flex: 0 0 auto; /* No crecer, no encoger, tamaño base automático */
    width: 350px;   /* Ancho fijo base para escritorio */
    
    /* Punto de anclaje para el scroll snap */
    scroll-snap-align: center; /* La tarjeta se centrará al soltar el scroll */

    /* ... el resto de tus estilos de tarjeta se mantienen igual ... */
    background: linear-gradient(145deg, #e8e8e8 0%, #d4d4d4 100%);
    border-radius: 20px;
    padding: 2.5rem 2rem;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(0, 0, 0, 0.1);
}"""

# New Script content
new_script = """    data() {
        return {
            isExpanded: false,
            // Se eliminaron todas las variables relacionadas con el arrastre manual y la pausa
            // isServicesPaused, isDragging, startX, scrollLeft, dragOffset, isDesktop
            baseServices: [
                {
                    icon: 'fa-users',
                    title: 'Derecho Familiar',
                    description: 'Asesoramiento en pensiones alimenticias, divorcios y juicios sucesorios.'
                },
                {
                    icon: 'fa-briefcase',
                    title: 'Derecho Empresarial',
                    description: 'Dotamos a tu empresa de las mejores herramientas: contratos, reglamentos, protección de marca, etc.'
                },
                {
                    icon: 'fa-gavel',
                    title: 'Derecho Penal',
                    description: 'Representación legal ante problemas graves que impliquen detenciones o delitos que se atienden en las Fiscalías.'
                }
            ],
        };
    },
    // Se eliminó la computed property 'services' que duplicaba el array.
    // Se eliminaron los métodos 'dragStart', 'dragMove', 'dragEnd'.
};"""

# Apply changes in reverse order to preserve indices

# 1. Remove 1184-1187 (Indices 1183-1187)
# Check if indices are valid
if len(lines) >= 1187:
    lines[1183:1187] = []
else:
    print("Warning: File shorter than expected for step 1")

# 2. Replace 947-1018 (Indices 946-1018)
if len(lines) >= 1018:
    lines[946:1018] = to_lines(new_mobile_css)
else:
    print("Warning: File shorter than expected for step 2")

# 3. Replace 443-462 (Indices 442-462)
if len(lines) >= 462:
    lines[442:462] = to_lines(new_css)
else:
    print("Warning: File shorter than expected for step 3")

# 4. Replace 136-202 (Indices 135-202)
if len(lines) >= 202:
    lines[135:202] = to_lines(new_script)
else:
    print("Warning: File shorter than expected for step 4")

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Successfully updated HomeView.vue")
