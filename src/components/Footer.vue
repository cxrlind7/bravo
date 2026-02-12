<template>
  <footer class="footer">
    <div class="footer-container">

      <!-- Columna 1: Logo y derechos -->
      <div class="footer-col">
        <img src="/public/logobravo.png" alt="" class="footer-logo-img">
        <p class="footer-copy">© 2025 Bravo & Asociados. Todos los derechos reservados.</p>
      </div>

      <!-- Columna 2: Enlaces -->
      <div class="footer-col">
        <nav class="footer-nav">
          <a href="#inicio" @click.prevent="scrollToSection('inicio')">Inicio</a>
          <a href="#about" @click.prevent="scrollToSection('about')">Nosotros</a>
          <a href="#services" @click.prevent="scrollToSection('services')">Servicios</a>
        </nav>
        <div class="footer-legal">
          <router-link to="/aviso-de-privacidad">Aviso de Privacidad</router-link>
        </div>
      </div>

      <!-- Columna 3: Contacto y redes -->
      <div class="footer-col">
        <p><strong>Tel:</strong> 55 5604 9890</p>
        <p><strong>WhatsApp:</strong> 618 122 2244</p>
        <p><strong>Email:</strong> administracion@bravoyasoc.com</p>
        <p><strong>Dirección:</strong> Río Pánuco 313, Durango, Dgo., 34120</p>
        <div class="footer-socials">
          <a href="https://facebook.com" target="_blank" aria-label="Facebook">
            <i class="bi bi-facebook"></i>
          </a>
          <a href="https://twitter.com" target="_blank" aria-label="Twitter">
            <i class="bi bi-twitter"></i>
          </a>
        </div>
        <!-- <a href="https://www.flaticon.es/iconos-gratis/grifo" title="grifo iconos">Grifo iconos creados por Pixel perfect - Flaticon</a> -->
      </div>
    </div>
  </footer>
</template>

<script setup>
// --- CAMBIO: Se añade toda la lógica del script ---

const scrollToSection = (sectionId) => {
  const element = document.getElementById(sectionId);
  if (!element) {
    console.warn(`La sección "${sectionId}" no fue encontrada.`);
    return;
  }

  // Se busca el navbar en el DOM para obtener su altura dinámicamente.
  // Es importante que tu navbar tenga la clase 'navbar'.
  const navbar = document.querySelector('.navbar');
  const navbarHeight = navbar ? navbar.offsetHeight : 80; // 80px como valor por defecto

  // Se calcula la posición final del scroll, restando la altura del navbar.
  const y = element.getBoundingClientRect().top + window.pageYOffset - navbarHeight;

  // Se realiza el scroll suave.
  window.scrollTo({ top: y, behavior: 'smooth' });
};
</script>
<style scoped>
@import url('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css');

.footer {
  background-color: #111;
  /* negro o gris muy oscuro */
  color: #f1f1f1;
  padding: 1rem;
  font-size: 0.9rem;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  gap: 2rem;
  flex-wrap: wrap;
}

.footer-col {
  flex: 1;
  min-width: 250px;
}

.footer-logo {
  font-size: 2rem;
  font-weight: bold;
  margin: 0;
  color: #fff;
}

.footer-subtitle {
  margin: 0.2rem 0 1rem;
  font-size: 1rem;
  color: #aaa;
}

.footer-copy {
  margin-top: 1rem;
  font-size: 0.8rem;
  color: #777;
}

.footer-nav {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.footer-nav a,
.footer-legal a {
  color: #ccc;
  text-decoration: none;
  transition: color 0.3s;
}

.footer-nav a:hover,
.footer-legal a:hover {
  color: #AFAFAF;
  /* verde corporativo */
}

.footer-legal {
  margin-top: 1rem;
}

.footer-socials {
  margin-top: 1rem;
  display: flex;
  gap: 1rem;
}

.footer-socials a {
  color: #fff;
  font-size: 1.4rem;
  /* tamaño de íconos */
  transition: color 0.3s;
}

.footer-socials a:hover {
  color: #AFAFAF;
}

.footer-logo-img {
  width: 120px;
  /* ajusta el ancho que quieras */
  height: auto;
  /* mantiene la proporción */
  margin-bottom: 0.5rem;
  /* espacio debajo del logo */
}
</style>
