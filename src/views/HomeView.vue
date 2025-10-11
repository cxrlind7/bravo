<template>

    <NavBar :isHomePage="true" />
    <div class="content">
        <h1>:)</h1>
        <div id="inicio" class="section parallax-section">
            <div class="parallax-bg"></div>

            <div class="section-content">
                <!-- <img src="/path/to/logo.png" alt="Bravo & Asociados" class="hero-logo" /> -->
                <h3 class="hero-title">Servicios Jurídicos y Asesoría Especializada de Alta Calidad</h3>
                <p class="hero-subtitle">Compromiso de ética, responsabilidad y justicia en todo México</p>
                <!-- <button class="hero-button">Agenda una Consulta</button> -->
            </div>
        </div>
        <div id="about" class="">
            <div class="top-right-corner">
                <h2>¿Quiénes somos?</h2>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae ipsa nam quod dolore repellendus,
                    odit culpa mollitia magnam similique explicabo velit aperiam fugit consequatur. Repudiandae sit
                    laboriosam velit doloribus voluptate!</p>
                <br />
                <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Assumenda qui fuga dolores ducimus nam
                    necessitatibus officia, iste ipsum nostrum, architecto inventore! Provident quos architecto
                    reiciendis nihil similique ullam animi quisquam!</p>
            </div>
            <div class="background-image"></div>
        </div>
        <div id="services" class="normal-section">
            <h2>Nuestros Servicios</h2>
            <p class="services-subtitle">Ofrecemos asesoría legal integral en las siguientes áreas:</p>

            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon">
                        <!-- <i class="bi bi-people"></i> -->
                        <i class="fa fa-users" aria-hidden="true"></i>
                    </div>
                    <h3>Derecho Familiar</h3>
                    <p>Asesoramiento en pensiones alimenticias, divorcios y juicios sucesorios.</p>
                </div>

                <div class="service-card">
                    <div class="service-icon">
                        <!-- <i class="bi bi-briefcase"></i> -->
                        <i class="fa fa-briefcase" aria-hidden="true"></i>
                    </div>
                    <h3>Derecho Empresarial</h3>
                    <p>Dotamos a tu empresa de las mejores herramientas: contratos, reglamentos, protección de marca,
                        etc.</p>
                </div>

                <div class="service-card">
                    <div class="service-icon">
                        <i class="fa fa-gavel" aria-hidden="true"></i>
                        <!-- <i class="bi bi-shield-fill-exclamation"></i> -->
                    </div>
                    <h3>Derecho Penal</h3>
                    <p>Representación legal ante problemas graves que impliquen detenciones o delitos que se atienden en
                        las Fiscalías.</p>
                </div>
            </div>
        </div>
                <div id="images" class="section normal-section">
            <div class="image-gallery">
                <div class="image-card">
                    <img src="/public/empresa.jpg" alt="Imagen 1">
                    <div class="overlay">
                        <h2>Lorem ipsum dolor. </h2>
                        <p style="font-size: 1.3rem;">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Impedit, veniam eaque dolor animi vitae nihil totam nam maiores? Laudantium nulla illum suscipit animi ratione a quod temporibus dolorem culpa quia.</p>
                    </div>
                </div>
                
                <div class="image-card">
                    <img src="/public/individual.jpg" alt="Imagen 2">
                    <div class="overlay">
                        <h2>Lorem ipsum dolor. </h2>
                        <p style="font-size: 1.3rem;">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Impedit, veniam eaque dolor animi vitae nihil totam nam maiores? Laudantium nulla illum suscipit animi ratione a quod temporibus dolorem culpa quia.</p>
                    </div>
                </div>
            </div>
            <br>
            <h2>Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur, quia, iusto culpa eius quis, cupiditate dolor tempore ad quas dignissimos odit nesciunt eveniet! Eaque eveniet necessitatibus perferendis, quaerat incidunt asperiores!</h2>
            <br>
            <h4>Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur, quia, iusto culpa eius quis, cupiditate dolor tempore ad quas dignissimos odit nesciunt eveniet! Eaque eveniet necessitatibus perferendis, quaerat incidunt asperiores! Lorem ipsum dolor sit amet, consectetur.</h4>
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
    }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');
@import url('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css');

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
    /* position: relative; */
    z-index: 1;
    color: white;
    /* ajusta según tu diseño */
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    font-size: 2rem;
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
    font-size: 1.4rem;
    font-family: 'Montserrat', sans-serif;
    font-weight: 400;
    /* Regular */
    letter-spacing: 0.3px;
    color: #252524;
    /* font-size: 1rem; */
    margin-bottom: 2rem;
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

/* Tablets */
@media (max-width: 1024px) {
    .parallax-bg {
        background-attachment: scroll;
        /* Mejor rendimiento en tablets */
        background-size: cover;
        /* En tablets, volver a cover para mejor ajuste */
    }

    .section-content {
        padding: 80px 30px;
    }

    .image-card {
        height: clamp(280px, 45vw, 350px);
    }
}

/* Mobile Large */
@media (max-width: 768px) {
    .content {
        padding-top: 70px;
    }

    .image-gallery {
        flex-direction: column;
        gap: 1.5rem;
        margin-top: 2rem;
    }

    .image-card {
        width: 100%;
        height: 280px;
        border-radius: 20px;
    }

    .overlay {
        padding: 1.5rem;
        background: linear-gradient(transparent, rgba(0, 0, 0, 0.85));
        text-align: center;
    }

    .overlay h2 {
        font-size: 1.3rem;
        margin-bottom: 1rem;
    }

    .overlay p {
        font-size: 1rem;
        margin-bottom: 1.2rem;
    }

    .cta-button {
        padding: 0.8rem 2rem;
        font-size: 0.95rem;
    }

    .normal-section {
        padding: 60px 1.5rem;
    }

    .text-content {
        margin-top: 3rem;
        text-align: center;
    }

    .main-title {
        font-size: 1.8rem;
        margin-bottom: 1.5rem;
    }

    .main-description {
        font-size: 1.1rem;
        text-align: left;
    }
}

/* Mobile Small */
@media (max-width: 480px) {
    .section-content {
        padding: 60px 15px;
    }

    .section-content h1 {
        font-size: 2.2rem;
    }

    .image-card {
        height: 250px;
        border-radius: 15px;
    }

    .overlay {
        padding: 1.2rem;
    }

    .overlay h2 {
        font-size: 1.2rem;
    }

    .overlay p {
        font-size: 0.95rem;
        line-height: 1.5;
    }

    .normal-section {
        padding: 40px 1rem;
    }

    .main-title {
        font-size: 1.6rem;
    }

    .main-description {
        font-size: 1rem;
    }
}

/* Extra Small Mobile */
@media (max-width: 360px) {
    .content {
        padding-top: 65px;
    }

    .image-card {
        height: 220px;
    }

    .overlay {
        padding: 1rem;
    }

    .cta-button {
        padding: 0.7rem 1.5rem;
        font-size: 0.85rem;
    }
}

/* Landscape Mobile */
@media (max-height: 500px) and (orientation: landscape) {
    .section-content {
        padding: 40px 20px;
    }

    .section-content h1 {
        font-size: 2rem;
    }

    .image-card {
        height: 200px;
    }
}
</style>