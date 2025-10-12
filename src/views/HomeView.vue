<template>

    <NavBar :isHomePage="true" />
    <div class="content">
        <div id="inicio" class="section parallax-section">
            <div class="parallax-bg"></div>

            <div class="section-content">
                <img src="../../public/logobravo.png" alt="Bravo & Asociados" class="hero-logo" />
                <h3 class="hero-title">Servicios Jurídicos y Asesoría Especializada de Alta Calidad</h3>
                <p class="hero-subtitle">Compromiso de ética, responsabilidad y justicia en todo México</p>
                <!-- <button class="hero-button">Agenda una Consulta</button> -->
            </div>
        </div>
        <div id="map" class="">
            <div class="background-image"></div>
        </div>
        <!-- <section class="mision-vision-section normal-section"> -->
        <div id="about" class="mision-vision-section">
            <h2>NOSOTROS</h2>
            <p class="description" :class="{ expanded: isExpanded }">
                Bravo & Asociados es un despacho jurídico especializado en la prestación de servicios
                legales de alta calidad, con presencia en toda la República Mexicana. Bajo el liderazgo de Roberto Bravo
                Romo, ofrecemos asesoría integral en las áreas de Derecho Familiar, Empresarial y Penal, con un enfoque
                en la excelencia profesional y el compromiso ético. Nuestra firma se distingue por brindar soluciones
                jurídicas efectivas, fundamentadas en la responsabilidad, fidelidad y justicia, garantizando la
                confianza y certidumbre que nuestros clientes merecen en cada asunto que nos encomiendan.
            </p>
            <button class="read-more-btn" @click="isExpanded = !isExpanded">
                {{ isExpanded ? 'Leer menos' : 'Leer más' }}
            </button>
            <div class="container">
                <div class="mision-box">
                    <div class="icon"><i class="fa fa-bullseye"></i></div>
                    <h3>Misión</h3>
                    <p>Brindar servicios jurídicos y asesoría especializada de alta calidad profesional, con un
                        ineludible compromiso de ética, responsabilidad, fidelidad y justicia, que den certidumbre de
                        confianza a nuestros clientes.</p>
                </div>

                <div class="vision-box">
                    <div class="icon"><i class="fa fa-eye"></i></div>
                    <h3>Visión</h3>
                    <p>Que la firma sea líder en brindar servicios jurídicos y asesoría especializada de alta calidad, a
                        nivel nacional e internacional bajo los principios de confianza, honestidad, responsabilidad y
                        calidad. Con el apoyo de tecnologías que nos permitan establecer dicho liderazgo.</p>
                </div>
            </div>
        </div>
        <div id="services" class="normal-section">
            <h2>Nuestros Servicios</h2>
            <p class="services-subtitle">Ofrecemos asesoría legal integral en las siguientes áreas:</p>

            <div class="services-grid" ref="servicesGrid" :class="{ 'is-paused': isServicesPaused }"
                @touchstart.prevent="dragStart" @touchmove.prevent="dragMove" @touchend="dragEnd">

                <div v-for="(service, index) in services" :key="'clone-' + index" class="service-card"
                    aria-hidden="true">
                    <div class="service-icon">
                        <i class="fa" :class="service.icon" aria-hidden="true"></i>
                    </div>
                    <h3>{{ service.title }}</h3>
                    <p>{{ service.description }}</p>
                </div>

            </div>
        </div>

        <div class="specialized-areas">
            <div class="area-card">
                <img src="/public/empresa.jpg" alt="Derecho Corporativo">
                <div class="overlay">
                    <h2 class="title-specialized">DERECHO CORPORATIVO</h2>
                    <ul>
                        <li>Constitución de sociedades</li>
                        <li>Fusiones y adquisiciones</li>
                        <li>Contratos mercantiles</li>
                        <li>Propiedad intelectual</li>
                    </ul>
                </div>
                <img src="/public/grifo.png" alt="Icono interactivo" class="interactive-icon">

            </div>

            <div class="area-card">
                <img src="/public/individual.jpg" alt="Asesoría Personal">
                <div class="overlay">
                    <h2 class="title-specialized">ASESORÍA PERSONAL</h2>
                    <ul>
                        <li>Testamentos y herencias</li>
                        <li>Divorcios y pensiones</li>
                        <li>Contratos civiles</li>
                        <li>Defensa penal</li>
                    </ul>
                </div>
                <img src="/public/grifo.png" alt="Icono interactivo" class="interactive-icon">
            </div>

            <div class="area-card">
                <img src="/public/fiscal.jpg" alt="Derecho Fiscal">
                <div class="overlay">
                    <h2 class="title-specialized">DERECHO FISCAL</h2>
                    <ul>
                        <li>Auditorías del SAT</li>
                        <li>Planeación tributaria</li>
                        <li>Recursos de revocación</li>
                        <li>Declaraciones anuales</li>
                    </ul>
                </div>
                <img src="/public/grifo.png" alt="Icono interactivo" class="interactive-icon">

            </div>
        </div>




    </div>
    <Footer />
</template>

<script>
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
export default {
    name: "HomeView",
    components: {
        NavBar,
        Footer
    },
    data() {
        return {
            isExpanded: false,
            isServicesPaused: false,
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
            isDragging: false,      // ¿Está el usuario arrastrando?
            startX: 0,              // Posición X inicial del toque
            scrollLeft: 0,          // Posición de scroll inicial del contenedor
            dragOffset: 0,
            isDesktop: window.innerWidth > 1024,
        };
    },
    computed: {
        services() {
            // **AQUÍ ESTÁ LA MAGIA**
            // Si NO es escritorio (es móvil), multiplica el arreglo.
            if (!this.isDesktop) {
                // Repite el arreglo para el bucle infinito en móvil.
                return Array.from({ length: 10 }).flatMap(() => this.baseServices);
            }
            // Si SÍ es escritorio, simplemente devuelve el arreglo original de 3 tarjetas.
            return this.baseServices;
        }
    },
    methods: {
        dragStart(e) {
            this.isDragging = true;
            this.isServicesPaused = true; // Pausa la animación al empezar a arrastrar
            // Guarda la posición inicial del dedo y el scroll del contenedor
            this.startX = e.touches[0].pageX - this.$refs.servicesGrid.offsetLeft;
            this.scrollLeft = parseFloat(this.$refs.servicesGrid.style.getPropertyValue('--drag-offset')) || 0;
        },
        dragMove(e) {
            if (!this.isDragging) return;
            e.preventDefault(); // Evita el scroll de la página
            const x = e.touches[0].pageX - this.$refs.servicesGrid.offsetLeft;
            const walk = (x - this.startX) * 1.5; // El * 1.5 hace el arrastre más rápido

            // Calcula el nuevo offset y lo aplica a la variable CSS
            this.dragOffset = this.scrollLeft + walk;
            this.$refs.servicesGrid.style.setProperty('--drag-offset', this.dragOffset + 'px');
        },
        dragEnd() {
            this.isDragging = false;
            this.isServicesPaused = false; // Reanuda la animación al soltar

            // Aquí podrías añadir lógica para "ajustar" la tarjeta más cercana,
            // pero para mantener la animación simple, solo reanudamos.
        }
    }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');
@import url('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css');

.hero-logo{
    display: none;
}

/* Estilos para el ícono de interactividad (versión con imagen) */
.area-card img.interactive-icon {
    position: absolute;
    bottom: 15px;
    right: 15px;

    /* Anula cualquier otra regla con !important */
    width: 40px !important;
    height: 40px !important;

    z-index: 10;
    filter: brightness(0) invert(1) drop-shadow(0px 2px 4px rgba(0, 0, 0, 0.5));
    transition: opacity 0.3s ease;
    pointer-events: none;
}

/* La regla para ocultar al hacer hover sigue siendo la misma */
.area-card:hover .interactive-icon {
    opacity: 0;
}

/* Sección de Áreas Especializadas */
.title-specialized {
    color: #c9a961;
    font-weight: 700;
    padding-bottom: 2rem;
}

.specialized-areas {
    background: #c1c1c1;
    padding: 4rem 2rem;
    text-align: center;
}

.specialized-areas {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    /* 👈 2 columnas */
    gap: 2rem;
    max-width: 1400px;
    margin: 0 auto;
    padding: 4rem 2rem;
    background: #c1c1c1;
}

.area-card {
    position: relative;
    height: 450px;
    overflow: hidden;
    border-radius: 15px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    box-sizing: border-box;
}

/* El tercer card ocupa las 2 columnas y se centra */
.area-card:nth-child(3) {
    grid-column: 1 / -1;
    /* 👈 Ocupa ambas columnas */
    max-width: 600px;
    /* 👈 Limita el ancho */
    margin: 0 auto;
    /* 👈 Centra */
}

.area-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25);
}

.area-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.area-card:hover img {
    transform: scale(1.2);
    filter: blur(12px);
    /* <-- Añade esta línea */
}

/* Overlay */
.area-card .overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(transparent, rgba(0, 0, 0, 0.85));
    color: white;
    padding: 2.5rem 2rem 2rem;
    transform: translateY(100%);
    transition: transform 0.3s ease;
}

.area-card:hover .overlay {
    transform: translateY(0);
}

.area-card .overlay h2 {
    margin: 0 0 1rem 0;
    font-size: 1.8rem;
    color: #c9a961;
    font-weight: 700;
}

.area-card .overlay ul {
    list-style: none;
    padding: 0;
    margin: 0;
    text-align: left;
}

.area-card .overlay li {
    padding: 0.5rem 0;
    font-size: 1rem;
    opacity: 0.95;
    position: relative;
    padding-left: 1.5rem;
}

.area-card .overlay li:before {
    /* content: '✓'; */
    position: absolute;
    left: 0;
    color: #c9a961;
    font-weight: bold;
}


.description {
    text-align: center;
    line-height: 1.6;
    font-size: 1.2rem;
    /* mejora la legibilidad */
}

.mision-vision-section {
    text-align: center;
    background: #1a1a1a;
    padding: 4rem 2rem;
    color: white;
}

.mision-vision-section .container {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
}

.mision-box,
.vision-box {
    padding: 2rem;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 8px;
    border-left: 4px solid #c9a961;
}

.mision-box .icon,
.vision-box .icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.mision-box h3,
.vision-box h3 {
    color: #c9a961;
    font-size: 1.8rem;
    margin-bottom: 1rem;
}


#services {
    background: linear-gradient(135deg, #B8B8B8 0%, #9E9E9E 100%);
    padding: 10px 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
    padding-bottom: 5rem;
}

#services::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 70%);
    animation: rotate 20s linear infinite;
}

@keyframes rotate {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}

#services h2 {
    font-size: 2rem;
    color: #1a1a1a;
    margin-bottom: 15px;
    font-weight: 700;
    position: relative;
    z-index: 1;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.services-subtitle {
    color: #2a2a2a;
    font-size: 1.15rem;
    margin-bottom: 60px;
    max-width: 650px;
    margin-left: auto;
    margin-right: auto;
    position: relative;
    z-index: 1;
    font-weight: 400;
}

.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2.5rem;
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}

.service-card {
    background: linear-gradient(145deg, #e8e8e8 0%, #d4d4d4 100%);
    border-radius: 20px;
    padding: 2.5rem 2rem;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(0, 0, 0, 0.1);
}

.service-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
    transition: left 0.5s ease;
}

.service-card:hover::before {
    left: 100%;
}

.service-card:hover {
    transform: translateY(-15px) scale(1.02);
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.25);
}

.service-icon {
    width: 90px;
    height: 90px;
    background: linear-gradient(135deg, #6a6a6a 0%, #4a4a4a 100%);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 30px;
    color: #ffffff;
    font-size: 2rem;
    border: 3px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
    transition: all 0.4s ease;
    position: relative;
}

.service-icon::after {
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.1);
    transform: scale(0);
    transition: transform 0.4s ease;
}

.service-card:hover .service-icon {
    animation: spinOnce 0.6s ease-in-out;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.3);
}

@keyframes spinOnce {
    0% {
        transform: rotateY(0deg);
    }

    100% {
        transform: rotateY(360deg);
    }
}

.service-card:hover .service-icon::after {
    transform: scale(1.2);
    opacity: 0;
    transition: all 0.6s ease;
}

.service-card h3 {
    font-size: 1.6rem;
    color: #1a1a1a;
    margin-bottom: 18px;
    font-weight: 700;
    transition: color 0.3s ease;
}

.service-card:hover h3 {
    color: #3a3a3a;
}

.service-card p {
    color: #4a4a4a;
    line-height: 1.7;
    font-size: 1rem;
    transition: color 0.3s ease;
}

.service-card:hover p {
    color: #2a2a2a;
}

/* Imagen central  */

.top-right-corner {
    position: absolute;
    top: 20px;
    right: 20px;
    width: 50vw;
    z-index: 1;
    color: white;
    background-color: rgba(0, 0, 0, 0.5);
    padding: 10px 15px;
    border-radius: 8px;
}

.top-right-corner p {
    text-align: justify;
    line-height: 1.6;
    /* mejora la legibilidad */
    margin: 0;
}

#about {
    position: relative;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 10px 20px 60px 20px;
    /* top, right, bottom, left */
    overflow: hidden;
    /* mantiene la imagen dentro del contenedor */
}

#map {
    position: relative;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 10px 20px 60px 90px;
    /* top, right, bottom, left */
    overflow: hidden;
    /* mantiene la imagen dentro del contenedor */
}

.background-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('../../public/mapa.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    z-index: -1;
    /* coloca la imagen detrás del contenido */
}

#about h2 {
    font-size: 2rem;
    color: #afafaf;
    margin-bottom: 15px;
    font-weight: 700;
    position: relative;
    z-index: 1;
    text-transform: uppercase;
    letter-spacing: 2px;
}


.hero-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    /* Bold */
    letter-spacing: 0.5px;
    color: #252524;
    font-size: 1.8rem;
    margin-bottom: 1rem;
}

.hero-subtitle {
    font-size: 1.2rem;
    font-weight: 400;
    letter-spacing: 2px;
    text-transform: uppercase;
    opacity: 0.9;
    text-align: center;
    text-shadow: 0 2px 5px rgba(0, 0, 0, 0.5);
    position: relative; /* Necesario para el pseudo-elemento */
    padding-bottom: 2rem; /* Espacio para la línea */
}

/* Esta es la línea divisora */
.hero-subtitle::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%); /* Centra la línea */
    width: 100px; /* Ancho de la línea */
    height: 2px;  /* Grosor de la línea */
    background-color: rgba(255, 255, 255, 0.8); /* Color blanco semi-transparente */
}

.content {
    padding-top: 80px;
}

.section {
    min-height: 100vh;
    position: relative;
}

/* Sección con efecto parallax */
.parallax-section {
    overflow: hidden;
}

.parallax-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 120vh;
    /* Un poco más grande para el efecto */
    background-image: url('/public/principal.jpg');
    background-size: cover;
    background-position: center;
    overflow: hidden;
    background-attachment: fixed;
    z-index: -1;
}

.section-content {
    position: absolute;
    top: 22rem;
    left: 0;
    right: 0;
    /* bottom: 0; */
    /* padding-top: 12rem; */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

/* Sección normal que tapa la imagen */
.normal-section {
    background-color: #c1c1c1;
    padding: 2rem 1rem;
    /* Padding mínimo */
    text-align: center;
    z-index: 2;
    position: relative;
    box-sizing: border-box;
}

.image-gallery {
    display: flex;
    gap: 1rem;
    /* Gap pequeño */
    justify-content: center;
    margin-top: 3rem;
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
}

.image-card {
    position: relative;
    flex: 1;
    width: calc(50% - 0.5rem);
    /* 50% menos la mitad del gap */
    height: 400px;
    overflow: hidden;
    border-radius: 15px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    box-sizing: border-box;
}

.image-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25);
}

.image-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.image-card:hover img {
    transform: scale(1.3);
}

/* Resto de estilos para overlay igual... */
.overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(transparent, rgba(0, 0, 0, 0.8));
    color: white;
    padding: 2rem 1.5rem 1.5rem;
    transform: translateY(100%);
    transition: transform 0.3s ease;
}

.image-card:hover .overlay {
    transform: translateY(0);
}

.overlay h3 {
    margin: 0 0 0.5rem 0;
    font-size: 1.2rem;
}

.overlay p {
    margin: 0;
    font-size: 0.9rem;
    opacity: 0.9;
}

.read-more-btn {
    display: none;
}


/* Mobile Large */
@media (max-width: 768px) {
    .hero-logo{
        display: block;
        width: 150px;
        margin-bottom: 0rem;
    }
    .content {
        padding-top: 70px;
    }

    /* ===== SECCIÓN MAP - Imagen completa sin recortar ===== */
 #map {
    padding: 0; /* Asegúrate de que el contenedor no tenga padding */
    min-height: 30vh; /* Dale una altura mínima para que la imagen sea visible */
  }
  
  .background-image {
    /* ...tus otras propiedades como position, top, left, etc... */
    background-size: cover; /* 👈 Este es el cambio principal */
    background-position: center;
    background-repeat: no-repeat;
    /* Ya no necesitas un background-color si la imagen siempre va a cubrir todo */
  }
    /* ===== SECCIÓN NOSOTROS ===== */
    #about {
        padding: 2rem 1rem;
        min-height: auto;
    }

    #about h2 {
        font-size: 1.8rem;
        margin-bottom: 1rem;
    }

    /* Descripción más pequeña y retráctil */
    .description {
        font-size: 0.9rem;
        line-height: 1.5;
        padding: 0 0.5rem;
        max-height: 150px;
        /* 👈 Altura máxima */
        overflow: hidden;
        position: relative;
        transition: max-height 0.3s ease;
    }

    .description.expanded {
        max-height: 1000px;
        /* 👈 Se expande al hacer clic */
    }

    /* Botón "Leer más" (necesitas agregarlo en el HTML) */
    .read-more-btn {
        display: block;
        margin: 1rem auto;
        padding: 0.5rem 1.5rem;
        background: #c9a961;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 0.9rem;
    }

    /* ===== MISIÓN Y VISIÓN - Slider horizontal ===== */
.mision-vision-section .container {
  display: flex;
  flex-wrap: nowrap;               /* evita que las tarjetas bajen */
  overflow-x: auto;                /* activa el scroll horizontal */
  overflow-y: hidden;
  scroll-snap-type: x mandatory;
  gap: 1rem;
  padding: 1rem 0;
  -webkit-overflow-scrolling: touch; /* suaviza scroll en iOS */
  
  width: 100%;
  max-width: 100%;                 /* elimina el límite de Bootstrap */
  box-sizing: border-box;
}

    .mision-vision-section .container::-webkit-scrollbar {
        display: none;
        /* Oculta scrollbar en Chrome/Safari */
    }

    .mision-box,
    .vision-box {
        width: 40vw;
        scroll-snap-align: center;
        padding: 1.5rem;
        flex-shrink: 0;
    }

    .mision-box .icon,
    .vision-box .icon {
        font-size: 2.5rem;
        margin-bottom: 0.8rem;
    }

    .mision-box h3,
    .vision-box h3 {
        font-size: 1.5rem;
        margin-bottom: 0.8rem;
    }

    .mision-box p,
    .vision-box p {
        font-size: 0.95rem;
        line-height: 1.5;
    }

    /* Indicadores de scroll (opcional) */
    .mision-vision-section::after {
        content: '← Desliza →';
        display: block;
        text-align: center;
        color: #c9a961;
        font-size: 0.85rem;
        margin-top: 1rem;
        opacity: 0.7;
    }

    /* ===== SERVICIOS - Slider automático ===== */
    #services {
        padding: 3rem 1rem;
        overflow: hidden;
        /* 👈 Importante para el slider */
    }

    #services h2 {
        font-size: 1.8rem;
        margin-bottom: 1rem;
    }

    .services-subtitle {
        font-size: 1rem;
        margin-bottom: 2rem;
        padding: 0 1rem;
    }

    .services-grid {
        display: flex;
        gap: 1.5rem;
        width: max-content;
        --drag-offset: 0px;
        /* 👈 Inicializa la variable de arrastre */
        transform: translateX(var(--drag-offset));
        /* 👈 Aplica el arrastre inicial */
        animation: autoScrollServices 30s linear infinite;
        /* Aceleré un poco la animación */
    }

    .service-card {
        min-width: 260px;
        flex-shrink: 0;
        padding: 2rem 1.5rem;
        background: #e8e8e8;
        /* Fondo simple */
        border-radius: 15px;
        /* Bordes redondeados */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        /* Sombra sutil */
        border: 1px solid rgba(0, 0, 0, 0.05);
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
    }

    /* 2. SE CONSERVA SOLO LA ANIMACIÓN DE SCROLL Y LA PAUSA */
    @keyframes autoScrollServices {
        0% {
            transform: translateX(var(--drag-offset));
        }

        100% {
            /* Mueve el 50% del ancho, MÁS el offset del arrastre del usuario */
            transform: translateX(calc(-50% + var(--drag-offset)));
        }
    }

    /* Pausa la animación al tocar (con JS) o al hacer hover (mouse) */
    .services-grid.is-paused,
    .services-grid:hover {
        animation-play-state: paused;
    }

    /* --- FIN DE CAMBIOS --- */


    /* Pausa al hacer hover (opcional) */
    /* Pausa la animación cuando se toca (añade la clase) O al hacer hover con el mouse */
    .services-grid.is-paused,
    .services-grid:hover {
        animation-play-state: paused;
    }

    /* ===== SPECIALIZED AREAS - Apiladas full width ===== */
    .specialized-areas {
        display: flex;
        /* 👈 Cambiado de grid a flex */
        flex-direction: column;
        gap: 1.5rem;
        padding: 3rem 1rem;
    }

    .area-card {
        width: 100%;
        /* 👈 Full width */
        max-width: 100%;
        height: 350px;
        margin: 0;
        /* 👈 Reset del margin auto */
    }

    .area-card:nth-child(3) {
        grid-column: auto;
        /* 👈 Reset del grid-column */
        max-width: 100%;
    }

    .area-card .overlay {
        padding: 2rem 1.5rem;
    }

    .area-card .overlay h2 {
        font-size: 1.5rem;
        padding-bottom: 1rem;
    }

    .area-card .overlay ul {
        text-align: left;
    }

    .area-card .overlay li {
        font-size: 0.9rem;
        padding: 0.4rem 0;
    }

    
.parallax-bg {
    position: fixed;
    height: 100vh;
    background-image: url('/public/fondo3.jpg');
    /* background-position: center -7rem; */
    z-index: -1;
}
    


.section-content {
    position: absolute;
    top: 18rem;
    left: 0;
    right: 0;
    /* bottom: 0; */
    /* padding-top: 12rem; */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

.hero-title {
    
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    /* Bold */
    letter-spacing: 0.5px;
    color: #252524;
    font-size: 1.8rem;
    margin-bottom: 1rem;
}


@media (max-width: 480px) {
    .hero-logo{
        display: block;
        width: 150px;
        margin-bottom: 0rem;
    }
.parallax-section {
    position: relative;
    width: 100%;
    height: 100vh; /* 👈 Altura completa de la pantalla */
    overflow: hidden; /* 👈 hidden, no auto */
}

.parallax-bg {
    position: absolute; /* 👈 Importante */
    top: 0;
    left: 0;
    width: 100%; 
}
  /* ===== SECCIÓN DE INICIO (HERO) ===== */
  /* Ajustamos el título superior para que no se vea tan grande */
  .hero-title {
    font-size: 1.6rem; /* Un poco más pequeño */
    padding: 1.5rem 1rem 2rem 1rem; /* Menos padding vertical */
  }
  
  /* Ajustamos el contenedor del subtítulo inferior */
.section-content {
    position: absolute;
    top: 10rem;
    left: 0;
    right: 0;
    /* bottom: 0; */
    /* padding-top: 12rem; */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

  /* Compactamos el subtítulo y su línea decorativa */
  .hero-subtitle {
    font-size: 0.9rem;
    text-align: center;
    line-height: 1.5;
    padding-bottom: 1.5rem;
    margin-bottom: 1.5rem;
  }
  .hero-subtitle::after {
    width: 50px; /* Línea más corta */
  }

  /* ===== SECCIÓN NOSOTROS ===== */
  .description {
    font-size: 0.85rem;
    max-height: 120px; /* Hacemos el área de texto inicial más pequeña */
  }

  /* ===== MISIÓN Y VISIÓN ===== */
  /* Hacemos que cada tarjeta ocupe casi todo el ancho para un mejor enfoque */
.mision-box,
.vision-box {
  width: 85vw; /* Usamos 'width' para anular explícitamente el '40vw' */
  flex-shrink: 0; /* Aseguramos que las tarjetas no se encojan */
}
  .mision-box p,
  .vision-box p {
    font-size: 0.9rem;
  }
  
  /* ===== SECCIÓN SERVICIOS ===== */
  .service-card {
    width: 40vw;
    padding: 1.5rem;
  }
  .service-card h3 {
    font-size: 1.2rem;
  }
  .service-card p {
    font-size: 0.9rem;
  }

  /* ===== ÁREAS ESPECIALIZADAS ===== */
  .area-card {
    height: 300px; /* Hacemos las tarjetas de imagen un poco menos altas */
  }
  .area-card .overlay h2 {
    font-size: 1.3rem; /* Títulos más pequeños en el overlay */
  }
  .area-card .overlay li {
    font-size: 0.85rem; /* Texto de la lista más pequeño */
  }
}


@media (max-width: 375px) {
  
  /* ===== SECCIÓN DE INICIO (HERO) ===== */
  /* Ajustamos el título superior para que no se vea tan grande */
  .hero-title {
    font-size: 1.6rem; /* Un poco más pequeño */
    padding: 1.5rem 1rem 2rem 1rem; /* Menos padding vertical */
  }
  
  /* Ajustamos el contenedor del subtítulo inferior */
.section-content {
    position: absolute;
    top: 6rem;
    left: 0;
    right: 0;
}
}

}
</style>